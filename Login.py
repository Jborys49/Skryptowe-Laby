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
    '''method returns user if user exists and password matches,else throws error'''
    if check_for_user(login):
        if check_password(login,password):
            user_file = open(folder_path + "\\" + login,"rb")
            currentUser = pickle.load(user_file)
            return currentUser
        else:
            raise Exception("Wrong password")
    else:
        raise Exception("User not registered in system")
def register_user(login:str,password:str,starting_funds:float)->User:
    '''registers a new user in the database if the login isnt already taken'''
    if check_for_user(login):
        raise Exception("Login already taken")
    currentUser=User(login,password,starting_funds)
    return currentUser


def end_session(currentUser:User)->bool:
    '''method saves the user to teh databes- used in relogging and closing the program'''
    dest_path=folder_path+"\\"+currentUser.get_login()
    if os.path.exists(dest_path):
        os.remove(dest_path)
    file=open(dest_path, "ab")
    pickle.dump(currentUser,file)
    file.close()
    return True
def test1():
    result = 0
    for i in range(1000000):
        result += i
    temp_list = [x for x in range(1000)]
    temp_dict = {i: i*i for i in range(1000)}
    for i in temp_list:
        result += temp_dict[i % 1000]
    for i in range(500):
        result *= 2
    for i in range(500):
        result /= 2
    print(f"Final result of long_method_one: {result}")

def test2():
    long_string = ""
    for i in range(10000):
        long_string += "This is a very long and pointless string. "
    word_count = len(long_string.split())
    reversed_string = long_string[::-1]
    for char in reversed_string:
        if char == ' ':
            word_count -= 1
    char_sum = sum(ord(char) for char in long_string)
    average_ascii = char_sum / len(long_string)
    print(f"Word count: {word_count}, Average ASCII value: {average_ascii}")


def test3():
    num_list = [i for i in range(100000)]
    for i in range(100000):
        num_list[i] = num_list[i] ** 2
    even_squares = [x for x in num_list if x % 2 == 0]
    odd_squares = [x for x in num_list if x % 2 != 0]
    even_sum = sum(even_squares)
    odd_sum = sum(odd_squares)
    total_sum = even_sum + odd_sum
    max_even = max(even_squares) if even_squares else None
    min_odd = min(odd_squares) if odd_squares else None
    print(f"Total sum: {total_sum}, Max even: {max_even}, Min odd: {min_odd}")
newUser=register_user("bingo","bango",200.0)
#newUser=return_user("bingo","bango")
newUser.print()
end_session(newUser)