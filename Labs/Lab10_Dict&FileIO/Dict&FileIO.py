"""
File I/O Lab with Dictionary

Update By: Jack K. Neckels-Wesnitzer

CSCI 110
Date: 4/11/23

Program finds the frequency of words in a given text document and print top 10 most
common words using dictionary and tuple data structures.
"""

def readText():
    """
    opens a file reads its contents and
    creates a histogram of words based on frequency using dictionary data structure
    """
    fileOk = False
    fin = None
    hist = {tuple()}
    # stores data in this form: hist = {'and': 10, 'python':15}
    # where 'and' appears 10 times and
    # python appears 15 times

    while not fileOk:
        fileName = input('Enter input text file => ')
        try:
            fin = open(fileName, 'r')
            fileOk = True
        except Exception as ex:
            print('Exception occured: ', ex)

    lines = fin.readlines()
    for line in lines:
        line = line.strip().lower()
        if line:
            # FIXME3
            # update words; split line into list of words and store the list into words object
            words = line.split()
            for word in words:
                hist[words] += 1
            else:
                hist[words] -= 1
                # FIXME4
                # if word exists as key in hist dict, increment the value by 1
                # else add word as new key with value 1 in hist dict
            return word

def reverseHistogramList(histDict):
    """
    given someDict,  returns list of tuples in descending order based 
    frequency of each word in histDict
    """
    reverseList = [(key, val) for key, val in histDict.items()]
        # FIXME5 - #FIXED#
        # append tuple with values in (val, key) order into reverseList list
    reverseList.sort(key = lambda x: x[1], reverse = True)

    # FIXME6
    # Sort the list reverseList in reverse order
    
    print(reverseList[:10])

def main():
    
    histogram = readText()
    # FIXME7 - Comment the following statement out when done
    print(histogram)  # see the output to understand what's going on so far

    aList = reverseHistogramList(histogram)

    # FIXME8 – print top 10 words with highest frequencies stored in aList
    print("10 most common words:")
    print(aList)

if __name__ == "__main__":
    main()