# Classe person
class Person:

    # Método inicial
    def __init__(self, Nome, Pagar):

        # Preparar para estãncias
        self.Nome = Nome

        self.Pagar = Pagar

    # Método de imposto
    def Imposto(self):

        # Varíavel para calcular o imposto
        calculo = lambda x: x * 0.3 # Usando lambda

        # Mostrar o imposto a pagar
        print(f"{self.Nome} deve pagar {calculo(self.Pagar)} de impostos.")

# Iniciar estãncias
if __name__ == "__main__":

    valor = int(input("Digite o valor a pagar: "))

    pessoa = Person("David", valor)

    pessoa.Imposto()
