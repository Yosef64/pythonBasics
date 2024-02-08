from collections import Counter
def isSubset( a1, a2, n, m):
    ourSet = Counter(a1)
    for num in a2:
        if not ourSet[num]:
            return "No"
        ourSet[num] -= 1
    return "Yes"
