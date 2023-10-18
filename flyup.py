paris = []
novayork = []
londres = []
passageiros = {}
passageirosp = {}
passageirosl = {}
passageirosny = {}
pagamentos_abertos = {}
pagamentos_efetuados = {}
pacotes_paris_restantes = (10 - sum(paris))
pacotes_londres_restantes = (10 - sum(londres))
pacotes_novayork_restantes = (10 - sum(novayork))
paris_disponivel = sum(paris) < 10
londres_disponivel = sum(londres) < 10
novayork_disponivel = sum(novayork) < 10
contador = 0

print("\n"
      "------------------------------------------------------\n"
      "Bem vindo(a) ao FlyUP Pacotes De Viagens! (BETA 3.O)\n"
      "------------------------------------------------------\n\n"
      "Alunos:\n"
      "Henrique Padilha Duda\n"
      "Luciano Kubiak Dal Pai\n"
      "Jhonnatan M. Cora Da Luz\n")

def menu():
    while True:
        print(  '----------------------------\n'
                'MENU PRINCIPAL:\n'
                '----------------------------\n'
                '1- Comprar passagem\n'
                '2- Ver destinos disponíveis\n'
                '3- Consultar valores\n'
                '4- Menu do administrador\n'
                '0- Sair\n'
                '----------------------------')

        continuar = int(input())
        if continuar == 1:
            comprar()
        elif continuar == 2:
            mostrar()
        elif continuar == 3:
            valores()
        elif continuar == 4:
            admin()
        elif continuar == 0:
            break
        else:
            return menu()

def compra_paris(paris, item):
    paris.append(item)

def passagem_paris():
    print('VOCÊ ESCOLHEU PARIS')
    if sum(paris) < 10:
        pacotesparis = int(input('Digite o número de pacotes: '))
        if pacotesparis <= (10 - sum(paris)):
            compra_paris(paris, pacotesparis)
            for a in range(0, pacotesparis):
                nome_passageiro_paris()
        else:
            novo_paris()
    elif sum(paris) == 10:
        print('Todos os pacotes para essa viagem já foram vendidos!!')
        comprar()

def nome_passageiro_paris():
    nomepassageiro = input(("Digite seu nome completo: "))
    nome = nomepassageiro.upper()
    passageiros.setdefault(nome, "PARIS")
    pagamentos_abertos.setdefault(nome, "Pagamento em aberto")

def novo_paris():
    print('Número de pacotes inválido')
    print("Ainda restam", (10 - sum(paris)), "pacote(s) restante(s)")
    num = int(input('Digite:\n'
                    '1- Novo número de pacotes\n'
                    '2- Menu\n'))
    if num == 1:
        return passagem_paris()
    if num == 2:
        return menu()
    else:
        return novo_paris()

def novo_londres():
    print('Número de pacotes inválido')
    print("Ainda restam", (10-sum(londres)), "pacote(s) restante(s)")
    num1 = int(input('Digite:\n'
                    '1- Novo número de pacotes\n'
                    '2- Menu\n'))
    if num1 == 1:
        return passagem_londres()
    if num1 == 2:
        return menu()
    else:
        return novo_londres()

def compra_londres(londres, item):
    londres.append(item)

def passagem_londres():
    print('VOCÊ ESCOLHEU LONDRES')
    if sum(londres) < 10:
        pacoteslondres = int(input('Digite o número de pacotes: '))
        if pacoteslondres <= 10-sum(londres):
            compra_londres(londres, pacoteslondres)
            for a in range(0, pacoteslondres):
                nome_passageiro_londres()
        else:
            novo_londres()
    elif sum(londres) == 10:
        print('Todos os pacotes para essa viagem já foram vendidos!!')
        menu ()

def nome_passageiro_londres():
    nomepassageiro = input(("Digite seu nome completo: "))
    nome = nomepassageiro.upper()
    passageiros.setdefault(nome, "LONDRES")
    pagamentos_abertos.setdefault(nome, "Pagamento em aberto")

def novo_novayork():
    print('Número de pacotes inválido')
    print("Ainda restam", (10-sum(novayork)), "pacote(s) restante(s)")
    num2 = int(input('Digite:\n'
                    '1- Novo número de pacotes\n'
                    '2- Menu\n'))
    if num2 == 1:
        return passagem_novayork()
    if num2 == 2:
        return menu()
    else:
        return novo_novayork()

def compra_novayork(novayork, item):
    novayork.append(item)

def passagem_novayork():
    print('VOCÊ ESCOLHEU NOVA YORK')
    if sum(novayork) < 10:
        pacotesnovayork = int(input('Digite o número de pacotes: '))
        if pacotesnovayork <= 10-(sum(novayork)):
            compra_novayork(novayork, pacotesnovayork)
            for a in range(0, pacotesnovayork):
                nome_passageiro_novayork()
            print("Parabéns, você já reservou sua viagem!!")
        else:
            novo_novayork()
    elif sum(novayork) == 10:
        print('Todos os pacotes para essa viagem já foram vendidos!!')
        menu()

def nome_passageiro_novayork():
    nomepassageiro = input(("Digite seu nome completo: "))
    nome = nomepassageiro.upper()
    passageiros.setdefault(nome, "NOVA YORK")
    pagamentos_abertos.setdefault(nome, "Pagamento em aberto")

def admin():
    print("-----------------------------\n"
          "MENU DO ADMINISTRADOR: \n"
          "-----------------------------")
    senha = 2022
    senha2 = int(input("Digite a senha: "))
    if senha == senha2:
        pagamentos()
    else:
        return admin()

