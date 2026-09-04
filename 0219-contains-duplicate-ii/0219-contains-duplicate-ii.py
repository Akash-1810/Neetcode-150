class Solution(object):
    def containsNearbyDuplicate(self, nums, k,):
        d = {}
        for i in range(len(nums)):
            if nums[i] in d and abs(d[nums[i]]-i) <= k:
                return True
            else:
                d[nums[i]] = i
        return False

    


        
            
        

        