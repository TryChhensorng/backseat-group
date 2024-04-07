from math import ceil
def chunking_by(numbers, chunck):
    temp = []
    for i in range(ceil(len(numbers)/chunck)):
        x = i*chunck
        if len(numbers) < x + chunck:
            a = numbers[x:len(numbers)]
        else:
            a = numbers[x:x+chunck]
        temp.append(a)
    return temp
    ... 