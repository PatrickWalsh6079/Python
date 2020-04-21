#################
# starting board.
#################
blank_board = ['   ', '|', '   ', '|', '   ', '\n---', '----', '----', '\n   ', '|', '   ', '|', '   ', '\n---', '----',
               '----', '\n   ', '|', '   ', '|', '   ','\n\n']

#################
# welcome screen.
#################
print('########################################\n########################################\n\n     WELCOME TO TIC TAC TOE! \n\n########################################\n########################################\n\n')

#########################################################
# function that continually prints board until game ends.
#########################################################
def print_board(board):
    end_game = False
    ###############################################
    # set to 3 until players choose who goes first.
    ###############################################
    counter = 3
    
    ####################################
    # decide which player will go first.
    ####################################
    while counter == 3:
        welcome_screen = input("Who would like to go first?\n\nPlease enter '1' or '2' and press 'Enter'\n")
        if welcome_screen == '1':
            counter = 0
            print('\n'*40)
        elif welcome_screen == '2':
            counter = 1
            print('\n'*40)
        else:
            print('\n'*40)
            print("Invalid entry! Must enter either '1' or '2'\n")
            continue
        

    ######################################################
    # while loop that continues as long as no one has won.
    ######################################################
    while end_game == False:
        
        ##################################################
        # variable that prints screen at end of each turn.
        ##################################################
        screen_display = print(''.join(board))

        ####################################################
        # variables that determine X or O and player number.
        ####################################################
        if counter % 2 == 0:
            player_turn = 1
            player_move = ' X '
        else:
            player_turn = 2
            player_move = ' O '

        ###################################################
        # input screen that asks for 1-9 to determine move.
        ###################################################
        player1_input = input("Player {}'s Turn:".format(player_turn))

        #########################################################################
        # takes input 1-9 and checks if that space is already filled. if it
        # is not filled, it puts either an X or O, depending on whose turn it is.
        #########################################################################
        if player1_input == '7':
            if blank_board[0] == '   ':
                blank_board[0] = player_move
                counter += 1
            else:
                print('\n'*40)
                print('Space already taken! Choose another spot.\n')
                continue
        elif player1_input == '8':
            if blank_board[2] == '   ':
                blank_board[2] = player_move
                counter += 1
            else:
                print('\n'*40)
                print('Space already taken! Choose another spot.\n')
                continue
        elif player1_input == '9':
            if blank_board[4] == '   ':
                blank_board[4] = player_move
                counter += 1
            else:
                print('\n'*40)
                print('Space already taken! Choose another spot.\n')
                continue
        elif player1_input == '4':
            if blank_board[8] == '\n   ':
                blank_board[8] = '\n' + player_move
                counter += 1
            else:
                print('\n'*40)
                print('Space already taken! Choose another spot.\n')
                continue
        elif player1_input == '5':
            if blank_board[10] == '   ':
                blank_board[10] = player_move
                counter += 1
            else:
                print('\n'*40)
                print('Space already taken! Choose another spot.\n')
                continue
        elif player1_input == '6':
            if blank_board[12] == '   ':
                blank_board[12] = player_move
                counter += 1
            else:
                print('\n'*40)
                print('Space already taken! Choose another spot.\n')
                continue
        elif player1_input == '1':
            if blank_board[16] == '\n   ':
                blank_board[16] = '\n' + player_move
                counter += 1
            else:
                print('\n'*40)
                print('Space already taken! Choose another spot.\n')
                continue
        elif player1_input == '2':
            if blank_board[18] == '   ':
                blank_board[18] = player_move
                counter += 1
            else:
                print('\n'*40)
                print('Space already taken! Choose another spot.\n')
                continue
        elif player1_input == '3':
            if blank_board[20] == '   ':
                blank_board[20] = player_move
                counter += 1
            else:
                print('\n'*40)
                print('Space already taken! Choose another spot.\n')
                continue
        else:
            print('\n'*40)
            print("Invalid entry! Must entry a number between 1-9 and hit 'Enter'\n")
            continue

        ############
        # if O wins.
        ############
        if blank_board[0] == ' O ' and blank_board[2] == ' O ' and blank_board[4] == ' O ' or blank_board[
            8] == '\n O ' and blank_board[10] == ' O ' and blank_board[12] == ' O ' or blank_board[16] == '\n O ' and \
                blank_board[18] == ' O ' and blank_board[20] == ' O ' or blank_board[0] == ' O ' and blank_board[
            8] == '\n O ' and blank_board[16] == '\n O ' or blank_board[2] == ' O ' and blank_board[10] == ' O ' and \
                blank_board[18] == ' O ' or blank_board[4] == ' O ' and blank_board[12] == ' O ' and blank_board[
            20] == ' O ' or blank_board[0] == ' O ' and blank_board[10] == ' O ' and blank_board[20] == ' O ' or \
                blank_board[16] == '\n O ' and blank_board[10] == ' O ' and blank_board[4] == ' O ':
            
            #########################################################
            # says which player won; asks if you want to play again.
            #########################################################
            print('\n' * 40)
            print('\n\nPlayer 2 wins!!!\n\n')
            print(''.join(board), '\n', '\n')
            
            while 1 == 1:
                play_again = input("Would you like to play again? Type 'Yes' or 'No' and hit 'Enter'\n")
                if play_again == 'yes'.lower():

                    #######################
                    # reset board to blank.
                    #######################
                    blank_board[0] = '   '
                    blank_board[2] = '   '
                    blank_board[4] = '   '
                    blank_board[8] = '\n   '
                    blank_board[10] = '   '
                    blank_board[12] = '   '
                    blank_board[16] = '\n   '
                    blank_board[18] = '   '
                    blank_board[20] = '   '

                    print('\n' * 40)
                
                    ####################################
                    # decide which player will go first.
                    ####################################
                    counter = 3
                    while counter == 3:
                        welcome_screen = input("Who would like to go first?\n\nPlease enter '1' or '2' and press 'Enter'\n")
                        if welcome_screen == '1':
                            counter = 0
                            break
                        elif welcome_screen == '2':
                            counter = 1
                            break
                        else:
                            print('\n'*40)
                            print("Invalid entry! Must enter either '1' or '2'\n")
                            continue
                    break
                        
                elif play_again == 'no'.lower():
                    print('\n' * 40)
                    print('\n\nThank you for playing!\n\n')
                    end_game = True
                    break
                    
                else:
                    print('\n' * 40)
                    print("Invalid entry! Must enter 'Yes' or 'No' and hit 'Enter'\n")
                    continue

        ############
        # if X wins.
        ############
        elif blank_board[0] == ' X ' and blank_board[2] == ' X ' and blank_board[4] == ' X ' or blank_board[
            8] == '\n X ' and blank_board[10] == ' X ' and blank_board[12] == ' X ' or blank_board[16] == '\n X ' and \
                blank_board[18] == ' X ' and blank_board[20] == ' X ' or blank_board[0] == ' X ' and blank_board[
            8] == '\n X ' and blank_board[16] == '\n X ' or blank_board[2] == ' X ' and blank_board[10] == ' X ' and \
                blank_board[18] == ' X ' or blank_board[4] == ' X ' and blank_board[12] == ' X ' and blank_board[
            20] == ' X ' or blank_board[0] == ' X ' and blank_board[10] == ' X ' and blank_board[20] == ' X ' or \
                blank_board[16] == '\n X ' and blank_board[10] == ' X ' and blank_board[4] == ' X ':
            
            #########################################################
            # says which player won; asks if you want to play again.
            #########################################################
            print('\n' * 40)
            print('\n\nPlayer 1 wins!!!\n\n')
            print(''.join(board), '\n', '\n')
            while 1 == 1:
                play_again = input("Would you like to play again? Type 'Yes' or 'No' and hit 'Enter'\n")
                if play_again == 'yes'.lower():

                    #######################
                    # reset board to blank.
                    #######################
                    blank_board[0] = '   '
                    blank_board[2] = '   '
                    blank_board[4] = '   '
                    blank_board[8] = '\n   '
                    blank_board[10] = '   '
                    blank_board[12] = '   '
                    blank_board[16] = '\n   '
                    blank_board[18] = '   '
                    blank_board[20] = '   '

                    print('\n' * 40)
                
                    ####################################
                    # decide which player will go first.
                    ####################################
                    counter = 3
                    while counter == 3:
                        welcome_screen = input("Who would like to go first?\n\nPlease enter '1' or '2' and press 'Enter'\n")
                        if welcome_screen == '1':
                            counter = 0
                            break
                        elif welcome_screen == '2':
                            counter = 1
                            break
                        else:
                            print('\n'*40)
                            print("Invalid entry! Must enter either '1' or '2'\n")
                            continue
                    break
                    
                elif play_again == 'no'.lower():
                    print('\n' * 40)
                    print('\n\nThank you for playing!\n\n')
                    end_game = True
                    break
                
                else:
                    print('\n' * 40)
                    print("Invalid entry! Must enter 'Yes' or 'No' and hit 'Enter'\n")
                    continue
        
        
        ##################
        # if it is a tie.
        #################
        elif blank_board[0] != '   ' and blank_board[2] != '   ' and blank_board[4] != '   ' and blank_board[8] != '\n   ' and blank_board[10] != '   ' and blank_board[12] != '   ' and blank_board[16] != '\n   ' and blank_board[18] != '   ' and blank_board[20] != '   ':
            print('\n' * 40)
            print('\n\nTie!\n\n')
            print(''.join(board), '\n', '\n')
            while 1 == 1:
                play_again = input("Would you like to play again? Type 'Yes' or 'No' and hit 'Enter'\n")
                if play_again == 'yes'.lower():

                    #######################
                    # reset board to blank.
                    #######################
                    blank_board[0] = '   '
                    blank_board[2] = '   '
                    blank_board[4] = '   '
                    blank_board[8] = '\n   '
                    blank_board[10] = '   '
                    blank_board[12] = '   '
                    blank_board[16] = '\n   '
                    blank_board[18] = '   '
                    blank_board[20] = '   '

                    print('\n' * 40)
                
                    ####################################
                    # decide which player will go first.
                    ####################################
                    counter = 3
                    while counter == 3:
                        welcome_screen = input("Who would like to go first?\n\nPlease enter '1' or '2' and press 'Enter'\n")
                        if welcome_screen == '1':
                            counter = 0
                            break
                        elif welcome_screen == '2':
                            counter = 1
                            break
                        else:
                            print('\n'*40)
                            print("Invalid entry! Must enter either '1' or '2'\n")
                            continue
                    break
                    
                elif play_again == 'no'.lower():
                    print('\n' * 40)
                    print('\n\nThank you for playing!\n\n')
                    end_game = True
                    break
                
                else:
                    print('\n' * 40)
                    print("Invalid entry! Must enter 'Yes' or 'No' and hit 'Enter'\n")
                    continue
        
        
        ########################################################
        # clears previous output by printing several new lines.
        ########################################################
        if end_game == False:
            print('\n' * 40)


    return screen_display

############################
# command to call function.
############################
print_board(blank_board)