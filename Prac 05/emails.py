def main():
    email_verify = {}
    # Comment// Was just an annoying (might be referenced before assignment bug) for name
    name = ""
    while True:
        email = input("Email: ")
        if email == "":
            break
        else:
            name = name_verify(email)
        correct_name = input(" Is your name {}? (Y/N)".format(name))
        if correct_name.upper() == "YES" or correct_name.upper() == "Y":
            final_name = name
        elif correct_name.upper() == "NO" or correct_name.upper() == "N":
            final_name = input("Name: ")
            final_name = name
    email_verify[email] = name
    print()
    for item in email_verify:
        print("{} ({})".format(email_verify[item], item))


def name_verify(email):
    new_email = email.split("@")
    name = new_email[0]
    if "." in name:
        new_name = name.split(".")
        return_name = new_name[0] + " " + new_name[1]
        return_name = return_name.title()
    else:
        return_name = name
    return return_name


main()
