from os import path
import sys
import requests
from datetime import date
from pathlib import Path


def input_path(day: int, year: int) -> str:
    # mains = Path(sys.path[0], "..")
    # print(mains)
    folder = "\\".join(sys.path[0].split("\\")[:-1])
    # print(folder)
    return f"{folder}/AoC_{year}/data/input{str(day).zfill(2)}.txt"


def download_input(day: int, year: int):
    folder_path = sys.path[0]
    # print(folder_path)

    # Get session cookie
    cookie_path = folder_path + "/" + "cookie.txt"
    if not path.exists(cookie_path):
        raise FileNotFoundError("You need to store the cookie from AoC as 'cookie.txt'")

    with open(cookie_path, "r") as f:
        cookie = f.read()

    # Get the day's url and make the request
    url = f"https://adventofcode.com/{year}/day/{day}/input"
    request = requests.get(url, cookies={"session": cookie})

    # Save to file
    if not path.exists(folder_path + "/" + "data"):
        raise FileNotFoundError("You need to create an empty folder named 'data'")

    # print("Saving file")
    save_path = input_path(day, year)
    # print(save_path)
    with open(save_path, "w") as f:
        f.write(request.text)


def load_input(day: int, year: int, splitlines: bool, strip: bool) -> list[str] | str:
    # print("Loading input")
    input = input_path(day, year)
    try:
        with open(input, "r") as fin:
            data = fin.read()
            if strip:
                data = data.strip()
            if splitlines:
                data = data.splitlines()
            return data
    except:
        raise ImportError(f"Failed to load {input} from disk")


def get_input(
    day=date.today().day, year=date.today().year, splitlines=True, strip=True
) -> list[str] | str:
    # print("Checking path")
    if not path.exists(input_path(day, year)):
        print("Proceding to download")
        download_input(day, year)
    return load_input(day, year, splitlines, strip)
