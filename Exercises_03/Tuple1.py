my_list = ["one","two","three"]
my_tuple = ("one","two","three")
print(type(my_list))
print(type(my_tuple))


my_tuple = ("one","two","three","one")
#how many times one appears
print(my_tuple.count("one"))
#what is the position of one
print(my_tuple.index("one"))