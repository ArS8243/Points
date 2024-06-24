##board = [[' ']*3 for _ in range(3)]
##print(board)
### Функция для отображения игрового поля
##def display_board():
##    for row in board:
##        print('|'.join(row))
##        print('-'*5)
##display_board()

alf = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J']

def board(n):
    if n > 20:
        print('Слишком большая доска!')
        return None
    a = [[alf[i] for i in range(n)]]+[ [alf[i+1]]+['.' for j in range(n-1)] for i in range(n-1) ]
    return a

    

def display_board(a):
    for i in range(len(a)):
        print()
        for j in range(len(a[i])):
            print(a[i][j],end=' ')

n = int(input('Размер доски(не больше 20): '))            
display_board(board(n))
print()
b = board(n)
print(b)
##desk = [['0' for j in range(n-1)] for i in range(n-1) ]
##for i in range(len(desk)):
##        print()
##        for j in range(len(desk[i])):
##            print(desk[i][j],end=' ')

##0 пустая клетка
##1 белая точка
##2 черная точка
##3 захваченная белая точка
##4 захваченная черная точка
##
##
def turn(n,x,y):
    l = [1,2]
    if b[x][y] == '.':
        b[x][y] = l[n]
        return True
    else:
        return False
    
n = 0
while True:
    print()
    k = input(f'Ход {n+1} игрока(enter чтобы закончить) ')
    if not k:
        #end()
        break
    if turn(n,int(alf.index(k[0])),int(alf.index(k[1]))):
        #chek
        if n == 1: n = 0
        else: n+=1
        display_board(b)
    else:
        print("Ошибка! Попробуйте снова")







    
    
