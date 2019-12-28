import prompt

name = ''


def run():
    global name
    name = prompt.string('May I have your name? ')
    print('Hello, {}\n'.format(name))
