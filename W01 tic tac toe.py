""" tic - tac - toe by Angela Murray"""
def main():
    #initialises and sets variables
    instructions = 'Instructions: There are two players. One is X the other O. \nX goes first \nPlay alternates back and forth between each player. \nEnter the number that isin the space you want to go\nthe first player who gets 3 in a row wins!'
    horizontalLine = '--+---+--'
    a = 1 
    b = 2 
    c = 3
    d = 4 
    e = 5
    f = 6
    g = 7
    h = 8 
    i = 9
    
    z = 0
    go = ''
    

    print(instructions)
    #print board 
    board = (f' {a} | {b} | {c} \n {horizontalLine} \n {d} | {e} | {f} \n {horizontalLine} \n {g} | {h} | {i}')

    # symbol = input('Are you X or O? ')
    #let the input from symbol change the mnumber in location
    
    #use a try block to make only a number input and an error if it is anything else
    # location = int(input('Where do you want to go? '))
    
    #changes the board location to the user chosen symbol
    # if location == 1:
    #     a = symbol
    # elif location == 2:
    #     b = symbol
    # elif location == 3:
    #     c = symbol
    # elif location == 4:
    #     d = symbol
    # elif location == 5:
    #     e = symbol
    # elif location == 6:
    #     f = symbol
    # elif location == 7:
    #     g = symbol
    # elif location == 8:
    #     h = symbol
    # elif location == 9:
    #     i = symbol
    #add else print(please enter a valid number)
    
    #why does the variable in board not change when the variable changes to symbol?
    board = (f' {a} | {b} | {c} \n {horizontalLine} \n {d} | {e} | {f} \n {horizontalLine} \n {g} | {h} | {i}')
    print(board) #this prints before the while loop

    # while loop runs until all squares are filled, 9 times
    while(z < 9 and go != 'no' ): #why did == yes not work when != no works?
        z += 1
        symbol = input('Are you X or O? ')
        location = int(input('Where do you want to go? '))
            #changes the board location to the user chosen symbol
        if location == 1:
            a = symbol
        elif location == 2:
            b = symbol
        elif location == 3:
            c = symbol
        elif location == 4:
            d = symbol
        elif location == 5:
            e = symbol
        elif location == 6:
            f = symbol
        elif location == 7:
            g = symbol
        elif location == 8:
            h = symbol
        else: 
            i = symbol
        go = solutionTest(a,b,c,d,e,f,g,h,i, board, horizontalLine, go) #why did setting 'go = ...' make this work?

        # print(z) #tracks the counter while testing
        # print(board)
        # input1()


def solutionTest(a,b,c,d,e,f,g,h,i, board,horizontalLine, go): #why is go acting like a local vaiable when the others are global?
    """checks to see if the game is won

    Parameters: letters a - i representing the spaces on the tic-tac-toe board. 

    Return:if game it over  
    """
   
    board = (f' {a} | {b} | {c} \n {horizontalLine} \n {d} | {e} | {f} \n {horizontalLine} \n {g} | {h} | {i}')

    #how do I turn this into a case?
    if  a == b == c:
       answer = print(f'Tic-tac-toe {a} won!')
       go = 'no'
       print(board)
       return go
    elif a == d == g:
        answer = print(f'Tic-tac-toe {a} won!')
        go = 'no'
        print(board)
        return go
    elif b == e == h:
        answer = print(f'Tic-tac-toe {b} won!')
        go = 'no'
        print(board)
        return go
    elif c == f == i:
        answer = print(f'Tic-tac-toe {c} won!')
        go = 'no'
        print(board)
        return go
    elif d == e == f:
        answer = print(f'Tic-tac-toe {d} won!')
        go = 'no'
        print(board)
        return go
    elif g == h == i:
        answer = print(f'Tic-tac-toe {g} won!')
        go = 'no'
        print(board)
        return go
    elif a == e == i:
        answer = print(f'Tic-tac-toe {a} won!')
        go = 'no'
        print(board)
        return go
    elif c == e == g:
        answer = print(f'Tic-tac-toe {c} won!')
        go = 'no'
        print(board)
        return go
    else: 
        answer =  print((f' {a} | {b} | {c} \n {horizontalLine} \n {d} | {e} | {f} \n {horizontalLine} \n {g} | {h} | {i}'))

if __name__ == "__main__":
    main()