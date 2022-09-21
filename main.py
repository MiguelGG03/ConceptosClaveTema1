import clases.puntos as p

def main():
    a=float(input('Coordenadas X:'))
    b=float(input('Coordenadas Y:'))
    point=p(a,b)
    point.__str__()


if __name__=='__main__':
    main()