
def getSmallest(number):

    if number == []:
        return None
    smallest = number[0]
    for num in number:
        if num < smallest:
            smallest = num
    return smallest

assert getSmallest([1, 2, 3]) == 1 
assert getSmallest([3, 2, 1]) == 1 
assert getSmallest([28, 25, 42, 2, 28]) == 2 
assert getSmallest([1]) == 1 
assert getSmallest([]) == None
