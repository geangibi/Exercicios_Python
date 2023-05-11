import abc

class Contas(abc.ABC):
    def __init__(self, agencia = int, conta = int, saldo = float) -> None:
        self.agencia = agencia
        self.conta = conta
        self.saldo = saldo
    
    #metodo abstrato, é implementado pela subclasse

    @abc.abstractmethod
    def sacar(self, valor: float) -> float:
        pass
    
    #metodo que deposita valor na conta

    def depositar(self, valor: float):
        self.saldo += valor
        self.detalhes(f'(Valor deposito {valor})')
    
    # Exibe o saldo na conta, após depósito
    def detalhes(self, msg=''):
        print(f'O seu saldo é {self.saldo:.2f}{msg}')

    def __repr__(self):
        class_name = type(self).__name__
        attrs = f'({self.agencia!r}, {self.conta!r}, {self.saldo!r})'
        return f'{class_name}, {attrs}'

# Cria uma subclasse que herda da classe Contas
class ContaCorrente(Contas):
    def __init__(self, agencia = int, conta = int, saldo = float, limite=0):
       # herda da Super Classe(Contas)
       super().__init__(agencia, conta, saldo)
       # adiciona mais um argumento
       self.limite = limite 

    # Implementa o médoto na subclasse ContaCorrente
    def sacar(self, valor):
        valor_pos_saque = self.saldo - valor
        limite_maximo = -self.limite

        if valor_pos_saque >= limite_maximo:
            self.saldo -= valor
            # Passa a mensagem para função detalhes
            self.detalhes(f'(SAQUE {valor})')
            return self.saldo

        print('Não foi posssível sacar o valor desejado')
        print(f'O seu limite é{-self.limite:.2f}')
        self.detalhes(f'(SAQUE NEGADO {valor})')

class ContaPoupanca(Contas):
    def sacar(self, valor):
        valor_pos_saque = self.saldo - valor

        if valor_pos_saque >=0:
            self.saldo -= valor 
            self.detalhes(f'(SAQUE NEGADO {valor})')
            return self.saldo
        
        # medoto para imprimir dados, caso contrário será impresso um endereço na memória

        def __repr__(self):
            class_name = type(self).__name__
            attrs = f'({self.agencia!r}{self.conta!r},{self.saldo!r},{self.limite!r})'
            return f'{class_name},{attrs}'

        print('Não foi possível sacar o valor desejado')
        self.detalhes(f'(SAQUE NEGADO {valor})')

if __name__== '__main__':

    print('##')

    cc1 = ContaCorrente(111,222,0, 100)
    cc1.sacar(1)
    cc1.depositar(2)
    cc1.sacar(1)


       
