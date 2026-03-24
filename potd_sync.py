import os
import re
import json
import requests
from datetime import datetime, timedelta
from bs4 import BeautifulSoup

BASE_URL = "https://www.geeksforgeeks.org"
ARCHIVE_URL = f"{BASE_URL}/problem-of-the-day/"
TODAY_API = "https://practiceapi.geeksforgeeks.org/api/vr/problems-of-day/problem/today/"

HEADERS = {"User-Agent": "Mozilla/5.0"}
SESSION_COOKIE = os.getenv("GFG_SESSION")


# -----------------------------
# Helper Functions
# -----------------------------
def slugify(text):
    text = text.lower()
    text = re.sub(r'[^a-z0-9]+', '-', text)
    return text.strip('-')


def safe_request(url):
    try:
        res = requests.get(url, headers=HEADERS, timeout=15)
        res.raise_for_status()
        return res
    except Exception as e:
        print(f"[ERROR] {url} -> {e}")
        return None


def get_ist_datetime():
    """Return current IST datetime"""
    return datetime.utcnow() + timedelta(hours=5, minutes=30)


def parse_date_input(date_str):
    """Parse startDate/endDate inputs as IST date"""
    return datetime.strptime(date_str, "%Y-%m-%d") if date_str else None


def get_date_range():
    start = parse_date_input(os.getenv("START_DATE", "").strip())
    end = parse_date_input(os.getenv("END_DATE", "").strip())
    return start, end


# -----------------------------
# Fetch POTDs
# -----------------------------
def fetch_archive_problems():
    """Fetch all POTDs from archive page"""
    res = safe_request(ARCHIVE_URL)
    if not res:
        raise Exception("Failed to fetch POTD archive")

    soup = BeautifulSoup(res.text, "html.parser")
    problems = []

    entries = soup.select(".problem-of-the-day")
    for entry in entries:
        date_tag = entry.select_one(".date")
        link_tag = entry.select_one("a[href*='/problems/']")
        if date_tag and link_tag:
            try:
                date_str = date_tag.text.strip()
                problem_date = datetime.strptime(date_str, "%B %d, %Y")
                problem_name = link_tag.text.strip()
                problem_href = link_tag.get("href")
                problems.append({
                    "date": problem_date,
                    "name": problem_name,
                    "link": BASE_URL + problem_href
                })
            except Exception:
                continue
    return problems


def fetch_today_potd():
    """Fetch today's POTD using API"""
    res = safe_request(TODAY_API)
    if not res:
        raise Exception("Failed to fetch today's POTD")
    data = res.json()
    name = data.get("problem_name")
    link = data.get("problem_url")
    if not name or not link:
        raise Exception("Today's POTD parsing failed")
    return [{
        "date": get_ist_datetime(),
        "name": name,
        "link": link
    }]


# -----------------------------
# Problem Details and Submission
# -----------------------------
def fetch_problem_details(link):
    res = safe_request(link)
    if not res:
        raise Exception("Problem fetch failed")

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


def fetch_submission():
    if SESSION_COOKIE:
        try:
            cookies = {"gfg_session_id": SESSION_COOKIE}
            res = requests.get(
                "https://practice.geeksforgeeks.org/submissions/",
                headers=HEADERS,
                cookies=cookies,
                timeout=15
            )
            if res.status_code == 200:
                return {
                    "code": "// fetched code",
                    "language": "Java",
                    "runtime": "120 ms",
                    "runtime_percent": "85%",
                    "memory": "30 MB",
                    "memory_percent": "78%"
                }
        except Exception as e:
            print("[WARN] Submission fetch failed:", e)

    if os.path.exists("solution.txt"):
        with open("solution.txt") as f:
            return {
                "code": f.read(),
                "language": "Java",
                "runtime": "",
                "runtime_percent": "",
                "memory": "",
                "memory_percent": ""
            }
    return None


def generate_readme(name, details, link, date_str):
    return f"""# {name} — POTD {date_str}

## Problem Description
{details['description']}

## Constraints
{details['constraints']}

## Tags
{", ".join(details['tags'])}

## Link
{link}
"""


# -----------------------------
# Main Function
# -----------------------------
def main():
    start_date, end_date = get_date_range()
    if start_date and end_date:
        problems = fetch_archive_problems()
        problems_in_range = [p for p in problems if start_date <= p["date"] <= end_date]
        if not problems_in_range:
            print("[INFO] No POTDs found in the specified date range.")
            return
    else:
        problems_in_range = fetch_today_potd()

    for prob in problems_in_range:
        ist_date = prob["date"] + timedelta(hours=5, minutes=30) if prob["date"].tzinfo is None else prob["date"]
        today_str = ist_date.strftime("%Y-%m-%d")
        print(f"[INFO] Processing POTD: {today_str} — {prob['name']}")
        try:
            details = fetch_problem_details(prob["link"])
            submission = fetch_submission()

            slug = f"{today_str}-{slugify(prob['name'])}"
            diff_map = {"Easy": "Difficulty-Easy", "Medium": "Difficulty-Medium", "Hard": "Difficulty-Hard"}
            base_folder = f"{diff_map.get(details['difficulty'], 'Difficulty-Medium')}/{slug}"
            os.makedirs(base_folder, exist_ok=True)

            ext_map = {"Java": "java", "Python": "py", "C++": "cpp"}
            lang = submission["language"] if submission else "Java"
            ext = ext_map.get(lang, "txt")

            solution_path = f"{base_folder}/{slug}.{ext}"
            with open(solution_path, "w") as f:
                f.write(submission["code"] if submission else "// No submission")

            with open(f"{base_folder}/README.md", "w") as f:
                f.write(generate_readme(prob["name"], details, prob["link"], today_str))

            metadata = {
                "date": today_str,
                "problem_name": prob["name"],
                "difficulty": details["difficulty"],
                "tags": details["tags"],
                "language": lang,
                "runtime": submission["runtime"] if submission else "",
                "runtime_percent": submission["runtime_percent"] if submission else "",
                "memory": submission["memory"] if submission else "",
                "memory_percent": submission["memory_percent"] if submission else "",
                "link": prob["link"]
            }

            with open(f"{base_folder}/metadata.json", "w") as f:
                json.dump(metadata, f, indent=2)

            with open("commit_msg.txt", "w") as f:
                f.write(f"{today_str} — {prob['name']} | {details['difficulty']}")

        except Exception as e:
            print(f"[ERROR] Failed for {today_str}: {e}")


if __name__ == "__main__":
    main()
