import re, sys

for line in sys.stdin:
    for token in re.findall("([,;:.!?\"]|\w+)", line.strip()):
        print(token)
