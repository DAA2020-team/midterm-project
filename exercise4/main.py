import sys
sys.path.append('../midterm-project')

"""
Implement a function change(value, currency), where value is a float number with at most
two decimal points and currency is an object of the class Currency.
The function must use a PriorityQueue to return the minimum number of coins of the given
currency that sums up to the given value. E.g.: on input 12,85 and EUR currency, the
function must return 6 corresponding to 10+2+0,50+0,20+0,10+0,5. Note that the function is
required to return both the number and the list of the corresponding coins.
"""
from exercise2.currency import Currency
from data_structures.heap_priority_queue import HeapPriorityQueue
from typing import Tuple, List


def change(value, currency, decimal=2) -> Tuple[List, int]:
    """
    Given a currency with standard denominations, returns the list and mimimum number of denominations that
    sum up to the parameter value. The parameter decimal is used to round the values due to the
    floating-point errors.
    :param value: the amount that will be divided into denominations
    :param currency: instance of the Currency class
    :param decimal: number of decimal points
    :return: a 2 element tuple, the list of the used denominations and its length
    """
    needed_denominations = [(e, e) for e in currency.iter_denominations(reverse=True) if e <= value]
    # Because this list is contructed in a decreasing order, it can be considered as an array rappresentation
    # of an heap. Hence, during the initialization of the ADT PriorityQueue, it is unnecessary to perform the
    # the heapify operation (which will check the entire array leaving as it is). The parameter is_sorted, is
    # used to indicate that the list is already sorted in such a way that it is a valid array rappresentation
    # of an heap.
    queue = HeapPriorityQueue(contents=needed_denominations, is_sorted=True)
    if queue.is_empty():
        raise ValueError("The currency " + str(currency._code) + " does not have any denomination.")
    used_den = []
    while round(value, decimal) > 0:
        if queue.is_empty():
            raise ValueError("The value and the denominations are not compatible (e.g. value is 1.01 and the smaller "
                             "denomination is 1.0).")
        m, _ = queue.remove_max()
        while round(value - m, decimal) >= 0:
            value = round(value - m, decimal)
            used_den.append(round(m, decimal))
    return used_den, len(used_den)


def test(n=3000, step=100, manual=False):
    """
    Test function to test the implementation of the change function.
    :param n: number of tests to perform
    :param step: how often the progress of the test will be printed, in test
    :param manual: if True, prints the return value of the fucntion change and waits for an "Enter" key input;
                    otherwise, the test will run automatically.
    :return: None
    """
    import random
    c = get_currency()
    for t in range(n):
        v = random.randint(1, 100000) / 100.0
        l, _ = change(v, currency=c)
        if t % step == 0:
            print("Test: " + str(t) + "/" + str(n))
        if manual:
            print(str(v) + ": " + str(l) + " --- Sum: " + str(round(sum(l), 2)))
            input("")
        assert(round(sum(l), 2) == round(v, 2))
    print(f"{n} tests completed")


def get_currency(c="EUR", d=None):
    """
    Method to create easily a currency with standard denominations, if none is provided.
    :param c: the currency name
    :param d: the list of denominations to be used
    :return: the new currency
    """
    if d is None:
        d = [0.01, 0.02, 0.05, 0.1, 0.2, 0.5, 1, 2, 5, 10, 20, 50, 100, 200, 500]
    cur = Currency(c)
    for i in d:
        cur.add_denomination(i)
    return cur


def main():
    cur = get_currency(d=[])
    dens = []
    den_number = 0
    try:
        dens, den_number = change(123.52, cur)
    except ValueError as e:
        print(e)
    print(dens)
    print(den_number)


if __name__ == '__main__':
    main()
    test(n=10, manual=True)
