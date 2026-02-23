# This is a sample Python script.

# Press <no shortcut> to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.


def print_hi(name):
    # Use a breakpoint in the code line below to debug your script.
    print(f'Hi, {name}')  # Press <no shortcut> to toggle the breakpoint.


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    print_hi('PyCharm')

enemies = ["Goblin", "Orc"]
enemies.append("Dragon")
print(enemies[0])

player_names = ["Guy", "Dude", "GigaChad"]

for name in player_names:
    print("Ready: " + str(name))


def i_take_a_number(the_number):
    return the_number * 2


result = i_take_a_number(5)
print(result)


def i_add_ten(number):
    return number + 10


list_of_numbers = [42, 67, 99]

for number in list_of_numbers:
    print(i_add_ten(number))


def triple_a_number(number):
    return number * 3


more_numbers = [42, 67, 99, 666]

for number in more_numbers:
    result = triple_a_number(number)
    print("Result " + str(result))

# Input
doubleInt = ""

while type(doubleInt) != int:
    user_input = input("Type an integer...")

    try:
        doubleInt = int(user_input)
        doubleInt *= 2
        print("Double your number is "+str(doubleInt))
        continue
    except ValueError:
        print("You didn't type an integer. Try again...")
