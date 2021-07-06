import sys

n = int(sys.argv[1])
soma = 0
maximo = 0
crescente = False
if n>=2:  
    for i in range(0, n):
        sequencia = int(sys.argv[i+2])
        
        if i == 0:
            num_anterior = sequencia
            num_atual = sequencia
            maior = menor = sequencia
        
        if sequencia > num_anterior:
            soma = num_anterior + sequencia 

            if soma > maximo:
                maximo = soma
                        
        if (i == n-1):
            if (crescente == True):
                print('max', maximo, 'seq.', str(menor), ',', str(maior))
            else:
                print('sem sequencia crescente')
                
        num_anterior = sequencia
else:
    print('entrada invalida')
