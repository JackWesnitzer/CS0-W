# NAME Jack K. Neckels-Wesnitzer
# DATE 2/16/23

from tkinter.tix import MAX


def slope(x1, y1, x2, y2):
    return ((y2-y1)/(x2-x1))

def intercept(x1, y1, x2, y2,):
    m = (y2-y1)/(x2-x1)
    b = (y1-m*x1)
    return b

def mid_point(x1, y1, x2, y2):
    mid_point_of_x = (x2-x1)/2
    mid_point_of_y = (y2-y1)/2
    return mid_point_of_x,mid_point_of_y


def test_slope():
    assert slope(5, 3, 4, 2) == 1.0
    assert slope(1, 2, 3, 2) == 0.0
    assert slope(1, 2, 3, 3) == 0.5
    assert slope(2, 4, 1, 2) == 2.0
    print('all test cases passed for slope()')

def test_intercept():
    assert intercept(1, 6, 3, 12) == 3.0
    assert intercept(6, 1, 1, 6) == 7.0
    assert intercept(4, 6, 12, 8) == 5.0
    print('all test cases passed for intercept()')

def test_mid_point():
    assert mid_point(0, 0, 2, 2) == (1,1)
    assert mid_point(1, 2 , 3, 2) == (1, 0.0)
    assert mid_point(3, 6, 12, 8) == (4.5, 1.0)
    print ('all test cases passed for mid_point()')

test_slope()
test_intercept()
test_mid_point()