import random

letters = list("ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz")

symbols = list("!@#$%^&*()-_+={}[]|\\:;'<>,./?")

char = letters + symbols


def main():
    print("Welcome to Secure Password Generator!")
    global length_of_pass
    length_of_pass = input("How many characters do you want your password to be: ")
    length_of_pass = int(length_of_pass)
main()

def generate_password():
    global password
    password = random.choices(char, k=length_of_pass)
    password = "".join(password)
    print(f"Your password is: {password}")
generate_password()

def save_password():
    save = input("Do You want to save your password in a text file?: (y/n) ")
    if save == "y":
        user_pass_file = open(file="YourPassword.txt", mode="w")
        user_pass_file.write(password)
        user_pass_file.close()
        print("Password saved in chosen file.")
        print("If your password did not save in chosen file, that file did not exist and we created it \nplease run program again with the same file \n and it will be updated.")
        generate_another = input("Would you like to generate another one?: (y/n) ")
        if generate_another == "y":
            generate_password()
        elif generate_another == "n":
            print("Goodbye.")
    elif save == "n":
        print("Okay, Goodbye.")
save_password()