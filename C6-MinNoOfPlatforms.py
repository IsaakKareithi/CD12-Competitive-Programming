# program to find minimum number of platforms
# required for a train/bus station
def findPlatform(arr, dep, n):
    """
    accepts two arrays with arrival and departure time
    and the size of the array
    Returns minimum number of platforms required.
    """

    # plat_needed indicates number of 
    # platforms needed at a time
    plat_needed = 1
    result = 1

    # run a nested loop to find a overlap
    for i in range(n):
        # minimum number of platforms needed
        plat_needed = 1

        for j in range(n):
            # Check for overlap
            if i != j:
                if (arr[i] >= arr[j] and dep[j] >= arr[i]):
                    plat_needed += 1

            # update result
        result = max(result, plat_needed)

    return result

# Driver code

def main():
    arr = [100, 300, 200, 500]
    dep = [900, 400, 550, 600]

    n = len(arr)

    print("{}".format(
        findPlatform(arr, dep, n)))
    
if __name__ == "__main__":
    main()