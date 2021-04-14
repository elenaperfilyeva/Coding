#1103 Distribute Candies to People
# We distribute some number of candies, to a row of n = num_people people in the following way:
#
# We then give 1 candy to the first person, 2 candies to the second person, and so on until we give n candies
# to the last person.
#
# Then, we go back to the start of the row, giving n + 1 candies to the first person, n + 2 candies to the second person,
# and so on until we give 2 * n candies to the last person.
#
# This process repeats (with us giving one more candy each time, and moving to the start of the row after we reach the end)
# until we run out of candies.  The last person will receive all of our remaining candies (not necessarily
# one more than the previous gift).
#
# Return an array (of length num_people and sum candies) that represents the final distribution of candies.

class Solution(object):
    def distributeCandies(self, candies, num_people):
        """
        :type candies: int
        :type num_people: int
        :rtype: List[int]
        """
        distributed_candies = [0]*num_people
        current_person = 0
        current_candies = 1
        while candies > 0:
            if current_person < num_people:
                if candies-current_candies>=0: distributed_candies[current_person]+=current_candies
                else: distributed_candies[current_person]+=candies
                candies-=current_candies
                current_candies+=1
                current_person+=1
            else:
                current_person = 0
                if candies-current_candies>=0: distributed_candies[current_person]+=current_candies
                else: distributed_candies[current_person]+=candies
                candies-=current_candies
                current_candies+=1
                current_person+=1
        return distributed_candies
