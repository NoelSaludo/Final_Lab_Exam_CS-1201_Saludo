from Models.User import User
import os

class UserManager():
    users = []
    islogined = False
    current_user = None
    dataPath = os.path.join("data", "users.txt")

    def __init__(self):
        if not os.path.exists("data"):
            os.makedirs("data")
            if open(self.dataPath, "x"):
                pass
            else:
                print ("Error creating file")
        self.load_users()
    
    def load_users(self):
        if not os.path.exists(self.dataPath):
            return
        with open(self.dataPath, "r") as file:
            for line in file:
                username, password = line.strip().split(",")
                self.users.append(User(username, password))
    
    def save_user(self):
        with open(self.dataPath, "w") as file:
            for user in self.users:
                file.write(f"{user.username},{user.password}\n")
    
    def validate_user(self, username, password):
        user = list(filter(lambda u: u.username == username and u.password == password, self.users))
        if not user:
            return False
        return True
    
    def register(self, username, password):
        
       user = list(filter(lambda u: u.username == username, self.users))
       if user:
           print ("Username already used!")
       else:
           print ("Successfully registered!")
           self.users.append(User(username, password))
           
    def log_in(self, username, password):
        if not self.validate_user(username, password):
            print ("Invalid username or password")
            return
        self.islogined = True
        self.current_user = User( username, password)
           
    def log_out(self):
        self.islogined = False 
        self.current_user = None
    