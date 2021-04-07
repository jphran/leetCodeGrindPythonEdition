# Given a set of non-overlapping intervals, insert a new interval into the
# intervals (merge if necessary).
#
# You may assume that the intervals were initially sorted according to
# their start times.
from typing import List, Tuple


def insert(self, intervals: List[List[int]], newInterval: List[int]) -> \
        List[List[int]]:
    # binary search for position
    [first_idx, first_is_between] = __binary_search(None, intervals,
                                                    newInterval[0])
    [second_idx, second_is_between] = __binary_search(None, intervals,
                                                      newInterval[1])

    # replace if necessary
    if first_is_between and not second_is_between:
        intervals[first_idx][1] = newInterval[1]
        result = intervals[:first_idx] + intervals[second_idx:]
    elif not first_is_between and second_is_between:
        intervals[second_idx][0] = newInterval[0]
        result = intervals[:first_idx+1] + intervals[second_idx+1:]
    elif not first_is_between and not second_is_between:
        result = intervals[:first_idx+1] + [newInterval] \
                 + intervals[second_idx:]
    else:
        result = intervals[:first_idx] \
                 + [[intervals[first_idx][0], intervals[second_idx][1]]] \
                 + intervals[second_idx + 1:]

    return result


def __binary_search(self, intervals: List[List[int]], number:
int, start_idx: int = 0, end_idx: int = -1) -> Tuple[int, bool]:
    """
    Returns the insertion idx and 
    True if in between returned interval at idx
    """

    if end_idx == -1:
        end_idx = len(intervals)

    mid_idx = 0
    while start_idx != end_idx:
        mid_idx = int((start_idx + end_idx) / 2)
        first = intervals[mid_idx][0]
        second = intervals[mid_idx][1]

        if number < first:
            end_idx = mid_idx
        elif number > second:
            start_idx = mid_idx + 1
        else:
            return mid_idx, True

    return mid_idx, False
