def twoSum(nums,target):
    pair_dict = {}
    diff=None
    j=None
    k=None
    for i, num in enumerate(nums):

        diff = target - num
        if diff in nums:
            pair_dict[diff] = i
            j=i
            if k is None:
                k=diff

    if k in pair_dict:
        return [pair_dict[k],j]

    raise ValueError("no solution exists")


print(twoSum([3,2,4],9))