from typing import List

def largestRectangleArea(heights: List[int]) -> int:
    max_area = heights[0]
    min_height_so_far = heights[0]
    L = 0
    for R in range(L + 1, len(heights)):
        w = R - L + 1
        h = min(min_height_so_far, heights[R])
        
        cur_area = w * h
        stick_area = heights[R]
        best_area = max(cur_area, stick_area)

        max_area = max(max_area, best_area)

        min_height_so_far = h
        if stick_area > cur_area:
            L = R
            min_height_so_far = heights[R]
    return max_area

arr = [2,1,5,6,2,3]
print(largestRectangleArea(arr))