def comprar():
    dest = int(input( "-----------------------------------\n"
                      "Selecione o seu destino dos sonhos!!\n"
                      "São os destinos disponíveis:\n"
                      '1- PARIS\n'
                      '2- LONDRES\n'
                      '3- NOVA YORQUE\n'
                      '-----------------------------------\n' ))

    if dest == 1:
        passagem_paris()
    if dest == 2:
        passagem_londres()
    if dest == 3:
        passagem_novayork()

def mostrar():
    print('-----------------------------------------------------')
    print('Paris ainda tem', (10 - sum(paris)),'lugares disponíveis')
    print('Londres ainda tem', (10 - sum(londres)), 'lugares disponíveis')
    print('Nova Yorque ainda tem', (10 - sum(novayork)), 'lugares disponíveis')
    print('------------------------------------------------------------------')

def valores():
    print('Pacote para Paris = R$ 3.499,90')
    print('Pacote para Londres = R$ 3.699,90')
    print('Pacote para Nova Iork = R$ 3.299,90')

def lista_passageiros():
    busca = int(input(  'Digite:\n'
                        '1- Exibir lista de passageiros\n'
                        '2- Buscar passageiro\n'
                        '3- Pagamentos\n'
                        '4- menu\n'))
    if busca == 1:
        if len(passageiros) != 0:
            for a in passageiros:
                print('Nome: ', a, ",destino: ", passageiros[a])
            return pagamentos()
        else:
            print("Ainda não há nenhum passageiro")
            return pagamentos()

    elif busca == 2:
        busca_passageiro = input("Digite o nome do passageiro: ")
        nome = busca_passageiro.upper()
        if passageiros.get(nome):
            print("Nome: ",nome,",Destino: ",passageiros[nome])
            return pagamentos()
        else:
            print("Passageiro não encontrado")
            return pagamentos()
    elif busca == 3:
        return pagamentos()
    elif busca == 4:
        menu()
    else:
        print("Digito inválido")
        return lista_passageiros()

def pagamentos():
    pag = int(input('1- Ver pagamentos em aberto \n'
                    '2- Consultar lista de passageiros\n'
                    '3- Consultar valores totais\n'
                    '4- Retornar ao menu\n'
                    '----------------------------\n'))
    if pag == 1:
        if len(pagamentos_abertos) == 0:
            print("Não há pagamentos em aberto!!")
            return pagamentos()

        else:
            for a in pagamentos_abertos:
                print('Nome:', a, '=', pagamentos_abertos[a])
            confirmar_pagamento()
    elif pag == 2:
        lista_passageiros()
    elif pag == 3:
        valorestotais()
    elif pag == 4:
        return menu()
    else:
        print("Dígito inválido!!")
        return pagamentos()

def confirmar_pagamento():
    baixa = input("Digite o nome do passageiro à confirmar o pagamento: ")
    nome = baixa.upper()
    if pagamentos_abertos.get(nome):
        del pagamentos_abertos[nome]
        pagamentos_efetuados.setdefault(nome, "Pagamento efetuado")
        print("O pagamento de", nome, 'foi confirmado!')
        for i in pagamentos_efetuados:
            print(i, '=', pagamentos_efetuados[i])
            return pagamentos()
    else:
        print("Passageiro não encontrado")
        a = int(input("1- Pesquisar novamente\n"
                        "2- Ver pacotes em aberto\n"
                        "3- Admin\n"
                        "4- Menu\n"))
        if a == 1:
            confirmar_pagamento()
        elif a == 2:
            pagamentos()
        elif a == 3:
            admin()
        elif a == 4:
            menu()
        else:
            print("Digito inválido!!")
            return confirmar_pagamento()

def valorestotais():
    valort = int(input('1- Valores totais de Paris\n'
                       '2- Valores totais de Londres\n'
                       '3- Valores totais de Nova York\n'
                       '4- Pagamentos\n'))
    if valort == 1:
        print(sum(paris), "passagens para Paris vendidas")
        x = int(input("Digite a quantidade de pacotes vendidos: "))
        if sum(paris) == x:
            somaparis(x)
            print(somaparis(x), "R$")
        else:
            print("Números divergem")
            return somaparis()
    elif valort == 2:
        print(sum(londres), "passagens para Londres vendidas")
        x = int(input("Digite a quantidade de pacotes vendidos: "))
        if sum(londres) == x:
            somalondres(x)
            print(somalondres(x), "R$")
        else:
            print("Números divergem")
            return somalondres()
    elif valort == 3:
        print(sum(novayork), "passagens para Nova York vendidas")
        x = int(input("Digite a quantidade de pacotes vendidos: "))
        if sum(novayork) == x:
            somany(x)
            print(somany(x), "R$")
        else:
            print("Números divergem")
            return somany()
    elif valort == 4:
        pagamentos()
    else:
        print("Digito inválido!!")
        return valorestotais()

def somalondres(n):
    if n == 0:
        return 0
    elif n == 1:
        return 3.699,90
    return n*3.699,90 + somalondres(n-1) - 3.699,90*(n-1)

def somany(n):
    if n == 0:
        return 0
    elif n == 1:
        return 3.299,90
    return n*3.299,90 + somany(n-1) - 3.299,90*(n-1)

def somaparis(n):
    if n == 0:
        return 0
    elif n == 1:
        return 3.499,90
    return n*3.499,90 + somaparis(n-1) - 3.499,90*(n-1)

menu()