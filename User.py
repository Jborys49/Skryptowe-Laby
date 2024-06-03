import datetime
from decimal import Decimal
class User:
    def __init__(self, login:str, password:str,starting_funds:Decimal,date:datetime.date=datetime.date(2005,1,10)):
        self.login = login
        self.password = password
        self.starting_funds =Decimal(starting_funds).quantize(Decimal('1.00'))
        self.currentfunds = Decimal(starting_funds).quantize(Decimal('1.00'))
        self.currentdate=date
        self.wallet={}
        self.history=[]
    def purchase(self,name:str,price:Decimal, nr_of_shares:int)->bool:
        '''This method is used to purchase a number of stocks. Returns true if purchase is succesfull
         and false when funds are insufficient. Also updates the history of user purchases'''
        overall_price = Decimal(price*nr_of_shares).quantize(Decimal('1.00'))
        if overall_price>self.currentfunds:
            return False
        else:
            self.currentfunds=(self.currentfunds-Decimal(overall_price)).quantize(Decimal('1.00'))
            self.history.append({'name':name,'price':price,'shares':nr_of_shares,
                                 'date':self.currentdate,'is_purchase':True})
            if name not in self.wallet:
                self.wallet[name]={'shares':nr_of_shares,'paid': overall_price}
            else:
                self.wallet[name]['shares']=self.wallet[name]['shares']+nr_of_shares
                self.wallet[name]['paid']=self.wallet[name]['paid']+overall_price
            return True
    def sell(self,name:str,price:Decimal,nr_of_shares:int)->bool:
        '''This method sells and upddates the current funds and the history of user purchases.
        If user does not have any stocks of the required item, or not enough shares, the function returns false'''
        overall_price = Decimal(price * nr_of_shares).quantize(Decimal('1.00'))
        if name not in self.wallet:
            return False
        else:
            if self.wallet[name]['shares']<nr_of_shares:
                return False
            else:
                self.history.append({'name': name, 'price': price, 'shares': nr_of_shares,
                                     'date': self.currentdate, 'is_purchase': False})
                self.wallet[name]['shares']=self.wallet[name]['shares']-nr_of_shares
                self.currentfunds=self.currentfunds+overall_price
                if self.wallet[name]['shares']==0:
                    del self.wallet[name]
                return True
    def get_number_of_stock(self,stock:str):
        return self.wallet[stock]['shares']
    def get_date(self)->datetime.date:
        return self.currentdate
    def next_day(self):
        self.currentdate += datetime.timedelta(days=1)
    def check_password(self, input_password:str)->bool:
        return self.password == input_password
    def get_login(self):
        return self.login
    def get_profit_percent(self)->float:
        '''this function is overly complicated'''
        return float((((self.currentfunds-self.starting_funds) / (self.starting_funds))*Decimal(100.0)).quantize(Decimal('1.00')))
    def get_password(self):
        return self.password
    def set_password(self,new_password):
        self.password =new_password
    def get_starting_funds(self):
        return self.starting_funds
    def get_current_funds(self):
        return self.currentfunds
    def set_current_funds(self, new_current_funds:Decimal):
        self.currentfunds=new_current_funds
    def get_wallet(self):
        return self.wallet
    def set_date(self,newdate=datetime.date):
        self.currentdate=newdate
    def print(self):
        print(self.login, self.password, self.get_current_funds())