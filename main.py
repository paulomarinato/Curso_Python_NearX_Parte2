# Task manager         


def adicionar_tarefa(tarefas):
    descrição = input("Digite o nome da Tarefa: ")

    tarefa = {
        "descricao": descrição,
        "concluido": False
    }
    tarefas.append(tarefa)

    print("\n>>>Tarefa Adicionada<<<")

def exibir_tarefas(tarefas):
    print(f"\nVocê tem {len(tarefas)} Tarefas")

    if len(tarefas) == 0:
        print("\n>>>>Nenhuma Tarefa!")

    for indice, tarefa in enumerate(tarefas):
        descrição = tarefa ["descricao"]
        concluido = tarefa ["concluido"]

        status = "Concluída" if concluido else "Não Concluída"

        print(f"{indice +1}. {descrição} - {status}")


def remover_tarefa(tarefas):
    if len(tarefas) == 0:
        print("\n>>>>Nenhuma Tarefa!")

    exibir_tarefas(tarefas)
    indice = int(input("Número da Tarefa para Remover: ")) - 1

    if 0 <= indice < len(tarefas):

        tarefas[indice] = tarefas[len(tarefas) - 1]
        tarefas.pop()

        print("\n>>>Tarefa Removida<<<")

    else:
        print("\n>>>Número da Tarefa Inválido<<<")

def concluir_tarefa(tarefas):
    if len(tarefas) == 0:
        print("\n>>>>Nenhuma Tarefa!")

    exibir_tarefas(tarefas)
    indice = int(input("Número da Tarefa Concluída: ")) -1

    if 0 <= indice < len(tarefas):
        tarefa = tarefas[indice]
        tarefa["concluido"] = True
        tarefas[indice] = tarefa

        print("Tarefa Concluída")

    else:
        print("Tarefa Inválida")


def menu():
    tarefas = []

    while True:
        print("\n📒 Gerenciador de Tarefas")
        print("1. Ver Todas as Tarefas")
        print("2. Adicionar uma Tarefas")
        print("3. Remover uma Tarefas")
        print("4. Concluir uma Tarefas")
        print("5. Sair")

        opcao = input("Escolha sua Opção: ")

        if opcao == "1":
            exibir_tarefas(tarefas)
        elif opcao == "2":
            adicionar_tarefa(tarefas)
        elif opcao == "3":
            remover_tarefa(tarefas)
        elif opcao == "4":
            concluir_tarefa(tarefas)
        elif opcao == "5":
            print("\n>>>Saindo do Programa<<<\n")
            break
        else:
            print("\nOpção Inválida")

menu()
        