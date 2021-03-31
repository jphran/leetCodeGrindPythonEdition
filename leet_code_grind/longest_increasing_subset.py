import sys
from typing import List
from collections import deque


def lengthOfLIS(self, nums: List[int]) -> int:
    lis_length = 0
    for i in range(len(nums)):
        prev_val = i
        for j in range(i+1, len(nums)):
            if i < j:
                prev_val = j
                lis_length += 1

# class Node:
#     def __init__(self, val: int):
#         self.val = val
#         self.next = None


# def binary_search(arr: List[List[int]], min_idx: int, max_idx: int, search_val:
#                     int) -> int:
#     """Only used on an sorted array"""
#
#     while min_idx != max_idx:
#         idx = (min_idx+max_idx) / 2
#         if arr[idx][0] < search_val:
#             min_idx = idx + 1
#         else:
#             max_idx = idx
#
#     return min_idx


# def lengthOfLIS(self, nums: List[int]) -> int:
#     bins = [[]]
#     bins[0] = [sys.maxsize]
#
#     for n in nums:
#         if n < bins[-1][0]:
#             bins.insert(-1, [n])
#         else:
#             # curr_list_idx = binary_search(bins, 0, len(bins), n)
#             #
#             # while curr_node.next:
#             #     if n < curr_node.val:
#             #         curr_node = None
#             #     else:
#             #         curr_node = curr_node.next
#             #
#             # curr_node.next.append(Node(n))



# best soln, but i don't understand it
def lengthOfLIS(self, nums: List[int]) -> int:
    tails = [0] * len(nums)
    size = 0
    for x in nums:
        i, j = 0, size
        while i != j:
            m = int((i + j) / 2)
            if tails[m] < x:
                i = m + 1
            else:
                j = m
        tails[i] = x
        size = max(i + 1, size)
    return size

