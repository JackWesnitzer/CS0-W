string = [input('Enter a registration code: ') for _ in range(1,6)]

index = []
for i in range(len(string)):
   
    if "FBI" in string[i]:
        index.append(str(i+1))
if index:
    print(" ".join(index))
else:
    print('HE GOT AWAY!')
# I tried a couple of different solutions, but kattis did'nt like this one or the one that we tried to develope together.
# Seems like the problem lies in the "range" function because kattis highlights that portion of code when I review it.
# Not sure what I'm doing wrong but I tried my best.