from Managers.Dice_game import DiceGame
from Managers.User_Manager import UserManager

def main():
    usermanager = UserManager()
    usermanager.load_users()
    dice_game = DiceGame()
    while True: 
        
        while not usermanager.islogined:
            print ("Welcome to Dice Game!")
            print ("1. Register")
            print ("2. Login")
            print ("3. Exit ")
            try:
                choice = int(input("Enter choice: "))
                if choice == 1:
                    username = ''
                    password = ''
                    while True:
                        username = input ("Enter username: ")
                        if len(username) < 4:
                            print("4 characters needed")
                            continue
                        password = input ("Enter password: ")
                        if len(password) < 8:
                            print("8 characters needed")
                            continue
                        break
                    usermanager.register(username, password)
                    break
                elif choice == 2:
                    username = input ("Enter username: ")
                    password = input ("Enter password: ")
                    usermanager.log_in(username, password)
                elif choice == 3:
                    print ("Exiting game...")
                    usermanager.save_user()
                    exit(0)
                else:
                    print ("Invalid Input")
            except ValueError as e:
                print (f"Error Occured {e}")
                
        while usermanager.islogined:
            print(f"Welcome {usermanager.current_user.username}!")
            print ("1. Play Game")
            print ("2. Show Top Scores")
            print ("3. Logout")
            try:
                choice = int(input("Enter choice: " ))
                loggedUser = usermanager.current_user.username
                if choice == 1:
                    dice_game.play_game(loggedUser)
                elif choice == 2:
                    dice_game.show_top_scores()
                elif choice == 3:
                    print ("Logging Out")
                    usermanager.log_out()
                    dice_game.save_scores()
                    break
            except ValueError as e:
                print (f"Error as occured: {e}")

if __name__ == "__main__":
    main()