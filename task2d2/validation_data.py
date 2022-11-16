#----------------------------------------------------------------------------
#----------IMPORTS-----------------------------------------------------------
#----------------------------------------------------------------------------

#----------------------------------------------------------------------------
#----------VARIABLES---------------------------------------------------------
#----------------------------------------------------------------------------
sym_for_name = (' ', '-', "'")
#----------------------------------------------------------------------------
#----------FUNCTIONS---------------------------------------------------------
#----------------------------------------------------------------------------
def disc_valid(disc):
    for i in range(len(disc)):
        if disc[i] == '|':
            return False
    else:
        return True
#----------------------------------------------------------------------------
def is_return(symbols):
    return symbols == '/return'  
#----------------------------------------------------------------------------
def is_valid_sym(sym):
    global sym_for_name
    for i in range(len(sym_for_name)):  
        if sym == sym_for_name[i]:
            return True
    else:
        return False
#----------------------------------------------------------------------------
def valid_name(nm):
    length = len(nm)
    if fist_last_sym_check(nm[0]) and fist_last_sym_check(nm[length - 1]):

        for i in range(length - 1):
            if nm[i].isalpha() or is_valid_sym(nm[i]):
                sym_sum = nm[i] + nm[i + 1]
                if (sym_sum == ' -') or (sym_sum == '- '):
                    return False
            else:
                return False
        else:
            return True
    return False
#----------------------------------------------------------------------------
def fist_last_sym_check(sym):
    return (sym.isalpha()) or (sym == "'")
#----------------------------------------------------------------------------
def tel_part(cue_i, sym, tel_str):
    if tel_str[cue_i].isdigit():
        for i in range(cue_i, len(tel_str)):
            if tel_str[i].isdigit():
                i += 1
            elif tel_str[i] == sym:
                if i > cue_i:
                    
                    return tel_str[cue_i : i]
            else:
                return 'err'
        else:
            return 'err'
    return 'err'
#----------------------------------------------------------------------------
def valid_tel(tel):
    tel_list = []
    if tel[0] == '+':
        st_i = 1
        sign_t = ('(', ')', '-', '-')
        
        for i in range(len(sign_t)):
            cur_part = tel_part(st_i, sign_t[i], tel)
            if cur_part == 'err':
                return False
            else:
                tel_list.append(cur_part)
                st_i += len(tel_list[-1]) + 1
            

        if tel[st_i : ].isdigit():
            tel_list.append(tel[st_i : ])
        else:
            return False

        return tuple(tel_list)
    else:
        return False
#----------------------------------------------------------------------------