number = [10, 20, 30, 40, 50]
fruits = ["Apple", "Banana", "Cherry"]
mixed = [1, "two", 3.0, True, 120,[1,2,3]]
empty = []
nested = [[1, 2, 3, 4, 5], [10, 20, 30], [100, 200, 300, 400]]
name = list("Ahmed")
range = list(range(1, 10))
age = "Ahmed"
print (type(age))
print (nested[1][1])
print ("Mixed", mixed)
print (fruits)
fruits [0] = "Blueberry"
print (fruits)
print (number[0:2])
fruits.append("Banana2")
print (fruits)
fruits = []
fruits.insert(0, "Apple")
print (fruits)
fruits = ["Apple"]
fruits2 = ["Banana", "Berry"]
fruits.extend(fruits2)
print (fruits)
fruits.remove("Banana")
print (fruits)
fruits.pop()
print (fruits)
fruits.clear()
print (fruits)
fruits.append("Apple")
fruits.append("Banana")
print (fruits.index("Banana"))
numbers = [3,5,6,7,1,0,9,8,4,2,10]
print (numbers)
numbers.sort()
print (numbers)
numbers.sort(reverse=True)
print (numbers)
print (len(numbers))
print ("Apple" in fruits)
print ("Apple" not in fruits)
a, b = [1,2,3], [4,5,6]
print (a + b)
print (a * 3)
print (sum(a + b))
