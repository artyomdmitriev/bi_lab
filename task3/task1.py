list1 = [a + b for a in 'ab' for b in 'bcd']
print(list1)

sliced_list1 = list1[::2]
print(sliced_list1)

list2 = [str(i) + "a" for i in range(1, 5)]
print(list2)

print(list2.pop(1))

list2_copy = list2.copy()
list2_copy.append('2a')
print(list2_copy)
