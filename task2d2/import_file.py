#----------------------------------------------------------------------------
#----------IMPORTS-----------------------------------------------------------
#----------------------------------------------------------------------------
import telebot.types
from records_access import append_records
from validation_file import file_path, is_return
from validation_data import valid_name, valid_tel, disc_valid
from bot_cration import get_bot
from help import show_help
#import requests
#----------------------------------------------------------------------------
#----------VARIABLES---------------------------------------------------------
#----------------------------------------------------------------------------
bot = get_bot()
#----------
file_name_path = './task2d2/files/file_import_rules.txt'
#----------------------------------------------------------------------------
#----------FUNCTIONS---------------------------------------------------------
#----------------------------------------------------------------------------
def print_intro(msg):
    bot.send_message(chat_id= msg.from_user.id, text="You would like to import all records from file. Follow the promts, please.")
#----------------------------------------------------------------------------
def get_file_name_path():
    return file_name_path
#----------------------------------------------------------------------------
def warning_type(msg):
    with open (get_file_name_path(), 'r', encoding= 'utf-8') as f_name_file:
        bot.send_message(chat_id= msg.from_user.id, text=f_name_file.read())
#----------------------------------------------------------------------------
def print_invalid(msg):
    bot.send_message(chat_id= msg.from_user.id, text='Invalid file format!')
#----------------------------------------------------------------------------
def import_success(msg):
    bot.send_message(chat_id= msg.from_user.id, text='Import successfully finished!')
#----------------------------------------------------------------------------
def strs_to_recs(strs):
    
    for i in range(len(strs)):
        print(strs[i])
        strs[i] = strs[i].split('|')[2 : 6]
        strs[i][0] = strs[i][0].strip()
        strs[i][1] = strs[i][1].strip()
        strs[i][2] = strs[i][2].strip().replace('\t', '').replace(' ', '')
        strs[i][3] = strs[i][3].strip().replace('\t', ' ')
    return(strs)
#----------------------------------------------------------------------------
def append_file_to_data(data):
    for i in range(len(data)):
        append_records(tuple(data[i]))
#----------------------------------------------------------------------------






def file2str_list(path):
    with open (path, 'r', encoding= 'utf-8') as f_name_file:
        lines = f_name_file.readlines()
    return lines
#----------------------------------------------------------------------------
def file_read():
    f_path = file_path()
    if is_return(f_path):
        return
    file_lines = file2str_list(f_path[0])
    if f_path[1] == 1:
        md_impo(file_lines)
    elif f_path[1] == 2:
        txt_impo(file_lines)
    print("Import procedure is finished.")
#----------------------------------------------------------------------------


#----------------------------------------------------------------------------
def txt_str_num_check(num):
    return num % 5 == 0
#----------------------------------------------------------------------------
def lines2moist_records(ln):
    dry = []
    for i in range(0, len(ln), 4):
        dry.append([ln[i], ln[i + 1], ln[i + 2], ln[i + 3]])
    return dry
#----------------------------------------------------------------------------

def every_fifth_is_enter(data):
    for i in range(4, len(data), 5):
        if data[i] != '':
            return False
    else:
        return True
#----------------------------------------------------------------------------
def delete_enters_and_spaces(data):
    mod_data = []
    for i in range(4, len(data), 5):
        if data[i] == '':
            mod_data.append(data[i - 4].strip())
            mod_data.append(data[i - 3].strip())
            mod_data.append(data[i - 2].strip().replace('\t', '').replace(' ', ''))
            mod_data.append(data[i - 1].strip().replace('\t', ' '))
    else:
        return mod_data
#----------------------------------------------------------------------------
def conver_telephone(full_data):
    for i in range(len(full_data)):
        full_data[i][2] = valid_tel(full_data[i][2])
    return full_data
#----------------------------------------------------------------------------
def append_file_to_data(data):
    for i in range(len(data)):
        append_records(tuple(data[i]))
#----------------------------------------------------------------------------
 
#----------------------------------------------------------------------------
def import_recs():
    print_intro()
    warning_type()
    file_read()




def impo_oper(msg):
    print_intro(msg)
    warning_type(msg)
    bot.send_message(chat_id= msg.from_user.id, text="Send import document or print '/return' to stop export procedure.")
    bot.register_next_step_handler(callback= impo_format_handler, message=msg)
#----------------------------------------------------------------------------
def impo_format(msg: telebot.types.Message):
    if msg.text != None:
        if is_return(msg.text.strip()):
            bot.send_message(chat_id= msg.from_user.id, text= show_help())
            return
    if msg.document != None:
        if msg.document.file_name[-3 : ] == '.md':
            bot.send_message(chat_id= msg.from_user.id, text= "Markdown file import.")
            md_impo(msg)
            
            return 
        elif msg.document.file_name[-4 : ] == '.txt':
            bot.send_message(chat_id= msg.from_user.id, text= "Text file import.")
            txt_impo(msg)

            return 
        else:
            bot.send_message(chat_id= msg.from_user.id, text="Invalid file extension. Send import document or print '/return' to stop export procedure.")
    else:
        bot.send_message(chat_id= msg.from_user.id, text="No document in the message. Send import document or print '/return' to stop export procedure.")
    bot.register_next_step_handler(callback= impo_format_handler, message=msg)
#----------------------------------------------------------------------------
def get_file(msg: telebot.types.Message):
    raw = msg.document.file_id
    #path = raw + dop
    file_info = bot.get_file(raw)
    downloaded_file = bot.download_file(file_info.file_path)
    return (str(downloaded_file)[2 : -1]).strip()
#----------------------------------------------------------------------------
def md_impo(msg):
    lines = get_file(msg).split('\\n')
    if (lines[0] == '|#|Name|Surename|Telephone number|Discription|') and (lines[1] == '|-:|-:|-:|-:|:-|'):
        lst = strs_to_recs(lines[2 : -1])
        if content_check(lst):
            print(lst)
            append_file_to_data(conver_telephone(lst))
            import_success(msg)
        else:
            print_invalid(msg)
    else:
        print_invalid(msg)
#----------------------------------------------------------------------------
def txt_impo(msg):
    lines = get_file(msg).split('\\n')
    lines = lines[: -1]
    length = len(lines)
    print(lines)
    if txt_str_num_check(length) and (length > 0):
        if every_fifth_is_enter(lines):
            lines = delete_enters_and_spaces(lines)
            lst = lines2moist_records(lines)
            if content_check(lst):
                print(lst)
                append_file_to_data(conver_telephone(lst))
                import_success(msg)
            else:
                print_invalid(msg)
        else:
            print_invalid(msg)
    else:
        print_invalid(msg) 
#----------------------------------------------------------------------------
def content_check(data):
    for i in range(len(data)):
        if not((valid_name(data[i][0])) and (valid_name(data[i][1])) and 
        (type(valid_tel(data[i][2])) == tuple) and (disc_valid(data[i][3]))):
            return False
    else:
        return True
#----------------------------------------------------------------------------
#----------HANDLERS----------------------------------------------------------
#----------------------------------------------------------------------------
def impo_format_handler(msg: telebot.types.Message):
    impo_format(msg)