# input variable for weight to compute shipping cost base on different options to see what is cheapest.
weight = 41.5
premium_ground_shipping = 120

# premium shipping; flat rate only
print("Premium Shipping Rate:")
print(premium_ground_shipping)

# ground shipping; cheaper flat rate plus cost per pound depending on weight
print("Ground Shipping Rate:")
if weight <= 2:
  print(20.00 + 1.50 * weight)
elif weight <= 6:
  print(20.00 + 3.00 * weight)
elif weight <= 10:
  print(20.00 + 4.00 * weight)
elif weight > 10:
  print(20.00 + 4.75 * weight)

# drone shipping; no flat rate, cost only determined by weight
print("Drone Shipping Rate:")
if weight <= 2:
  print(4.50 * weight)
elif weight <= 6:
  print(9.00 * weight)
elif weight <= 10:
  print(12.00 * weight)
elif weight > 10:
  print(14.25 * weight)
