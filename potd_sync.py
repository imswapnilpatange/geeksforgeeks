import os
import re
import asyncio
from playwright.async_api import async_playwright
from bs4 import BeautifulSoup

BASE_DIR = os.getcwd()


def slugify(text):
    return re.sub(r'[^a-z0-9]+', '-', text.lower()).strip('-')


# -----------------------------
# Parse POTD (HTML PRESERVATION)
# -----------------------------
async def parse_potd(page):
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

    # -------- Extract exact HTML blocks --------
    h2 = soup.find("h2")
    h3 = soup.find("h3")

    content_div = soup.find("div", class_=lambda x: x and "problem_content" in x)

    # Extract Company + Topic tags
    extra_html = ""
    for p in soup.find_all("p"):
        text = p.get_text()
        if "Company Tags" in text or "Topic Tags" in text:
            extra_html += str(p)

    # -------- Metadata --------
    title = "Unknown Problem"
    if soup.find("h1"):
        title = soup.find("h1").text.strip()
    
    difficulty = "Unknown"
    if soup.find("h3"):
        match = re.search(r'(Easy|Medium|Hard)', soup.find("h3").text)
        if match:
            difficulty = match.group(1)
    
    # -------- Build REQUIRED HEADER (CRITICAL FIX) --------
    header_html = f'<h2><a href="{problem_url}">{title}</a></h2>'
    
    difficulty_html = ""
    h3 = soup.find("h3")
    if h3:
        difficulty_html = str(h3)
    else:
        difficulty_html = f"<h3>Difficulty Level : Difficulty: {difficulty}</h3>"
    
    # -------- Extract content --------
    content_div = soup.find("div", class_=lambda x: x and "problem_content" in x)
    
    extra_html = ""
    for p in soup.find_all("p"):
        text = p.get_text()
        if "Company Tags" in text or "Topic Tags" in text:
            extra_html += str(p)
    
    # -------- Final HTML --------
    final_html = ""
    final_html += header_html
    final_html += difficulty_html
    final_html += "<hr>"
    
    if content_div:
        final_html += str(content_div)
    
    final_html += extra_html
    if not title:
    title = "Unknown Problem"

    if not difficulty:
        difficulty = "Unknown"
    
    if not final_html:
        final_html = f'<h2><a href="{problem_url}">{title}</a></h2><h3>Difficulty Level : Difficulty: {difficulty}</h3><hr>'
    
    return {
        "title": title,
        "difficulty": difficulty,
        "url": problem_url,
        "html": final_html
    }

# -----------------------------
# README (RAW HTML)
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
    try:
        async with async_playwright() as p:
            browser = await p.chromium.launch(headless=True)
            page = await browser.new_page()

            await page.goto("https://practice.geeksforgeeks.org/problem-of-the-day", timeout=60000)
            await page.wait_for_load_state("networkidle")

            data = await parse_potd(page)

            if not data:
                print("Parse failed. Using fallback.")
                data = {
                    "title": "Unknown Problem",
                    "difficulty": "Unknown",
                    "url": "https://practice.geeksforgeeks.org/problem-of-the-day",
                    "html": "<h2>Fallback Problem</h2><h3>Difficulty Level : Difficulty: Unknown</h3><hr>"
                }

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

    # Write README (HTML preserved)
    with open(readme_path, "w", encoding="utf-8") as f:
        f.write(generate_readme(data))

    # Create empty Java file if not exists
    if not os.path.exists(solution_path):
        with open(solution_path, "w", encoding="utf-8") as f:
            f.write(generate_empty_java())

    print("Sync completed successfully")


if __name__ == "__main__":
    asyncio.run(main())
