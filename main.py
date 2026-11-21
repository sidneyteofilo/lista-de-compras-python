compras = []

while True:

    print("\n=====LISTA DE COMPRAS=====")
    print("[1] Adicionar produto")
    print("[2] Remover produto")
    print("[3] Mostrar lista")
    print("[4] Mostrar quantidade de produtos")
    print("[5] Sair")

    listaOpc = input("\nEscolha a opção: ")

    if listaOpc == "1":
        compraAdd = input("\nAdicione um produto a sua lista de compras: ")
        compras.append(compraAdd)
        print(f"\nO produto {compraAdd} foi adicionado à sua lista.")
    elif listaOpc == "2":
        compraRemove = input("\n Digite corretamente qual produto você deseja remover da sua lista de compras: ")
        if compraRemove in compras:
            compras.remove(compraRemove)
            print("\nO produto "f"{compraRemove} foi removido(a) à sua lista.")
        else:
            print("\nO produto inserido não pertence a lista de compras.")
    elif listaOpc == "3":
        if len(compras) == 0:
            print("\nVocê não adicionou nenhum produto à sua lista de compras")
        else:
            print("=====LISTA DE COMPRAS=====")
            for produto in compras:
                print(produto)
    elif listaOpc == "4":
        print("\nA quantidade de produtos atuais na sua lista é de: "f"{len(compras)} produtos")
    elif listaOpc == "5":
        print("\nVocê escolheu sair.")
        break
    else:
        print("\nOpção não implementada.")
        continue
        


