"""
CP1404/CP5632 Practical
Code for List_Warm-up (Questions and Answers)
"""

numbers = [3, 1, 4, 1, 5, 9, 2]
'''
Questions
1.) 3
2.) 2
3.) 1
4.) 3, 1, 4, 1, 5, 9, 2
5.) 1, 5 - Incorrect (Correct answer is [1] or 1)
6.) True
7.) False
8.) False
9.) 3, 1, 4, 1, 5, 9, 2, 6, 5, 3
'''
print("Question 1", numbers[0])
print("Question 2", numbers[-1])
print("Question 3", numbers[3])
print("Question 4", numbers[:-1])
print("Question 5", numbers[3:4])
print("Question 6", 5 in numbers)
print("Question 7", 7 in numbers)
print("Question 8", "3" in numbers)
print("Question 9", numbers + [6, 5, 3])

numbers[0] = "ten"
numbers[-1] = 1
print(numbers[1:-1])
print(9 in numbers)
