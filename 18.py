triangle = '''75
95 64
17 47 82
18 35 87 10
20 04 82 47 65
19 01 23 75 03 34
88 02 77 73 07 63 67
99 65 04 28 06 16 70 92
41 41 26 56 83 40 80 70 33
41 48 72 33 47 32 37 16 94 29
53 71 44 65 25 43 91 52 97 51 14
70 11 33 28 77 73 17 78 39 68 17 57
91 71 52 38 17 14 91 43 58 50 27 29 48
63 66 04 68 89 53 67 30 73 16 69 87 40 31
04 62 98 27 23 09 70 98 73 93 38 53 60 04 23'''

lc = 0

nums = [[int(n) for n in row.split(' ')] for row in triangle.split("\n")]
rows = sum([1 for row in nums])

def recursive_subtriangle(row, col):
    global lc
    lc += 1
    if row == rows - 1:
        # We're at the bottom row, just return self
        return nums[row][col]
    # Otherwise this point becomes the pinacle of a new triangle
    # Find the max path of this triangle
    return nums[row][col] + max([
        recursive_subtriangle(row + 1, col),
        recursive_subtriangle(row + 1, col + 1),
    ])

print recursive_subtriangle(0, 0)
