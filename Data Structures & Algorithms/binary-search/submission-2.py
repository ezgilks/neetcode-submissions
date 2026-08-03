class Solution:
    def search(self, nums: List[int], target: int) -> int:
        mid = len(nums) // 2
        if not nums:
            return -1
        if target == nums[mid]:
            return mid
        elif target < nums[mid]:
            return self.search(nums[:mid], target)
        elif target > nums[mid]:
            result = self.search(nums[mid + 1:], target)
            if result == -1:
                return -1
            return result + mid + 1 