def printJobScheduling(arr, t):
    #length of array
    n = len(arr)

    # Sort all jobs according to decreasing order of profit 
    for i in range(n):
        for j in range(n-1-i):
            if arr[j][2] < arr[j+1][2]:
                arr[j], arr[j+1] = arr[j+1], arr[j]

    # to keep track of all free time slots
    result = [False]*t
    job = ['-1'] * t

    # Iterate through all given jobs 
    for i in range(len(arr)):

        # Find a free time slot for this job 
        # (We must start from the last possible slot)

        for j in range(min(t - 1, arr[i][1]-1), -1, -1):

            # Freee slot found
            if result[j] is False:
                result[j] = True
                job[j] = arr[i][0]
                break

    print(job)

if __name__ == '__main__':
    # Job array
    arr = [['a', 2, 100],
           ['b', 1, 19],
           ['c', 2, 27],
           ['d', 1, 25],
           ['e', 3, 15]
           ]
    
    print("The following is the maximum profit sequence of jobs: ", printJobScheduling(arr, 3))