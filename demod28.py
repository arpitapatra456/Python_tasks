class vendor:
    def __init__(self, vname):
        self.




class vendor:
    def billing(self,pname,pQTY,pCost=0.0):
        s3 = f'product cost:{self.pCost} Total (includingTax):{self.gs} '
        s4 = f'po date/time:{time.ctime()}\n'
        wobj.write(s1+s2+s3+s4)

vobj1 = vendor('Klabs' , 'GST123')
vobj1.billing('pA',5,1000)
time.sleep(3)
vobj1.
