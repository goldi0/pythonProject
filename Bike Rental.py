class bikeshop:

    def_init_(self,stock)
        self.stock=stock
    def displayBike(self):
        print("Total Bikes",self.stock)
    def rentforBike(self,q)

        if q<=0:
            print("Enter the positive value or greter than zero")
        elif q> self.stock:
            print("Enter the (value less than stock)")
        else:
            self.stock=self.stock.a
            print("Total price",q*100)
            print("Total Bikes",self.stock)

while True:
        obj=bikeshop(100)
        uc=int(input('''
        
        1 Display Stock
        2 Rent Bike
        3 Exit
        
        ''')
        if uc==1:
            bj.displayBike()
        elif uc==2:
            n=int(input"Enter the Qty:-.....")
            obj.rentforBike(n)
        else:
            break
