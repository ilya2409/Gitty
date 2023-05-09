import time
import os
import math
import random
import playsound
import func_list

# Для базовых переменых и словарей

com_list = {
    "привет": {"text" : "Приветствую создатель", "com": "file_hello.mp3", "exit" : False},
    "команда некоректно": {"text": "Команда некоректно (╯ ° □ °)╯ ┻━┻ ", "com" : "file_err_4.mp3", "exit" : False},
    "пока": {"text": "Было приятно побеседовать", "com": "file_exit.mp3", "exit" : True},
}


def text_in():
    return input("- ").lower()


def do_command(do_message):
    if do_message in com_list:
        say(do_message)
    elif do_message in func_list.knopki:
        say(do_message)
    else:
        print(com_list["команда некоректно"]["text"])
        playsound.playsound(com_list["команда некоректно"]["com"])


def say(say_message):
    print(com_list[say_message]["text"])
    playsound.playsound(com_list[say_message]["com"])
    com_exit(com_list[say_message]["exit"])


def com_exit(func):
    if func:
        return exit()


while True:
    text = text_in()
    do_command(text)


