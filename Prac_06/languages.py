from Prac_06.ProgrammingLanguage import ProgrammingLanguage

ruby = ProgrammingLanguage("Ruby", "Dynamic", True, 1995)
python = ProgrammingLanguage("Python", "Dynamic", True, 1991)
visual_basic = ProgrammingLanguage("Visual Basic", "Static", False, 1991)
print(python)
Languages = [ruby, python, visual_basic]
print("The dynamically typed languages are:")
for language in Languages:
    if language.is_dynamic():
        print(language.name)
