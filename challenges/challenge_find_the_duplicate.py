def find_duplicate(nums: list[int]):
    for num in nums:
        if not isinstance(num, int) or num < 0:
            return False

    nums.sort()

    for i in range(len(nums) - 1):
        if nums[i] == nums[i + 1]:
            return nums[i]

    return False


print(find_duplicate([3, 1, 2, 4, 6, 5, 7, 7, 7, 8]))
