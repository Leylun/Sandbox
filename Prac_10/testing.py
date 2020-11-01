"""
CP1404/CP5632 Practical
Testing demo using assert and doctest
"""

import doctest
from Prac_06.car import Car


def repeat_string(s, n):
    """Repeat string s, n times, with spaces in between."""
    init_string = s
    if n == 1:
        pass
    else:
        for index in range(1, n):
            s = s + " " + init_string
    return s


def is_long_word(word, length=5):
    """
    Determine if the word is as long or longer than the length passed in
    >>> is_long_word("not")
    False
    >>> is_long_word("supercalifrag")
    True
    >>> is_long_word("Python", 6)
    True
    """
    return len(word) >= length


def run_tests():
    """Run the tests on the functions."""

    assert repeat_string("Python", 1) == "Python"

    assert repeat_string("hi", 2) == "hi hi"

    test_car = Car()
    assert test_car.odometer == 0, "Car does not set odometer correctly"

    test_car = Car(fuel=10)
    test_car1 = Car()
    assert test_car.fuel == 10, 'Car has incorrect fuel field'
    assert test_car1.fuel == 0, 'Car has incorrect fuel field'


def to_sentence(phrase):
    """
    Rephrase input into sentence format
    >>> to_sentence('hello')
    'Hello.'
    >>> to_sentence('It is an ex parrot.')
    'It is an ex parrot.'
    >>> to_sentence('typing cold is criminal')
    'Typing cold is criminal.'
    """
    sentence = phrase.split(" ")
    sentence[0] = sentence[0].title()
    phrase = ' '.join(sentence)
    if phrase[-1] == ".":
        pass
    else:
        phrase += '.'
    return phrase


run_tests()
doctest.testmod()
