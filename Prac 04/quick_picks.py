from random import randint


def main():
    while True:
        try:
            given_lines = int(input("Quick picks:"))
        except ValueError:
            print("Please input a integer value.")
            continue
        else:
            break
    for index in range(0, given_lines):
        line_list = [randint(1, 45)]
        for number in range(0, 5, 1):
            while True:
                generated_number = randint(1, 45)
                if generated_number == line_list[number]:
                    continue
                else:
                    line_list.append(generated_number)
                    break
        line_list.sort()
        print(line_list)


main()
