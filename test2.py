##for i in range(10):
##    print(ord(str(i)))

    
##for i in range(200):
##    print(chr(i))

'''
TODO:
Вся матрица(доска) из Point()
Добавить пустую точку
turn
game
'''
alf = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J']
skins = ['.','@','#','!','x','o']
class Point():
    def __init__(self,x,y,pl = 0):
        self.imp = 0
        self.x = x
        self.y = y
        self.type = pl
        self.skin = pl
        self.act = True
    def cout(self):
        return skins[self.skin]
        
def board(n):
    if n > 20:
        print('Слишком большая доска!')
        return None
    a = [[alf[i] for i in range(n)]]+[ [alf[i+1]]+[Point(i,j) for j in range(n-1)] for i in range(n-1) ]
    return a

def mates(p1, p2):
    match p1,p2:
        case 1,2: return False
        case 2,1: return False
    return True 


##def display(a):
##    print('!!!!!!!!!!!!!!!!!!!!!!!')
##    for i in range(len(a)):
##        print()
##        for j in range(len(a[i])):
##            try:
##                print(a[i][j].cout(),end=' ')
##            except:
##                print(a[i][j],end=' ')
                

def check(board):
    #try:
    ln = len(board)-1
    b = [ [board[j+1][i+1] for i in range(ln)] for j in range(ln) ]
    for i in range(ln):
        for j in range(ln):
            if (i == 0 or i == ln-1) or (j == 0 or j == ln-1):
                b[i][j].imp = 1
    for n in range(int(ln)):
        for i in range(ln):
            for j in range(ln):
                if b[i][j].imp: b[i][j].imp = 1
                elif b[i+1][j].imp and mates(b[i][j].type,b[i+1][j].type):
                    b[i][j].imp = 1
                    b[i][j].skin = b[i][j].type
                elif b[i][j+1].imp and mates(b[i][j].type,b[i][j+1].type):
                    b[i][j].imp = 1
                    b[i][j].skin = b[i][j].type
                elif b[i-1][j].imp and mates(b[i][j].type,b[i-1][j].type):
                    b[i][j].imp = 1
                    b[i][j].skin = b[i][j].type
                elif b[i][j-1].imp and mates(b[i][j].type,b[i][j-1].type):
                    b[i][j].imp = 1
                    b[i][j].skin = b[i][j].type
                else:
                    b[i][j].skin = b[i][j].type + 2
                    b[i][j].act = False
                    print('!!!!!!!!!!!!!!!!!!!!!!')
    for i in range(ln):
            for j in range(ln):
                b[i][j].imp = 0
      #for i in range(ln):
          #for j in range(ln):
              #if b[i][j].imp: b[i][j].skin = 5
    #except: print("Ошибка проверки!")


def end():
    a =1
##def display_board(a):
##    for i in range(len(a)):
##        print()
##        for j in range(len(a[i])):
##            print(a[i][j],end=' ')


        
        
##p1 = Point(1,2)
##p2 = Point(4,8,False)
##print(p1.x,p1.act)
##print(p2.x,p2.act)


class Board():
    alf = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J']    

    def __init__(self,n):
        self.n = n
        self.b = board(n)
        
    def display(self):
        a = self.b
        for i in range(len(a)):
            print()
            for j in range(len(a[i])):
                try:
                    print(a[i][j].cout(),end=' ')
                except:
                    print(a[i][j],end=' ')
    def get(self,x,y):
        return self.b[x][y]


b = Board(int(input('Board size (max 20):')))
b.display()


##def turn(player,x,y):
##    Point.set(x,y)
##    check_lines()
##    print(pole)

def turn(n,x,y):
    while True:
        if b.b[x][y].type == 0:
            b.b[x][y] = Point(x,y,n)
            check(b.b)
            break
        else:
            print("Ошибка! Попробуйте снова")
            return None
    

def game():
    n = 0
    while True:
        print()
        k = input(f'Ход {n+1} игрока(enter чтобы закончить) ')
        if not k:
            #end() return res
            break
        turn(n+1,int(alf.index(k[0])),int(alf.index(k[1])))
        n = int(not n)
        b.display()
game()



    
    
##point_list = [[1,0],[0,1],[-1,0],[0,-1]]
##def fill(point_list):
##    flag = False
##    x = min([i[0] for i in point_list])
##    print(x)
##    y = min([i[1] for i in point_list])-1
##    while [i[0] for i in point_list].count(x) > 0:
##        if [i[0] for i in point_list].count(x) == 0:
##            x+=1
##            continue
##        else:
##            while True:
##                y-=1
##                if [x,y] in point_list:
##                    flag = not flag







        
