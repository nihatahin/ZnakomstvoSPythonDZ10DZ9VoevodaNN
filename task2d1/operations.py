#----------------------------------------------------------------------------
#----------IMPORTS-----------------------------------------------------------
#----------------------------------------------------------------------------
import telebot.types
from telebot import TeleBot
from operands import is_valid, coefs, invalid_answer
from tel_logging import tel_log
#----------------------------------------------------------------------------
#----------VARIABLES---------------------------------------------------------
#----------------------------------------------------------------------------
oper_enter = True
#---------
bot = TeleBot("YOUR ID")
#----------------------------------------------------------------------------
#----------FUNCTIONS---------------------------------------------------------
#----------------------------------------------------------------------------
def get_bot():
    return bot
#----------------------------------------------------------------------------
def get_oper_flag():
    return oper_enter
#----------------------------------------------------------------------------
def set_oper_flag(val: bool):
    global oper_enter
    oper_enter = val
#----------------------------------------------------------------------------
def operation_logic(msg, oper):
    match oper:
        case 'add':
            bot.send_message(chat_id= msg.from_user.id, text= 'Addition')
            bot.send_message(chat_id= msg.from_user.id, text="Enter two operands splited via space (example: 19+4i -17.45i)")
            bot.register_next_step_handler(callback= add_items, message=msg)
        case 'sub':
            bot.send_message(chat_id= msg.from_user.id, text= 'Subtraction')
            bot.send_message(chat_id= msg.from_user.id, text="Enter two operands splited via space (example: 19+4i -17.45i)")
            bot.register_next_step_handler(callback= sub_items, message=msg)
        case 'mul':
            bot.send_message(chat_id= msg.from_user.id, text= 'Multiplication')
            bot.send_message(chat_id= msg.from_user.id, text="Enter two operands splited via space (example: 19+4i -17.45i)")
            bot.register_next_step_handler(callback= mul_items, message=msg)
        case 'div':
            bot.send_message(chat_id= msg.from_user.id, text= 'Division')
            bot.send_message(chat_id= msg.from_user.id, text="Enter two operands splited via space (example: 19+4i -17.45i)")
            bot.register_next_step_handler(callback= div_items, message=msg)
        case _:
            bot.send_message(chat_id= msg.from_user.id, text= 'ERROR!')
#----------------------------------------------------------------------------
def add_items(msg: telebot.types.Message):
    tel_log(str(msg.from_user.username), str(msg.from_user.id), msg.text)
    bot.send_message(chat_id= msg.from_user.id, text= add(msg.text))
#----------------------------------------------------------------------------
def add(text):
    cd = is_valid(text)
    if cd == 1:
        inp = coefs(text)
        out = ((inp[0][0] + inp[1][0]), (inp[0][1] + inp[1][1]))
        return coefs_to_str(out)
    else:
        return str(invalid_answer(cd))
#----------------------------------------------------------------------------
def sub_items(msg: telebot.types.Message):
    tel_log(str(msg.from_user.username), str(msg.from_user.id), msg.text)
    bot.send_message(chat_id= msg.from_user.id, text= sub(msg.text))
#----------------------------------------------------------------------------
def sub(text):
    cd = is_valid(text)
    if cd == 1:
        inp = coefs(text)
        out = ((inp[0][0] - inp[1][0]), (inp[0][1] - inp[1][1]))
        return coefs_to_str(out)
    else:
        return str(invalid_answer(cd))
#----------------------------------------------------------------------------
def mul_items(msg: telebot.types.Message):
    tel_log(str(msg.from_user.username), str(msg.from_user.id), msg.text)
    bot.send_message(chat_id= msg.from_user.id, text= mul(msg.text))
#----------------------------------------------------------------------------
def mul(text):
    cd = is_valid(text)
    if cd == 1:
        inp = coefs(text)
        out = ((inp[0][0] * inp[1][0] - inp[0][1] * inp[1][1]), (inp[0][0] * inp[1][1] + inp[0][1] * inp[1][0]))
        return coefs_to_str(out)
    else:
        return str(invalid_answer(cd))
#----------------------------------------------------------------------------
def div_items(msg: telebot.types.Message):
    tel_log(str(msg.from_user.username), str(msg.from_user.id), msg.text)
    bot.send_message(chat_id= msg.from_user.id, text= div(msg.text))
#----------------------------------------------------------------------------
def div(text):
    cd = is_valid(text)
    if cd == 1:
        inp = coefs(text)
        out = (((inp[0][0] * inp[1][0] + inp[0][1] * inp[1][1]) / (inp[1][0] * inp[1][0] + inp[1][1] * inp[1][1])),
         ((inp[0][1] * inp[1][0] - inp[0][0] * inp[1][1]) / (inp[1][0] * inp[1][0] + inp[1][1] * inp[1][1])))
        return coefs_to_str(out)
    else:
        return str(invalid_answer(cd))
#----------------------------------------------------------------------------
def coefs_to_str(cfc):
    c_str = ''
    coefs = list(cfc)
    coefs[0] = round(coefs[0], 3)
    if coefs[0] != 0:
        c_str += str(coefs[0])
    coefs[1] = round(coefs[1], 3)
    mean = ''
    if coefs[1] == 1:
        mean == ''
    elif coefs[1] == -1:
        mean = '-'
    else:
        mean = str(coefs[1])
    if (coefs[1] > 0):
        if (coefs[0] != 0):
            c_str += '+' + mean + 'i'
        else:
            c_str += mean + 'i'
    elif coefs[1] < 0:
        c_str += mean + 'i'
    else:
        if coefs[0] == 0:
            c_str = '0.0'
    return c_str
#----------------------------------------------------------------------------