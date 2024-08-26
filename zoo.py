class Animal:
    def __init__(self, nome, idade, barulho, movimento, alimentacao, habitat, vizinhos, horas):
        self.nome = nome
        self.idade = idade
        self.barulho = barulho
        self.movimento = movimento
        self.alimentacao = alimentacao
        self.habitat = habitat
        self.vizinhos = vizinhos
        self.horas = horas

class Mamifero(Animal):
    pass

class Aves(Animal):
    pass

class Reptil(Animal):
    pass

class Zoologico:
    def __init__(self):
        self.animais = []

    def adicionar_animal(self, nome, idade, barulho, movimento, alimentacao, habitat, vizinhos, horas):
        novo_animal = Animal(nome, idade, barulho, movimento, alimentacao, habitat, vizinhos, horas)
        self.animais.append(novo_animal) 
        print(f"Você adicionou {nome}")

    def listar_animal(self):
        pass

def menu():
    zoologico = Zoologico()  # Instanciação do Zoologico
    while True:
        print("<Menu>")
        print("1. Adicionar Animal")
        print("2. Listar Animal")
        print("3. Buscar Animal")
        print("4. Listar por categoria")
        print("5. Listar Vizinhos de um animal")
        print("6. Simular alimentação")
        print("7. Sair")
        op = input("Digite a opção que deseja: ")

        if op == '1':
            nome = input("Digite o nome do animal: ")
            idade = input("Digite a idade do animal: ")
            barulho = input("Qual o som característico do animal: ")
            movimento = input("Digite a forma de locomoção do animal: ")
            alimentacao = input("Digite qual a dieta do animal: ")
            habitat = input("Digite o habitat do animal: ")
            vizinhos = input("Digite quais os vizinhos do animal: ")
            horas = input("Digite a hora que o animal se alimenta: ")
            zoologico.adicionar_animal(nome, idade, barulho, movimento, alimentacao, habitat, vizinhos, horas)

        elif op == '2':
            pass

        elif op == '3':
            pass

        elif op == '4':
            pass

        elif op == '5':
            pass

        elif op == '6':
            pass

        elif op == '7':
            print("Saindo...")
            break

menu()
