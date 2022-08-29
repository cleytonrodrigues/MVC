class View():
    def start(self):
        print ("Bem vindo a Calculadora python\n")
        return self.menu()

    def menu(self):
        print ("1 - Para somar dois numeros")
        print ("2 - Para subtrair dois numeros")
        print ("3 - Para multiplicar dois numeros")
        print ("4 - Para dividir dois numeros")
        print ("0 - Sair")

        return int(input("\nDigite a opção: "))

    def getOperando(self):
        print ("\nDigite os valores a serem calculado");

        primeiro = int(input("O primeiro valor: "))
        segundo = int(input("O segundo valor: "))

        return primeiro, segundo

    def mostrarResultado(self, resultado):
        print ("O resultado calculado foi: %d\n" % resultado);

    def finalizar(self):
        print ("Programa finalizado!");