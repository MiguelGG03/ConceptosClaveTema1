from clases.puntos import Punto as p

def main():
    seguir=True
    while(seguir==True):
        a=input('Coordenadas X:')
        b=input('Coordenadas Y:')
        point = p(a,b)
        point.setIDx()
        point.setIDy()
        point.añadir_a_la_lista()
        preg=input('Desea seguir poniendo puntos? 0=NO 1=SI :')
        if(preg==0):
            seguir=False
        elif(preg==1):
            seguir=True
        else:
            print('Eso no es un 1 o un 2, asimilamos un 1 como respuesta')    
    
    
    p.chequear_p_existentes()
    point.__str__()


if __name__=='__main__':
    main()