
answer = 'HE GOT AWAY'
ans2 = ""
for i in range(1,6):
    string = input('Enter a registration code: ')
    if string.find('FBI') != -1:
        ans2 = ans2 +str(i) + ' '
if ans2 == "":
    print(answer)
else:
    print(ans2)
