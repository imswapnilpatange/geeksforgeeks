import os
import re
import asyncio
from playwright.async_api import async_playwright
from bs4 import BeautifulSoup

BASE_DIR = os.getcwd()
COOKIE = os.getenv("GFG_COOKIE")


def slugify(text):
    return re.sub(r'[^a-z0-9]+', '-', text.lower()).strip('-')


# -----------------------------
# Fetch POTD page
# -----------------------------
async def fetch_potd_page():
    async with async_playwright() as p:
        browser = await p.chromium.launch(headless=True)
        page = await browser.new_page()

        await page.goto("https://practice.geeksforgeeks.org/problem-of-the-day", timeout=60000)
        await page.wait_for_load_state("networkidle")

        content = await page.content()
        await browser.close()
        return content


# -----------------------------
# Extract difficulty robustly
# -----------------------------
def extract_difficulty(soup):
    for tag in soup.find_all(["span", "p", "div"]):
        text = tag.get_text(strip=True)
        if text in ["Easy", "Medium", "Hard"]:
            return text
    return "Unknown"


# -----------------------------
# Parse POTD
# -----------------------------
def parse_potd(html):
    soup = BeautifulSoup(html, "html.parser")

    problem_url = None

    for a in soup.find_all("a", href=True):
        if "/problems/" in a["href"]:
            href = a["href"]

            if href.startswith("http"):
                problem_url = href
            else:
                problem_url = "https://practice.geeksforgeeks.org" + href

            break

    if not problem_url:
        raise Exception("POTD link not found")

    async def fetch_problem_details():
        async with async_playwright() as p:
            browser = await p.chromium.launch(headless=True)
            page = await browser.new_page()

            await page.goto(problem_url, timeout=60000)
            await page.wait_for_load_state("networkidle")

            html = await page.content()
            await browser.close()
            return html

    loop = asyncio.get_event_loop()
    prob_html = loop.run_until_complete(fetch_problem_details())
    prob_soup = BeautifulSoup(prob_html, "html.parser")

    title_tag = prob_soup.find("h1")
    title = title_tag.text.strip() if title_tag else "Unknown Problem"

    difficulty = extract_difficulty(prob_soup)

    desc_div = prob_soup.find("div")
    description = desc_div.text.strip()[:2000] if desc_div else "Refer GfG"

    return {
        "title": title,
        "difficulty": difficulty,
        "url": problem_url,
        "description": description
    }


# -----------------------------
# Fetch accepted solution
# -----------------------------
async def get_accepted_solution(problem_url):
    if not COOKIE:
        return None

    try:
        async with async_playwright() as p:
            browser = await p.chromium.launch(headless=True)
            context = await browser.new_context()

            # Inject cookies
            cookies = []
            for item in COOKIE.split(";"):
                if "=" in item:
                    name, value = item.strip().split("=", 1)
                    cookies.append({
                        "name": name,
                        "value": value,
                        "domain": ".geeksforgeeks.org",
                        "path": "/"
                    })

            await context.add_cookies(cookies)

            page = await context.new_page()

            await page.goto(problem_url + "/submissions/", timeout=60000)
            await page.wait_for_load_state("networkidle")

            content = await page.content()
            soup = BeautifulSoup(content, "html.parser")

            for row in soup.find_all("tr"):
                text = row.text

                if "Accepted" in text and "Java" in text:
                    link = row.find("a", href=True)
                    if not link:
                        continue

                    sub_url = link["href"]
                    if not sub_url.startswith("http"):
                        sub_url = "https://practice.geeksforgeeks.org" + sub_url

                    await page.goto(sub_url)
                    await page.wait_for_load_state("networkidle")

                    code_html = await page.content()
                    code_soup = BeautifulSoup(code_html, "html.parser")

                    code_tag = code_soup.find("pre")
                    if code_tag:
                        await browser.close()
                        return code_tag.text.strip()

            await browser.close()
            return None

    except Exception:
        return None


# -----------------------------
# README
# -----------------------------
def generate_readme(data):
    return f"""# {data['title']}

**Difficulty:** {data['difficulty']}  
**Link:** {data['url']}

---

## Problem Description
{data['description']}
"""


def generate_stub():
    return """class Solution {

    public int solve() {
        // TODO: Implement solution
        return 0;
    }
}
"""


# -----------------------------
# Main
# -----------------------------
async def main():
    try:
        html = await fetch_potd_page()
        data = parse_potd(html)
    except Exception as e:
        print("POTD fetch failed:", e)
        return

    solution_code = await get_accepted_solution(data["url"]) or generate_stub()

    difficulty_folder = f"Difficulty: {data['difficulty']}"
    problem_folder = data["title"]

    full_path = os.path.join(BASE_DIR, difficulty_folder, problem_folder)
    os.makedirs(full_path, exist_ok=True)

    readme_path = os.path.join(full_path, "README.md")
    solution_filename = slugify(data["title"]) + ".java"
    solution_path = os.path.join(full_path, solution_filename)

    with open(readme_path, "w", encoding="utf-8") as f:
        f.write(generate_readme(data))

    if not os.path.exists(solution_path):
        with open(solution_path, "w", encoding="utf-8") as f:
            f.write(solution_code)
    else:
        with open(solution_path, "r", encoding="utf-8") as f:
            existing = f.read()

        if "TODO: Implement solution" in existing:
            with open(solution_path, "w", encoding="utf-8") as f:
                f.write(solution_code)

    print("Sync completed successfully")


if __name__ == "__main__":
    asyncio.run(main())
