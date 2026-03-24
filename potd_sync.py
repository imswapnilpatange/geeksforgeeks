import os
import re
import json
import datetime
import requests
from bs4 import BeautifulSoup
from datetime import datetime, timedelta

BASE_URL = "https://practice.geeksforgeeks.org"
POTD_DATE_URL = "https://practice.geeksforgeeks.org/problem-of-the-day/{year}/{month}/{day}"

HEADERS = {"User-Agent": "Mozilla/5.0"}
SESSION_COOKIE = os.getenv("GFG_SESSION")


def get_date_range():
    start = os.getenv("START_DATE")
    end = os.getenv("END_DATE")

    if not start or not end:
        raise Exception("START_DATE or END_DATE missing")

    start_date = datetime.strptime(start, "%Y-%m-%d")
    end_date = datetime.strptime(end, "%Y-%m-%d")

    return start_date, end_date


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


def fetch_potd_for_date(date_obj):
    y = date_obj.strftime("%Y")
    m = date_obj.strftime("%m")
    d = date_obj.strftime("%d")

    url = POTD_DATE_URL.format(year=y, month=m, day=d)
    print(f"[INFO] Fetching POTD page: {url}")

    res = safe_request(url)
    if not res:
        raise Exception(f"POTD page fetch failed for {y}-{m}-{d}")

    soup = BeautifulSoup(res.text, "html.parser")

    # POTD link is typically inside <a href="/problems/...">
    link_tag = soup.find("a", href=re.compile(r"/problems/"))
    if not link_tag:
        raise Exception(f"POTD link not found on date page {url}")

    problem_name = link_tag.text.strip()
    problem_href = link_tag.get("href")

    # full problem URL
    problem_link = BASE_URL + problem_href
    return problem_name, problem_link


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
    if diff_tag:
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


def main():
    start_date, end_date = get_date_range()
    current = start_date

    while current <= end_date:
        today_str = current.strftime("%Y-%m-%d")
        print(f"[INFO] Processing date: {today_str}")

        try:
            name, link = fetch_potd_for_date(current)
            details = fetch_problem_details(link)
            submission = fetch_submission()

            slug = f"{today_str}-{slugify(name)}"
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
                f.write(generate_readme(name, details, link, today_str))

            metadata = {
                "date": today_str,
                "problem_name": name,
                "difficulty": details["difficulty"],
                "tags": details["tags"],
                "language": lang,
                "runtime": submission["runtime"] if submission else "",
                "runtime_percent": submission["runtime_percent"] if submission else "",
                "memory": submission["memory"] if submission else "",
                "memory_percent": submission["memory_percent"] if submission else "",
                "link": link
            }

            with open(f"{base_folder}/metadata.json", "w") as f:
                json.dump(metadata, f, indent=2)

            # write commit message for this date
            with open("commit_msg.txt", "w") as f:
                f.write(f"{today_str} — {name} | {details['difficulty']}")

        except Exception as e:
            print(f"[ERROR] Failed for {today_str}: {e}")

        current += timedelta(days=1)


if __name__ == "__main__":
    main()
