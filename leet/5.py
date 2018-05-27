import sys


class Solution:
    # noinspection PyMethodMayBeStatic
    def findRadius(self, houses, heaters):
        """
        :type houses: List[int]
        :type heaters: List[int]
        :rtype: int
        """
        houses = sorted(houses)
        heaters = sorted(heaters)

        maximum = 0
        for house in houses:
            i = 0
            distance = sys.maxsize
            index = i
            while i < len(heaters) and abs(house - heaters[i]) < distance:
                index = i
                distance = abs(house - heaters[i])
                i += 1

            radius = abs(house - heaters[index])
            if radius > maximum:
                maximum = radius

        return maximum


s = Solution()
assert s.findRadius([282475249, 622650073, 984943658, 144108930, 470211272, 101027544, 457850878, 458777923],
                    [823564440, 115438165, 784484492, 74243042, 114807987, 137522503, 441282327, 16531729, 823378840, 143542612]) == 161834419
assert s.findRadius([1, 2, 3, 4], [1, 4]) == 1
assert s.findRadius([1, 2, 3], [2]) == 1
assert s.findRadius([1, 3], [2]) == 1
