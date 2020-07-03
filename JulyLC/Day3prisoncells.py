class Solution:
    def prisonAfterNDays(self, cells: List[int], N: int) -> List[int]:
        def flipCells(current_row):
            new_row = []
            for i in range(len(cells)):
                if i - 1 > -1 and i + 1 < len(cells):
                    if current_row[i-1] == current_row[i+1]:
                        new_row.append(1)
                    else:
                        new_row.append(0)
                else:
                    new_row.append(0)
            return new_row

        N = N%14 + 14
        while N > 0:
            #print(cells)
            cells = flipCells(cells)
            N -= 1

        return cells