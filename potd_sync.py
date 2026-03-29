import os
import re
import asyncio
from playwright.async_api import async_playwright
from bs4 import BeautifulSoup

BASE_DIR = os.getcwd()


def slugify(text):
    return re.sub(r'[^a-z0-9]+', '-', text.lower()).strip('-')


# -----------------------------
# Fetch POTD page (JS rendered)
# -----------------------------
async def fetch_potd():
    async with async_playwright() as p:
        browser = await p.chromium.launch(headless=True)
        page = await browser.new_page()

        await page.goto("https://practice.geeksforgeeks.org/problem-of-the-day", timeout=60000)
        await page.wait_for_load_state("networkidle")

        content = await page.content()
        await browser.close()

        return content


# -----------------------------
# Parse POTD safely
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

    title = problem_url.split("/problems/")[-1].replace("-", " ").title()

    return {
        "title": title,
        "difficulty": "Unknown",
        "url": problem_url,
        "description": "Refer problem link"
    }


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


def generate_empty_java():
    return """class Solution {

}
"""


# -----------------------------
# Main
# -----------------------------
async def main():
    try:
        html = await fetch_potd()
        data = parse_potd(html)
    except Exception as e:
        print("POTD fetch failed:", e)
        return

    difficulty_folder = f"Difficulty: {data['difficulty']}"
    problem_folder = data["title"]

    full_path = os.path.join(BASE_DIR, difficulty_folder, problem_folder)
    os.makedirs(full_path, exist_ok=True)

    readme_path = os.path.join(full_path, "README.md")
    solution_filename = slugify(data["title"]) + ".java"
    solution_path = os.path.join(full_path, solution_filename)

    # Always write README
    with open(readme_path, "w", encoding="utf-8") as f:
        f.write(generate_readme(data))

    # Always create empty Java file if not exists
    if not os.path.exists(solution_path):
        with open(solution_path, "w", encoding="utf-8") as f:
            f.write(generate_empty_java())

    print("Sync completed successfully")


if __name__ == "__main__":
    asyncio.run(main())
