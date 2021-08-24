def equivalente(horas, minutos, segundos):
    minutossegundos=minutos*60
    horas=horas*60*60

    segundost=segundos+minutossegundos+horas
    return segundost

def main():
    #escribe tu código abajo de esta línea
    pass

    print('Proceso 1')
    horas=(int(input('Dame las horas del P1: ')))
    minutos=int(input('Dame los minutos del P1: '))
    segundos=int(input('Dame los segundos del P1: '))

    print('Total de segundos del P1 son '+str(equivalente(horas, minutos, segundos)))

print(equivalente(2,20,8))

if __name__=='__main__':
    main()
