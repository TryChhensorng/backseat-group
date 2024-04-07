def reverse_ascending(numbers):
    result = []
    ascend = []
    for num in numbers:
        if not ascend or num > ascend[-1]:
            ascend.append(num)
        else:
            result.extend(ascend[::-1])
            ascend=[num]
    
    result.extend(ascend[::-1])
    return result
...

print(list(reverse_ascending([1,2,3,4,5])))
print(list(reverse_ascending([5, 7, 10, 4, 2, 7, 8, 1, 3])))
print(list(reverse_ascending([5, 4, 3, 2, 1])))
print(list(reverse_ascending([])))