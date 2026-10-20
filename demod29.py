class product:
    pname = 'pA'
    pCost = 1000
    pqty = 5

class customer(product):
    cus_id = 'cus-A'
    cus_name = 'Mr.A'
    pqty = 10
    QTY = product.pqty

obj = customer()
print(obj.pname)
print(obj.pCost)
print(obj.cus_id)
print(obj.cus_name)
print(obj.pqty)