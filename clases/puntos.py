import math

class Punto:

    def __init__(self,x,y):
        self.p_existentes=[]
        self.x=x
        self.y=y

    def setIDx(self):
        if(self.x==''):
            self.x=0
        else:
            self.x=int(self.x)

    def setIDy(self):
        if(self.y==''):
            self.y=0
        else:
            self.y=int(self.y)

    def getIDx(self):
        return print('Coordenada en el eje X: {}'.format(str(self.x)))

    def getIDy(self):
        return print('Coordenada en el eje Y: {}'.format(str(self.y)))

    def string(self):
        return print('({},{})'.format(self.x,self.y))

    def cuadrante(self):
        if(self.x==0 and self.y==0):
            print('El punto esta en el origen')
        elif(self.x!=0 and self.y==0):
            print('El punto esta en el eje de abscisas')
        elif(self.x==0 and self.y!=0):
            print('El punto esta en el eje de ordenadas')
        elif(self.x>0 and self.y>0):
            print('El punto esta en le cuadrante 1')
        elif(self.x<0 and self.y>0):
            print('El punto esta en le cuadrante 2')
        elif(self.x<0 and self.y<0):
            print('El punto esta en le cuadrante 3')
        elif(self.x>0 and self.y<0):
            print('El punto esta en le cuadrante 4')

    def vector(self,vx,vy):
        self.vx=vx
        self.vy=vy

    def setIDvx(self):
        if(self.vx==''):
            self.vx=0
        else:
            self.vx=int(self.vx)
    
    def setIDvy(self):
        if(self.vy==''):
            self.vy=0
        else:
            self.vy=int(self.vy)