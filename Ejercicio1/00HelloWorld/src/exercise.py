def equivalente(horas, minutos, segundos):
    minutossegundos=minutos*60
    horas=horas*60*60

    segundost=segundos+minutossegundos+horas
    return segundost

def main():
    #escribe tu código abajo de esta línea
    pass

print(equivalente(2,20,8))

if __name__=='__main__':
    main()
