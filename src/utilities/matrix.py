from src.utilities.enums.directions import Directions

class Matrix:

    def countCharsInDirection(matrix = [], target = '', direction = Directions.RIGHT, maxCount = -1):
        count = 0
        for i in range (0, len(matrix)):
            for j in range (0, len(matrix[i])):
                if matrix[i][j] == target:
                    newCount = 1

                    if direction == Directions.UP:
                        for up in range (i-1, -1 or newCount == maxCount, -1):
                            if matrix[up][j] == target:
                                newCount +=1
                            else:
                                break
                    elif direction == Directions.DOWN:
                        #TODO code logic
                        return -1
                    elif direction == Directions.LEFT:
                        #TODO code logic
                        return -1
                    elif direction == Directions.RIGHT:
                        #TODO code logic
                        return -1
                    elif direction == Directions.UP_LEFT:
                        #TODO code logic
                        return -1
                    elif direction == Directions.UP_RIGHT:
                        #TODO code logic
                        return -1
                    elif direction == Directions.DOWN_LEFT:
                        #TODO code logic
                        return -1
                    elif direction == Directions.DOWN_RIGHT:
                        #TODO code logic
                        return -1

                    if newCount > count:
                        count = newCount
                    if count == maxCount:
                        return count
        return count