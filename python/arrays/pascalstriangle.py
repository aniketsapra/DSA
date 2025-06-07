class Solution(object):
    def generate(self, numRows):
        triangle = []

        for row_num in range(numRows):
            row = [1] * (row_num + 1)

            for j in range(1, row_num):
                row[j] = triangle[row_num - 1][j - 1] + triangle[row_num - 1][j]

            triangle.append(row)

        return triangle
    
# Iteration 1:

#     row_num = 0

#     row = [1]

#     triangle = [[1]]

# Iteration 2:

#     row_num = 1

#     row = [1, 1]

#     triangle = [[1], [1, 1]]

# Iteration 3:

#     row_num = 2

#     row = [1, 1, 1]

#     update row[1] = triangle[1][0] + triangle[1][1] = 1 + 1 = 2

#     final row = [1, 2, 1]

#     triangle = [[1], [1, 1], [1, 2, 1]]


# Start row 0: [1]
# Final row 0: [1]

# Start row 1: [1, 1]
# Final row 1: [1, 1]

# Start row 2: [1, 1, 1]
#   Updated row[1] = 2
# Final row 2: [1, 2, 1]

# Start row 3: [1, 1, 1, 1]
#   Updated row[1] = 3
#   Updated row[2] = 3
# Final row 3: [1, 3, 3, 1]

# Start row 4: [1, 1, 1, 1, 1]
#   Updated row[1] = 4
#   Updated row[2] = 6
#   Updated row[3] = 4
# Final row 4: [1, 4, 6, 4, 1]

# Pascal's Triangle:
# [1]
# [1, 1]
# [1, 2, 1]
# [1, 3, 3, 1]
# [1, 4, 6, 4, 1]
