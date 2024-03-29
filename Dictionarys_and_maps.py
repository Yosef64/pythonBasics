# Enter your code here. Read input from STDIN. Print output to STDOUT
from collections import defaultdict
test = int(input())
ourMap = defaultdict(str)
for _ in range(test):
    name,telephone = list(input().split(' '))
    ourMap[name] = int(telephone)
while True:
    try:
        query = input()
        if query in ourMap:
            print(f"{query}={ourMap[query]}")
        else:
            print("Not found")
    except EOFError:
        break
    
