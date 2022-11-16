from emoji import emojize


def task_enter():
    print(f'Task #1')
    while True:
        stro = input("Enter '/start' to start the game or '/exit' to exit task: ")
        if stro == '/exit':
            return
        elif stro == '/start':
            task_basic_func()
        else:
            print("Invalid cmd. Try again.")
#--------------------------------------------------------------------
#--------------------------------------------------------------------
#--------------------------------------------------------------------
def task_basic_func():
    print('Hello, my dear friends! Let\'s play the game (Music from "Saw" on the back!).')
    battle_area = empty_area()
    print_area(battle_area)

    turn = True
    cnt = 1

    vert = [0, 0, 0]
    horz = [0, 0, 0]
    diag = [0, 0]
    while True:
        
        cur_cord = get_ij_from_cell_num(turn, battle_area)
        score = win_score(turn)
        battle_area = set_cell(turn, battle_area, cur_cord)
        print_area(battle_area)
        horz[cur_cord[0] - 1] += score
        vert[cur_cord[1] - 1] += score
        print(cnt)
        if (cur_cord[0] == cur_cord[1]):
            diag[0] += score
        if (cur_cord[0] + cur_cord[1] == 4):
            diag[1] += score
        if cnt >= 9:
            print("No chamion. Both will die!")
            break 
        elif cnt >= 5:
            if win_check(horz, vert, diag):
                print(f"{player_name(turn)} wins! {player_name(not turn)} will die!")
                break
                   
        turn = not turn
        cnt += 1
#--------------------------------------------------------------------
#--------------------------------------------------------------------
#--------------------------------------------------------------------
def empty_area():
    area = [['' for j in range(5)] for i in range(5)]
    
    for i in range(5):
        area[i][0] = '/////'
        area[i][4] = '/////'
    for i in range(1, 4):
        area[0][i] = '/////'
        area[4][i] = '/////'
        for j in range(1, 4):
            area[i][j] = f"| {j + (i - 1) * 3} |"
    return area
#--------------------------------------------------------------------
#--------------------------------------------------------------------
#--------------------------------------------------------------------
def print_area(area):
    length = len(area)
    for i in range(length):
        for j in range(length):
            print(area[i][j], end='')
        print()
#--------------------------------------------------------------------
#--------------------------------------------------------------------
#--------------------------------------------------------------------
def set_cell(t, area, cord_list):
    area[cord_list[0]][cord_list[1]] = insert_sign(sign_change(t))
    return area
#--------------------------------------------------------------------
#--------------------------------------------------------------------
#--------------------------------------------------------------------
def get_ij_from_cell_num(t, area):
    cell = int(input(f"{player_name(t)}'s go! Choose cell number: "))
    while True:
        if 9 >= cell >= 1:
            i = ((cell - 1) // 3) + 1
            j = ((cell - 1) % 3) + 1
            if (area[i][j] == emojize('| :thumbs_up: |')) or (area[i][j] == emojize('| :thumbs_down: |')):
                cell = int(input("Cell is filled. Choose another: "))
            else:
                return [i , j]
        else:
            cell = int(input("Invalid input. Try again: "))
#--------------------------------------------------------------------
#--------------------------------------------------------------------
#--------------------------------------------------------------------
def insert_sign(sign):
    return str('| ' + sign + ' |')
#--------------------------------------------------------------------
#--------------------------------------------------------------------
#--------------------------------------------------------------------
def win_score(t):
    if t:
        return 1
    else:
        return -1
#--------------------------------------------------------------------
#--------------------------------------------------------------------
#--------------------------------------------------------------------
def sign_change(t):
    if t:
        return emojize(':thumbs_up:')
    else:
        return emojize(':thumbs_down:')
#--------------------------------------------------------------------
#--------------------------------------------------------------------
#--------------------------------------------------------------------
def win_check(h, v, d):
    for i in range(len(h)):
        if (h[i] == 3) or (h[i] == -3):
            return True
    for i in range(len(d)):
        if (d[i] == 3) or (d[i] == -3):
            return True
    for i in range(len(v)):
        if (v[i] == 3) or (v[i] == -3):
            return True
    return False
#--------------------------------------------------------------------
#--------------------------------------------------------------------
#--------------------------------------------------------------------
def player_name(t):
    if t:
        return 'Crusader'
    else:
        return 'Zero'
#--------------------------------------------------------------------
#--------------------------------------------------------------------
#--------------------------------------------------------------------
task_enter()
