# Enter your code here. Read input from STDIN. Print output to STDOUT
def queries(phone):
    for i in range(n):
        query = str(input())
        if query in phone:
            # print(k+"="+str(v[0]))
            print(query + "=" + phone[query][0])
        else:
            print("Not found")

if __name__ == '__main__':
    n = int(input("Enter N test case: "))
    phone = {}
    for i in range(n):
        s = list(map(str, input("Enter (Name number): ").rstrip().split()))
        if len(s) == 2:
            phone[s[0]] = []
            phone[s[0]].append(s[1])

    queries(phone)