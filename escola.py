import json
#função para salvar os dados mesmo após encerrar programa
import keyboard
#adicionando função para interação do programa com o teclado

from ast import Continue

alunos = []
materias = []
discentes = []
turmas = []
matriculas = []
# Criação de listas para cada item do Primeiro menu

def Primeiro_Menu():
    while True:
        print("\n \033[1m Bem vindo ao Menu.\033[0m")
        print(f"\n \033[1m Opções de navegação \033[0m")
        print("\n 1 - Estudante\n 2 - Disciplina\n 3 - Professor\n 4 - Turma\n 5 - Matrícula\n 6 - Sair")

        opcao = int(input("\n Digite sua opção: "))
        #defindo opções do menu

        if opcao == 1:
            print("\n \t ESTUDANTE")
            selecionado = "ESTUDANTE"
            SegundoMenu(selecionado)

        elif opcao == 2:
            print("\n \t DISCIPLINA")
            selecionado = "DISCIPLINA"
            SegundoMenu(selecionado)

        elif opcao == 3:
            print("\n \t PROFESSOR")
            selecionado = "PROFESSOR"
            SegundoMenu(selecionado)

        elif opcao == 4:
            print("\n \t TURMA")
            selecionado = "TURMA"
            SegundoMenu(selecionado)

        elif opcao == 5:
            print("\n \t MATRÍCULA")
            selecionado = "MATRÍCULA"
            SegundoMenu(selecionado)

        elif opcao == 6:
            print("\n \t Sair")
            print("Pressione ENTER para confirmar a saída.")
            while True:
                if keyboard.is_pressed('ENTER'):
                    print("Tecla 'ENTER' pressionada. Saindo do programa.")
                    return
        else:
            continue

def SegundoMenu(selecionado):
    while True:
        print("\n \t \033[1m [" + selecionado + "] MENU DE TAREFAS \n \033[0m")
        print('\t (1) Incluir.')
        print('\t (2) Listar.')
        print('\t (3) Atualizar.')
        print('\t (4) Excluir.')
        print('\t (6) Voltar.')
        #definindo as funcionalidade do menu
        operacao = int(input("\n \t Digite o numero correspondente a operacao desejada: "))

        if operacao == 1:
            print("\n \t \033[1m Incluir \n \033[0m")
            nome = input("\n \t Nome do aluno: ")
            codigo = input("\n \t Código do aluno: ")
            cpf = input("\n \t CPF do aluno: ")
            aluno = {'nome': nome, 'codigo': codigo, 'cpf': cpf}
            alunos.append(aluno)
            print("Aluno incluído com sucesso!")

        elif operacao == 2:
            print("\n \t \033[1m  Listar \n \033[0m")
            if len(alunos) < 1:
                print("\n \t Não há alunos para listar.")
            else:
                for aluno in alunos:
                    print(" - Nome: " + aluno['nome'])

        elif operacao == 3:
            print("\n \t \033[1m  Atualizar \n \033[0m")
            if len(alunos) < 1:
                print("\n \t Não há alunos para atualizar.")
            else:
                print("Atualizar dados dos alunos.")

        elif operacao == 4:
            print("\n \t \033[1m  Excluir \n \033[0m")
            if len(alunos) < 1:
                print("\n \t Não há alunos para excluir.")
            else:
                print("Digite o índice do aluno que deseja excluir: ")
                index = int(input())
                if index < len(alunos):
                    del alunos[index]
                    print("Aluno excluído com sucesso!")
                else:
                    print("Índice inválido.")

        elif operacao == 6:
            print("\n \t Voltando ao menu principal.")
            break 
        else:
            continue

Primeiro_Menu()
