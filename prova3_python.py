def adicionar_aluno(alunos):
    nome = input("Digite o nome do aluno: ")
    matricula = input("Digite o número de matrícula do aluno: ")
    alunos[matricula] = nome
    print("Aluno adicionado com sucesso!")

def remover_aluno(alunos):
    matricula = input("Digite o número de matrícula do aluno a ser removido: ")
    if matricula in alunos:
        del alunos[matricula]
        print("Aluno removido com sucesso!")
    else:
        print("Número de matrícula não encontrado.")

def visualizar_alunos(alunos):
    print("\nLista de alunos:")
    for matricula, nome in alunos.items():
        print(f"Matrícula: {matricula}, Nome: {nome}")

alunos = {}

print("Bem-vindo ao sistema de gerenciamento de alunos!")

while True:
    print("\nSelecione uma opção:")
    print("1. Adicionar aluno")
    print("2. Remover aluno")
    print("3. Visualizar todos os alunos")
    print("4. Sair")

    opcao = input("Opção: ")

    if opcao == '1':
        adicionar_aluno(alunos)
    elif opcao == '2':
        remover_aluno(alunos)
    elif opcao == '3':
        visualizar_alunos(alunos)
    elif opcao == '4':
        print("Encerrando o programa...")
        break
    else:
        print("Opção inválida. Por favor, selecione uma opção válida.")