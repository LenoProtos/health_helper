import telebot

from keyboards import *
from bs4 import BeautifulSoup
import requests as rq

from fake_headers import Headers

from const import *
from text import text
from os import getcwd
from datetime import datetime
from time import time
# import mysql.connector as sql
# from sql import *

bot = telebot.TeleBot('TOKEN')

name = ''
surename = ''
age = 0

class user:
    def __init__(self):
        self.name = name
        self.surname = surname
        self.age = age



@bot.message_handler(commands=['start'])
def send_welcome(message):
    bot.reply_to(message, "Здравствуйте, вы обратились в службу спасения\n Завершите регистрацию, чтобы использовать все возможности сервиса")

@bot.message_handler(func=lambda m: True)
def echo_all(message):
    bot.send_message(message.from_user.id, "Введите имя:")
    bot.register_next_step_handler(message, reg_name)

def reg_name(message):
    global name
    name = message.text
    bot.send_message(message.from_user.id, "Введите фамилию")
    bot.register_next_step_handler(message, reg_surename)


def reg_surename(message):
    global surename
    surename= message.text
    bot.send_message(message.from_user.id, "Ввведите возраст (цифрами):")
    bot.register_next_step_handler(message, reg_age)
    bot.reply_to(message, "'+name+' '+surename+' '+age+'")

#    global age
#   #age = message.text
#  while age == 0:
#       try:
#          age = int(message.text)
#    except Exception:
#          bot.send_message(message.from_user.id, "Введите цифрами")