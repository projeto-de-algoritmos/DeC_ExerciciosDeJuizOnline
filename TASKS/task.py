import json
from datetime import datetime

class Tarefa:
    def __init__(self, descricao, prioridade, data_entrega, data_criacao=None):
        self.descricao = descricao
        self.prioridade = prioridade
        self.data_entrega = self.validar_data(data_entrega)
        self.data_criacao = datetime.now() if data_criacao is None else self.validar_data(data_criacao)

    def validar_data(self, data_string):
        try:
            data = datetime.strptime(data_string, "%d-%m-%Y %H:%M")
            if data <= datetime.now():
                raise ValueError("A data de entrega deve ser posterior à data atual.")
            return data
        except ValueError as e:
            print(f"Erro: {e}")
            raise

    def to_dict(self):
        return {
            "descricao": self.descricao,
            "prioridade": self.prioridade,
            "data_entrega": self.data_entrega.strftime("%d-%m-%Y %H:%M"),
            "data_criacao": self.data_criacao.strftime("%d-%m-%Y %H:%M")
        }

    def __repr__(self):
        return f"Tarefa('{self.descricao}', {self.prioridade}, {self.data_entrega.strftime('%d/%m/%Y %H:%M')}, {self.data_criacao.strftime('%d/%m/%Y %H:%M')})"


def merge_sort(tarefas):
    if len(tarefas) > 1:
        meio = len(tarefas) // 2
        metade_esquerda = tarefas[:meio]
        metade_direita = tarefas[meio:]

        merge_sort(metade_esquerda)
        merge_sort(metade_direita)

        i = j = k = 0

        while i < len(metade_esquerda) and j < len(metade_direita):
            if metade_esquerda[i].prioridade < metade_direita[j].prioridade:
                tarefas[k] = metade_esquerda[i]
                i += 1
            else:
                tarefas[k] = metade_direita[j]
                j += 1
            k += 1

        while i < len(metade_esquerda):
            tarefas[k] = metade_esquerda[i]
            i += 1
            k += 1

        while j < len(metade_direita):
            tarefas[k] = metade_direita[j]
            j += 1
            k += 1


def exibir_tarefas(tarefas):
    print("\nTarefas:")
    print("{:<5} {:<20} {:<20} {:<20} {:<20}".format("ID", "Descrição", "Prioridade", "Data de Criação", "Data de Entrega"))
    print("-" * 85)
    for idx, tarefa in enumerate(tarefas):
        print("{:<5} {:<20} {:<20} {:<20} {:<20}".format(idx, tarefa.descricao, tarefa.prioridade, tarefa.data_criacao.strftime('%d/%m/%Y %H:%M'), tarefa.data_entrega.strftime('%d/%m/%Y %H:%M')))


def salvar_tarefas(tarefas):
    with open("./tarefas.json", "w") as file:
        tarefas_dict = [tarefa.to_dict() for tarefa in tarefas]
        json.dump(tarefas_dict, file, indent=2)


def carregar_tarefas():
    try:
        with open("./tarefas.json", "r") as file:
            tarefas_dict = json.load(file)
            tarefas = [Tarefa(**tarefa) for tarefa in tarefas_dict]
        return tarefas
    except FileNotFoundError:
        return []


def main():
    tarefas = carregar_tarefas()

    while True:
        print("\nGerenciador de Tarefas para alunos da UnB")
        print("Opções:")
        print("1. Adicionar Tarefa")
        print("2. Exibir Tarefas")
        print("3. Excluir Tarefa")
        print("4. Sair")

        escolha = input("Digite sua escolha: ")

        if escolha == '1':
            descricao = input("Digite a descrição da tarefa: ")
            prioridade = int(input("Digite a prioridade da tarefa (1-5): "))
            while True:
                data_entrega = input("Digite a data de entrega (DD-MM-AAAA HH:MM): ")
                try:
                    nova_tarefa = Tarefa(descricao, prioridade, data_entrega)
                    break
                except ValueError:
                    pass 
            tarefas.append(nova_tarefa)
            salvar_tarefas(tarefas)
            print("Tarefa adicionada com sucesso!")

        elif escolha == '2':
            if not tarefas:
                print("Não há tarefas para exibir.")
            else:
                merge_sort(tarefas)
                exibir_tarefas(tarefas)

        elif escolha == '3':
            if not tarefas:
                print("Não há tarefas para excluir.")
            else:
                exibir_tarefas(tarefas)
                try:
                    indice_excluir = int(input("Digite o ID da tarefa que deseja excluir: "))
                    if 0 <= indice_excluir < len(tarefas):
                        tarefas.pop(indice_excluir)
                        salvar_tarefas(tarefas)
                        print("Tarefa excluída com sucesso!")
                    else:
                        print("ID de tarefa inválido.")
                except ValueError:
                    print("Por favor, digite um número válido.")

        elif escolha == '4':
            print("Encerrando o programa. Adeus!")
            break

        else:
            print("Escolha inválida. Por favor, digite uma opção válida.")


if __name__ == "__main__":
    main()
