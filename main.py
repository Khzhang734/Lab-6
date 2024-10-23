#Lab 6 Group 45
#This is Kevin's code
#Aara Ahn modified this

def encode(password):
    encoded_pass = ""
    for digit in password:
        # Shift each digit up by 3 numbers
        new_digit = (int(digit) + 3) % 10
        encoded_pass += str(new_digit)
    return encoded_pass


def decode(encoded_pass):
    decoded_pass = ""
    for digit in encoded_pass:
        # Shift each digit down by 3 numbers
        new_digit = (int(digit) - 3) % 10
        decoded_pass += str(new_digit)
    return decoded_pass


def main():
    encoded_password = ""
    #Dislplay menu options
    while True:
        print("\nMenu\n-------------")
        print("1. Encode")
        print("2. Decode")
        print("3. Quit")

        option = input("Please enter an option: ")  #Allows the user to input options from the menu

        if option == '1':
            password = input("Please enter your password to encode: ")
            encoded_password = encode(password)
            print("Your password has been encoded and stored!")

        elif option == '2':
            if encoded_password:
                original_password = decode(encoded_password)
                print(f"The encoded password is {encoded_password}, and the original password is {original_password}.")
            else:
                print("No password has been encoded yet.")

        elif option == '3':
            break
        #"Exiting the program" statement is not needed, great catch!
        else:
            print("Invalid option. Please try again.")
#Kevin did a great job!

if __name__ == "__main__":
    main()