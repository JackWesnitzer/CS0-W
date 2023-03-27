line = input()

def histogram(word, hist):
    for c in word:
        c = c.lower()
        if c in hist: # if the key already exists, add 1 to the value
            hist[c] += 1
        else: # if the key doesn't exist, create it and set value to 1
            hist[c] = 1

h = {}
histogram(line, h)
c = 0
t = 0
g = 0
if 't' in h:
    t = h['t']
if 'c' in h:
    c = h['c']
if 'g' in h:
    g = h['g']

min_set = c
if t<min_set:
    min_set = t
if g<min_set:
    min_set = g

score = t**2 + c**2 + g**2 + 7*min_set
print(score)