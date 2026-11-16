Loop = True

while Loop:#jsghfgjgfhjagjhfgjhsa
    row_0 = ['_', '_', '_', '_', '_', '_', '_', '_', '_']
    row_1 = ['_', '_', '_', '_', '_', '_', '_', '_', '_']
    row_2 = ['_', '_', '_', '_', '_', '_', '_', '_', '_']
    row_3 = ['_', '_', '_', '_', '_', '_', '_', '_', '_']
    row_4 = ['_', '_', '_', '_', '_', '_', '_', '_', '_']
    row_5 = ['_', '_', '_', '_', '_', '_', '_', '_', '_']
    row_6 = ['_', '_', '_', '_', '_', '_', '_', '_', '_']
    row_7 = ['_', '_', '_', '_', '_', '_', '_', '_', '_']
    Whole = [row_0, row_1, row_2, row_3, row_4, row_5, row_6, row_7]
    num_store1 = []
    num_store2 = []
    num_store3 = []
    num_store4 = []
    num_store5 = []
    num_store6 = []
    num_store7 = []
    num_store_list = [num_store1, num_store2, num_store3, num_store4, num_store5, num_store6, num_store7]
    rounds = 0
    position = 1
    win_condition = False
    player = 'placeholder'
    while rounds < 42 and win_condition == False:

        for row in str(654321):
            liner = str(Whole[int(row)]).replace("['_', '", '').replace("', '_']", "").replace("', '", " | ")
            print(liner)
        print('1 | 2 | 3 | 4 | 5 | 6 | 7')

        if rounds % 2 == 0:
            player = 'X'
        else:
            player = 'O'
        proper_input = False
        while not proper_input:
            position = input('Player ' + player + "'s turn : ")
            if not (position == '1' or position == '2' or position == '3' or position == '4' or position == '5' or position == '6' or position == '7'):
                print("invalid inputs")
            elif len(num_store_list[int(position) - 1]) == 6:
                print("invalid input")
            else:
                position = int(position)
                Whole[len(num_store_list[int(position) - 1]) + 1][position] = player
                num_store_list[int(position) - 1].append(player)
                rounds += 1
                proper_input = True

        position_checker = True
        y_pos = len(num_store_list[int(position) - 1])
        x_pos = int(position)
        while position_checker:
            if Whole[len(num_store_list[int(position) - 1])][x_pos] == \
                    Whole[len(num_store_list[int(position) - 1]) + 1][
                        x_pos + 1]:
                x_pos += 1
            else:
                position_checker = False

        position_checker = True
        xy_pos = int(position)
        yx_pos = len(num_store_list[int(position) - 1])
        while position_checker:
            if Whole[yx_pos][xy_pos] == Whole[yx_pos + 1][xy_pos + 1]:
                xy_pos += 1
                yx_pos += 1
            else:
                position_checker = False

        position_checker = True
        xy_pos_down = int(position)
        yx_pos_down = len(num_store_list[int(position) - 1])
        while position_checker:
            if Whole[yx_pos_down][xy_pos_down] == Whole[yx_pos_down - 1][xy_pos_down + 1]:
                xy_pos_down += 1
                yx_pos_down -= 1
            else:
                position_checker = False

        if Whole[yx_pos_down][xy_pos_down] == Whole[yx_pos_down + 1][xy_pos_down - 1] == Whole[yx_pos_down + 2][
            xy_pos_down - 2] == Whole[yx_pos_down + 3][xy_pos_down - 3]:
            win_condition = True
        if Whole[yx_pos][xy_pos] == Whole[yx_pos - 1][xy_pos - 1] == Whole[yx_pos - 2][xy_pos - 2] == Whole[yx_pos - 3][
            xy_pos - 3]:
            win_condition = True
        if Whole[y_pos][x_pos] == Whole[y_pos][x_pos - 1] == Whole[y_pos][x_pos - 2] == Whole[y_pos][x_pos - 3]:
            win_condition = True
        if Whole[y_pos][int(position)] == Whole[y_pos - 1][int(position)] == Whole[y_pos - 2][int(position)] == \
                Whole[y_pos - 3][int(position)]:
            win_condition = True

    for row in str(654321):
        liner = str(Whole[int(row)]).replace("['_', '", '').replace("', '_']", "").replace("', '", " | ")
        print(liner)

    print('Player ' + player + ' won')
    valid_check = True
    while valid_check:
        Replay = input('Would you guys like to play again? (type y/n): ')
        if Replay == 'y' :
            print('NEW GAME')
            valid_check = False
        elif Replay == 'n' :
            Loop = False
            valid_check = False
        else:
            print('Invalid input try again(no exclamation mark)')
