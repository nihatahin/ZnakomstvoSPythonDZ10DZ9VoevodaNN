#----------------------------------------------------------------------------
#----------IMPORTS-----------------------------------------------------------
#----------------------------------------------------------------------------
import telebot.types
from records_access import get_records, clear_records
from validation_file import is_return
from to_str_convertion import tel2str
from bot_cration import get_bot, set_start
from help import show_help
#----------------------------------------------------------------------------
#----------VARIABLES---------------------------------------------------------
#----------------------------------------------------------------------------
bot = get_bot()
#----------
file_txt_name_path = './task2d2/files/telebug_data.txt'
file_md_name_path = './task2d2/files/telebug_data.md'
file_example_md_name_path = './task2d2/files/file_examples/example.md'
file_example_txt_name_path = './task2d2/files/file_examples/example.txt'
#----------------------------------------------------------------------------
#----------FUNCTIONS---------------------------------------------------------
#----------------------------------------------------------------------------
def get_example_file_md_name_path():
    return file_example_md_name_path
#----------------------------------------------------------------------------
def get_example_file_txt_name_path():
    return file_example_txt_name_path
#----------------------------------------------------------------------------
def get_file_md_name_path():
    return file_md_name_path
#----------------------------------------------------------------------------
def get_file_txt_name_path():
    return file_txt_name_path
#----------------------------------------------------------------------------
def print_intro(msg):
    bot.send_message(chat_id= msg.from_user.id, text="You would like to export all records to file. Follow the promts, please.")
#----------------------------------------------------------------------------
def empty_record_list(msg):
    bot.send_message(chat_id= msg.from_user.id, text="Records list is empty. Nothing to export.")
#----------------------------------------------------------------------------
def txt_expo(path, mode):
    with open (path, mode, encoding= 'utf-8') as f_name_file:
        buffer = get_records()
        for i in range(len(buffer)):
            f_name_file.write(buffer[i][0] + '\n')
            f_name_file.write(buffer[i][1] + '\n')
            f_name_file.write(tel2str(buffer[i][2]) + '\n')
            f_name_file.write(buffer[i][3] + '\n\n')
#----------------------------------------------------------------------------
def md_expo(path, mode):
    if mode == 'a':
        with open (path, 'r', encoding= 'utf-8') as f_name_file:
            base_add = len(f_name_file.readlines()) - 1
            if base_add <= 1:
                mode = 'w'

    with open (path, mode, encoding= 'utf-8') as f_name_file:
        if mode == 'w':
            base_add = 1
            f_name_file.write('|#|Name|Surename|Telephone number|Discription|\n')
            f_name_file.write('|-:|-:|-:|-:|:-|\n')
        buffer = get_records()
        for i in range(len(buffer)):
            f_name_file.write(f"|{i + base_add}|{buffer[i][0]}|{buffer[i][1]}|{tel2str(buffer[i][2])}|{buffer[i][3]}|\n")
#----------------------------------------------------------------------------
def expo_oper(msg):
    print_intro(msg)
    if len(get_records()) > 0:
        bot.send_message(chat_id= msg.from_user.id, text="You can export data to the files of .md and .txt formats. What format do you prefer?\nPrint '1' for .md, '2' for .txt or '/return' to stop export procedure.")
        bot.register_next_step_handler(callback= expo_format_handler, message=msg)
    else:
        empty_record_list(msg)
#----------------------------------------------------------------------------
def example_oper(msg):
    bot.send_message(chat_id= msg.from_user.id, text= "Import file structure examples.")
    bot.send_document(chat_id=msg.from_user.id, document=open(get_example_file_md_name_path(), 'rb'))
    bot.send_document(chat_id=msg.from_user.id, document=open(get_example_file_txt_name_path(), 'rb'))
