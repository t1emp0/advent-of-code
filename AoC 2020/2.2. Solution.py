def extractLineInfo(line):
    colon = line.index(":")
    password = line[colon+2:]
    letter = line[colon-1:colon]

    dash = line.index("-")
    lower_limit, upper_limit = line[:dash], line[dash+1:colon-2]
    
    return letter, upper_limit, lower_limit, password

def isValidPassword1(fun, *args):
    letter, upper_limit, lower_limit, password = fun( *args )
    instances = password.count(letter)
    if (instances >= int(lower_limit)) and (instances <= int(upper_limit)):
        return True
    else:
        return False

def isValidPassword2(fun, *args):
    letter, upper_limit, lower_limit, password = fun( *args )
    
    if (password[int(lower_limit)-1] == letter) != (password[int(upper_limit)-1] == letter):
        return True
    else:
        return False


filepath = "2.1. Puzzle input.txt"

with open(filepath) as fp:
    lines = fp.readlines()

    correctPasswords1 = 0
    correctPasswords2 = 0

    for line in lines:
        if isValidPassword1(extractLineInfo, line):
            correctPasswords1 +=1
        if isValidPassword2(extractLineInfo, line):
            correctPasswords2 +=1

    
    print("Correct passwords 1: ", correctPasswords1)
    print("Correct passwords 2: ", correctPasswords2)