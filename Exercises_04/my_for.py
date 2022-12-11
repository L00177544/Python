iterable_variable = [1,2,3,4,5,6]

for item in iterable_variable:
 # For each item, execute this code block
 print(item)

iterable_variable = [1,2,3,4,5,6]
for item in iterable_variable:
 if item %2 != 0:
  print(item)
 
print('Print even numbers only')
iterable_variable = [1,2,3,4,5,6]
for item in iterable_variable:
 if item %2 == 0:
  print(item)
 
print('Test ident')
iterable_variable = [1,2,3,4,5,6]
total = 0
for item in iterable_variable:
 total = total + item
 print(total)

print('Find the letter in my name')
# Define a string to iterate over
for this_letter in "Tomasz Lesniak":
 # Specify which letter to test for
 if this_letter == "k":
  # Found the test letter
  print(f"Woo hoo, found a {this_letter}!")
  # Exit the current loop
  break
else:
  # Didn't find the test letter
  print(f"Aww man, I didn't want a {this_letter}!")

print('Try the code below')
my_list = [1,2,3,0]
for my_number in my_list:
 if my_number == 1:
  pass
 if my_number == 2:
  continue
 if my_number == 3:
  print(f"Found the number {my_number}")
 if my_number == 0:
   break

list_of_tuples = [(1,2), (3,4), ("A", "B")]
for item in list_of_tuples:
 print(item)

print('Tuple unpacking')
# Tuple unpacking
list_of_tuples = [(1,2), (3,4), ("A", "B")]
for a,b in list_of_tuples:
 print(a)
 print(b)

print('Code to try with step 5')
for index in range(1, 100, 5):
 print(index)

print('Code to try with step 3')
for index in range(0, 100, 3):
 print(index)

print()
print('Exercise scan')
scan = {"192.168.3.10": "80", "192.168.3.11": "443", "192.168.3.55": "22"}
for ipv4, port in scan.items():
 print(f"Found a service on {ipv4} at {port}")