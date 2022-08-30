# A hotel manager has to process N advance bookings of rooms for the next season. His hotel has C rooms. Bookings contain an arrival date and a departure date. He wants to find out whether there are enough rooms in the hotel to satisfy the demand. Write a program that solves this problem in time O(N log N) .

# Input Format
# First argument is an integer array A containing arrival time of booking.
# Second argument is an integer array B containing departure time of booking.
# Third argument is an integer C denoting the count of rooms.

# Output Format
# Return True if there are enough rooms for N bookings else return False.
# Return 0/1 for C programs.

# Example Input
# Input 1:
#  A = [1, 3, 5]
#  B = [2, 6, 8]
#  C = 1

# Example Output
# Output 1:
#  0

# Example Explanation
# Explanation 1:
#  At day = 5, there are 2 guests in the hotel. But I have only one room.

class Solution:
    # @param arrive : list of integers
    # @param depart : list of integers
    # @param K : integer
    # @return a boolean
    def hotel(self, arrive, depart, K):
        ans = []
        
        for i in range(len(arrive)):
            ans.append([arrive[i], 1])
            ans.append([depart[i], 0])
        
        ans.sort()
        curr = 0
        active_rooms = 0
        
        for i in range(len(ans)):
            if ans[i][1] == 1:
                curr += 1
                
                active_rooms = max(active_rooms, curr)
                
                if active_rooms > K:
                    return 0
            
            else:
                curr -= 1
        
        return 1
