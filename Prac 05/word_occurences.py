given_string = input("Please input a sentence.")
list_string = given_string.split(' ')
final_list = list(dict.fromkeys(list_string))
for word in final_list:
    count = 0
    for index in list_string:
        if word == index:
            count += 1
    print("{:<10} {} {}".format(word, ":", count))
