if __name__ == '__main__':
    n = int(input())
    arr = map(int, input().split())
    firstSecore , secondScore = float("-inf") , float("-inf")
    for score in arr:
        if score > firstSecore:
            secondScore = firstSecore
            firstSecore = score
        elif score !=firstSecore and score>secondScore:
            secondScore = score
    print(secondScore)
        
