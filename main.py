from clases.puntos import Punto as p

def main():
    seguir=True
    while(seguir==True):
        a=input('Coordenadas p1 X:')
        b=input('Coordenadas p1 Y:')
        c=input('Coordenadas p2 Y:')
        d=input('Coordenadas p2 Y:')
        point = p(a,b)
        vector=point.vector(c,d)
        point.setIDvx()
        point.setIDvy()
        vector
        point.setIDx()
        point.setIDy()
        print('------------CARACTERISTICAS DEL PUNTO------')
        point.string()
        print('------------CARACTERISTICAS DEL VECTOR------')
        point.distancia()
        print('------------CUADRANTE DEL PUNTO------------')
        point.cuadrante()
        preg=input('Desea seguir poniendo puntos? 0=NO 1=SI :')
        if(preg=='0'):
            seguir=False
        elif(preg=='1'):
            seguir=True
        else:
            print('Eso no es un 1 o un 2, asimilamos un 1 como respuesta')    


if __name__=='__main__':
    main()