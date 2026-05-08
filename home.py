total = 0
while (True):
    print ("========== Cafeteria nada barato ==========")
    print("1 - Comprar Café\n2 - Entrega\n3 - sair")
    opcao = int(input("Escolha uma opçao:"))
    if opcao == 1:
        while(True):
            print ("1 - Cappucino - R$ 15,00")
            print ("2 - Expresso - R$ 8,00") 
            print ("3 - Fraputinno - R$ 18,00")
            print ("4 - Coado - R$ 5,00")
            print ("5 - Coffe and milk of Vaca - R$ 7,00")
            print ("6 - Moka - R$ 12,00")
            print ("7 - Prensa Francesa - R$ 9,00")
            print ("8 - Coffe gourmet - R$ 25,00")
            print ("9 - Voltar ao Menu Principal")
            print ("10 - Finalizar compra")
            opcafe = int(input("Escolha uma opção de café "))
            if opcafe == 1: 
                quantidade  = int(input("Digite a quantidade:"))
                valortotal = quantidade * 15
                total = total + valortotal
                print ("Voce escolheu Cappucino")
                print ("Seu caixa atualizado é de: R$", total)
                print ("")
            elif opcafe == 2:
                quantidade  = int(input("Digite a quantidade:"))
                valortotal = quantidade * 8
                total = total + valortotal
                print ("Voce escolheu Expresso")
                print ("Seu caixa atualizado é de: R$", total) 
                print ("")
            elif opcafe == 3:
                quantidade  = int(input("Digite a quantidade:"))
                valortotal = quantidade * 18
                total = total + valortotal
                print ("Voce escolheu Fraputinno")
                print ("Seu caixa atualizado é de: R$", total)
                print ("")
            elif opcafe == 4:
                quantidade  = int(input("Digite a quantidade:"))
                valortotal = quantidade * 5
                total = total + valortotal
                print ("Voce escolheu Coado")
                print ("Seu caixa atualizado é de: R$", total)
                print ("")
            elif opcafe == 5:
                quantidade  = int(input("Digite a quantidade:"))
                valortotal = quantidade * 7
                total = total + valortotal
                print ("Voce escolheu Coffe and milk of Vaca")
                print ("Seu caixa atualizado é de: R$", total)
                print ("")
            elif opcafe == 6:
                quantidade  = int(input("Digite a quantidade:"))
                valortotal = quantidade * 12
                total = total + valortotal
                print ("Voce escolheu Moka")
                print ("Seu caixa atualizado é de: R$", total)
                print ("")
            elif opcafe == 7:
                quantidade  = int(input("Digite a quantidade:"))
                valortotal = quantidade * 9
                total = total + valortotal
                print ("Voce escolheu Prensa Francesa")
                print ("Seu caixa atualizado é de: R$", total)
                print ("")
            elif opcafe == 8:  
                quantidade  = int(input("Digite a quantidade:"))  
                valortotal = quantidade * 25    
                total = total + valortotal       
                print ("Voce escolheu coffe gourmet")
                print ("Seu caixa atualizado é de: R$", total)
                print ("")
            elif opcafe == 9:
                print ("Voltar ao Menu Principal ")
                break
            elif opcafe == 10:
                print("Seu total é de : R$", total)
                endereço = input("Digite seu endereço de entrega: ")
                bairro = input("Digite seu bairro: ")
                if bairro == "Centro"  or bairro == "Benfica" or bairro == "Montese":
                    total = total + 5
                    print("Seu totsl com frete é de: R$", total)
                    pagamento = input("Forma de pagamento: ") 
                    if pagamento == "Credito":
                        print("Pagamento realizado com sucesso")
                        total = 0
                        break 
                    elif pagamento == "Débito":
                        print("Pagamento realizado com sucesso")
                        total = 0
                        break
                elif bairro ==   "Aldeota" or bairro == "Meireles" or bairro == "Fátima":
                      total = total + 15
                      print("Seu totsl com frete é de: R$", total)   
                      pagamento = input("Forma de pagamento: ") 
                      if pagamento == "Credito":
                        print("Pagamento realizado com sucesso")
                        total = 0 
                        break 
                      elif pagamento == "Débito":
                        print("Pagamento realizado com sucesso")
                        total = 0
                        break
                else:
                    print("Não entregamos nesse bairro!")        
            else:
                print("Opção de café invalida")
        
    elif opcao == 2:
        bairro = input("Escreva seu bairro ")  
        if bairro == "Centro"  or bairro == "Benfica" or bairro == "Montese":
            print ("5 reais de frete")
            
        elif bairro == "Aldeota" or bairro == "Meireles" or bairro == "Fátima":
            print ("15 reais de frete")
            
        else:
            print("Não entregamos nesse bairro!")

    elif opcao == 3:
        print ("Programa encerrado com sucesso!")
        break