__author__ = 'Peter'

items_required = int(input("How many items do you wish to ship?"))
shipping_total=0
while items_required != 0:
    item_cost = float(input("how much shipping does this item cost?"))
    shipping_total = shipping_total + item_cost
    items_required = items_required - 1
if shipping_total >=100:
    discount = shipping_total * .1
    shipping_total = shipping_total - discount

print("Your Shipping comes to a total of ${:.2f}".format(shipping_total))