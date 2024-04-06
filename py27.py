def volume(*nums):
    mul = 1
    for n in nums:
        mul*=n
    print(mul)
volume(3,2)
volume(2,2,2)