#----------------------------------------------------------------------------
def expo_format(msg):
    answer = msg.text.strip()

    if is_return(answer):
        bot.send_message(chat_id= msg.from_user.id, text= show_help())
    elif answer == '1':
        md_expo(get_file_md_name_path(), 'w')
        bot.send_message(chat_id= msg.from_user.id, text="Export procedure is finished.")
        bot.send_document(chat_id=msg.from_user.id, document=open(get_file_md_name_path(), 'rb'))
        bot.send_message(chat_id= msg.from_user.id, text= show_help())
    elif answer == '2':
        txt_expo(get_file_txt_name_path(), 'w')
        bot.send_message(chat_id= msg.from_user.id, text="Export procedure is finished.")
        bot.send_document(chat_id=msg.from_user.id, document=open(get_file_txt_name_path(), 'rb'))
        bot.send_message(chat_id= msg.from_user.id, text= show_help())
    else:
        bot.send_message(chat_id= msg.from_user.id, text="Invalid answe was sent. Try again.\n\nPrint '1' for .md, '2' for .txt or '/return' to stop export procedure.")
        bot.register_next_step_handler(callback= expo_format_handler, message=msg)
#----------------------------------------------------------------------------
def exit_oper(msg):
    bot.send_message(chat_id= msg.from_user.id, text="Would you like to export data before leaving?\n\nPrint 'y' as yes, 'n' as no or '/return' to stop exit procedure.")
    bot.register_next_step_handler(callback= exit_handler, message=msg)
#----------------------------------------------------------------------------
def exit_func(msg):
    answer = msg.text.strip()

    if is_return(answer):
        bot.send_message(chat_id= msg.from_user.id, text= show_help())
    elif (answer == 'y') or (answer == 'Y'):
        exit_expo_oper(msg)
    elif (answer == 'n') or (answer == 'N'):
        clear_records()
        set_start(False)
        bot.send_message(chat_id= msg.from_user.id, text= 'It is pity, but you leave TELBUG! We will look foward to meet you again!')
    else:
        bot.send_message(chat_id= msg.from_user.id, text="Invalid answe was sent. Try again.\n\nPrint 'y' as yes, 'n' as no or '/return' to stop exit procedure.")
        bot.register_next_step_handler(callback= exit_handler, message=msg)
#----------------------------------------------------------------------------
def exit_expo_oper(msg):
    print_intro(msg)
    if len(get_records()) > 0:
        bot.send_message(chat_id= msg.from_user.id, text="You can export data to the files of .md and .txt formats. What format do you prefer?\nPrint '1' for .md, '2' for .txt or '/return' to stop export procedure.")
        bot.register_next_step_handler(callback= exit_expo_format_handler, message=msg)
    else:
        empty_record_list(msg)
        set_start(False)
        bot.send_message(chat_id= msg.from_user.id, text= 'It is pity, but you leave TELBUG! We will look foward to meet you again!')
#----------------------------------------------------------------------------
def exit_expo_format(msg):
    answer = msg.text.strip()

    if is_return(answer):
        bot.send_message(chat_id= msg.from_user.id, text= show_help())
    elif answer == '1':
        md_expo(get_file_md_name_path(), 'w')
        bot.send_message(chat_id= msg.from_user.id, text="Export procedure is finished.")
        bot.send_document(chat_id=msg.from_user.id, document=open(get_file_md_name_path(), 'rb'))
        set_start(False)
        clear_records
        bot.send_message(chat_id= msg.from_user.id, text= 'It is pity, but you leave TELBUG! We will look foward to meet you again!')
    elif answer == '2':
        txt_expo(get_file_txt_name_path(), 'w')
        bot.send_message(chat_id= msg.from_user.id, text="Export procedure is finished.")
        bot.send_document(chat_id=msg.from_user.id, document=open(get_file_txt_name_path(), 'rb'))
        set_start(False)
        clear_records()
        bot.send_message(chat_id= msg.from_user.id, text= 'It is pity, but you leave TELBUG! We will look foward to meet you again!')
    else:
        bot.send_message(chat_id= msg.from_user.id, text="Invalid answe was sent. Try again.\n\nPrint '1' for .md, '2' for .txt or '/return' to stop export procedure.")
        bot.register_next_step_handler(callback= exit_expo_format_handler, message=msg)
#----------------------------------------------------------------------------
#----------HANDLERS----------------------------------------------------------
#----------------------------------------------------------------------------
def expo_format_handler(msg: telebot.types.Message):
    expo_format(msg)
#----------------------------------------------------------------------------
def exit_handler(msg: telebot.types.Message):
    exit_func(msg)
#----------------------------------------------------------------------------
def exit_expo_format_handler(msg: telebot.types.Message):
    exit_expo_format(msg)