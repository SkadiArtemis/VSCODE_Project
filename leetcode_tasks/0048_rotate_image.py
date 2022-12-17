class Solution:
    def rotate(self, matrix):
        for row in range(len(matrix) // 2):
            for col in range(len(matrix[0])):
                matrix[row][col], matrix[len(matrix) -1 - row][col] = \
                matrix[len(matrix) - 1 - row][col], matrix[row][col]


        for col in range(0, len(matrix[0])):
            for row in range(0, col):
                matrix[row][col], matrix[col][row] = \
                matrix[col][row], matrix[row][col]