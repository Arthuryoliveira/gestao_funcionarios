#Print com meu nome completo 
print(' Bem vindo a fabrica de camisetas do Arthur Yan Oliveira Silva')
print()

def escolha_modelo(): #Para definir o modelo da camiseta
  while True:
    #Ira solicita o modelo da camisa
    modelo = input(' Entre com o modelo desejado\n MCS - Manga Curta Simples \n MLS - Manga Longa Simples \n MCE - Manga Curta Com Estampada \n MLE - Manga Longa Com Estampada \n >>')
    if modelo == "MCS": #Retorna o preço referente ao modelo escolhido
      return 1.80
    elif modelo == 'MLS':
      return 1.90
    elif modelo == 'MCE':
      return 2.10
    elif modelo == 'MLE':
      return 3.20
    else: #Caso digitar uma opção invalida aparece a seguinte mensagem é Inicia novamente 
      print(' Escolha invalida, entre com o modelo novamente ')
      print()

def num_camisetas():#Para definir a quantidade de camiseta é calcular desconto
    while True:
        try:
            quantidade = int(input(' Entre com o número de camisetas: ')) #P/ perguntar a quantidade de camisetas 
            
            if quantidade > 20000: #Caso o numero de camisetas seja superior a 20000, ira executar o print é perguntar novamente
                print(' Não aceitamos tantas camisetas de uma vez.\n Por favor entre com o numero de camisetas novamente.\n')
      
            elif quantidade >= 2000:  #p/ calcular o desconto
                desconto = 0.12
                print() 
                return quantidade * (1 - desconto)
            elif quantidade >= 200:  #p/ calcular o desconto
                desconto = 0.07
                print()
                return quantidade * (1 - desconto)
            elif quantidade >= 20:  #p/ calcular o desconto
                desconto = 0.05
                print()
                return quantidade * (1 - desconto)
            else:
                print()
                return quantidade
        except ValueError:
            
            print('Quantidade invalida. tente novamente.')

def frete(): #Para definir um tipo de frete
    while True: 
        frete1 = input(' Escolha o tipo de frete: \n 1 - Frete para Transportadora - R$ 100.00 \n 2 - Frete para Sedex R$ 200.00 \n 0 - Retirar pedido na Fabrica - R$ 0.00 \n >>') 
        
        if frete1 == "1":
            return 100.00
        elif frete1 == "2":
            return 200.00
        elif frete1 == "0":
            return 0.00
        else:#Se não for uma das opções acima ira solicitar novamente qual o tipo de frete
            print('Opção de frete inválida. Tente novamente.')

#programa Principal
try:
    modelo1 = escolha_modelo()
    qnt = num_camisetas()
    frete2 = frete()
    
    if modelo1 > 20000: 
        print('Por favor,  entre com o numero de camisetas novamente.')

    else:
        total = (modelo1 * qnt) + frete2 #Total a pagar
        print(f' Total: R$ {total:.2f} (Modelo: {modelo1:.2f} * Quantidade(com desconto): {qnt:.0f} + frete: {frete2:.2f})')

except Exception as e:
    print(f' Ocorreu um erro inesperado: {e}\n')

