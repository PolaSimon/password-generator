import random
import os

def password_gen():

    '''Returns a file with a list of password generated according instructions below.'''

    file_name = str(input("Select name for file: "))
    file_path = str(input("Select path for file or if you want to save the file in default path tap enter: "))
    number_of_passwords = int(input("How many passwords you want to generate: "))
    sign_in_password = int(input("How many signs the password should have: "))
    default_path = os.path.expanduser('~/Documents/')

    passwords_list = []

    for _ in range(number_of_passwords):
        password = ""
        for _ in range(sign_in_password):
            character = chr(random.randint(33,126))
            password += character   
        passwords_list.append(password)

    if file_path == '':
        final_path = default_path
    else:
        final_path = file_path

    textfile = open(f"{final_path}/{file_name}.txt", "w")

    for x in passwords_list:
        textfile.write(x + "\n")
    textfile.close()


if __name__ == "__main__":
    password_gen()