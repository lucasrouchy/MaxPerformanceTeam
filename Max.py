import bisect

#Binary Insert
#the team is hired from the most efffecient people to the less.
class Solution:
    def maxPerformance(n: int, speed: 'list[int]', efficiency: 'list[int]', k: int) -> int:
        #efffiecency list to insert the sorted list
        e = []
        #setting res and sum to zero
        res = sumSpeed = 0
        # iterates through the sorted tuple of efficiency and speed
        for i, s in sorted(zip(efficiency, speed), reverse=1):
            #bisect and insort used to ffind and place the number in the right spot of the list so it remains sorted
            bisect.insort(e, -s)
            #sum is updated to reflect the sum of the speeed of the team
            sumSpeed += s
            #if the length of the list is greater than the amount of people you can hire on your team(k)
            if len(e) > k:
                #sum is updated to reflect the team laying off the engineer with the smallest speed
                sumSpeed += e.pop()
            #res is equal to the sum 
            res = max(res,sumSpeed * i)
        return res % (10**9 + 7)
    print(6, [2,10,3,1,5,8], [5,4,3,9,7,2], 2 )
    print(maxPerformance(6, [2,10,3,1,5,8], [5,4,3,9,7,2], 2 ))
    print(7, [20,25, 440, 2, 3, 5, 10], [1, 1, 20, 30, 50, 60, 70], 4)
    print(maxPerformance(7, [20,25, 440, 2, 3, 5, 10], [1, 1, 20, 30, 50, 60, 70], 4))
        

