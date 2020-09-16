class ProgrammingLanguage:

    def __init__(self, name, typing, reflection, year):
        self.name = name.title()
        self.typing = typing.title()
        self.reflection = reflection
        self.year = year

    def is_dynamic(self):
        if self.typing == "Dynamic":
            return True
        elif self.typing == "Static":
            return False

    def __str__(self):
        print("{}, {} Typing, Reflection={}, First appeared in {}".format(self.name, self.typing,
                                                                          self.reflection, self.year))
        return ""
