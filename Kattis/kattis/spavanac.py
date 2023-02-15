#Written by Jack Wesnitzer
#Kattis Problem Spavanac
#date 2/15/23

H, M = input().split()
H = int(H)
M = int(M)

#print(f'H = {H}. M = {M}')

minutes_passed_in_the_day = H*60+M

minutes_passed_in_the_day -= 45

minutes_passed_in_the_day += 1440

alarm_hour = int(minutes_passed_in_the_day/60)%24
alarm_minutes = int(minutes_passed_in_the_day%60)

print(f'{alarm_hour} {alarm_minutes}')