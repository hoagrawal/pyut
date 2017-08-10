def print_board(size):
    ''' print a board of x X x'''

    Next_line=1-size
    for i in range(size):
         Next_line = Next_line+ size
         line=[]
         for j in range (size):
            line.append(Next_line+j)
         print(line)

print_board(3)