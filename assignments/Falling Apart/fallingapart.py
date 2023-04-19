def testFunction(): # comment all of this function out when running in kattis
    p = [2,3,4,3]
    p2 = [1,4,1,2]
    p3 = [2,1,2,3]
    assert(solution(p)) == (7,5)
    assert(solution(p2)) == (5,3)
    assert(solution(p3)) == (5,3)
    print("All test cases pass...")

def solution(pieces):

    alice = 0 # alice starts with zero pieces
    bob = 0 # bob starts with zero pieces

    while pieces: # while there are still pieces left to choose from...
        alice += max(pieces) # alice goes first, she chooses the highest value piece available, adds it to her pile
        pieces.remove(max(pieces)) # remove the highest value piece from the pieces in the pile
        if pieces: # if there are pieces left after alice takes her turn, bob chooses the highest value piece available
            bob += max(pieces) # bob adds his piece to his pile
            pieces.remove(max(pieces)) # removes the piece bob chose from the main pile
    return(alice, bob)

n = int(input()) # enter the number of pieces available to choose from

pieces = [int(x) for x in input().split()] # assign a value to each piece, seperated by spaces
alice, bob = solution(pieces)

print(alice, bob) # when no pieces are left, nobody tkaes a turn and the total is calculated

testFunction()