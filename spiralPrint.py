class Solution:
    # @param A : tuple of list of integers
    # @return a list of integers
    def spiralOrder(self, A):
        result = []
        ## Actual code to populate result

        top = 0
        bottom = len(A) - 1
        left = 0
        right = len(A[0]) - 1

        """
        0: left to right
        1: top to bottom
        2: right to left
        3: bottom to top
        """
        direction = 0

        row = 0
        col = 0

        while top <= bottom and left <= right:
            if direction == 0:  # left -> right
                # row += 1
                # if row >= right:
                #     direction = 1
                #     top +=1
                for i in range(left,right+1):
                    result.append(A[top][i])
                top += 1
                direction = 1
            elif direction == 1: # top -> bottom
                # col += 1
                # if col >= bottom:
                #     direction = 2
                #     right -= 1
                for i in range(top,bottom + 1):
                    result.append(A[i][right])
                right -= 1
                direction = 2
            elif direction == 2:  # right -> left
                # row -= 1
                # if row <= left:
                #     direction = 3
                #     bottom -= 1
                for i in range(right,left-1, -1):
                    result.append(A[bottom][i])
                bottom -= 1
                direction = 3
            elif direction == 3:
                # col -= 1
                # if col <= top:
                #     direction = 0
                #     left += 1
                for i in range(bottom,top-1, -1):
                    result.append(A[i][left])
                left += 1
                direction = 0
            # result.append(A[col][row])

        return result


if __name__=='__main__':
    x = Solution()
    print(x.spiralOrder([[1]]))
    print(x.spiralOrder([[1, 2, 3],
        [4, 5, 6],
        [7, 8, 9]]))
