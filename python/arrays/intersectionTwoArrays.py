class Solution(object):
    def intersection(self, nums1, nums2):
        new_set = set()
        arr = []
        for num in nums1:
            if num not in new_set:
                new_set.add(num)
        for num in nums2:
            if num not in arr:
                if num in new_set:
                    arr.append(num)
        return arr


class Solution(object):
    def intersection(self, nums1, nums2):
        s1 = set(nums1)
        s2 = set(nums2)
        li = []
        for i in s2:
            if i in s1:
                li.append(i)
        return li