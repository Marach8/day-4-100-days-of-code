print('''
Welcome to your adventure simulator. I am going to ask you a bunch of questions and then create an epic story with you as the star!
''')
print()
a = input('\033[32mWhat is your name?\033[0m ')
b = input("\033[31mWhat is your worst enemy's name? ")
c = input('What is your superpower? \033[0m')
d = input('\033[32mWhere do you live? ')
e = input('What is your favorite food? \033[0m')
print()
print(f'''
Hello \033[32m{a}\033[0m! Your ability to \033[31m{c}\033[0m will make sure you never have to look at \033[31m{b}\033[0m again. Go eat {e} as you walk down the streets of {d} and use \033[31m{c}\033[0m for good and not evil!
''')