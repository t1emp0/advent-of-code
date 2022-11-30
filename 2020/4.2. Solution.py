# filepath = "4.1. Puzzle example.txt"
filepath = "4.1. Puzzle input.txt"

with open(filepath) as fp:
    lines = fp.readlines()

# you may also want to remove whitespace characters like \n at the end of each line
lines = [x.strip() for x in lines]
# print(lines)

passports = []
current = {}
for l in lines:
    if l:
        items = [item.split(":") for item in l.split(" ")]
        items = {key: val for (key, val) in items}
        current.update(items)
    else:
        passports.append(current)
        current = {}
passports.append(current)

print("Total passports:", len(passports))

full_passports = [
    p
    for p in passports
    if len(p.keys()) == 8 or ("cid" not in p.keys() and len(p.keys()) == 7)
]
print("Full passports: ", len(full_passports))

valid_passports = 0
for p in full_passports:
    val_byr = 1920 <= int(p["byr"]) <= 2002
    val_iyr = 2010 <= int(p["iyr"]) <= 2020
    val_exp = 2020 <= int(p["eyr"]) <= 2030

    hgt_value, hgt_unit = p["hgt"][:-2], p["hgt"][-2:]
    if hgt_unit == "cm":
        val_hgt = 150 <= int(hgt_value) <= 193
    elif hgt_unit == "in":
        val_hgt = 59 <= int(hgt_value) <= 76
    else:
        val_hgt = False

    val_hcl = (
        len(p["hcl"]) == 7
        and p["hcl"][0] == "#"
        and len([i for i in p["hcl"][1:] if i in "0123456789abcdef"]) == 6
    )

    val_ecl = p["ecl"] in ["amb", "blu", "brn", "gry", "grn", "hzl", "oth"]

    val_pid = (
        len(p["pid"]) == 9 and len([i for i in p["pid"] if i in "0123456789"]) == 9
    )

    valids = [val_byr, val_iyr, val_exp, val_hgt, val_hcl, val_ecl, val_pid]

    if all(valids):
        valid_passports += 1

print("Valid passports:", valid_passports)
