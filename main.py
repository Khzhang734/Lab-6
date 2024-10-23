def encode(password):
    encoded_pass = ''
    for digit in password:
        # Shift each digit up by 3 numbers
        new_digit = (int(digit) + 3) % 10
        encoded_pass += str(new_digit)
    return encoded_pass


def decode(encoded_pass):
    decoded_pass = ''
    for digit in encoded_pass:
        # Shift each digit down by 3 numbers
        new_digit = (int(digit) - 3) % 10
        decoded_pass += str(new_digit)
    return decoded_pass


def main():
    encoded_password = ''

    while True:
        print("Menu")
        print("-------------")
        print("1. Encode")
        print("2. Decode")
        print("3. Quit")

        option = input("Please enter an option: ")

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

        else:
            print("Invalid option. Please try again.")


if __name__ == "__main__":
    main()