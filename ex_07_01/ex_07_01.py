fhand = open('words.txt')

for line in fhand:
    print(line.upper().rstrip())
