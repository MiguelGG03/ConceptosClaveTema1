from clases.puntos import Punto as p

def main():
    a=input('Coordenadas X:')
    b=input('Coordenadas Y:')
    point = p(a,b)
    point.setIDx()
    point.setIDy()
    point.__str__()


if __name__=='__main__':
    main()