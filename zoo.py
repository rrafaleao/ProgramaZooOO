class Animal:
    def __init__(self, tipo, nome, idade, barulho, movimento, alimentacao, habitat, vizinhos, horas_alimentacao):
        self.tipo = tipo
        self.nome = nome
        self.idade = idade
        self.barulho = barulho
        self.movimento = movimento
        self.alimentacao = alimentacao
        self.habitat = habitat
        self.vizinhos = vizinhos
        self.horas_alimentacao = horas_alimentacao
    
    def simular_alimentacao(self):
        return f"{self.nome} foi alimentado!"

class Mamifero(Animal):
    def __init__(self, nome, idade, barulho, movimento, alimentacao, habitat, vizinhos, horas_alimentacao):
        super().__init__("Mamífero", nome, idade, barulho, movimento, alimentacao, habitat, vizinhos, horas_alimentacao)

class Aves(Animal):
    def __init__(self, nome, idade, barulho, movimento, alimentacao, habitat, vizinhos, horas_alimentacao):
        super().__init__("Ave", nome, idade, barulho, movimento, alimentacao, habitat, vizinhos, horas_alimentacao)

class Reptil(Animal):
    def __init__(self, nome, idade, barulho, movimento, alimentacao, habitat, vizinhos, horas_alimentacao):
        super().__init__("Réptil", nome, idade, barulho, movimento, alimentacao, habitat, vizinhos, horas_alimentacao)

class Zoologico:
    def __init__(self):
        self.animais = []

    def adicionar_animal(self, animal):
        self.animais.append(animal) 
        print(f"Você adicionou {animal.nome}, que é um {animal.tipo}")

    def listar_animal(self):
        if not self.animais:
            print("Nenhum animal cadastrado.")
        for animal in self.animais:
            print(f"{animal.nome} ({animal.tipo}) - Idade: {animal.idade}")

    def buscar_animal(self, busca_animal):
        resultados = [animal for animal in self.animais if busca_animal.lower() in animal.nome.lower()]
        if resultados:
            print("Animal encontrado:")
            for animal in resultados:
                print(f"{animal.nome} ({animal.tipo}) - Idade: {animal.idade}")

    def listar_categoria(self, busca_categoria):
        resultados = [animal for animal in self.animais if busca_categoria.lower() in animal.tipo.lower()]
        if resultados:
            print("Animal encontrado:")
            for animal in resultados:
                print(f"{animal.nome} ({animal.tipo}) - Idade: {animal.idade}")
    
    def busca_vizinho(self, busca_vizinho):
        resultados = [animal for animal in self.animais if busca_vizinho.lower() in animal.nome.lower()]
        if resultados:
            print("Animal encontrado:")
            for animal in resultados:
                print(f"{animal.vizinhos} é o vizinho de {animal.nome}")

    def simular_alimentacao(self, nome_animal):
        for animal in self.animais:
            if animal.nome.lower() == nome_animal.lower():
                print(animal.simular_alimentacao())
                return
        print("Animal não encontrado.")

def menu():
    zoologico = Zoologico()
    while True:
        print("<Menu>")
        print("1. Adicionar Animal")
        print("2. Listar Animais")
        print("3. Buscar Animal")
        print("4. Listar por categoria")
        print("5. Listar Vizinhos de um animal")
        print("6. Simular alimentação")
        print("7. Sair")
        op = input("Digite a opção que deseja: ")

        if op == '1':
            tipo = input("Digite o tipo do animal (Mamifero, Ave ou Reptil): ").capitalize()
            nome = input("Digite o nome do animal: ")
            idade = input("Digite a idade do animal: ")
            barulho = input("Qual o som característico do animal: ")
            movimento = input("Digite a forma de locomoção do animal: ")
            alimentacao = input("Digite qual a dieta do animal: ")
            habitat = input("Digite o habitat do animal: ")
            vizinhos = input("Digite quais os vizinhos do animal: ")
            horas_alimentacao = input("Digite a hora que o animal se alimenta: ")
            
            if tipo == 'Mamifero':
                animal = Mamifero(nome, idade, barulho, movimento, alimentacao, habitat, vizinhos, horas_alimentacao)
            elif tipo == 'Ave':
                animal = Aves(nome, idade, barulho, movimento, alimentacao, habitat, vizinhos, horas_alimentacao)
            elif tipo == 'Reptil':
                animal = Reptil(nome, idade, barulho, movimento, alimentacao, habitat, vizinhos, horas_alimentacao)
            else:
                print("Tipo de animal inválido.")
                continue

            zoologico.adicionar_animal(animal)

        elif op == '2':
            zoologico.listar_animal()

        elif op == '3':
            busca_animal = input("Digite o nome do animal que deseja buscar: ")
            zoologico.buscar_animal(busca_animal)

        elif op == '4':
            busca_categoria = input("Digite a categoria que deseja buscar (Mamifero, Ave, Reptil): ")
            zoologico.listar_categoria(busca_categoria)

        elif op == '5':
            busca_vizinho = input("Digite o nome do animal que você quer ver os vizinhos: ")
            zoologico.busca_vizinho(busca_vizinho)

        elif op == '6':
            animal_alimentado = input("Digite o nome do animal que deseja alimentar: ")
            zoologico.simular_alimentacao(animal_alimentado)

        elif op == '7':
            print("Você escolheu sair")
            break

menu()
