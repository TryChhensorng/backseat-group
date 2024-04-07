from math import pow
def index_power(numnbers, n):
    try:
        return int(pow(numnbers[n], n))
    except:
        return -1
    ...


print(index_power([1, 2], 3))