"""
Modulo que implementa um gerenciador de tarefas
"""


lista_de_tarefas: list[dict[str]] = [
    {"prioridade": True, "tarefa": "Estudar Python"},
    {"prioridade": False, "tarefa": "Tomar banho"},
    {"prioridade": False, "tarefa": "Assistir série"},
]


lista_de_tarefas: list[dict[str]] = []

def adicionar_tarefa(prioridade: bool, tarefa: str):
    if prioridade not in [True, False]:
        raise ValueError("Prioridade inválida")
    for item in lista_de_tarefas:
        if item["tarefa"] == tarefa:
            raise ValueError("Tarefa já existe")

    dicti = {"prioridade": prioridade, "tarefa": tarefa}
    lista_de_tarefas.append(dicti)

def remove_tarefas(indices: tuple[int]):
    for indice in reversed(indices):
        if indice < 0 or indice >= len(lista_de_tarefas):
            raise ValueError("Tarefa não existe")
        lista_de_tarefas.pop(indice)

def encontra_tarefa(tarefa: str) -> int:
    for i, item in enumerate(lista_de_tarefas):
        if item["tarefa"] == tarefa:
            return i

    raise ValueError("Tarefa não existe")

def ordena_por_prioridade():
    def pega_texto(tarefa):
        if tarefa["prioridade"]:
            prefixo = "AAA-"
        else:
            prefixo = "ZZZ-"
        return prefixo + tarefa["tarefa"]

    lista_de_tarefas.sort(key=pega_texto)

def get_lista_de_tarefas():
    texts = []
    for tarefa in lista_de_tarefas:
        texto = tarefa["tarefa"]
        prioridade = tarefa["prioridade"]
        texts.append(f"{'*' if prioridade else ''} {texto}")
    return tuple(texts)

