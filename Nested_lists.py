from collections import defaultdict
if __name__ == '__main__':
    fLowest,sLowest = float('inf'),float('inf')
    dic = defaultdict(list)
    for _ in range(int(input())):
        name = input()
        score = float(input())
        dic[score].append(name)
        if score<fLowest:
            sLowest = fLowest
            fLowest = score
        elif score!=fLowest and score < sLowest:
            sLowest = score 
    for name in sorted(dic[sLowest]):
        print(name)   
