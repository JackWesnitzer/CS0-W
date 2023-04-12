
def answer(name):
    repeat = ''
    for i in range(len(name)):
        if i == 0:
            repeat += name[i]
        else:
            if (name[i] != name[i-1]):
                repeat += name[i]
    return repeat

def testFunctions():

    assert(answer('Alfreeeed')) == 'Alfred'
    assert(answer('Daaaaaviiiiid')) == 'David'
    assert(answer('Thooomaaas')) == 'Thomas'
    assert(answer('Weeeeendy')) == 'Wendy'
    assert(answer('Cooouurtneey')) == 'Courtney'

name = input('Enter an Apaxiaan name: ')
print(answer(name))

testFunctions()
print('All test cases passed...')