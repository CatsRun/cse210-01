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
    
    

    print(instructions)
    #print board 
    board = (f' {a} | {b} | {c} \n {horizontalLine} \n {d} | {e} | {f} \n {horizontalLine} \n {g} | {h} | {i}')
    # solutionTest(a,b,c,d,e,f,g,h,i)

    # input1()
    symbol = input('Are you X or O? ')
    #let the input from symbol change the mnumber in location
    
    #use a try block to make only a number input and an error if it is anything else
    location = int(input('Where do you want to go? '))
    

    #why does the variable in board not change when the variable changes to symbol?
    board = (f' {a} | {b} | {c} \n {horizontalLine} \n {d} | {e} | {f} \n {horizontalLine} \n {g} | {h} | {i}')
    # print(board) #this in in the while loop

    # while loop runs until all squares are filled, 9 times
    while(z < 9 ):
        z += 1
        locSym(location, symbol,a,b,c,d,e,f,g,h,i)
        solutionTest(a,b,c,d,e,f,g,h,i, board)

        symbol = input('Are you X or O? ')
        location = int(input('Where do you want to go? '))


        print(z)
        # print(board)
        # input1()

    

def solutionTest(a,b,c,d,e,f,g,h,i, board):
    """checks to see if the game is won

    Parameters: letters a - i representing the spaces on the tic-tac-toe board. 

    Return:if game it over  
    """
    #set x = i then change test to be == i and test for each X and O
    # if a == 'x' and b == 'q' and c == 't':
    
    #how do I turn this into a case?
    if  a == b == c:
       answer = print(f'Tic-tac-toe {a} won!')
    elif a == d == g:
        answer = print(f'Tic-tac-toe {a} won!')
    elif b == e == h:
        answer = print(f'Tic-tac-toe {b} won!')
    elif c == f == i:
        answer = print(f'Tic-tac-toe {c} won!')
    elif d == e == f:
        answer = print(f'Tic-tac-toe {d} won!')
    elif g == h == i:
        answer = print(f'Tic-tac-toe {g} won!')
    elif a == e == i:
        answer = print(f'Tic-tac-toe {a} won!')
    elif c == e == g:
        answer = print(f'Tic-tac-toe {c} won!')
    else: 
        answer =  print(board)
        # input1()
        #add function call to run the question

def locSym(location, symbol, a, b, c, d, e, f, g, h, i):#**********why does a b c not pas into this function when location and symbol do?
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
    elif location == 9:
        i = symbol
    
    # return answer is a return needed?
    #remove 'answer =' ?

# """User input for symbol and location     
# """
# def input1():
#     symbol = input('Are you X or O? ')

#     location = input('Where do you want to go? ')




#user input must be changed to lower case but accept upper and lower case


#case to change user input into constant symbol 
#o, O, 0 == o
#x, X == X


# def solutionCaseText(a,b,c,d,e,f,g,h,i):
#     # case: 
#     return

















if __name__ == "__main__":
    main()