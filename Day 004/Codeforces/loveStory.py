def loveStory(s : str) -> int:
    if len(s) != 10 :
        return "Invalid string"
    count = 0
    stringList = []
    love = "codeforces"
    loveList = [] 
    for char in s:
        stringList.append(char)
    for char in love:
        loveList.append(char)

    for i in range(10):
        if stringList[i] == loveList[i]:
            continue
        else:
            count = count + 1
    return count
num = int(input())
for i in range(num):
    s = input()
    print(loveStory(s))

