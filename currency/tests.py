from currency.Currency import Currency


cur = Currency("EUR")
cur.add_denomination(1)
cur.add_denomination(3)
cur.add_denomination(5)
cur.add_denomination(7)

cur.del_denomination(3)

print(cur.min_denomination(1))
print(cur.max_denomination(5))

print(cur.next_denomination(7))
print(cur.prev_denomination(1))

print(cur.has_denominations())
print(cur.num_denominations())

cur.clear_denominations()
print()
for i in range(1, 16):
    cur.add_denomination(i*i)

for i in cur.iter_denominations():
    print(i)
for i in cur.iter_denominations(True):
    print(i)

cur.add_change("ZZZ", 10)
cur.add_change("USD", 10)
cur.add_change("ASD", 199)

cur.remove_change("ASD")
cur.add_change("ASD", 19.983475823498572394857902348750931)
cur.add_change("AWD", 12)
cur.remove_change("ASD")
cur.remove_change("ZZZ")


cur.update_change("ASD", 13.45)

print(cur.get_change("ASD"))


cur_copy = cur.copy()
print(cur._changes == cur_copy._changes)
print(cur._denominations == cur_copy._denominations)
print(cur._code == cur_copy._code)
print(cur._changes is cur_copy._changes)
print(cur._denominations is cur_copy._denominations)
print(cur._code is cur_copy._code)

cur_copy.update_change("USD", 10)
print(cur.get_change("USD"))
print(cur_copy.get_change("USD"))
cur.update_change("USD", 5)
print(cur.get_change("USD"))
print(cur_copy.get_change("USD"))
cur_copy.update_change("USD", 2)
print(cur.get_change("USD"))
print(cur_copy.get_change("USD"))

print("\n\n\n")

cur_deepcopy = cur.deep_copy()
cur_deepcopy.update_change("USD", 10)
print(cur.get_change("USD"))
print(cur_deepcopy.get_change("USD"))
cur.update_change("USD", 5)
print(cur.get_change("USD"))
print(cur_deepcopy.get_change("USD"))
cur_deepcopy.update_change("USD", 2)
print(cur.get_change("USD"))
print(cur_deepcopy.get_change("USD"))


for i in cur.iter_denominations():
    print(i)

cur_copy.add_denomination(1010)
for i in cur.iter_denominations():
    print(i)

cur_deepcopy.add_denomination(1010)
for i in cur_deepcopy.iter_denominations():
    print(i)

cur_copy.del_denomination(1)
for i in cur.iter_denominations():
    print(i)

cur_deepcopy.del_denomination(225)
for i in cur.iter_denominations():
    print(i)