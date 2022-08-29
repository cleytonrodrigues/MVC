#from model.calculadora import Calculadora
#from viewTerminal.view import View

from view import View
from model import Calculadora


class CtrlCalculadora():
    def start(self):
        opcao = self.view.start()

        while opcao != 0:
            resultado = self.operacao(opcao)
            self.view.mostrarResultado(resultado)

            opcao = self.view.menu()

        self.view.finalizar()

    def operacao(self, opcao):
        primeiro, segundo = self.view.getOperando()

        if opcao == 1:
            return self.model.soma(primeiro, segundo)
        elif opcao == 2:
            return self.model.subtracao(primeiro, segundo)
        elif opcao == 3:
            return self.model.multiplicacao(primeiro, segundo)
        else:
            return self.model.divisao(primeiro, segundo)

    def __init__(self):
        self.model = Calculadora()
        self.view = View()


if __name__ == "__main__":
    main = CtrlCalculadora()
    main.start()