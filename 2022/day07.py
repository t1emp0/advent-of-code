from utils import get_input


def parse_input(data: str):
    file_tree = {"": {"size": 0, "depth": 0}}
    currentDir, currentSize = "", 0
    for d in data[1:]:
        if d.startswith("$ cd"):
            if file_tree[currentDir]["size"] == 0:
                file_tree[currentDir]["size"] = currentSize
                currentSize = 0
            if d.endswith(".."):
                currentDir = "/".join(currentDir.split("/")[:-1])
                continue
            currentDir = currentDir + "/" + d.split(" ")[2]

        if d.startswith("dir"):
            file_tree[currentDir + "/" + d.split(" ")[1]] = {
                "parent": currentDir,
                "size": 0,
                "depth": file_tree[currentDir]["depth"] + 1,
            }

        if d[0].isnumeric():
            currentSize += int(d.split(" ")[0])
    file_tree[currentDir]["size"] = currentSize

    folders = sorted(file_tree.values(), key=lambda f: f["depth"], reverse=True)

    for f in folders[:-1]:
        parent = f["parent"]
        file_tree[parent]["size"] += f["size"]

    return file_tree


def part1(file_tree):
    MAX_FOLDER_SIZE = 100_000
    dirs = [v["size"] for v in file_tree.values() if v["size"] <= MAX_FOLDER_SIZE]
    print("Directories:", sum(dirs))


def part2(file_tree):
    TOTAL_SPACE = 70_000_000
    NEEDED_SPACE = 30_000_000
    free_space = TOTAL_SPACE - file_tree[""]["size"]
    needed_space = NEEDED_SPACE - free_space

    smallest_deletion = sorted(
        [f for f in file_tree.values() if f["size"] >= needed_space],
        key=lambda f: f["size"],
    )[0]
    print("Smallest deletion:", smallest_deletion["size"])


if __name__ == "__main__":
    data = get_input(day=7)
    file_tree = parse_input(data)
    part1(file_tree)
    part2(file_tree)
