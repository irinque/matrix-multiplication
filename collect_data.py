from sys import stdin

def collect_matrix():
    matrix = list()
    previous_line = ""
    for line in stdin:
        if previous_line == "":
            previous_line = line
        if len(previous_line.split()) == len(line.split()):
            matrix.append(line.rstrip("\n"))
            previous_line = line
        elif line == "\n":
            break
        else:
            print("warning: the string is not saved. the number of elements is not equal.")
    return matrix
