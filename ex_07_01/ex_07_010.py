fname = open('words.txt')

for line in fname:
    nfh = line.upper().rstrip()
    print(nfh)
