def remove_all_after(numbers, n):
    x = numbers.index(n)
    return numbers[:x+1]
    ...
print(remove_all_after([1, 2, 3, 4, 5], 3) )