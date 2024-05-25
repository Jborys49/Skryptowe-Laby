import datetime
class User:
    def __init__(self, login:str, password:str,starting_funds:float):
        self.login = login
        self.password = password
        self.starting_funds =starting_funds
        self.currentfunds = starting_funds
        self.currentdate=datetime.date(2001,1,10)

    def __init__(self, login:str, password:str,starting_funds:float,date:datetime.date):
        self.login = login
        self.password = password
        self.starting_funds =starting_funds
        self.currentfunds = starting_funds
        self.currentdate=date
    def get_date(self):
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