class Carro:
    def __init__(self, modelo, cor, ano):
        self.modelo = modelo
        self.cor = cor
        self.ano = ano
        self.ligado = False
        self.velocidade = 0

    def ligar(self):
        if not self.ligado:
            print(f"{self.modelo} ligado.")
            self.ligado = True
        else:
            print(f"{self.modelo} já está ligado.")

    def desligar(self):
        if self.ligado:
            print(f"{self.modelo} desligado.")
            self.ligado = False
            self.velocidade = 0
        else:
            print(f"{self.modelo} já está desligado.")

    def acelerar(self, velocidade):
        if self.ligado:
            self.velocidade += velocidade
            print(f"{self.modelo} acelerando a {self.velocidade} km/h.")
        else:
            print(f"{self.modelo} precisa estar ligado para acelerar.")


meu_carro = Carro(modelo="Fiat Uno", cor="Vermelha", ano=2003)


meu_carro.ligar()
meu_carro.acelerar(30)
meu_carro.acelerar(20)
meu_carro.desligar()
