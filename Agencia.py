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


ag1 = Agencia('123456', '12345679', 1010)
ag1.caixa = 1000000
ag1.verificar_caixa()

ag1.emprestar_dinheiro(70000, 124365412, 0.02)
print(ag1.emprestimos)
ag1.verificar_caixa()

ag1.adicionar_cliente('Guilherme', 1457921324, 120504)
print(ag1.clientes)