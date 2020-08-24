

def main():
    user_password = input("Please input a password.")
    print(hide_password(user_password))


def hide_password(password):
    hidden_password = ""
    for index in password:
        hidden_password += "*"
    return hidden_password


main()
