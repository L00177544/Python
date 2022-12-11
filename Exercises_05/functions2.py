def calculate_circumference(radius):
 """
 Calculate the circumference of a circle based on its radius
 """
 return 2 * 3.142 * radius
# Get a radius value as a string
r = input("Provide a radius value: ")
# Convert it to a float
r_float = float(r)
# Call the function and create the variable for the return value
a = calculate_circumference(r_float)
print(a)


def most_expensive(price_list):
    """
    Iterate through a list and find the most expensive item
    """
    # Set up the variables
    max_price = 0
    max_price_item = ""
    # Iterate, unpacking the tuple
    for description, price in price_list:
            # If this is the maximum price, record that in our variables
            if price > max_price:
                max_price = price
                max_price_item = description
            # If it is not the maximum price, do nothing
            else:
                pass
    # Return the maximum prices item and its price
    return max_price_item, max_price

# Provide the data
price_list = [("Pineapple", 1.0), ("Apples", .5), ("Pears", .7), ("Peaches", .8)]
# Call the function and unpack its return values
product, price = most_expensive(price_list)
product, price, availability = most_expensive(price_list)
print(product, price)

#ValueError: not enough values to unpack (expected 3, got 2)