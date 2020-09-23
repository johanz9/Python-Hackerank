import sys

def indexString(s):
    odd = ""
    even = ""
    for i in range(len(s)):
        if i%2 == 0:
            even += s[i]
        else:
            odd += s[i]
    print(even + " " + odd)


if __name__ == '__main__':
    t = int(input("Enter number of test case: "))
    for i in range(t):
        s =  str(input("Enter string: "))
        indexString(s)