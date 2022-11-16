"""from cmd_work import basement, show_hello

show_hello()
basement()"""
#----------------------------------------------------------------------------
#----------IMPORTS-----------------------------------------------------------
#----------------------------------------------------------------------------
import telebot.types
from bot_cration import get_bot, get_start, set_start
from cmd_work import show_hello, basement
from help import show_help
#----------------------------------------------------------------------------
#----------VARIABLES---------------------------------------------------------
#----------------------------------------------------------------------------
bot = get_bot()
#----------------------------------------------------------------------------
#----------FUNCTIONS---------------------------------------------------------
#----------------------------------------------------------------------------

#----------------------------------------------------------------------------
#----------HANDLERS----------------------------------------------------------
#----------------------------------------------------------------------------
@bot.message_handler(commands=['start'])
def start_hand(message: telebot.types.Message):
    set_start(True)
    bot.send_message(chat_id= message.from_user.id, text= show_hello())
    bot.send_message(chat_id= message.from_user.id, text= show_help())
#----------------------------------------------------------------------------
@bot.message_handler(commands=['help'])
def help_hand(message: telebot.types.Message):
    if not get_start():
        basement(message, 'help')
#----------------------------------------------------------------------------
@bot.message_handler(commands=['exit'])
def exit_hand(message: telebot.types.Message):
    basement(message, 'exit')
#----------------------------------------------------------------------------
@bot.message_handler(commands=['show'])
def show_hand(message: telebot.types.Message):
    if get_start():
        basement(message, 'show')
#----------------------------------------------------------------------------
@bot.message_handler(commands=['add'])
def add_hand(message: telebot.types.Message):
    if get_start():
        basement(message, 'add')
#----------------------------------------------------------------------------
@bot.message_handler(commands=['impo'])
def impo_hand(message: telebot.types.Message):
    if get_start():
        basement(message, 'impo')
#----------------------------------------------------------------------------
@bot.message_handler(commands=['expo'])
def expo_hand(message: telebot.types.Message):
    if get_start():
          basement(message, 'expo')
#----------------------------------------------------------------------------
@bot.message_handler(commands=['exmp'])
def exanole_hand(message: telebot.types.Message):
    if get_start():
          basement(message, 'exmp')
#----------------------------------------------------------------------------
#----------INF CYCLE---------------------------------------------------------
#----------------------------------------------------------------------------
bot.polling()