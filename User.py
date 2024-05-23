class User:
    def __init__(self, login, password):
        self.login = login
        self.password = password

    def check_password(self, input_password):
        return self.password == input_password