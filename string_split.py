def split_and_join(line):
    # write your code here
    ansList = line.split(' ')
    return '-'.join(ansList)

if __name__ == '__main__':
    line = input()
    result = split_and_join(line)
    print(result)
