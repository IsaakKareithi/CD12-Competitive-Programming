# Python program for weighted job scheduling 
# using dynamic programming

# Importing all the following module to 
# Sort array based on our custom comparison function
from functools import cmp_to_key

# A list with start time, finish time and profit
class Job:
    def __init__(self, start, finish, profit):
        self.start = start
        self.finish = finish
        self.profit = profit

# A utility function that is used for sorting 
# events according to finish time
def jobComparator(s1, s2):
    return s1.finish < s2.finish

def latestNonConflict(arr, i):
    for j in range(i -1, -1, -1):
        if arr[j].finish <= arr[i-1].start:
            return j
    return -1

# The main function that returns the maximum possible
# Profit from given array of jobs

def findMaxProfit(arr, n):
    # Sort jobs accoring to finish times
    arr = sorted(arr, key=cmp_to_key(lambda s1, s2: s1.finish < s2.finish))

    #Create an array to store solutions of subproblems.
    # table[i] stores the profit for jobs till arr[i]
    # (including arr[i])
    table = [None] * n
    table[0] = arr[0].profit

    # Fill entries in table[] using recursive property
    for i in range(1, n):
        # Find profit including the current job
        incProf = arr[i].profit
        l = latestNonConflict(arr, i)
        if l != -1:
            incProf += table[l]

        # Store maximum of including and excluding 
        table[i] = max(incProf, table[i-1])
    
    # Store results 
    result = table[i-1]

    return result 

# Driver code
values = [(3, 10, 20),
          (1, 2, 50),
          (6, 19, 100),
          (2, 100, 200), ]

arr =[]
for i in values:
    arr.append(Job(i[0], i[1], i[2]))

n = len(arr)

#Print results
print("The optimal profit is: ", findMaxProfit(arr, n))