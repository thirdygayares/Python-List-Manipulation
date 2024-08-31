groceries_cost = [200, 350, 360, 380]

def maxCustom(groceries_cost):
    max_cost = 0
    for cost in groceries_cost:
        if cost > max_cost:
            max_cost = cost
    return max_cost

# Built-in function
print("The max is " , max(groceries_cost))
print("The min is ", min(groceries_cost))

#custom function
print(maxCustom(groceries_cost))