class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        s = set()
        for c in nums:
            if c in s:
                return True
            else:
                s.add(c)
        return False    

            
