#Jack K Neckels-Wesnitzer
#3/8/23
# Kattis Problem: Height Ordering
#Algorithm steps:
#1) input n for number of following
#2) input a line of text and turn it into a list of numbers
#3) cycle through list, if we see a number greater than last, the student steps back

def main():
    n_line = int(input())

    for i in range(n_line):
        in_list =list(map(int, input().split()))
        k = in_list[0]
        order_list = []
        order_list.append(in_list[1])
        students = in_list[2::]

        steps = 0
        for stud in students:
            added = False
            index = 0
            for s in order_list:
                if (stud < s):
                    steps = steps + len(order_list[index::])
                    order_list.insert(index, stud)
                    added = True
                    break
                index += 1
            if(not added):
                order_list.append.stud

        print(f"{k} {steps}")
    
if __name__ == "__main__":
    main()
