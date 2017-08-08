__author__ = 'Peter'

sales = float(input("Enter sales: $"))
while sales >= 0:
    if sales < 1000:
        bonus = sales * .1
    else:
        bonus = sales * .15
    print(bonus)
    sales = float(input("Enter sales: $"))


