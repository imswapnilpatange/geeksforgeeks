import os
import re
import asyncio
import json
from datetime import datetime
from playwright.async_api import async_playwright
from bs4 import BeautifulSoup

BASE_DIR = os.getcwd()


def slugify(text):
    return re.sub(r'[^a-z0-9]+', '-', text.lower()).strip('-')


# -----------------------------
# Parse POTD (HTML PRESERVATION + SAFE)
# -----------------------------
async def parse_potd(page):
    try:
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

        # Open problem page
        await page.goto(problem_url, timeout=60000)
        await page.wait_for_load_state("networkidle")

        html = await page.content()
        soup = BeautifulSoup(html, "html.parser")

        # -------- Title --------
        title = "Unknown Problem"
        h1 = soup.find("h1")
        if h1 and h1.get_text(strip=True):
            title = h1.get_text(strip=True)
        else:
            # fallback from URL slug
            slug = problem_url.split("/problems/")[-1].strip("/")
            title = slug.replace("-", " ").title()

        # -------- Difficulty --------
        difficulty = "Unknown"
        page_text = soup.get_text()
        match = re.search(r'Difficulty\s*:\s*(Easy|Medium|Hard)', page_text)
        
        if match:
            difficulty = match.group(1)

        # -------- Build HEADER (manual h2) --------
        header_html = f'<h2><a href="{problem_url}">{title}</a></h2>'
        difficulty_html = f'<h3>Difficulty Level : Difficulty: {difficulty}</h3>'

        # -------- Content --------
        content_div = soup.find("div", class_=lambda x: x and "problem_content" in x)

        # -------- Tags --------
        extra_html = ""
        for p in soup.find_all("p"):
            text = p.get_text()
            if "Company Tags" in text or "Topic Tags" in text:
                extra_html += str(p)

        # -------- Final HTML --------
        final_html = header_html + difficulty_html + "<hr>"

        if content_div:
            final_html += str(content_div)

        final_html += extra_html

        # -------- Fallback safety --------
        if not final_html.strip():
            final_html = f'<h2><a href="{problem_url}">{title}</a></h2><h3>Difficulty Level : Difficulty: {difficulty}</h3><hr>'

        return {
            "title": title,
            "difficulty": difficulty,
            "url": problem_url,
            "html": final_html
        }

    except Exception as e:
        print("Parse error:", e)
        return None


# -----------------------------
# README
# -----------------------------
def generate_readme(data):
    return data["html"]


def generate_empty_java():
    return """class Solution {

}
"""


# -----------------------------
# Main
# -----------------------------
async def main():
    data = None  # IMPORTANT: define upfront

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

    # -------- GLOBAL FAIL-SAFE (ALWAYS EXECUTES) --------
    if not data:
        print("Using fallback data")
        data = {
            "title": "Unknown Problem",
            "difficulty": "Unknown",
            "url": "https://practice.geeksforgeeks.org/problem-of-the-day",
            "html": "<h2><a href='https://practice.geeksforgeeks.org/problem-of-the-day'>Fallback Problem</a></h2><h3>Difficulty Level : Difficulty: Unknown</h3><hr>"
        }

    # -------- SAFE USAGE --------
    difficulty_folder = f"Difficulty: {data.get('difficulty', 'Unknown')}"
    problem_folder = data.get("title", "Unknown Problem")

    full_path = os.path.join(BASE_DIR, difficulty_folder, problem_folder)
    os.makedirs(full_path, exist_ok=True)

    readme_path = os.path.join(full_path, "README.md")
    solution_filename = slugify(problem_folder) + ".java"
    solution_path = os.path.join(full_path, solution_filename)

    # Write README
    with open(readme_path, "w", encoding="utf-8") as f:
        f.write(data.get("html", ""))

    # Create empty Java file if not exists
    if not os.path.exists(solution_path):
        with open(solution_path, "w", encoding="utf-8") as f:
            f.write("class Solution {\n\n}")
    
    print("Sync completed successfully")

if __name__ == "__main__":
    asyncio.run(main())
