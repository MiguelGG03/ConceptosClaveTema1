class Punto:

    p_existentes=[]

    def __init__(self,x,y):
        self.x=xself.y=y

    def __del__ (self):
        i= Punto.p_existentes.index(self.x)
        del (Punto.p_existentes[i])

    def setIDx(self,x):
         self.x = int(input("Introduce la comp X"))

    def setIDy(self,y):
        self.y =  int(input("Introduce la comp Y "))

    def __str__(self):
        return ( str(self.x)   + str(self.y) )