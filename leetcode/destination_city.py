#1436 Destination City
# You are given the array paths, where paths[i] = [cityAi, cityBi] means there exists a direct path going from cityAi to
# cityBi. Return the destination city, that is, the city without any path outgoing to another city.
# It is guaranteed that the graph of paths forms a line without any loop, therefore, there will be exactly one destination city.

class Solution(object):
    def destCity1(self, paths):
        """
        :type paths: List[List[str]]
        :rtype: str
        """
        cityA = []
        cityB = []
        for p in paths:
            cityA.append(p[0])
            cityB.append(p[1])
        res = set(cityB) - set(cityA)
        return ''.join(res)

    def destCity2(self, paths):
        """
        :type paths: List[List[str]]
        :rtype: str
        """
        cityA = [p[0] for p in paths]
        for p in paths:
            if p[1] not in cityA:
                return p[1]
