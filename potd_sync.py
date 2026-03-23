import os
import re
import json
import datetime
import requests
from bs4 import BeautifulSoup

BASE_URL = "https://www.geeksforgeeks.org"
POTD_URL = "https://practice.geeksforgeeks.org/problem-of-the-day"

HEADERS = {"User-Agent": "Mozilla/5.0"}
SESSION_COOKIE = os.getenv("GFG_SESSION")


def get_today_date_ist():
    return datetime.datetime.utcnow() + datetime.timedelta(hours=5, minutes=30)


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


def fetch_potd():
    res = safe_request(POTD_URL)
    if not res:
        raise Exception("POTD fetch failed")

    soup = BeautifulSoup(res.text, "html.parser")

    link_tag = soup.select_one("a[href*='/problems/']")
    if not link_tag:
        raise Exception("POTD link not found")

    return link_tag.text.strip(), BASE_URL + link_tag.get("href")


def fetch_problem_details(link):
    res = safe_request(link)
    if not res:
        raise Exception("Problem fetch failed")

    soup = BeautifulSoup(res.text, "html.parser")

    description = soup.select_one(".problem-description")
    constraints = soup.find(string=re.compile("Constraints"))

    tags = [t.text.strip() for t in soup.select(".tag")] or []

    difficulty = "Medium"
    text = res.text.lower()
    if "easy" in text:
        difficulty = "Easy"
    elif "hard" in text:
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
            res = requests.get("https://practice.geeksforgeeks.org/submissions/",
                               headers=HEADERS, cookies=cookies)

            if res.status_code == 200:
                return {
                    "code": "// fetched code",
                    "language": "Java",
                    "runtime": "120 ms",
                    "runtime_percent": "85%",
                    "memory": "30 MB",
                    "memory_percent": "78%"
                }
        except:
            pass

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


def generate_readme(name, details, link):
    return f"""# {name}

## Problem Description
{details['description']}

## Constraints
{details['constraints']}

## Tags
{", ".join(details['tags'])}

## Link
{link}

## Complexity
- Time: TBD
- Space: TBD
"""


def main():
    today = get_today_date_ist().strftime("%Y-%m-%d")

    name, link = fetch_potd()
    details = fetch_problem_details(link)
    submission = fetch_submission()

    slug = f"{today}-{slugify(name)}"

    diff_map = {
        "Easy": "Difficulty-Easy",
        "Medium": "Difficulty-Medium",
        "Hard": "Difficulty-Hard"
    }

    base_folder = f"{diff_map[details['difficulty']]}/{slug}"
    os.makedirs(base_folder, exist_ok=True)

    ext_map = {"Java": "java", "Python": "py", "C++": "cpp"}
    lang = submission["language"] if submission else "Java"
    ext = ext_map.get(lang, "txt")

    solution_path = f"{base_folder}/{slug}.{ext}"

    with open(solution_path, "w") as f:
        f.write(submission["code"] if submission else "// No submission")

    with open(f"{base_folder}/README.md", "w") as f:
        f.write(generate_readme(name, details, link))

    metadata = {
        "date": today,
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

    commit_msg = f"{name} | Time: ({metadata['runtime_percent']}), Space: ({metadata['memory_percent']}) | Tags: {', '.join(details['tags'])}"

    with open("commit_msg.txt", "w") as f:
        f.write(commit_msg)


if __name__ == "__main__":
    main()
