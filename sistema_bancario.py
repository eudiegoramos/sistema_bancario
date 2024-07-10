LIMITE_NUMERO_SAQUE = 3
LIMITE_VALOR_SAQUE = 500.00
contador_saque = 0
contador_conta = 1
saldo_total = 0.00
relatorio_extrato = []
usuarios = {
    10101010101:{'nome':'Diego Ramos','data_nascimento':'07/07/2000','endereco':'Rua da Alegria - 220 - Vila Verde - Três Pombos/RJ'}
}

contas = {
    1:{'agencia':'0001','usuario':10101010101},1:{'agencia':'0001','usuario':10101010101}
}

menu = f'''
============= MENU =============

    [1] - DEPOSITAR
    [2] - SACAR
    [3] - EXTRATO
    [4] - CADASTRAR USUÁRIO
    [5] - CADASTRAR CONTA
    [6] - RELATÓRIO USUÁRIOS
    [7] - RELATÓRIO CONTAS
    [0] - SAIR

================================
'''


def depositar(valor,saldo,/):
    while valor < 0:
        print('Ops! Não é possível depositar um valor negativo')
        valor = float(input('Digite o valor que deseja depositar: '))
    
    saldo += valor
    print(f'Depósito de R${valor:.2f} realizado com sucesso!')
    relatorio_extrato.append(f'Depósito: + R${valor:.2f}')
    return saldo


def sacar(*,valor,saldo,limite_saques,limite_valor):
    global contador_saque
    if contador_saque < limite_saques:
        while valor > limite_valor or valor < 0:
            print(f'Ops! Não é possível sacar um valor maior que R${limite_valor:.2f} ou menor que R$ 0.00')
            valor = float(input('Digite o valor que deseja sacar: '))
        
        if saldo >= valor:
            contador_saque += 1
            saldo -= valor
            print(f'Saque de R${valor:.2f} realizado com sucesso!')
            relatorio_extrato.append(f'Saque: - R${valor:.2f}')
            return saldo
        else:
            print('Não foi possível realizar o saque por saldo insuficiente, tente novamente!')
    else:
        print('Você atingiu o limite de saque diário, mas ainda pode utilizar outros serviços:')
        print()


def imprimir_extrato(saldo,/,*,relatorio):
    print('=========== EXTRATO ============')
    print()
    if relatorio:
        for i in range(len(relatorio)):
            print(relatorio[i])
    else:
        print('Não houveram movimentações na conta!')
    print()
    print(f'Seu saldo total é de: {saldo:.2f}')
    print()


def cadastrar_usuario(*,nome,data_nascimento,cpf,logradouro,numero,bairro,cidade,estado):
    if cpf in usuarios:
        print('Usuario já cadastrado, tente novamente!')
    else:
        endereco = f'{logradouro} - {numero} - {bairro} - {cidade}/{estado}'
        usuario = {'nome':nome,'data_nascimento':data_nascimento,'endereco':endereco}
        usuarios[cpf] = usuario
        print()
        print('Usuário cadastrado com sucesso!')



def cadastrar_conta(*,usuario):
    global contador_conta
    contador_conta += 1
    if contador_conta in contas:
        print('Conta já cadastrada, tente novamente!')
    else:
        conta = {'agencia':'0001','usuario':usuario}
        contas[contador_conta] = conta
        print('Conta cadastrada com sucesso!')


def listar_usuarios():
    print('======= RELATÓRIO USUÁRIOS =======')
    print()
    for chave,valor in usuarios.items():
        print(f'Usuário {chave}, associado às informações: ', 'Nome:', valor['nome'],' - ', 'Data de nascimento:', valor['data_nascimento'])


def listar_contas():
    print('======= RELATÓRIO CONTAS =======')
    print()
    for chave,valor in contas.items():
        print(f'Conta n° {chave}, associada ao usuário: ', valor['usuario'])


while True:
    print(menu)
    operacao = int(input('Digite a operação desejada: '))
    print()
    
    if operacao == 1:
        valor = float(input('Digite o valor que deseja depositar: '))
        print()
        saldo_total = depositar(valor,saldo_total)
    
    elif operacao == 2:
        valor = float(input('Digite o valor que deseja sacar: '))  
        print()  
        saldo_total = sacar(valor=valor, saldo=saldo_total, limite_saques=LIMITE_NUMERO_SAQUE, limite_valor=LIMITE_VALOR_SAQUE)
    
    elif operacao == 3:
        imprimir_extrato(saldo_total,relatorio=relatorio_extrato)

    elif operacao == 4:
        print('====== PREENCHA ABAIXO =======')
        nome = input('Digite seu nome: ')
        data_nascimento = input('Digite sua data de nascimento (dd/mm/aaaa): ')
        cpf = int(input('Digite seu CPF (apenas números): '))
        print()
        print('===== DADOS RESIDENCIAIS =====')
        logradouro = input('Digite seu logradouro: ')
        numero = input('Digite seu numero: ')
        bairro = input('Digite seu bairro: ')
        cidade = input('Digite sua cidade: ')
        estado = input('Digite seu estado (UF): ')
        cadastrar_usuario(nome=nome,data_nascimento=data_nascimento,cpf=cpf,logradouro=logradouro,numero=numero,bairro=bairro,cidade=cidade,estado=estado)

    elif operacao == 5:
        print('====== PREENCHA ABAIXO =======')
        cpf = int(input('Digite seu usuário(CPF) para cadastrar uma conta: '))
        print()
        cadastrar_conta(usuario=cpf)

    elif operacao == 6:
        listar_usuarios()

    elif operacao == 7:
        listar_contas()

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