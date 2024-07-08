LIMITE_NUMERO_SAQUE = 3
LIMITE_VALOR_SAQUE = 500.00
contador_saque = 0
saldo_total = 0.00
relatorio_extrato = []


menu = f'''
================MENU================

        [1] - DEPOSITAR
        [2] - SACAR
        [3] - EXTRATO
        [0] - SAIR

====================================
'''

while True:
    print(menu)
    operacao = int(input('Digite a operação desejada: '))
    print()
    if operacao == 1:
        valor = float(input('Digite o valor que deseja depositar: '))
        print()
        while valor < 0:
            print('Ops! Não é possível depositar um valor negativo')
            valor = float(input('Digite o valor que deseja depositar: '))
        
        saldo_total += valor
        print(f'Depósito de R${valor:.2f} realizado com sucesso!')
        relatorio_extrato.append(f'Depósito: + R${valor:.2f}')
    
    elif operacao == 2:
        valor = float(input('Digite o valor que deseja sacar: '))  
        print()  
        if contador_saque < LIMITE_NUMERO_SAQUE:
            while valor > LIMITE_VALOR_SAQUE or valor < 0:
                print(f'Ops! Não é possível sacar um valor maior que R${LIMITE_VALOR_SAQUE:.2f} ou menor que R$ 0.00')
                valor = float(input('Digite o valor que deseja sacar: '))
            
            if saldo_total >= valor:
                contador_saque += 1
                saldo_total -= valor
                print(f'Saque de R${valor:.2f} realizado com sucesso!')
                relatorio_extrato.append(f'Saque: - R${valor:.2f}')
            else:
                print('Não foi possível realizar o saque por saldo insuficiente, tente novamente!')
        else:
            print('Você atingiu o limite de saque diário, mas ainda pode utilizar outros serviços:')
            print()
    
    elif operacao == 3:
        print('=========== EXTRATO ===========')
        print()
        if relatorio_extrato:
            for i in range(len(relatorio_extrato)):
                print(relatorio_extrato[i])
        else:
            print('Não houveram movimentações na conta!')
        print()
        print(f'Seu saldo total é de: {saldo_total:.2f}')
        print()
    
    elif operacao == 0:
        print(f'''
              Você finalizou a operação, iremos deslogar sua seção!
              
                        O banco DRAS agradece a confiança!
                                    _____  
                                   /     \ 
                                  |  ^ ^  |
                                  |  \_/  |
                                   \_____/
            ''')
        break
    else:
        print('Operação inválida, tente novamente!')