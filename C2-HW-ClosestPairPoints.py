import heapq

def distance(s, f):
    # Check if input lists are the same length
    if len(s) != len(f):
        print("Error: Start and finish lists must have the same length.")
        return

    # Create a list of tuples, (finish_time, start_time), for use with the min-heap
    activities = []
    for start, finish in zip(s, f):
        activities.append((finish, start))
    
    # Use heapq.heapify to efficiently create a min-heap sorted by finish time
    heapq.heapify(activities)
    """
    # The original function seems to be an attempt at finding an optimal schedule (Activity Selection Problem)
    # The user request asks to "fix this" to find the "closest pair of numbers" (likely shortest 'distance' or duration).
    # We will assume "closest pair" means the activity with the shortest duration.

    # Find the activity with the minimum duration
    # Duration is finish - start. We can sort by duration after popping elements or calculate durations.
    # To find the single shortest duration efficiently, we can add duration to the heap tuple
    """
    duration_activities = []
    for start, finish in zip(s, f):
        duration = finish - start
        if duration >= 0: # Ensure valid duration
            # Push (duration, start, finish) into the heap
            heapq.heappush(duration_activities, (duration, start, finish))
    
    if not duration_activities:
        print("No valid activities found.")
        return

    # Pop the element with the minimum duration
    min_duration, start, finish = heapq.heappop(duration_activities)
    
    print(f"The activity with the shortest duration is: start={start}, finish={finish}, duration={min_duration}")

# Driver code
if __name__ == "__main__":
    s = [1, 3, 0, 5, 8, 5]
    finish = [2, 4, 6, 7, 9, 9]
    # Function call
    distance(s, finish)
