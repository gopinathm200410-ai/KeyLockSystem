#Security keyLockSystem

import time

class KeyLockSystem:

    # -----------------------------
    # Constructor
    # -----------------------------

    def __init__(self):

        self.users = {
            "admin": {
                "password": "admin123",
                "attempts": 3,
                "locked": False
            }
        }

        self.logs = []

    # -----------------------------
    # Show Menu
    # -----------------------------

    def show_menu(self):

        print("\n===================================")
        print("        KEY LOCK SYSTEM")
        print("===================================")

        print("1. Register User")
        print("2. Login")
        print("3. Change Password")
        print("4. Forgot Password")
        print("5. View Logs")
        print("6. Exit")

        print("===================================\n")

    # -----------------------------
    # Register User
    # -----------------------------

    def register_user(self):

        username = input("Enter new username: ")

        if username in self.users:
            print("User already exists!")
            return

        password = input("Enter password: ")

        self.users[username] = {
            "password": password,
            "attempts": 3,
            "locked": False
        }

        print("User Registered Successfully!")
        self.logs.append("REGISTER: " + username)

    # -----------------------------
    # Login System with Warning
    # -----------------------------

    def login(self):

        username = input("Enter username: ")

        if username not in self.users:
            print("User not found!")
            return

        user = self.users[username]

        if user["locked"]:
            print("ACCOUNT IS LOCKED!")
            return

        password = input("Enter password: ")

        if password == user["password"]:

            print("\nACCESS GRANTED ✅")

            user["attempts"] = 3

            self.logs.append("SUCCESS LOGIN: " + username)

        else:

            user["attempts"] -= 1

            print("\n❌ WRONG PASSWORD!")

            warning_level = 3 - user["attempts"]
            print("WARNING LEVEL:", warning_level)

            if user["attempts"] == 2:
                print("⚠ WARNING 1")

            elif user["attempts"] == 1:
                print("⚠ WARNING 2 - FINAL WARNING")

            elif user["attempts"] == 0:
                user["locked"] = True
                print("🚨 ACCOUNT LOCKED!")

            self.logs.append("FAILED LOGIN: " + username)

    # -----------------------------
    # Change Password
    # -----------------------------

    def change_password(self):

        username = input("Enter username: ")

        if username not in self.users:
            print("User not found!")
            return

        old_pass = input("Enter old password: ")

        if old_pass == self.users[username]["password"]:

            new_pass = input("Enter new password: ")

            self.users[username]["password"] = new_pass

            print("Password Changed Successfully!")

            self.logs.append("PASSWORD CHANGED: " + username)

        else:

            print("Incorrect old password!")

    # -----------------------------
    # Forgot Password (ACCESS CODE SYSTEM)
    # -----------------------------

    def forgot_password(self):

        username = input("Enter username: ")

        if username not in self.users:
            print("User not found!")
            return

        print("\n--- FORGOT PASSWORD ---")
        access_code = input("Enter access code: ")

        if access_code == "ADMIN@123":

            new_pass = input("Enter new password: ")

            self.users[username]["password"] = new_pass
            self.users[username]["attempts"] = 3
            self.users[username]["locked"] = False

            print("\nPassword Reset Successful 🔐")

            self.logs.append("PASSWORD RESET: " + username)

        else:

            print("Wrong access code!")

            self.users[username]["attempts"] -= 1

            print("Warning increased!")

            if self.users[username]["attempts"] <= 0:
                self.users[username]["locked"] = True
                print("ACCOUNT LOCKED!")

    # -----------------------------
    # View Logs
    # -----------------------------

    def view_logs(self):

        print("\n========== SYSTEM LOGS ==========")

        if len(self.logs) == 0:
            print("No logs available")

        else:
            for log in self.logs:
                print("-", log)

    # -----------------------------
    # Main Loop
    # -----------------------------

    def run(self):

        while True:

            self.show_menu()

            choice = input("Enter choice: ")

            if choice == "1":
                self.register_user()

            elif choice == "2":
                self.login()

            elif choice == "3":
                self.change_password()

            elif choice == "4":
                self.forgot_password()

            elif choice == "5":
                self.view_logs()

            elif choice == "6":
                print("Exiting System...")
                break

            else:
                print("Invalid Choice!")


# -----------------------------
# MAIN PROGRAM
# -----------------------------

print("===================================")
print("   ADVANCED KEY LOCK SYSTEM")
print("===================================")

system = KeyLockSystem()
system.run()