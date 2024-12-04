# aoc_fetcher.py
import requests
import os

def fetch_aoc_input(day, year=2024):
    url = f"https://adventofcode.com/{year}/day/{day}/input"
    session_cookie = os.getenv("AOC_SESSION_COOKIE")

    if not session_cookie:
        raise Exception("Session cookie not found. Set it as an environment variable.")

    cookies = {"session": session_cookie}
    response = requests.get(url, cookies=cookies)

    if response.status_code == 200:
        return response.text.strip()
    else:
        raise Exception(f"Failed to fetch data. Status code: {response.status_code}")
