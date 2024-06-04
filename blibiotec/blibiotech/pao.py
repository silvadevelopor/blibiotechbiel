
# Inicializar registros de usuários e livros
registro = {}
livros_reservados = []
livros_cadastrados = []

# Função para carregar dados de arquivos
def carregar_dados():
    global registro, livros_cadastrados, livros_reservados
    try:
        with open("usuarios.txt", "r") as file:
            for line in file:
                login, senha = line.strip().split(",")
                registro[login] = senha
    except FileNotFoundError:
        print("Arquivo de usuários não encontrado. Criando novo arquivo...")
        open("usuarios.txt", "w").close()

    try:
        with open("livros.txt", "r") as file:
            for line in file:
                livros_cadastrados.append(line.strip())
    except FileNotFoundError:
        print("Arquivo de livros não encontrado. Criando novo arquivo...")
        open("livros.txt", "w").close()

    try:
        with open("reservas.txt", "r") as file:
            for line in file:
                livros_reservados.append(line.strip())
    except FileNotFoundError:
        print("Arquivo de reservas não encontrado. Criando novo arquivo...")
        open("reservas.txt", "w").close()

# Função para salvar dados em arquivos
def salvar_dados():
    with open("usuarios.txt", "w") as file:
        for login, senha in registro.items():
            file.write(f"{login},{senha}\n")

    with open("livros.txt", "w") as file:
        for livro in livros_cadastrados:
            file.write(f"{livro}\n")

    with open("reservas.txt", "w") as file:
        for livro in livros_reservados:
            file.write(f"{livro}\n")

# Algoritmo de ordenação por inserção
def insertion_sort(arr):
    for i in range(1, len(arr)):
        key = arr[i]
        j = i - 1
        while j >= 0 and key < arr[j]:
            arr[j + 1] = arr[j]
            j -= 1
        arr[j + 1] = key

def login(registro):
    print("_" * 28)
    print(f'{"Biblioteca Institucional":^28}')
    print("_" * 28)
    while True:
        login = input("Login: ")
        senha = input("Senha: ")

        if login in registro:
            if registro[login] == senha:
                return login
            else:
                print("Senha Errada")
        else:
            print("Login ou senha incorretos")
            continue

def criacao():
    while True:
        print("1 - Cadastrar Usuário")
        print("2 - Excluir Usuário")
        print("3 - Listar Usuários")
        print("4 - Voltar")

        selecao = input("Escolha uma das opções: ")

        if selecao == "1":
            cadastrar_user()
        elif selecao == "2":
            deletar_user = input("Escolha o usuario que queira deletar: ")
            if deletar_user in registro:
                del registro[deletar_user]
                print("Usuario deletado")
            else:
                print("Usuário não encontrado")
        elif selecao == "3":
            print("Lista de Usuários:")
            for usuario, senha in registro.items():
                print(f"Login: {usuario}, Senha: {senha}")
        elif selecao == "4":
            break

def cadastrar_user():
    print("_" * 25)
    print(f'{"Cadastro de usuário": ^25}')
    print("_" * 25)
    login = input("login: ")
    senha = input("senha: ")
    if login not in registro:
        registro[login] = senha
        print("Usuário cadastrado com sucesso")
    else:
        print("Usuário já cadastrado")

def gerenciar_livros():
    while True:
        print("_" * 27)
        print(f'{"Gerenciamento de livro": ^27}')
        print("_" * 27)
        print("1 - Adicionar Livro")
        print("2 - Remover Livro")
        print("3 - Listar Livro")
        print("4 - Voltar")
        escolha = input("Escolha uma das alternativas: ")

        if escolha == "1":
            print("_" * 25)
            print("Tela de Adicionar Livro")
            print("_" * 25)
            titulo = input("Digite o Título: ")
            print("_" * 25)
            autor = input("Digite o Nome do Autor: ")
            print("_" * 25)
            data = input("Data de Lançamento: ")
            print("_" * 25)
            print("Livro cadastrado")
            print("_" * 25)
            livros_cadastrados.append(titulo)
            insertion_sort(livros_cadastrados)
        elif escolha == "2":
            Nome_do_livro_remover = input("Digite o nome do Livro que você quer Remover: ")
            if Nome_do_livro_remover in livros_cadastrados:
                livros_cadastrados.remove(Nome_do_livro_remover)
        elif escolha == "3":
            print("-" * 25)
            print(f'{"Lista de livros:":^25}')
            print("-" * 25)
            for livro in livros_cadastrados:
                print('-', livro)
        elif escolha == "4":
            break
        else:
            print("Escolha uma opção válida")

def verificar_disponibilidade(pesquisa, livros_cadastrados):
    inicio, fim = 0, len(livros_cadastrados) - 1

    while inicio <= fim:
        meio = (inicio + fim) // 2

        if livros_cadastrados[meio] == pesquisa:
            return meio
        elif livros_cadastrados[meio] < pesquisa:
            inicio = meio + 1
        else:
            fim = meio - 1

    return -1

