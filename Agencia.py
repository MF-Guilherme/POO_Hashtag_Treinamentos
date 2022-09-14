from random import randint

class Agencia:

    def __init__(self, telefone, cnpj, numero):
        self.telefone = telefone
        self.cnpj = cnpj
        self.numero = numero
        self.clientes = []
        self.caixa = 0
        self.emprestimos = []

    def verificar_caixa(self):
        if self.caixa < 1000000:
            print(f'Caixa abaixo do nível recomendado. Caixa Atual: R$ {self.caixa:,.2f}')
        else:
            print(f"O valor de caixa está OK! Caixa Atual: R$ {self.caixa:,.2f}")

    def emprestar_dinheiro(self, valor, cpf, juros):
        if self.caixa > valor:
            self.caixa -= valor
            self.emprestimos.append((valor, cpf, juros))
        else:
            print('Empréstimo não autorizado. Valor não disponível em caixa.')

    def adicionar_cliente(self, nome, cpf, patrimonio):
        self.clientes.append((nome, cpf, patrimonio))


class AgenciaVirtual(Agencia):

    def __init__(self, telefone, cnpj, site):
        super().__init__(telefone, cnpj, 1000)#chamando o método __init__ da superclasse
        self.site = site
        self.caixa = 1000000


class AgenciaComum(Agencia):

    def __init__(self, telefone, cnpj):
        super().__init__(telefone, cnpj, randint(1001, 9999))
        self.caixa = 1000000


class AgenciaPremium(Agencia):

    def __init__(self, telefone, cnpj):
        super().__init__(telefone, cnpj, randint(10000, 99999))
        self.caixa = 10000000


agv = AgenciaPremium(123456, 123451569)
agv.verificar_caixa()

