'''
Created on Nov 5, 2017

@author: ishank
'''
from collections import namedtuple

Rectangle = namedtuple("Rectangle", "top bottom left right")

def findRectangles(arr):
    
    # Deeply copy the array so that it can be modified safely
    arr = [row[:] for row in arr]

    rectangles = []

    for top, row in enumerate(arr):
        start = 0

        # Look for rectangles whose top row is here
        while True:
            try:
                left = row.index(0, start)
            except ValueError:
                break

            # Set start to one past the last 0 in the contiguous line of 0s
            try:
                start = row.index(1, left)
            except ValueError:
                start = len(row)

            right = start - 1

            if (  # Width == 1
                  left == right or
                  # There are 0s above
                  top > 0 and not all(arr[top-1][left:right + 1])):
                continue

            bottom = top + 1
            while (bottom < len(arr) and
                   # No extra zeroes on the sides
                   (left == 0 or arr[bottom][left-1]) and
                   (right == len(row) - 1 or arr[bottom][right + 1]) and
                   # All zeroes in the row
                   not any(arr[bottom][left:right + 1])):
                bottom += 1

            # The loop ends when bottom has gone too far, so backtrack
            bottom -= 1

            if (  # Height == 1
                  bottom == top or
                  # There are 0s beneath
                  (bottom < len(arr) - 1 and
                   not all(arr[bottom + 1][left:right+1]))):
                continue

            rectangles.append(Rectangle(top, bottom, left, right))

            # Remove the rectangle so that it doesn't affect future searches
            for i in range(top, bottom+1):
                arr[i][left:right+1] = [1] * (right + 1 - left)


    return rectangles

arr = [
    [1, 1, 1, 1, 1, 1, 1, 1, 1],
    [1, 1, 1, 1, 1, 1, 1, 1, 0],
    [1, 1, 1, 0, 0, 0, 1, 0, 0],
    [1, 0, 1, 0, 0, 0, 1, 0, 0],
    [1, 0, 1, 1, 1, 1, 1, 1, 1],
    [1, 0, 1, 0, 0, 1, 1, 1, 1],
    [1, 1, 1, 0, 0, 1, 1, 1, 1],
    [1, 1, 1, 1, 1, 1, 1, 1, 1],
]

print findRectangles(arr)

