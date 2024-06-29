import os

restaurantes = [{'nome': 'Praça', 'categoria': 'Japonesa', 'ativo': False}, 
                {'nome': 'Pizzaria Duarte', 'categoria': 'Italiano', 'ativo': True},
                {'nome': 'Nagano', 'categoria': 'Japones', 'ativo': False} ]

def exibir_nome_do_programa():
    print('''
        ░██████╗░█████╗░██████╗░░█████╗░██████╗░  ███████╗██╗░░██╗██████╗░██████╗░███████╗░██████╗░██████╗
        ██╔════╝██╔══██╗██╔══██╗██╔══██╗██╔══██╗  ██╔════╝╚██╗██╔╝██╔══██╗██╔══██╗██╔════╝██╔════╝██╔════╝
        ╚█████╗░███████║██████╦╝██║░░██║██████╔╝  █████╗░░░╚███╔╝░██████╔╝██████╔╝█████╗░░╚█████╗░╚█████╗░
        ░╚═══██╗██╔══██║██╔══██╗██║░░██║██╔══██╗  ██╔══╝░░░██╔██╗░██╔═══╝░██╔══██╗██╔══╝░░░╚═══██╗░╚═══██╗
        ██████╔╝██║░░██║██████╦╝╚█████╔╝██║░░██║  ███████╗██╔╝╚██╗██║░░░░░██║░░██║███████╗██████╔╝██████╔╝
        ╚═════╝░╚═╝░░╚═╝╚═════╝░░╚════╝░╚═╝░░╚═╝  ╚══════╝╚═╝░░╚═╝╚═╝░░░░░╚═╝░░╚═╝╚══════╝╚═════╝░╚═════╝░
            
        ''')


def exibir_subtitulo(texto):
    os.system('cls')
    linha = '*' *  (len(texto)) 
    print(linha)
    print(texto)
    print(linha)
    print()

def voltar_ao_menu_principal():
    input('\nDigite uma tecla para voltar ao menu principal: ')
    main()

def exibir_opcoes():
    print('1. Casdastrar restaurante')
    print('2. Listar restaurante')
    print('3. Alternar estado do restaurante')
    print('4. Sair\n ')


def finalizar_app():
    exibir_subtitulo('finalizando app')
    

def opcao_invalida():
    print('Opção inválida!')
    voltar_ao_menu_principal()


def cadastrar_novo_restaurante():
    '''Essa função serve para cadastrar novos restaurantes
     
      Inputs:
      - Nome do restaurante
      - Categoria do restaurante

      Outputs:
      - Adiciona um novo restaurante a lista de restaurantes
       
         '''
    
    exibir_subtitulo('cadastrar novo restaurante')
    nome_do_restaurante = input('Digite o nome do restaurante que deseja cadastrar: ')
    categoria = input(f'Digite o nome da categoria do restaurante {nome_do_restaurante} ')
    dados_do_restaurante = {'nome': nome_do_restaurante, 'categoria':categoria, 'ativo': False}
    restaurantes.append(dados_do_restaurante)
    print(f'O restaurante {nome_do_restaurante} foi cadastrado com sucesso!!')
    voltar_ao_menu_principal()


def listar_restaurantes():

     ''' Essa função serve para listar os nomes, categorias e os status dos restaurantes

     '''

     exibir_subtitulo('listanto os restaurantes') 
     print(f'{'Nome do restaurante'.ljust(22)} | {'Categoria'.ljust(20)} | Status')
     for restaurante in restaurantes:
        nome_restaurante = restaurante['nome']
        categoria = restaurante['categoria']
        ativo = 'ativado' if restaurante['ativo'] else 'desativado'
        print(f'- {nome_restaurante.ljust(20)} | {categoria.ljust(20)} | {ativo}')

     voltar_ao_menu_principal()


def alternar_estado_restaurante():

    ''' Essa função serve para alterar o status de um restaurante (todo restaurante recém cadastrado está desativado por norma de contrato)'''

    exibir_subtitulo('Alterando estado do restaurante')
    nome_restaurante = input('Digite o nome do restaurante que deseja alterar o estado: ')
    restaurante_encontrado = False

    for restaurante in restaurantes:
        if nome_restaurante == restaurante['nome']:
            restaurante_encontrado = True
            restaurante['ativo'] = not restaurante['ativo']
            mensagem = f'O restaurante {nome_restaurante} foi ativado com sucesso' if restaurante['ativo'] else f'O restaurante foi desativado com sucesso'
            print(mensagem)
    if not restaurante_encontrado:
        print('O restaurante não foi encontrado')
    voltar_ao_menu_principal()

               



def escolher_opcao():
    try:
        opcao_escolhida = int(input('Escolha uma opção '))
        print('Você escolheu a opção ', opcao_escolhida)

        if opcao_escolhida == 1:
            cadastrar_novo_restaurante()
        elif opcao_escolhida == 2:
            listar_restaurantes()
        elif opcao_escolhida == 3:
            alternar_estado_restaurante()
        elif opcao_escolhida == 4:
            finalizar_app()
        else:
            opcao_invalida() 
    except:
        opcao_invalida()  




def main():
    os.system('cls')
    exibir_nome_do_programa()
    exibir_opcoes()
    escolher_opcao()
    



if __name__ == '__main__':
    main()

