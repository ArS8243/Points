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
skins = ['@','#']
def board(n,s = '.'):
    if n > 20:
        print('Слишком большая доска!')
        return None
    a = [[alf[i] for i in range(n)]]+[ [alf[i+1]]+[s for j in range(n-1)] for i in range(n-1) ]
    return a


def display_board(a):
    for i in range(len(a)):
        print()
        for j in range(len(a[i])):
            print(a[i][j],end=' ')

            

class Point():
    def __init__(self,x,y,pl,impuls = 0):
        self.x = x
        self.y = y
        self.imp = impuls
        self.skin = skins[pl]
        
        
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
                if type(a[i][j]) is Point:
                    print(a[i][j].skin,end=' ')
                else:
                    print(a[i][j],end=' ')
    def get(self,x,y):
        return self.b[x][y]


b = Board(20)
b.display()


##def turn(player,x,y):
##    Point.set(x,y)
##    check_lines()
##    print(pole)

def turn(n,x,y):
    if b.b[x][y] == '.':
        b.b[x][y] = Point(x,y,n)
        return True
    else:
        return False
    

def game():
    n = 0
    while True:
        print()
        k = input(f'Ход {n+1} игрока(enter чтобы закончить) ')
        if not k:
            #end() return res
            break
        if turn(n,int(alf.index(k[0])),int(alf.index(k[1]))):
            #chek
            if n == 1: n = 0
            else: n+=1
            b.display()
        else:
            print("Ошибка! Попробуйте снова")
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







        
