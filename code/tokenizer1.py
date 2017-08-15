import re, sys

regex_pattern = "([,;:.!?\"]|\w+)"
for line in sys.stdin:
    for token in re.findall(regex_pattern,line.strip()):
        print(token)
