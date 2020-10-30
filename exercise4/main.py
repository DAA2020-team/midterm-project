"""
Implement a function change(value, currency), where value is a float number with at most
two decimal points and currency is an object of the class Currency.
The function must use a PriorityQueue to return the minimum number of coins of the given
currency that sums up to the given value. E.g.: on input 12,85 and EUR currency, the
function must return 6 corresponding to 10+2+0,50+0,20+0,10+0,5. Note that the function is
required to return both the number and the list of the corresponding coins.
"""
from currency.Currency import Currency
from data_structures.heap_priority_queue import HeapPriorityQueue


def change(value, currency, decimal=2):
    needed_denominations = [(e, e) for e in currency.iter_denominations(reverse=True) if e <= value]
    queue = HeapPriorityQueue(contents=needed_denominations)
    used_den = []
    while round(value, decimal) > 0:
        m, _ = queue.remove_max()
        while round(value - m, decimal) >= 0:
            value = round(value - m, decimal)
            used_den.append(round(m, decimal))
    return used_den, len(used_den)


def test(n=10000, step=100, manual=False):
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


def get_currency(c="EUR"):
    cur = Currency(c)
    d = [0.01, 0.02, 0.05, 0.1, 0.2, 0.5, 1, 2, 5, 10, 20, 50, 100, 200, 500]
    for i in d:
        cur.add_denomination(i)
    return cur


def main():
    cur = get_currency()
    dens, den_number = change(0, cur)
    print(dens)
    print(den_number)


if __name__ == '__main__':
    main()
    test(manual=False)
