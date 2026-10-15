odonto= []
paciente= []
usuario_odonto= []
usuario_paciente= []

while True:
    print('\n----MENU---- \n 1- CADASTRAR \n 2- FAZER O LOGIN \n 3- VOLTAR AO MENU PRNCIPAL ')
    cad=int(input('\n Digite sua opçao: '))

    if cad==1:
        print('\n PRIMEIRA INFORMAÇAO PARA O SEU CADASTRO \n 1- ADMINISTRADOR \n 2- PACIENTE')
        adm_paci=int(input('\nDigite a sua opçao: '))
        if adm_paci==1:
            nome=input('\nDigite seu nomeeeeee: \n').lower
            cpf=input('Digite seu CPF: \n')
            if len(cpf)==11:
                print('CPF cadastrado com sucesso')
            else:
                print('o CPF inserido e invalido')
            senha=input('Digite sua senha: \n')
            if len(senha)==6:
                print('senha cadastrado com sucesso')
            else:
                print('senha inserido e invalido')
            numero=input('Digite seu numero de telefone: \n')
            if len(numero)==11:
                print('telefone cadastrado com sucesso')
            else:
                print('telefone inserido e invalido')


