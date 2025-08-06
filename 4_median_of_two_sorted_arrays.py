"""
Given two sorted arrays nums1 and nums2 of size m and n respectively, return the median of the two sorted arrays.

The overall run time complexity should be O(log (m+n)).

 

Example 1:

Input: nums1 = [1,3], nums2 = [2]
Output: 2.00000
Explanation: merged array = [1,2,3] and median is 2.

Example 2:

Input: nums1 = [1,2], nums2 = [3,4]
Output: 2.50000
Explanation: merged array = [1,2,3,4] and median is (2 + 3) / 2 = 2.5.

 

Constraints:

    nums1.length == m
    nums2.length == n
    0 <= m <= 1000
    0 <= n <= 1000
    1 <= m + n <= 2000
    -106 <= nums1[i], nums2[i] <= 106

"""

class Solution(object):
    def findMedianSortedArrays(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: float
        """
        count_nums1 = len(nums1)
        count_nums2 = len(nums2)
        total_nums = count_nums1 + count_nums2

        median_index = total_nums/2.0
        print(median_index) 

        if count_nums1 > count_nums2:
            max_number = nums1[-1]
        elif count_nums1 < count_nums2:
            max_number = nums2[-1]
        else:
            max_number = max(nums1[-1],nums2[-1])

        nums1.append(max_number)
        nums2.append(max_number)

        i,j = 0,0
        merged = []
        while (i+j)<median_index+1:
            print(merged)
            if nums1[i]>nums2[j]:
               merged.append(nums2[j])
               j+=1
            else:
               merged.append(nums1[i])
               i+=1

        print(merged)
        print(median_index)
        if median_index%1 ==0 :
            median = 0.5 * (merged[-2] + merged[-1])
        else:
            median = merged[-2]


        return median

print(Solution().findMedianSortedArrays([100001],[100000])) 

         