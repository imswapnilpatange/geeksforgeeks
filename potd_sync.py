import os
import re
import asyncio
from playwright.async_api import async_playwright
from bs4 import BeautifulSoup

BASE_DIR = os.getcwd()


def slugify(text):
    return re.sub(r'[^a-z0-9]+', '-', text.lower()).strip('-')


# -----------------------------
# Parse POTD + Problem Details
# -----------------------------
async def parse_potd(page):
    # Step 1: Find problem URL
    anchors = await page.query_selector_all("a")

    problem_url = None
    for a in anchors:
        href = await a.get_attribute("href")
        if href and "/problems/" in href:
            if href.startswith("http"):
                problem_url = href
            else:
                problem_url = "https://practice.geeksforgeeks.org" + href
            break

    if not problem_url:
        raise Exception("POTD link not found")

    # Step 2: Open problem page
    await page.goto(problem_url, timeout=60000)
    await page.wait_for_load_state("networkidle")

    html = await page.content()
    soup = BeautifulSoup(html, "html.parser")

    # -------- Title --------
    title_tag = soup.find("h1")
    title = title_tag.text.strip() if title_tag else "Unknown Problem"

    # -------- Difficulty --------
    difficulty = "Unknown"
    for tag in soup.find_all(["span", "p"]):
        text = tag.get_text(strip=True)
        if text in ["Easy", "Medium", "Hard"]:
            difficulty = text
            break

    # -------- Description / Examples / Constraints --------
    content_blocks = []
    for div in soup.find_all("div"):
        text = div.get_text("\n", strip=True)
        if len(text) > 200:
            content_blocks.append(text)

    description = "\n\n".join(content_blocks[:3]) if content_blocks else "Refer problem link"

    # -------- Tags --------
    tags = []
    for a in soup.find_all("a"):
        text = a.get_text(strip=True)
        if text and len(text) < 30 and text not in tags:
            if text.lower() not in ["login", "submit"]:
                tags.append(text)
    tags = tags[:10]

    # -------- Company Tags --------
    companies = []
    for span in soup.find_all("span"):
        text = span.get_text(strip=True)
        if text and len(text) < 25 and text not in companies:
            if text not in ["Easy", "Medium", "Hard"]:
                companies.append(text)
    companies = companies[:10]

    return {
        "title": title,
        "difficulty": difficulty,
        "url": problem_url,
        "description": description,
        "tags": tags,
        "companies": companies
    }


# -----------------------------
# README Generator
# -----------------------------
def generate_readme(data):
    tags = ", ".join(data["tags"]) if data["tags"] else "Not specified"
    companies = ", ".join(data["companies"]) if data["companies"] else "Not specified"

    return f"""# {data['title']}

## Difficulty
{data['difficulty']}

## Problem
[{data['title']}]({data['url']})

## Description
{data['description']}

## Tags
{tags}

## Company Tags
{companies}

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
        async with async_playwright() as p:
            browser = await p.chromium.launch(headless=True)
            page = await browser.new_page()

            await page.goto("https://practice.geeksforgeeks.org/problem-of-the-day", timeout=60000)
            await page.wait_for_load_state("networkidle")

            data = await parse_potd(page)

            await browser.close()

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

    # Write README
    with open(readme_path, "w", encoding="utf-8") as f:
        f.write(generate_readme(data))

    # Create empty Java file if not exists
    if not os.path.exists(solution_path):
        with open(solution_path, "w", encoding="utf-8") as f:
            f.write(generate_empty_java())

    print("Sync completed successfully")


if __name__ == "__main__":
    asyncio.run(main())
