def knows(a, b):
    matrix = [ [0, 0, 1, 0],
               [0, 0, 1, 0],
               [0, 0, 0, 0],
               [0, 0, 1, 0] ]
    return matrix[a][b]

def findCelebrity(n):
    potential = 0
    for i in range(1,n):
        if knows(potential,i):
            potential = i
    
    for i in range(n):
        if i != potential:
            if not knows(i,potential):
                return -1
            if i < potential and knows(potential, i):
                return -1
    return potential


if __name__ == "__main__":
    
    # matrix = [ [0, 0, 1, 0],
    #            [0, 0, 1, 0],
    #            [0, 0, 0, 0],
    #            [0, 0, 1, 0] ]
   
    id = findCelebrity(4)
    if id == -1:
        print("No celebrity")
    else:
        print(f"Celebrity ID {id}")

        