import os
import requests
from bs4 import BeautifulSoup
import re

BASE_DIR = os.getcwd()
COOKIE = os.getenv("GFG_COOKIE")

HEADERS = {
    "User-Agent": "Mozilla/5.0"
}


def slugify(text):
    return re.sub(r'[^a-z0-9]+', '-', text.lower()).strip('-')


def get_potd():
    url = "https://practice.geeksforgeeks.org/problem-of-the-day"
    res = requests.get(url, headers={"User-Agent": "Mozilla/5.0"}, timeout=10)

    html = res.text

    # --- Strategy 1: Extract from embedded JSON (most reliable) ---
    match = re.search(r'"problem_url":"(.*?)"', html)
    if match:
        slug = match.group(1)
        problem_url = f"https://practice.geeksforgeeks.org/problems/{slug}"
    else:
        problem_url = None

    # --- Strategy 2: fallback anchor scan ---
    if not problem_url:
        soup = BeautifulSoup(html, "html.parser")
        for a in soup.find_all("a", href=True):
            if "/problems/" in a["href"]:
                problem_url = "https://practice.geeksforgeeks.org" + a["href"]
                break

    if not problem_url:
        raise Exception("POTD link not found (all strategies failed)")

    # --- Visit problem page ---
    prob_res = requests.get(problem_url, headers={"User-Agent": "Mozilla/5.0"}, timeout=10)
    prob_html = prob_res.text
    prob_soup = BeautifulSoup(prob_html, "html.parser")

    # Title
    title_tag = prob_soup.find("h1")
    title = title_tag.text.strip() if title_tag else "Unknown Problem"

    # Difficulty (better regex)
    difficulty = "Unknown"
    diff_match = re.search(r'Difficulty\s*:\s*(Easy|Medium|Hard)', prob_html)
    if diff_match:
        difficulty = diff_match.group(1)

    # Description (safe trimmed)
    desc_div = prob_soup.find("div")
    description = desc_div.text.strip()[:2000] if desc_div else "Refer GfG"

    return {
        "title": title,
        "difficulty": difficulty,
        "url": problem_url,
        "description": description
    }


def get_accepted_solution(problem_url):
    """
    Fetch accepted Java submission using session cookie
    """

    if not COOKIE:
        return None

    headers = {
        "cookie": COOKIE,
        "user-agent": "Mozilla/5.0"
    }

    try:
        submissions_url = problem_url + "submissions/"
        res = requests.get(submissions_url, headers=headers, timeout=10)

        if res.status_code != 200:
            return None

        soup = BeautifulSoup(res.text, "html.parser")
        rows = soup.find_all("tr")

        for row in rows:
            text = row.text

            if "Accepted" in text and "Java" in text:
                link = row.find("a", href=True)
                if not link:
                    continue

                submission_link = "https://practice.geeksforgeeks.org" + link["href"]
                code_res = requests.get(submission_link, headers=headers, timeout=10)

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


def main():
    try:
        data = get_potd()
    except Exception as e:
        print("Error fetching POTD:", e)
        return

    # --- Try fetching accepted solution ---
    solution_code = get_accepted_solution(data["url"])

    # --- Fallback to stub if not available ---
    if solution_code is None:
        solution_code = generate_stub()

    difficulty_folder = f"Difficulty: {data['difficulty']}"
    problem_folder = data["title"]

    full_path = os.path.join(BASE_DIR, difficulty_folder, problem_folder)
    os.makedirs(full_path, exist_ok=True)

    readme_path = os.path.join(full_path, "README.md")
    solution_filename = slugify(data["title"]) + ".java"
    solution_path = os.path.join(full_path, solution_filename)

    # --- Always overwrite README ---
    with open(readme_path, "w", encoding="utf-8") as f:
        f.write(generate_readme(data))

    # --- Solution handling ---
    if not os.path.exists(solution_path):
        # First time → write whatever we have (real or stub)
        with open(solution_path, "w", encoding="utf-8") as f:
            f.write(solution_code)
    else:
        # Replace only if existing is stub
        with open(solution_path, "r", encoding="utf-8") as f:
            existing = f.read()

        if "TODO: Implement solution" in existing:
            with open(solution_path, "w", encoding="utf-8") as f:
                f.write(solution_code)

    print("Sync completed successfully")


if __name__ == "__main__":
    main()
