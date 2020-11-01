"""
Tristan Harrington - CP1404
Wikipedia Search Tool
"""
from wikipedia import summary
from wikipedia import exceptions


def search_wiki():
    while True:
        user_inp = input("Search: ")
        if user_inp == '':
            quit()
        else:
            try:
                # Tries to parse summary into easily readable chunks however, method is far from optimal.
                search_list = summary(user_inp)
                search_list.split()
                new_list = [''.join(search_list[i:i + 120]) for i in range(0, len(search_list), 120)]
                for item in new_list:
                    print(item)
            except exceptions.DisambiguationError as parser:
                for index in range(1, 10):
                    print(parser.options[index])


search_wiki()
