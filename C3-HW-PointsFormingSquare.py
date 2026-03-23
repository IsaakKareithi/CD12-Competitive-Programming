# python program to check whether
# four points form a square

def checkSquare(a, b, c, d):
    dp = [[0 for i in range(10)]
          for i in range(10)]
    presum = [[0 for i in range(10)]
              for j in range(10)]
    points = [a, b, c, d]

    #Calculating the horizontal dist
    for i in range(4):
        for j in range
    