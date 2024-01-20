
menu = """
[1]Deposito
[2]Saque
[3]Extrato
[4]Sair
=> """

saldo = 0
limite = 1000
extrato = ""
numero_saque = 0
LIMITE_SAQUE = 5

while True:
    
    opcao = input(menu)

    if opcao == "1":
        deposito = float(input("infome o valor: "))
    
        if deposito > 0:
            saldo += deposito
            extrato += f"Deposito: R$ {deposito:.2f}\n"
        else:
            print("Operação invalida, valor infromado é invalido")
    elif opcao == "2":
        saque = float(input("infome o valor para saque: "))
        
        saldo_excedido = saque > saldo
        
        limite_excedido = saque > limite
        
        saque_execedido = numero_saque >= LIMITE_SAQUE      
         
        if limite_excedido:
            print("Valor Maior que permitido")
            
        elif saque_execedido:
            print("Limite de saque maior que permitido")
            
        elif saldo_excedido:
            print("Não existe saldo suficiente para saque")
            
        elif saque > 0:   
            saldo -= saque
            extrato += f"Saque: R$ {saque:.2f}\n"
            print("Saque realizado com Sucesso")
            numero_saque += 1 
        else:
           print("Operação falhou, valor informado invalido")
    elif opcao == "3":
        print("\n==============Extrato================")
        print("Não foram realizadas movimentações." if not extrato else extrato)
        print(f"\nSaldo: R$ {saldo:.2f}")
        print("===================================================================")
    
    elif opcao == "4":
        break
    else:
        print("Opção invalida, selecione novamente a opção desejada")
        