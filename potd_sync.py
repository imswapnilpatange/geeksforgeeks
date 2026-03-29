import os
import re
import asyncio
from playwright.async_api import async_playwright
from bs4 import BeautifulSoup
import requests

BASE_DIR = os.getcwd()
COOKIE = os.getenv("GFG_COOKIE")


def slugify(text):
    return re.sub(r'[^a-z0-9]+', '-', text.lower()).strip('-')


async def fetch_potd_page():
    async with async_playwright() as p:
        browser = await p.chromium.launch(headless=True)
        page = await browser.new_page()

        await page.goto("https://practice.geeksforgeeks.org/problem-of-the-day", timeout=60000)
        await page.wait_for_load_state("networkidle")

        content = await page.content()
        await browser.close()
        return content


def parse_potd(html):
    soup = BeautifulSoup(html, "html.parser")

    problem_url = None

    for a in soup.find_all("a", href=True):
        if "/problems/" in a["href"]:
            problem_url = "https://practice.geeksforgeeks.org" + a["href"]
            break

    if not problem_url:
        raise Exception("POTD link not found even after JS render")

    # Visit problem page
    res = requests.get(problem_url, headers={"User-Agent": "Mozilla/5.0"})
    prob_soup = BeautifulSoup(res.text, "html.parser")

    title = prob_soup.find("h1").text.strip()

    difficulty = "Unknown"
    match = re.search(r'Difficulty\s*:\s*(Easy|Medium|Hard)', res.text)
    if match:
        difficulty = match.group(1)

    desc_div = prob_soup.find("div")
    description = desc_div.text.strip()[:2000] if desc_div else "Refer GfG"

    return {
        "title": title,
        "difficulty": difficulty,
        "url": problem_url,
        "description": description
    }


def get_accepted_solution(problem_url):
    if not COOKIE:
        return None

    headers = {
        "cookie": COOKIE,
        "user-agent": "Mozilla/5.0"
    }

    try:
        res = requests.get(problem_url + "/submissions/", headers=headers)
        soup = BeautifulSoup(res.text, "html.parser")

        for row in soup.find_all("tr"):
            if "Accepted" in row.text and "Java" in row.text:
                link = row.find("a", href=True)
                if not link:
                    continue

                sub_url = "https://practice.geeksforgeeks.org" + link["href"]
                code_res = requests.get(sub_url, headers=headers)

                code_soup = BeautifulSoup(code_res.text, "html.parser")
                code_tag = code_soup.find("pre")

                if code_tag:
                    return code_tag.text.strip()

        return None

    except Exception:
        return None


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


async def main():
    try:
        html = await fetch_potd_page()
        data = parse_potd(html)
    except Exception as e:
        print("POTD fetch failed:", e)
        return

    solution_code = get_accepted_solution(data["url"]) or generate_stub()

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
        with open(solution_path, "r") as f:
            existing = f.read()

        if "TODO: Implement solution" in existing:
            with open(solution_path, "w") as f:
                f.write(solution_code)

    print("Sync completed")


if __name__ == "__main__":
    asyncio.run(main())
