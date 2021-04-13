#1496 Path Crossing
# Given a string path, where path[i] = 'N', 'S', 'E' or 'W', each representing moving one unit north, south, east,
# or west, respectively. You start at the origin (0, 0) on a 2D plane and walk on the path specified by path.
#
# Return True if the path crosses itself at any point, that is, if at any time you are on a location you've
# previously visited. Return False otherwise.

class Solution(object):
    def isPathCrossing1(self, path):
        """
        :type path: str
        :rtype: bool
        """
        current_position_arr = [[0,0]]
        current_position = current_position_arr[0]
        for el in path:
            if el == 'N':
                current_position = [current_position[0]+1, current_position[1]]
                if current_position in current_position_arr:
                    return True
                current_position_arr.append(current_position)
            elif el == 'S':
                current_position = [current_position[0]-1, current_position[1]]
                if current_position in current_position_arr:
                    return True
                current_position_arr.append(current_position)
            elif el == 'E':
                current_position = [current_position[0], current_position[1]+1]
                if current_position in current_position_arr:
                    return True
                current_position_arr.append(current_position)
            elif el == 'W':
                current_position = [current_position[0], current_position[1]-1]
                if current_position in current_position_arr:
                    return True
                current_position_arr.append(current_position)
        return False

    def isPathCrossing2(self, path):
        """
        :type path: str
        :rtype: bool
        """
        move = {
            'N': [1, 0],
            'S': [-1, 0],
            'E': [0, 1],
            'W': [0, -1]
        }

        visited = set()
        visited.add((0, 0))
        x, y = 0, 0
        for el in path:
            x += move[el][0]
            y += move[el][1]
            if (x, y) in visited:
                return True
            visited.add((x, y))
        return False
