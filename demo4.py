productname = input("Enter the product name: ")
productquant = input("Enter the product quantity: ")
productcost = input("Enter the product cost: ")
totalcost = int(productquant) * float(productcost)
Gst = totalcost * 0.18
finalcost = totalcost + Gst
print(f'''Product name is: {productname}
-----------------------------------
Product quantity is: {productquant}
-----------------------------------
Product cost is: {productcost}
-----------------------------------
Total cost is: {totalcost}
-----------------------------------
GST (18%) is: {Gst}
-----------------------------------
Final cost is: {finalcost}
-----------------------------------
''')