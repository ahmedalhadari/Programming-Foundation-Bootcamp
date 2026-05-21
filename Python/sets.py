colors = {"Red", "Blue", "Green"}
print(type(colors))

numbers = {1, 2, 3, 4, 5}
mixed = {1, "two", 3.5, 2, 1, True, (4, 5)}
print(mixed)
empty_set = set()
print (empty_set)
set1 = set ([1,2,3,4,5,6])
print (set1)
set1 = set("Hello")
print (set1)
set1 = set(range(10))
set1 = set(range(5,10))
print (set1)
numbers = set ([10, 5, 2, 20])
numbers.add(20)
print (numbers)
numbers.update([4, 5, 6, 7])
numbers.remove(20)
print (numbers)
numbers.discard(10)
print (numbers)
numbers.pop()
print (numbers)
numbers.clear()
print (numbers)
set1 = {1,2,3}
set2 = {4,5,6}
print (set1 | set2)
print (set1.union(set2))
