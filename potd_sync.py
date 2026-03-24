import os
import re
import json
from datetime import datetime, timedelta
import requests
from bs4 import BeautifulSoup
from playwright.sync_api import sync_playwright

BASE_URL = "https://www.geeksforgeeks.org"
ARCHIVE_URL = f"{BASE_URL}/problem-of-the-day/"
TODAY_API = "https://practiceapi.geeksforgeeks.org/api/vr/problems-of-day/problem/today/"

HEADERS = {"User-Agent": "Mozilla/5.0"}
SESSION_COOKIE = os.getenv("GFG_SESSION")

def slugify(text):
    text = text.lower()
    text = re.sub(r'[^a-z0-9]+', '-', text)
    return text.strip('-')

def safe_request(url):
    try:
        res = requests.get(url, headers=HEADERS, timeout=15)
        res.raise_for_status()
        return res
    except:
        return None

def get_ist_datetime():
    return datetime.utcnow() + timedelta(hours=5, minutes=30)

def parse_date_input(date_str):
    return datetime.strptime(date_str, "%Y-%m-%d") if date_str else None

def get_date_range():
    start = parse_date_input(os.getenv("START_DATE", "").strip())
    end = parse_date_input(os.getenv("END_DATE", "").strip())
    return start, end

def fetch_archive_problems():
    res = safe_request(ARCHIVE_URL)
    if not res:
        return []
    soup = BeautifulSoup(res.text, "html.parser")
    problems = []
    for entry in soup.select(".problem-of-the-day"):
        date_tag = entry.select_one(".date")
        link_tag = entry.select_one("a[href*='/problems/']")
        if date_tag and link_tag:
            try:
                problem_date = datetime.strptime(date_tag.text.strip(), "%B %d, %Y")
                problems.append({
                    "date": problem_date,
                    "name": link_tag.text.strip(),
                    "link": BASE_URL + link_tag.get("href")
                })
            except:
                continue
    return problems

def fetch_today_potd():
    res = safe_request(TODAY_API)
    if not res:
        return []
    data = res.json()
    name, link = data.get("problem_name"), data.get("problem_url")
    if not name or not link:
        return []
    return [{"date": get_ist_datetime(), "name": name, "link": link}]

def fetch_problem_details(link):
    res = safe_request(link)
    if not res:
        return {"description": "", "constraints": "", "tags": [], "difficulty": "Medium"}
    soup = BeautifulSoup(res.text, "html.parser")
    description = soup.select_one(".problem-description")
    constraints = soup.find(string=re.compile("Constraints"))
    tags = [t.text.strip() for t in soup.select(".tag")] or []
    difficulty = "Medium"
    diff_tag = soup.find(string=re.compile("Difficulty", re.IGNORECASE))
    if diff_tag and diff_tag.find_parent():
        parent_text = diff_tag.find_parent().text.lower()
        if "easy" in parent_text:
            difficulty = "Easy"
        elif "hard" in parent_text:
            difficulty = "Hard"
    return {
        "description": description.text.strip() if description else "",
        "constraints": constraints.strip() if constraints else "",
        "tags": tags,
        "difficulty": difficulty
    }

def fetch_latest_submission():
    submission = {"code": "// No submission", "language": "Java", "runtime": "", "runtime_percent": "", "memory": "", "memory_percent": ""}
    if not SESSION_COOKIE:
        return submission
    try:
        with sync_playwright() as p:
            browser = p.chromium.launch(headless=True)
            page = browser.new_page()
            page.context.add_cookies([{"name": "gfg_session_id", "value": SESSION_COOKIE, "domain": ".geeksforgeeks.org", "path": "/"}])
            page.goto("https://practice.geeksforgeeks.org/submissions/")
            page.wait_for_timeout(3000)
            row = page.query_selector("table tbody tr")
            if row:
                cells = row.query_selector_all("td")
                if len(cells) >= 5:
                    submission["language"] = cells[2].inner_text().strip()
                    submission["runtime"] = cells[3].inner_text().strip()
                    submission["memory"] = cells[4].inner_text().strip()
                    row.click()
                    page.wait_for_selector("pre, textarea")
                    code_area = page.query_selector("pre") or page.query_selector("textarea")
                    if code_area:
                        submission["code"] = code_area.inner_text()
            browser.close()
    except:
        pass
    return submission

def generate_readme(name, details, link, date_str):
    return f"# {name} — POTD {date_str}\n\n## Problem Description\n{details['description']}\n\n## Constraints\n{details['constraints']}\n\n## Tags\n{', '.join(details['tags'])}\n\n## Link\n{link}"

def main():
    start_date, end_date = get_date_range()
    if start_date and end_date:
        problems = fetch_archive_problems()
        problems_in_range = [p for p in problems if start_date <= p["date"] <= end_date]
        if not problems_in_range:
            return
    else:
        problems_in_range = fetch_today_potd()
    for prob in problems_in_range:
        today_str = prob["date"].strftime("%Y-%m-%d")
        try:
            details = fetch_problem_details(prob["link"])
            submission = fetch_latest_submission()
            slug = f"{today_str}-{slugify(prob['name'])}"
            diff_map = {"Easy": "Difficulty-Easy", "Medium": "Difficulty-Medium", "Hard": "Difficulty-Hard"}
            base_folder = f"{diff_map.get(details['difficulty'], 'Difficulty-Medium')}/{slug}"
            os.makedirs(base_folder, exist_ok=True)
            ext_map = {"Java": "java", "Python": "py", "C++": "cpp"}
            lang = submission.get("language", "Java")
            ext = ext_map.get(lang, "txt")
            solution_path = f"{base_folder}/{slug}.{ext}"
            with open(solution_path, "w") as f:
                f.write(submission.get("code", "// No submission"))
            with open(f"{base_folder}/README.md", "w") as f:
                f.write(generate_readme(prob["name"], details, prob["link"], today_str))
            metadata = {
                "date": today_str,
                "problem_name": prob["name"],
                "difficulty": details["difficulty"],
                "tags": details["tags"],
                "language": lang,
                "runtime": submission.get("runtime", ""),
                "runtime_percent": submission.get("runtime_percent", ""),
                "memory": submission.get("memory", ""),
                "memory_percent": submission.get("memory_percent", ""),
                "link": prob["link"]
            }
            with open(f"{base_folder}/metadata.json", "w") as f:
                json.dump(metadata, f, indent=2)
            with open("commit_msg.txt", "w") as f:
                f.write(f"{today_str} — {prob['name']} | {details['difficulty']}")
        except:
            continue

if __name__ == "__main__":
    main()
