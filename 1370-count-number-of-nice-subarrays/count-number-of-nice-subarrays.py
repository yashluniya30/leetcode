from collections import defaultdict

class Solution:
    def numberOfSubarrays(self, nums, k):
        # Initialize a dictionary to store the frequency of prefix odd counts
        count_map = defaultdict(int)
        
        # We start by having seen an odd count of 0 once (this is useful for subarrays starting from index 0)
        count_map[0] = 1
        
        # Initialize a variable to track the number of odd numbers encountered so far
        odd_count = 0
        
        # Initialize the result to count the number of nice subarrays
        result = 0
        
        # Iterate through the array
        for num in nums:
            # If the current number is odd, increment the odd_count
            if num % 2 == 1:
                odd_count += 1
                
            # If we've previously encountered (odd_count - k), that means we found a nice subarray
            if odd_count - k in count_map:
                result += count_map[odd_count - k]
                
            # Record the current odd_count in the map (this helps us find nice subarrays later)
            count_map[odd_count] += 1
        
        # Return the final count of nice subarrays
        return result
