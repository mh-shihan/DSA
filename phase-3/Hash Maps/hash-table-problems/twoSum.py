from typing import List


def twoSum(nums: List[int], target: int) -> List[int]:
    hash_map = {}
    for i in range(len(nums)):
        hash_map[nums[i]] = i
    
    for i in range(len(nums)):
        complement = target - nums[i]
        if complement in hash_map and hash_map[complement] != i:
            return [i, hash_map[complement]]
    return []


# Test cases
if __name__ == "__main__":
    # Test case 1
    nums1 = [2, 7, 11, 15]
    target1 = 9
    result1 = twoSum(nums1, target1)
    print(f"Input: nums = {nums1}, target = {target1}")
    print(f"Output: {result1}")
    print()
    
    # Test case 2
    nums2 = [3, 2, 4]
    target2 = 6
    result2 = twoSum(nums2, target2)
    print(f"Input: nums = {nums2}, target = {target2}")
    print(f"Output: {result2}")
    print()
    
    # Test case 3
    nums3 = [3, 3]
    target3 = 6
    result3 = twoSum(nums3, target3)
    print(f"Input: nums = {nums3}, target = {target3}")
    print(f"Output: {result3}")
            