#----------------------------------------------------------------------------
#----------IMPORTS-----------------------------------------------------------
#----------------------------------------------------------------------------
from bot_cration import get_bot
from help import show_help, show_help_invalid
from add import add_oper
from show import show_rec
from records_access import get_records
from export_file import expo_oper, exit_oper, example_oper
from import_file import impo_oper
#----------------------------------------------------------------------------
#----------VARIABLES---------------------------------------------------------
#----------------------------------------------------------------------------
bot = get_bot()
#----------------------------------------------------------------------------
#----------FUNCTIONS---------------------------------------------------------
#----------------------------------------------------------------------------
def show_hello():
    return 'Hello. Welcome to telephone directory main menu.'
#----------------------------------------------------------------------------
def basement(msg, oper):
    match oper:
        case 'help':
            bot.send_message(chat_id= msg.from_user.id, text= show_help_invalid())
        case 'add':
            bot.send_message(chat_id= msg.from_user.id, text= 'Add procedure')
            add_oper(msg)
        case 'show':
            bot.send_message(chat_id= msg.from_user.id, text= 'Show list')
            show_rec(msg, get_records())
            bot.send_message(chat_id= msg.from_user.id, text= show_help())
        case 'impo':
            bot.send_message(chat_id= msg.from_user.id, text= 'Import procedure')
            impo_oper(msg)
        case 'expo':
            bot.send_message(chat_id= msg.from_user.id, text= 'Export procedure')
            expo_oper(msg)
        case 'exmp':
            bot.send_message(chat_id= msg.from_user.id, text= 'Example transmit')
            example_oper(msg)
        case 'exit':
            exit_oper(msg)
        case _:
            bot.send_message(chat_id= msg.from_user.id, text= 'ERROR!')
            bot.send_message(chat_id= msg.from_user.id, text= show_help())

        #bot.send_message(chat_id= msg.from_user.id, text= show_help())
#----------------------------------------------------------------------------

