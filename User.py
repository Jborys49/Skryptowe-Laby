import datetime
class User:
    def __init__(self, login:str, password:str,starting_funds:float):
        self.login = login
        self.password = password
        self.starting_funds =starting_funds
        self.currentfunds = starting_funds
        self.currentdate=datetime.date(2001,1,10)
        self.history={}
        self.wallet={}

    def __init__(self, login:str, password:str,starting_funds:float,date:datetime.date):
        self.login = login
        self.password = password
        self.starting_funds =starting_funds
        self.currentfunds = starting_funds
        self.currentdate=date
        self.wallet={}
        self.history=[]
    def purchase(self,name:str,price:float, nr_of_shares:int)->bool:
        '''This method is used to purchase a number of stocks. Returns true if purchase is succesfull
         and false when funds are insufficient. Also updates the history of user purchases'''
        if price * nr_of_shares>self.currentfunds:
            return False
        else:
            self.currentfunds-=price * nr_of_shares
            self.history.append({'name':name,'price':price,'shares':nr_of_shares,
                                 'date':self.currentdate,'is_purchase':True})
            if name not in self.wallet:
                self.wallet[name]={'shares':nr_of_shares,'paid':price*nr_of_shares}
            else:
                self.wallet[name]['shares']+=nr_of_shares
                self.wallet[name]['paid']+=price*nr_of_shares
            return True
    def sell(self,name:str,nr_of_shares:float,price:float)->bool:
        '''This method sells and upddates the current funds and the history of user purchases.
        If user does not have any stocks of the required item, or not enough shares, the function returns false'''
        if name not in self.wallet:
            return False
        else:
            if self.wallet[name]['shares']<nr_of_shares:
                return False
            else:
                self.history.append({'name': name, 'price': price, 'shares': nr_of_shares,
                                     'date': self.currentdate, 'is_purchase': False})
                self.wallet[name]['shares']-=nr_of_shares
                self.currentfunds+=nr_of_shares*price
                if self.wallet[name]['shares']==0:
                    del self.wallet[name]
                return True

    def get_date(self)->datetime.date:
        return self.currentdate
    def next_day(self):
        self.currentdate += datetime.timedelta(days=1)
    def check_password(self, input_password:str)->bool:
        return self.password == input_password
    def get_login(self):
        return self.login
    def get_profit_percent(self)->float:
        return (float(self.currentfunds) / float(self.starting_funds))*100.0
    def get_password(self):
        return self.password
    def set_password(self,new_password):
        self.password =new_password
    def get_starting_funds(self):
        return self.starting_funds
    def get_current_funds(self):
        return self.currentfunds
    def set_current_funds(self, new_current_funds:float):
        self.currentfunds=new_current_funds
    def print(self):
        print(self.login, self.password, self.get_current_funds())