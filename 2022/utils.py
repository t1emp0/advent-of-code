from os import path
import requests
from datetime import date


def input_path(day: int):
    return f"data/input{str(day).zfill(2)}.txt"


def download_input(day: int):
    # Get session cookie
    if not path.exists("cookie.txt"):
        raise FileNotFoundError("You need to store the cookie from AoC")
    
    with open("cookie.txt", "r") as f:
        cookie = f.read()

    # Get today's date and make request
    url = f"https://adventofcode.com/2022/day/{day}/input"
    request = requests.get(url, cookies={"session": cookie})

    # Save to file
    if not path.exists("data"):
        raise FileNotFoundError("You need to create an empty folder named 'data'")

    with open(input_path(day), "w") as f:
        f.write(request.text)


def load_input(day: int, splitlines: bool, strip: bool):
    input = input_path(day)
    try:
        with open(input, "r") as fin:
            data = fin.read()
            if strip:
                data = data.strip()
            if splitlines:
                data = data.splitlines()
            return data
    except:
        print(f"Failed to load {input} from disk")


def get_input(day=date.today().day, splitlines=True, strip=True):
    if not path.exists(input_path(day)):
        download_input(day)
    return load_input(day, splitlines, strip)
