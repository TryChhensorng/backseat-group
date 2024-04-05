def replace_last(numbers):
    temp = numbers[:]
    last = len(numbers)-1
    temp[0]=numbers[last]
    for i in range(len(numbers)-1):
        temp[i+1] = numbers[i]
    return temp
    ...

print(replace_last([1,2,3,4,5,6]))
