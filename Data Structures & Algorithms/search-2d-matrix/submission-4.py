class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:

        matrix_pointer_l = 0
        matrix_pointer_r = len(matrix) - 1

        middle_finding = None

        # go through the array of arrays

        while matrix_pointer_l <= matrix_pointer_r:
            matrix_pointer_m = (matrix_pointer_r + matrix_pointer_l) // 2

            middle_low = matrix[matrix_pointer_m][0]
            middle_high = matrix[matrix_pointer_m][-1]
            if middle_low <= target <= middle_high:
                # print(f"{target} is greater than {middle_low} and {target} is less than {middle_high}")
                # print("testing ", matrix_pointer_m)
                middle_finding = matrix_pointer_m
                break
            elif target < middle_low:
                matrix_pointer_r = matrix_pointer_m - 1
            else:
                matrix_pointer_l = matrix_pointer_m + 1

        if middle_finding == None:
            return False
       
        arr = matrix[middle_finding] 

        l, r = 0, len(arr) - 1

        while l <= r:
            m = ((r + l) // 2)
            # print(arr[l:r], l,m,r)
            if arr[m] == target:
                return True
                break

            elif arr[m] < target:
                l = m + 1
            else:
                r = m - 1

        return False
        