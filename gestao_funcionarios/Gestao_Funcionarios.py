import copy 
#Print com meu nome
print("Bem vindo a empresa do Arthur Yan Oliveira Silva")
#Lista de funcionarios é id
lista_funcionarios = []
id_global = 4297913 

def cadastrar_funcionario(id): #Para cadastrar funcionario
    print('--------- MENU CADASTRO DE FUNCIONÁRIOS ---------')
    print(id_global)
    nome = input("Por favor entre com o nome do Funcionário: ") #Para cadastrar o nome do funcionario
    setor = input("Por favor entre com o setor do Funcionário: ") #Para cadastrar setor funcionario
    salario = float(input("Por favor entre com o salário do Funcionário: ")) #Para cadastrar salario do funcionario
    salario_formatado = format(salario, ".1f")

    funcionario = {
        "ID": id,
        "Nome": nome,
        "Setor": setor,
        "Salário": salario_formatado }  
    
    lista_funcionarios.append(copy.deepcopy(funcionario))
def consultar_funcionarios(): #Para consultar funcionario
    while True:
        print('------------------------------------------------')
        print('----------- MENU CONSULTAR FUNCIONARIO----------')    
        opcao = input('Escolha a opção desejada:\n 1 - Consultar todos os Funcionários\n 2 - Consultar Funcionário por id\n 3 - Consultar Funcionário(s) por setor\n 4 - Retornar\n >>')
        print('-------------')
        if opcao == "1": #opção 1 para consultar  todos funcionarios cadastrados
            for func in lista_funcionarios:
                print(f" ID: {func['ID']}\n Nome: {func['Nome']}\n Setor: {func['Setor']}\n Salário: {func['Salário']}")
                print()
                
        elif opcao == "2": #opção 2 para consultar Funcionário por id
            id_consulta = int(input('Digite o id do funcionario: '))
            print('--------------')
            for func in lista_funcionarios:
                if func["ID"] == id_consulta:
                    print(f"ID: {func['ID']}\n Nome: {func['Nome']}\n Setor: {func['Setor']}\n Salário: {func['Salário']}")
                    print()
                    print('--------------')
                    break
            else: #Caso funcionario nao seja encontrado
                print("Funcionário não encontrado.") 

        elif opcao == "3":# para consultar Funcionário(s) por setor
            setor_consulta = input("Digite o setor do(s) funcionarios(s): ")
            print('--------------')
            encontrados = [func for func in lista_funcionarios if func["Setor"] == setor_consulta]
            for func in encontrados:
                print(f"ID: {func['ID']}\n Nome: {func['Nome']}\n Setor: {func['Setor']}\n Salário: {func['Salário']}")
                print()
            if not encontrados:
                print("Nenhum funcionário encontrado nesse setor.")
        elif opcao == "4": #p/ retornar 
            return
        else:
            print("Opção inválida")

def remover_funcionario(): #Para remover funcionario
    while True:
        id_remocao = int(input('Digite o id do funcionario a ser removido: ')) #Ira solicitar o id do funcionario que sera removido
        for func in lista_funcionarios: 
            if func["ID"] == id_remocao:
                lista_funcionarios.remove(func) # Ira remover funcionario pelo id desque o id seja valido 
                print('Funcionário removido com sucesso!\n')
                return
        print("Id inválido, tente novamente.") #caso id seja invalido 
#Programa principal
while True:
    print('------------------------------------------------')
    print('---------------- MENU PRINCIPAL ----------------')     #Ira apresentar o menu, e logo apos dara as opçoespara escolher se quer cadastrar, consultar, remover é encerrar o programa
    opcao = input('Escolha a opção desejada:\n 1 - Cadastrar Funcionários\n 2 - Consultar Funcionário(s)\n 3 - Remover Funcionário\n 4 - Sair\n >>')
    print('------------------------------------------------')
    if opcao == "1":
        id_global += 1
        cadastrar_funcionario(id_global)
    elif opcao == "2":
        consultar_funcionarios()
    elif opcao == "3":
        remover_funcionario()
    elif opcao == "4":
        print("Encerrando o programa...")
        break
    else: #Caso escolha opção invalida
        print("Opção inválida, tente novamente.") 

