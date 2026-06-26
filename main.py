# This is a sample Python script.
from tools import Tools


# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.


def print_hi(name):
    # Use a breakpoint in the code line below to debug your script.
    text = f'Hi, {name}'
    print(text)  # Press Ctrl+F8 to toggle the breakpoint.
    tools = Tools().repair_print(text)
    print(tools)


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    print_hi('PyCharm')

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
