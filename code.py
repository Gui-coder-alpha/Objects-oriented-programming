class Animal:
    #Animal, Nome, Idade, Raça
    def __init__(self,animais, nome, idade, raça):
        self.animais = animais
        self.nome = nome
        self.idade = idade
        self.raca = raça

    def conjunto_animal(self):
        return f"Animal:{self.animais}",f"Nome:{self.nome}", f"Idade:{self.idade}", f"Raça:{self.raca}"
    

class Cliente:
    def __init__(self, cliente, telefone, chamada):
        self.cliente = cliente
        self.telefone = telefone
        self.id = chamada

    def chamada_cliente(self):
        return f"Cliente:{self.cliente}", f"Telefone:{self.telefone}", f"ID:{self.id}"

class Servico:
    def __init__(self, servico, descricao, preco):
        self.servico = servico
        self.descricao = descricao
        self.preco = preco
        
    def conjunto_servico(self):
        return f"Serviço:{self.servico}", f"Descrição:{self.descricao}", f"Valor:{self.preco}"

     

animais_colocados = Animal("Cachorro", "Rex", 3, "Labrador")
cliente_chamou = Cliente("João", "123456789", "banho")
servico_a_realizar = Servico("Banho", "Banho simples", "$30")
print(animais_colocados.conjunto_animal())




class PetShop:
    def __init__(self, conjunto_animais, chamada, conjunto):
        self.conjunto_animais = conjunto_animais
        self.chamada = chamada
        self.conjunto = conjunto

    def colocando_tudo(self):
        return [self.conjunto_animais, self.chamada, self.conjunto]

todas_as_informações_necessarias = PetShop(animais_colocados.conjunto_animal(), cliente_chamou.chamada_cliente(), servico_a_realizar.conjunto_servico())
print(todas_as_informações_necessarias.colocando_tudo())
