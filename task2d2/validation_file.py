#----------------------------------------------------------------------------
#----------IMPORTS-----------------------------------------------------------
#----------------------------------------------------------------------------

#----------------------------------------------------------------------------
#----------VARIABLES---------------------------------------------------------
#----------------------------------------------------------------------------

#----------------------------------------------------------------------------
#----------FUNCTIONS---------------------------------------------------------
#----------------------------------------------------------------------------
def valid_file(name):           #   1 - .md     2 - .txt    -1 - error_format   -2 - error_name
    format_letters = 0
    file_format = 0
    if name[-3 : ] == '.md':
        format_letters = 3
        file_format = 1
    elif (name[-4 : ]) == '.txt':
        format_letters == 4
        file_format = 2
    else:
        return -1


    if valid_name(name[ : -format_letters]):
        return file_format
    else:
        return -2
#----------------------------------------------------------------------------
def valid_name(str_name):
    sign_t = ('.', '/', '_', '-')
    for i in range(len(str_name)):
        if not (str_name[i].isalpha() or str_name[i].isdigit()):
            for j in range(len(sign_t)):
                if str_name[i] == sign_t[j]:
                    break
            else:
                return False         
    return True
#----------------------------------------------------------------------------
def is_return(symbols):
    return symbols == '/return'   
#----------------------------------------------------------------------------
def add_or_write():
    print("Would you like to rewrite data or add data? ") 
    while True:   
        mode = input("Print 'a' to add, 'r' to rewrite or '/return' to stop export procedure: ")
        match mode:
            case 'a':
                return mode
            case 'r':
                return 'w'
            case '/return':
                return mode
            case _:
                print("Invalid parameter. Try again.")
#----------------------------------------------------------------------------
def file_path():
    while True:
        path = input("Enter file path or '/return' to stop export procedure: ")
        if is_return(path):
            return path
        v_path = valid_file(path)
        match v_path:
            case -2:
                print("Invalid symbols in file path were used. Try again.")
            case -1:
                print("Invalid file extension was use. Try again.")
            case 1:
                return (path, v_path)
            case 2:
                return (path, v_path)
            case _:
                print("ERROR")