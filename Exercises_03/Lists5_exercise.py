
#testing remove
my_list = ["One","Two","Three"]
print(my_list)
print('Testing .remove')
my_list.remove("One")
print(my_list)

#testing count
fruits = ['orange', 'apple', 'pear', 'banana', 'kiwi', 'apple', 'banana']
x = fruits.count('apple')
print(x)

#testing index
fruits = ['pear', 'orange', 'apple', 'pear', 'banana', 'kiwi', 'apple', 'banana']
x = fruits.index('pear')
print(x)
x = fruits.index('pear',1)
print(x)

#testing reverse
fruits = ['pear', 'orange', 'apple', 'pear', 'banana', 'kiwi', 'apple', 'banana']
x = fruits.reverse()
print(fruits)

#testing sort
fruits = ['pear', 'orange', 'apple', 'pear', 'banana', 'kiwi', 'apple', 'banana']
x = fruits.sort()
print(fruits)