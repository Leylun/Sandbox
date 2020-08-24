from random import randint

def main():
    user_choice = input("[G]iven Score or [R]andom Score? (G or R accepted)")
    if user_choice == "G":
        user_input = int(input("What is your score? (Number between 1 and 100)"))
        print("Your result:", score_checker(user_input))
    elif user_choice == "R":
        score = randint(1, 100)
        print(score)
        print("Your result:", score_checker(score))


def score_checker(score):
    result = ""
    if score < 0 or score > 100:
        result = "Invalid score"
    elif score >= 90:
        result = "Excellent"
    elif score >= 50:
        result = "Passable"
    elif score < 50:
        result = "Bad"
    return result

main()