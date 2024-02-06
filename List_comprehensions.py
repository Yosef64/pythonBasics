if __name__ == '__main__':
    x = int(input())
    y = int(input())
    z = int(input())
    n = int(input())
    ans = []
    for xCord in range(x+1):
        for yCord in range(y+1):
            for zCord in range(z+1):
                if xCord + yCord+zCord != n:
                    ans.append([xCord,yCord,zCord])
    print(ans)
