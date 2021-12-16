from src.utilities.enums.directions import Directions

class Matrix:

    def countCharsInDirection(matrix = [], target = '', direction = Directions.RIGHT, maxCount = -1):
        count = 0
        direction = direction.value
        for i in range (0, len(matrix)):
            for j in range (0, len(matrix[i])):

                if matrix[i][j] == target:
                    newCount = 1
                    row = i
                    column = j
                    while (row+direction[0] < len(matrix) and column+direction[1] < len(matrix[0]) and newCount != maxCount):
                        if matrix[row+direction[0]][column+direction[1]] == target:
                            newCount +=1
                            row += direction[0]
                            column += direction[1]
                        else:
                            break

                    if newCount > count:
                        count = newCount
                    if count == maxCount:
                        return count
        return count