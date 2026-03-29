import os
import requests
from bs4 import BeautifulSoup
import re

BASE_DIR = os.getcwd()
COOKIE = os.getenv("GFG_COOKIE")


def slugify(text):
    return re.sub(r'[^a-z0-9]+', '-', text.lower()).strip('-')


def get_potd():
    url = "https://practice.geeksforgeeks.org/problem-of-the-day"
    res = requests.get(url)
    soup = BeautifulSoup(res.text, "html.parser")

    link_tag = soup.find("a", href=True, string="Solve Problem")
    problem_url = "https://practice.geeksforgeeks.org" + link_tag['href']

    prob_res = requests.get(problem_url)
    prob_soup = BeautifulSoup(prob_res.text, "html.parser")

    title = prob_soup.find("h1").text.strip()

    difficulty_tag = prob_soup.find(string=re.compile("Difficulty"))
    difficulty = difficulty_tag.split(":")[-1].strip()

    desc_div = prob_soup.find("div", class_="problem-statement")
    description = desc_div.text.strip() if desc_div else "Refer GfG"

    return {
        "title": title,
        "difficulty": difficulty,
        "url": problem_url,
        "description": description
    }


def get_accepted_solution(problem_url):
    """
    Requires GFG_COOKIE (logged-in session cookie)
    Attempts to fetch last accepted Java submission
    """

    if not COOKIE:
        return None

    headers = {
        "cookie": COOKIE,
        "user-agent": "Mozilla/5.0"
    }

    try:
        submissions_url = problem_url + "submissions/"
        res = requests.get(submissions_url, headers=headers)

        if res.status_code != 200:
            return None

        soup = BeautifulSoup(res.text, "html.parser")

        # Find accepted submission rows
        rows = soup.find_all("tr")

        for row in rows:
            if "Accepted" in row.text and "Java" in row.text:
                link = row.find("a", href=True)
                if not link:
                    continue

                submission_link = "https://practice.geeksforgeeks.org" + link['href']
                code_res = requests.get(submission_link, headers=headers)

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


def generate_stub(title):
    return f"""class Solution {{

    public int solve() {{
        // TODO: Implement solution
        return 0;
    }}
}}
"""


def main():
    data = get_potd()

    # STEP 1: Try fetching accepted solution
    solution_code = get_accepted_solution(data["url"])

    # STEP 2: If no solution found → DO NOT SKIP (fallback to stub)
    if solution_code is None:
        solution_code = generate_stub(data["title"])

    difficulty_folder = f"Difficulty: {data['difficulty']}"
    problem_folder = data["title"]

    full_path = os.path.join(BASE_DIR, difficulty_folder, problem_folder)
    os.makedirs(full_path, exist_ok=True)

    readme_path = os.path.join(full_path, "README.md")
    solution_filename = slugify(data["title"]) + ".java"
    solution_path = os.path.join(full_path, solution_filename)

    # Overwrite README always
    with open(readme_path, "w", encoding="utf-8") as f:
        f.write(generate_readme(data))

    # Only write solution if file doesn't exist OR was previously stub
    if not os.path.exists(solution_path):
        with open(solution_path, "w", encoding="utf-8") as f:
            f.write(solution_code)
    else:
        with open(solution_path, "r", encoding="utf-8") as f:
            existing = f.read()

        if "TODO: Implement solution" in existing:
            with open(solution_path, "w", encoding="utf-8") as f:
                f.write(solution_code)


if __name__ == "__main__":
    main()
