class Punto:

    p_existentes=[]

    def __init__(self,x,y):
        self.x=x
        self.y=y

    def __del__ (self):
        i= Punto.p_existentes.index(self.x)
        del (Punto.p_existentes[i])

    def setIDx(self):
        if(self.x==None):
            self.x=0
        else:
            self.x=self.x

    def setIDy(self):
        if(self.y==None):
            self.y=0
        else:
            self.y=self.y

    def getIDx(self):
        return print('Coordenada en el eje X: {}'.format(str(self.x)))

    def getIDy(self):
        return print('Coordenada en el eje Y: {}'.format(str(self.y)))

    def __str__(self):
        return ( str(self.x)+ str(self.y) )