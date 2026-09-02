"""Problem statement:  Write a program that calculates a monthly electricity bill from the number of units consumed, using a slab-based tariff and a set of reusable functions.

"""


def compute_units_cost(units):
    cost=0
    units_above_100 = 0
    units_above_300 = 0
    if units <=100:
        cost = units*12
    elif units>100 and units<=300:
        units_above_100=units-100
        cost=100*12
        cost+=units_above_100*18
    else:
        units_above_100=units-100
        cost=100*12
        units_above_300 = units_above_100 -200
        cost+=200*18
        cost+=units_above_300*25
    return cost

def compute_bill(units, tax_rate=0.17, fixed_charges=150):
    cost = compute_units_cost(units)
    tax = cost*tax_rate
    final_payable = cost+tax+fixed_charges

    return final_payable

units = int(input("Enter no of units: "))
print("Total bill for default arguments: ")
print(compute_bill(units))

print("Total bill for overriden tax rate: ")
print(compute_bill(units, tax_rate=0.2))

print("Total bill for overriden tax rate and fixed charges: ")
print(compute_bill(units, tax_rate=0.2, fixed_charges=200))
