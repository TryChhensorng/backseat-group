def replace_last(numbers):
    if numbers == []:
        return []
    temp = numbers[:]
    x = len(numbers) - 1
    temp[0] = numbers[x]
    temp[1:x] = numbers[0:x-1]
    return temp
    ...