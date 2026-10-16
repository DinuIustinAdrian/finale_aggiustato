import os
import csv

# Funzione salva sala

def salva_sala(sala):
    '''Salva la sala in un file sala.csv per poterla caricare in un altra sessione del programma

    @sala: lista di liste contenente la sala da salvare
    '''
    with open("sala.csv", "w", newline="") as file:       
        writer = csv.writer(file)                           
        writer.writerows(sala)                            
    print("Stato della sala salvato in sala.csv")


# Funzione carica sala
 
def carica_sala(incasso):
    ''' Carica l'incasso di una precedente sessione

    @incasso: [int] variabile dove salvare l'incasso
    '''
    if os.path.exists("sala.csv") and os.path.exists("incasso_sala.txt"):

        with open("sala.csv", "r", newline="") as file:
            reader = csv.reader(file)
            sala = [row for row in reader]

        with open("incasso_sala.txt", "r") as file:
            incasso = int(file.read().strip())

        print("incasso caricato:", incasso)
        print("Stato della sala caricato.")

        return sala, incasso

    else:
        return None, None

    
 
def salva_incasso(incasso):
    ''' Carica l'incasso dell'attuale sessione su un
        file txt
    
        @incasso: [int] variabile da salvare
        '''
    with open("incasso_sala.txt", "w") as file:       
        file.write(str(incasso))                           
    print("Incasso in incasso_sala.txt")