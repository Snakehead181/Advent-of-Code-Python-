TESTING = True

def part1():
    file.seek(0)
    lines = [line.rstrip() for line in file]
    print ("Input lines:", lines)
    return

def part2():
    file.seek(0)
    return


if TESTING:
    file = open("sampleInput.txt", "r")
else:
    file = open("input.txt", "r")

print("Part 1: ", part1())
print("Part 2: ", part2())
