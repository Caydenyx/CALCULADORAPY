# CALCULADORA EM PYTHON USANDO WHILE!!!
while True:
    numero1 = input ('DIGITE O PRIMEIRO NÚMERO:  ')
    operador = input ('DIGITE O OPERADOR [+,-,/,*]: ')
    numero2 = input ('DIGITE O SEGUNDO NÚMERO: ')

    try:
        numero1 = float(numero1)
        numero2 = float(numero2)

        if numero1 == '' or numero2 == '' or operador == '':
            print ('NÃO DEIXE CAMPOS VAZIOS')
            continue
        
        if operador == '+':
            print (numero1 + numero2)
        elif operador == '-':
            print (numero1 - numero2)
        elif operador == '*':
            print (numero1 * numero2)
        elif operador == '/':
            print (numero1 / numero2)
        else:
            print ('DIGITE SOMENTE COISAS VÁLIDAS')
            continue
  
        sair = input ('VOCÊ DESEJA [S]AIR?: ').lower().endswith('s')
        if sair is True:
            print ('VOCÊ SAIU!!')
            break
    
    except:
        print ('VOCÊ NÃO DIGITOU NÚMEROS OU DEIXOU ESPAÇOES EM BRANCO')
        


