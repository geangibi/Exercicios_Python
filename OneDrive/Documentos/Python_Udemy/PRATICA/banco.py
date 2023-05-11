import contas
import pessoas

class Banco:
# Medoto init importa lista de clientes e lista de contas
    def __init__(self,
        agencias: list[int] | None = None,
        clientes: list[pessoas.Pessoa] | None = None,
        contas: list[contas.Contas] | None = None
    ):
        self.agencias = agencias or []
        self.clientes = clientes or []
        self.contas = contas or []
    
    def chega_agencia(self, conta):
        if conta.agencia in self.agencias:
            print('Checa agencia', True)
            return True
        print('Chega agencia', False )
        return False

    def chega_cliente(self, cliente):
        if cliente in self.clientes:
            print('Checa cliente', True)
            return True
        print('Checa cliente', False )
        return False

    def chega_conta(self, conta):
        if conta in self.contas:
            print('Checa conta', True)
            return True
        print('Chega conta', False )
        return False

    def chega_conta_e_do_cliente(self, cliente, conta):
        if conta in cliente.conta:
            print('Chega conta do cliente', True)
            return True
        print('Checa conta do cliente', False)
        return False

    # executa as funções que fazem validação 
    def autenticar(self, cliente: pessoas.Pessoa, conta: contas.Contas):
        return self.chega_agencia(conta) and \
            self.chega_cliente(cliente) and \
            self.chega_conta(conta) and \
            self.chega_conta_e_do_cliente(cliente, conta)

    # permite imprimir os valores na tela
    def __repr__(self):
            class_name = type(self).__name__
            attrs = f'({self.agencias!r}, {self.clientes!r}, {self.contas!r})'
            return f'{class_name}{attrs}'

if __name__ == '__main__':
    c1 = pessoas.Cliente('Luiz', 30)
    cc1 = contas.ContaCorrente(111, 222, 0, 0)
    c1.conta = cc1
    c2 = pessoas.Cliente('Maria', 18)
    cp1 = contas.ContaPoupanca(112, 223, 100)
    c2.conta = cp1
    banco = Banco()
    banco.clientes.extend([c1, c2])
    banco.contas.extend([cc1, cp1])
    banco.agencias.extend([111, 222])

    if banco.autenticar(c1, cc1):
        cc1.depositar(10)
        c1.conta.depositar(100)
        print(c1.conta)