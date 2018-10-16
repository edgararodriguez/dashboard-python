import matplotlib.pyplot as plt
import numpy as np
from collections import Counter
import json


sales = None
staff = None
#opens Json files
with open('report-generation/sales.json') as salesFile:
    sales = json.loads(salesFile.read())
with open('report-generation/sales_staff.json') as staffFile:
    staff = json.loads(staffFile.read())


total = []
base = []
acc = []
tax = []

for x in sales:
    base.append(float(x["base_price"][1:]))
    acc.append(float(x["accessories"][1:]))
    tax.append(float(x["taxes"][1:]))
base_sum = sum(base)
acc_sum = sum(acc)
tax_sum = sum(tax)
total = base_sum + acc_sum - tax_sum

print(total)

make = {}

for x in range(len(sales)):
    make[sales[x]["make"]] = 0

for x in range(len(sales)):
    make[sales[x]["make"]] += 1

print(make)

fig, ax = plt.subplots()
y_pos = range(len(make))
values = (list(make.values()))

ax.barh(y_pos, values, align="center")
plt.yticks(range(len(make)), list(make.keys()))
plt.show()
