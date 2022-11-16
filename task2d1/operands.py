#----------------------------------------------------------------------------
#----------IMPORTS-----------------------------------------------------------
#----------------------------------------------------------------------------

#----------------------------------------------------------------------------
#----------VARIABLES---------------------------------------------------------
#----------------------------------------------------------------------------

#----------------------------------------------------------------------------
#----------FUNCTIONS---------------------------------------------------------
#----------------------------------------------------------------------------
def is_valid(text):
    opers = text.strip().split()
    length = len(opers)
    if length == 2:
        for i in range(length):
            cur_str = opers[i].replace('-', '+-')
            if cur_str[0] == '+':
                cur_str = cur_str[1 : ]
            parts = cur_str.split('+')
            if len(parts) == 2:
                if parts[0][-1] == 'i':
                    if parts[1][-1] == 'i':
                        return -3
                    else:
                        if len(parts[0]) == 1:
                            buf = '1'
                        else:
                            buf = parts[0][ : -1]
                        parts[0] = parts[1]
                        parts[1] = buf
                else:
                    if parts[1][-1] != 'i':
                        return -3
                    else:
                        if len(parts[1]) == 1:
                            parts[1] = '1'
                        else:
                            parts[1] = parts[1][ : -1]
            elif len(parts) == 1:
                if parts[0][-1] == 'i':
                    if len(parts[0]) == 1:
                        parts[0] = '1'
                    else:
                        parts[0] = parts[0][: -1]
                    parts.insert(0, "0")
                else:
                    parts.append('0')
            else:
                return -2   #invalid complex number form
            if parts[1] == '-':
                parts[1] = '-1'
            for j in range(2):
                if parts[j] == '-0':
                    parts[j] = '0'
            if not(is_number(parts[0]) and is_number(parts[1])):
                return -4
        else:
            return 1
    else:
        return -1   #more than two operands
#----------------------------------------------------------------------------
def is_number(str_num):
    #is_neg = False
    abs_mean = ''
    if str_num[0] == '-':
        #is_neg = True
        abs_mean = str_num[1 : ]
    else:
        abs_mean = str_num
        #is_neg = False
    parts = abs_mean.split('.')
    length = len(parts)
    if length == 1:
        return parts[0].isdigit()
    elif length == 2:
        return parts[0].isdigit() and parts[1].isdigit()
    else:
        return False
#----------------------------------------------------------------------------
def invalid_answer(code):
    match code:
        case -1:
            return 'More than two operands were entered!'
        case -2:
            return 'Invalid complex number form!'
        case -3:
            return 'Invalid complex number form!'
        case -4:
            return 'Invalid symbols were used!'
        case _:
            return 'ERROR!'
#----------------------------------------------------------------------------
def coefs(text):
    opers = text.strip().split()
    length = len(opers)
    cfc = []
    if length == 2:
        for i in range(length):
            cur_str = opers[i].replace('-', '+-')
            if cur_str[0] == '+':
                cur_str = cur_str[1 : ]
            parts = cur_str.split('+')
            if len(parts) == 2:
                if parts[0][-1] == 'i':
                    if parts[1][-1] == 'i':
                        return
                    else:
                        if len(parts[0]) == 1:
                            buf = '1'
                        else:
                            buf = parts[0][ : -1]
                        parts[0] = parts[1]
                        parts[1] = buf
                else:
                    if parts[1][-1] != 'i':
                        return
                    else:
                        if len(parts[1]) == 1:
                            parts[1] = '1'
                        else:
                            parts[1] = parts[1][ : -1]
            elif len(parts) == 1:
                if parts[0][-1] == 'i':
                    if len(parts[0]) == 1:
                        parts[0] = '1'
                    else:
                        parts[0] = parts[0][: -1]
                    parts.insert(0, "0")
                else:
                    parts.append('0')
            else:
                return
            if parts[1] == '-':
                parts[1] = '-1'
            for j in range(2):
                if parts[j] == '-0':
                    parts[j] = '0'
            cfc.append((float(parts[0]), float(parts[1])))
        else:
            return cfc
#----------------------------------------------------------------------------
