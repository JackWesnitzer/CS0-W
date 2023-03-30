string = [input('Enter a registration code: ') for _ in range(1,6)]

index = []
for i in range(len(string)):
   
    if "FBI" in string[i]:
        index.append(str(i+1))
if index:
    print(" ".join(index))
else:
    print('HE GOT AWAY!')
