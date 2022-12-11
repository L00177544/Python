money_to_spend = 2600*6
print("Money to spend in the semester is:", end = ' ')
print(money_to_spend, end = ' ') 
print("Euro")
#Constant payments variables 
#All is divided by 6 or dividied by 6
#Internet variable
print("Internet 55e per month.", end = ' ')
internet=55*6
print("Total", end = ' ')
print(internet)
#Room rental variable
print("Room rental in Dublin 500e per month.", end = ' ')
room=500*6
print("Total", end = ' ')
print(room)
#Bills variable
print("Bills including energy, mobile 130e per month.", end = ' ')
bills=130*6
print("Total", end = ' ')
print(bills)
#ATU variable
print("ATU payments, 670e per year.", end = ' ')
atu=670/2
print("Total per semester", end = ' ')
print(atu)
#food variable
print("Grocery and food (eat out included), 250e per week.", end = ' ')
food=(250*4)*6
print("Total", end = ' ')
print(food)
print()
#Sum up all the costs
costs=internet+room+bills+atu+food
print("Total money required for the semester is:", end = ' ')
print("", end = ' ')
print(costs)
print()
# Money left at the end of semester
print("Money left and avaiable to use", end = ' ')
print(money_to_spend-costs, end = ' ')
monthleft=(money_to_spend-costs)/6
#Round what if left to 1 digit
monthlyround = round(monthleft, 1)
print("or monthly", end = ' ')
print(monthlyround)