#----------------------------------------------------------------------------
#----------IMPORTS-----------------------------------------------------------
#----------------------------------------------------------------------------
import telebot.types
from records_access import append_records
from validation_data import is_return, disc_valid, valid_name, valid_tel
from bot_cration import get_bot
from help import show_help
#----------------------------------------------------------------------------
#----------VARIABLES---------------------------------------------------------
#----------------------------------------------------------------------------
bot = get_bot()
#---------
cur_name = ''
cur_surename = ''
cur_phone = ()
cur_descript = ''
#----------------------------------------------------------------------------
#----------FUNCTIONS---------------------------------------------------------
#----------------------------------------------------------------------------
def get_cur_descript():
    return cur_descript
#----------------------------------------------------------------------------
def set_cur_descript(val):
    global cur_descript
    cur_descript = val
#----------------------------------------------------------------------------
def get_cur_phone():
    return cur_phone
#----------------------------------------------------------------------------
def set_cur_phone(val):
    global cur_phone
    cur_phone = val
#----------------------------------------------------------------------------
def get_cur_surename():
    return cur_surename
#----------------------------------------------------------------------------
def set_cur_surename(val):
    global cur_surename
    cur_surename = val
#----------------------------------------------------------------------------
def get_cur_name():
    return cur_name
#----------------------------------------------------------------------------
def set_cur_name(val):
    global cur_name
    cur_name = val
#----------------------------------------------------------------------------
def print_start(msg):
    bot.send_message(chat_id= msg.from_user.id, text="You would like to add new record to TELEBUG. Follow the promts, please.")
#----------------------------------------------------------------------------
def add_oper(msg):
    print_start(msg)
    bot.send_message(chat_id= msg.from_user.id, text="Enter person name (for examle, Alex) or '/return' to stop add procedure. Use only letters, spacebar and symbols ' \' ', '-'.")
    bot.register_next_step_handler(callback= add_name_handler, message=msg)
#----------------------------------------------------------------------------  
def add_name(msg):
    not_filtered_string = msg.text.strip()

    if is_return(not_filtered_string):
        bot.send_message(chat_id= msg.from_user.id, text= show_help())
    elif valid_name(not_filtered_string.replace('\t', ' ')):
        set_cur_name(not_filtered_string)
        bot.send_message(chat_id= msg.from_user.id, text=f"{not_filtered_string} is valid name.")
        
        bot.send_message(chat_id= msg.from_user.id, text="Enter person surename (for examle, Kipaev) or '/return' to stop add procedure. Use only letters, spacebar and symbols ' \' ', '-'.")
        bot.register_next_step_handler(callback= add_surename_handler, message=msg)
    else:
        bot.send_message(chat_id= msg.from_user.id, text="Invalid name was entered. Try again.\n\nEnter person name (for examle, Alex) or '/return' to stop add procedure. Use only letters, spacebar and symbols ' \' ', '-'.")
        bot.register_next_step_handler(callback= add_name_handler, message=msg)
#----------------------------------------------------------------------------
def add_surename(msg):
    not_filtered_string = msg.text.strip()

    if is_return(not_filtered_string):
        bot.send_message(chat_id= msg.from_user.id, text= show_help())
    elif valid_name(not_filtered_string.replace('\t', ' ')):
        set_cur_surename(not_filtered_string)
        bot.send_message(chat_id= msg.from_user.id, text=f"{not_filtered_string} is valid surename.")
        
        bot.send_message(chat_id= msg.from_user.id, text="Enter person phone number. Use correct data format (for examle, +7(999)888-77-66) or '/return' to stop add procedure.")
        bot.register_next_step_handler(callback= add_phone_handler, message=msg)
    else:
        bot.send_message(chat_id= msg.from_user.id, text="Invalid surename was entered. Try again.\n\nEnter person surename (for examle, Kipaev) or '/return' to stop add procedure. Use only letters, spacebar and symbols ' \' ', '-'.")
        bot.register_next_step_handler(callback= add_surename_handler, message=msg)
#----------------------------------------------------------------------------
def add_phone(msg):
    not_filtered_string = msg.text.replace('\t', '').replace(' ', '')

    if is_return(not_filtered_string):
        bot.send_message(chat_id= msg.from_user.id, text= show_help())
    elif type(valid_tel(not_filtered_string)) == tuple:
        set_cur_phone(valid_tel(not_filtered_string))
        bot.send_message(chat_id= msg.from_user.id, text=f"{not_filtered_string} is valid telephone.")
        
        bot.send_message(chat_id= msg.from_user.id, text="Enter person discription (for examle, Cool body!) or '/return' to stop add procedure.  Don't use symbol '|'.")
        bot.register_next_step_handler(callback= add_descrip_handler, message=msg)
    else:
        bot.send_message(chat_id= msg.from_user.id, text="Invalid phone number was entered. Try again.\n\nEnter person phone number. Use correct data format (for examle, +7(999)888-77-66) or '/return' to stop add procedure.")
        bot.register_next_step_handler(callback= add_phone_handler, message=msg)
#----------------------------------------------------------------------------
def add_discript(msg):
    not_filtered_string = msg.text.strip()

    if is_return(not_filtered_string):
        bot.send_message(chat_id= msg.from_user.id, text= show_help())
    elif disc_valid(not_filtered_string):
        set_cur_descript(not_filtered_string)
        bot.send_message(chat_id= msg.from_user.id, text=f"Description is valid.")

        rec_append()
        bot.send_message(chat_id= msg.from_user.id, text="Add procedure is finished.")
        bot.send_message(chat_id= msg.from_user.id, text= show_help())
    else:
        bot.send_message(chat_id= msg.from_user.id, text="Invalid description was entered. Try again.\n\nEnter person discription (for examle, Cool body!) or '/return' to stop add procedure.  Don't use symbol '|'.")
        bot.register_next_step_handler(callback= add_descrip_handler, message=msg)
#----------------------------------------------------------------------------
def rec_append():
    app_add = (get_cur_name(), get_cur_surename(), get_cur_phone(), get_cur_descript())
    print(app_add)
    append_records(app_add)
#----------------------------------------------------------------------------
#----------HANDLERS----------------------------------------------------------
#----------------------------------------------------------------------------
def add_name_handler(msg: telebot.types.Message):
    add_name(msg)
#----------------------------------------------------------------------------
def add_surename_handler(msg: telebot.types.Message):
    add_surename(msg)
#----------------------------------------------------------------------------
def add_phone_handler(msg: telebot.types.Message):
    add_phone(msg)
#----------------------------------------------------------------------------
def add_descrip_handler(msg: telebot.types.Message):
    add_discript(msg)

#bot.register_next_step_handler(callback= add_rc, message=msg)