import pickle
from User import User
import os

folder_path='Stock_Users'

def check_for_user(login:str)->bool:
    '''This method checks if we have saved an user in the database'''
    return os.path.isfile(folder_path+"\\"+login)

def check_password(login:str,password:str)->User:
    '''method checks whether an *existing* user has the same password as provided'''
    #we have to open the file in binary mode for pickle
    user_file=open(folder_path+"\\"+login, "rb")
    currentUser=pickle.load(user_file)
    return password==currentUser.get_password()


def return_user(login:str,password:str)->User:
    if check_for_user(login):
        if check_password(login,password):
            user_file = open(folder_path + "\\" + login,"rb")
            currentUser = pickle.load(user_file)
            return currentUser
        else:
            raise Exception("Wrong password")
    else:
        raise Exception("shit")
def register_user(login:str,password:str,starting_funds:float)->User:
    if check_for_user(login):
        raise Exception("Login already taken")
    currentUser=User(login,password,starting_funds)
    return currentUser


def end_session(currentUser:User)->bool:
    dest_path=folder_path+"\\"+currentUser.get_login()
    if os.path.exists(dest_path):
        os.remove(dest_path)
    file=open(dest_path, "ab")
    pickle.dump(currentUser,file)
    file.close()
    return True

#newUser=register_user("bingo","bango",200.0)
newUser=return_user("bingo","bango")
newUser.print()
end_session(newUser)