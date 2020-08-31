
def main():
    user_numlist = []
    for index in range(0, 5, 1):
        user_numlist.append(int(input("Number:")))
    print("The first number is {}".format(user_numlist[0]))
    print("The last number is {}".format(user_numlist[-1]))
    print("The smallest number is {}".format(min(user_numlist)))
    print("The largest number is {}".format(max(user_numlist)))
    print("The average of the numbers is {}".format(sum(user_numlist)/len(user_numlist)))
    usernames = ['jimbo', 'giltson98', 'derekf', 'WhatSup', 'NicolEye', 'swei45', 'BaseInterpreterInterface',
                 'BaseStdIn', 'Command', 'ExecState', 'InteractiveConsole', 'InterpreterInterface', 'StartServer',
                 'bob']
    given_name = input("Username:")
    if given_name in usernames:
        print("Access Granted")
    else:
        print("Access Denied")


main()
