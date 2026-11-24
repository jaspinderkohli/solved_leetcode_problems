class Solution(object):
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        # Step 1: Create an empty dictionary (hash map) to store numbers we have already seen.
        # Format will be -> { number : index }
        chars = {}
        
        # Step 2: Loop through the list using enumerate() to get both:
        # 'i' = the current index (0, 1, 2...)
        # 'x' = the current number at that index
        for i, x in enumerate(nums):
            
            # Step 3: Calculate the missing number needed to reach 'target' (target - x),
            # and check if we have already seen and saved that number in 'chars'.
            # Note: Checking 'in chars' automatically searches the dictionary keys in O(1) instant time.
            if (target - x) in chars:
                
                # Step 4: Match found!
                # chars[target - x] retrieves the index of the earlier number.
                # 'i' is the index of the current number.
                # Return both indices as a list and immediately exit the function.
                return [chars[target - x], i]
            
            # Step 5: No match yet. Save the current number as the key and its index as the value.
            # Note: 'nums[i]' is the exact same value as 'x', so chars[x] = i works identically.
            chars[x] = i

