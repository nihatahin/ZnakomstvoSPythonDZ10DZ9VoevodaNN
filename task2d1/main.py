#----------------------------------------------------------------------------
#----------IMPORTS-----------------------------------------------------------
#----------------------------------------------------------------------------
import telebot.types
from print_msg import start_msg
from operations import operation_logic, get_bot
from tel_logging import tel_log
#----------------------------------------------------------------------------
#----------VARIABLES---------------------------------------------------------
#----------------------------------------------------------------------------
log_path = './task2d1/files/log_file.txt'
#----------
bot = get_bot()
#----------------------------------------------------------------------------
#----------FUNCTIONS---------------------------------------------------------
#----------------------------------------------------------------------------

#----------------------------------------------------------------------------
#----------HANDLERS----------------------------------------------------------
#----------------------------------------------------------------------------
@bot.message_handler(commands=['start', 'help'])
def start(message: telebot.types.Message):
    tel_log(str(message.from_user.username), str(message.from_user.id), message.text)
    bot.send_message(chat_id= message.from_user.id, text= start_msg())
#----------------------------------------------------------------------------
@bot.message_handler(commands=['add'])
def start(message: telebot.types.Message):
    tel_log(str(message.from_user.username), str(message.from_user.id), message.text)
    operation_logic(message, 'add')
#----------------------------------------------------------------------------
@bot.message_handler(commands=['sub'])
def start(message: telebot.types.Message):
    tel_log(str(message.from_user.username), str(message.from_user.id), message.text)
    operation_logic(message, 'sub')
#----------------------------------------------------------------------------
@bot.message_handler(commands=['mul'])
def start(message: telebot.types.Message):
    tel_log(str(message.from_user.username), str(message.from_user.id), message.text)
    operation_logic(message, 'mul')
#----------------------------------------------------------------------------
@bot.message_handler(commands=['div'])
def start(message: telebot.types.Message):
    tel_log(str(message.from_user.username), str(message.from_user.id), message.text)
    operation_logic(message, 'div')
#----------------------------------------------------------------------------
#----------INF CYCLE---------------------------------------------------------
#----------------------------------------------------------------------------
bot.polling()