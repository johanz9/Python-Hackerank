import sys

S = input().strip()

try:
    integer = int(S)
    print(integer)
except ValueError:
    sys.stdout.write("Bad String")
