__author__ = 'Peter'

TARIFF_11 = 0.244168
TARIFF_34 = 0.136928
tariff_used = int(input("Which Tariff is being used 11 or 34?"))
daily_use = float(input("Enter amount of kWh used per day"))
billing_Period = float(input("How long is the billing period"))
if tariff_used == 11:
    estimated_cost = ((TARIFF_11 * daily_use) * billing_Period) / 100
    print("Your estimated bill is ${:.2f}".format(estimated_cost))
elif tariff_used == 34:
    estimated_cost = ((TARIFF_34 * daily_use) * billing_Period) / 100
    print("Your estimated bill is ${:.2f}".format(estimated_cost))
else:
    print("An error has occured please try again.")
