from heapq import heappop, heappush

def distance(s, f):
    ans = []
    p = []

    # push elements into list
    for i, j in zip(s, f):
        heappush(p, (j,i))

    it = heappop()
    start = it[1]
    end = it[0]
    ans.append(it)

    print("The closest pair of numbers are:")
    for f, s in ans:
        print(f"{s}{f}")

# Driver code 
if __name__ == "__main__":
    s = [1, 3, 0, 5, 8, 5]
    finish = [2, 4, 6, 7, 9, 9]

    # Function call 
    distance(s, finish)