def main():
    carregar_dados()
    verificar = login(registro)
    if verificar == 'admin':
        while True:
            print("-" * 25)
            print(f'{"Biblioteca Virtual:":^25} ')
            print("-" * 25)
            print("1 - Pesquisar Livros")
            print("2 - Livros Reservados")
            print("3 - Cancelar Reserva")
            print("4 - Gerenciar Usuários")
            print("5 - Gerenciar Livros")
            print("6 - Sair\n")

            selecao = input("Selecione uma das opções acima: ")

            if selecao == "1":
                print("-" * 25)
                print(f'{"Pesquisar Livros":^25}')
                print("-" * 25)

                pesquisa = input("Digite o nome do Livro: ")

                verificar = verificar_disponibilidade(pesquisa, livros_cadastrados)

                if verificar == -1:
                    print('Livro não encontrado.')
                else:
                    reservar = input("O livro foi encontrado. Deseja reservar o livro? [S/N] ").lower()
                    if reservar == "s":
                        livros_reservados.append(pesquisa)
                        print("Livro reservado!")

            elif selecao == "2":
                print("-" * 25)
                print(f'{"Livros Reservados:":^25}')
                print("-" * 25)
                for livro in livros_reservados:
                    print('-', livro)
                print('''
''')
            elif selecao == "3":
                cancelar_reserva = input("Digite o nome do livro que deseja cancelar a reserva: ")
                if cancelar_reserva in livros_reservados:
                    livros_reservados.remove(cancelar_reserva)

            elif selecao == "4":
                criacao()

            elif selecao == "5":
                gerenciar_livros()

            elif selecao == "6":
                print("Obrigado por usar a nossa biblioteca!")
                salvar_dados()
                break
    elif verificar == 'professor':
        while True:
            print("-" * 25)
            print(f'{"Biblioteca Virtual:":^25} ')
            print("-" * 25)
            print("1 - Pesquisar Livros")
            print("2 - Livros Reservados")
            print("3 - Cancelar Reserva")
            print("4 - Sair\n")

            selecao = input("Selecione uma das opções acima: ")

            if selecao == "1":
                print("-" * 25)
                print(f'{"Pesquisar Livros":^25}')
                print("-" * 25)

                pesquisa = input("Digite o nome do Livro: ")

                verificar = verificar_disponibilidade(pesquisa, livros_cadastrados)

                if verificar == -1:
                    print('Livro não encontrado.')
                else:
                    reservar = input("O livro foi encontrado. Deseja reservar o livro? [S/N] ").lower()
                    if reservar == "s":
                        livros_reservados.append(pesquisa)
                        print("Livro reservado!")

            elif selecao == "2":
                print("-" * 25)
                print(f'{"Livros Reservados:":^25}')
                print("-" * 25)
                for livro in livros_reservados:
                    print('-', livro)
                print('''
''')

            elif selecao == "3":
                cancelar_reserva = input("Digite o nome do livro que deseja cancelar a reserva: ")
                if cancelar_reserva in livros_reservados:
                    livros_reservados.remove(cancelar_reserva)

            elif selecao == "4":
                print("Obrigado por usar a nossa biblioteca!")
                salvar_dados()
                break
    elif verificar == 'aluno':
        while True:
            print("-" * 25)
            print(f'{"Biblioteca Virtual:":^25} ')
            print("-" * 25)
            print("1 - Pesquisar Livros")
            print("2 - Livros Reservados")
            print("3 - Cancelar reserva")
            print("4 - Sair\n")

            selecao = input("Selecione uma das opções acima: ")

            if selecao == "1":
                print("-" * 25)
                print(f'{"Pesquisar Livros":^25}')
                print("-" * 25)
                pesquisa = input("Digite o nome do Livro: ")

                verificar = verificar_disponibilidade(pesquisa, livros_cadastrados)

                if verificar == -1:
                    print('Livro não encontrado.')
                else:
                    reservar = input("O livro foi encontrado. Deseja reservar o livro? [S/N] ").lower()
                    if reservar == "s":
                        livros_reservados.append(pesquisa)
                        print("Livro reservado!")

            elif selecao == "2":
                print("-" * 25)
                print(f'{"Livros Reservados:":^25}')
                print("-" * 25)
                for livro in livros_reservados:
                    print('-', livro)
                print('''
''')

            elif selecao == "3":
                cancelar_reserva = input("Digite o nome do livro que deseja cancelar a reserva: ")
                if cancelar_reserva in livros_reservados:
                    livros_reservados.remove(cancelar_reserva)
            elif selecao == "4":
                print("Obrigado por usar a nossa biblioteca!")
                salvar_dados()
                break

# Carregar dados e ordenar a lista de livros cadastrados
carregar_dados()
insertion_sort(livros_cadastrados)

if __name__ == "__main__":
    main()