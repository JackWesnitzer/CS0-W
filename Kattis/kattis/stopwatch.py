N = int(input())
if(N%2 == 1):
    print("still running")
else:
    i = 0
    diff = 0
    while True:
        t1 = int(input())
        t2 = int(input())
        diff += t2-t1
        i += 2
        if(i == N):
            break
    print(diff)
