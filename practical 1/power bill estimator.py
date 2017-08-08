__author__ = 'Peter'

power_cost = float(input("Enter cents per kWh"))
daily_use = float(input("Enter amount of kWh used per day"))
billing_Period = float(input("How long is the billing period"))
estimated_cost = ((power_cost * daily_use) * billing_Period) /100
print("Your estimated bill is ${:.2f}".format(estimated_cost))
