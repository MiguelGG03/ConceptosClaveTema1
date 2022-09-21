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

    def __str__(self):
        return print('{},{}'.format(self.x,self.y))

    def añadir_a_la_lista(self):
        palalista=(self.x,self.y)
        for i in self.p_existentes:
            if self.x==i[0]:
                if self.y==i[0]:
                    print('No se puedde añadir el punto X:{} Y:{} ,porque ya existe.'.format(self.x,self.y))
                else:
                    self.p_existentes.append(palalista)
            else:
                self.p_existentes.append(palalista)

    def chequear_p_existentes(self):
        return self.p_existentes


    def cuadrante_checker(self):
        if(self.x==0 and self.y==0):
            print('El punto esta en el origen')
        elif(self.x>0 and self.y==0):
            print('El punto esta entre los cuadrantes 1 y 4')
        elif(self.x<0 and self.y==0):
            print('El punto esta entre los cuadrantes 2 y 3')
        elif(self.x==0 and self.y>0):
            print('El punto esta entre los cuadrantes 1 y 2')
        elif(self.x==0 and self.y<0):
            print('El punto esta entre los cuadrantes 3 y 4')
        elif(self.x>0 and self.y>0):
            print('El punto esta en le cuadrante 1')
        elif(self.x<0 and self.y>0):
            print('El punto esta en le cuadrante 2')
        elif(self.x<0 and self.y<0):
            print('El punto esta en le cuadrante 3')
        elif(self.x>0 and self.y<0):
            print('El punto esta en le cuadrante 4')

