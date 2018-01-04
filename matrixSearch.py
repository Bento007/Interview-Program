class Solution:
    # @param A : list of list of integers
    # @param B : integer
    # @return an integer
    def searchMatrix(self, A, B):
        found = 0

        first = 0
        last = len(A) - 1
        mid = len(A) // 2

        while (first <= last and not found):
            current = A[mid]

            # check upper
            if B > current[0]:
                first = mid + 1
                mid = mid + mid // 2
                found = self.binSearch(current, B)
            # check lower
            elif B < current[0]:
                last = mid - 1
                mid = mid - mid // 2
            # check equal
            elif B == current[0]:
                found = 1

        return found

    def binSearch(self, A, B):
        found = False

        first = 0
        last = len(A) - 1
        mid = len(A) // 2

        while (first <= last and not found):
            current = A[mid]

            if B > current:  # check upper
                first = mid + 1
                mid = mid + mid // 2
            elif B < current:  # check lower
                last = mid - 1
                mid = mid - mid // 2
            elif B == current:  # check equal
                found = 1

        return found


if __name__=='__main__':
    x = Solution()

    solution = x.searchMatrix([
                              [3],
                              [29],
                              [36],
                              [63],
                              [67],
                              [72],
                              [74],
                              [78],
                              [85]
                            ], 41)
    solution = x.searchMatrix([
                  [1,   3,  5,  7],
                  [10, 11, 16, 20],
                  [23, 30, 34, 50]
                    ], 3)