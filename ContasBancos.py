from datetime import datetime
import pytz
from random import randint


class ContaCorrente: # nome da classe inicia-se com letra maiúscula e utiliza CamelCase
    # caso tenhamos algum atributo estático (que é padrão para todas as instâncias da classe), colocamos antes do init

    # docstring para descrever o que a classe faz, quais são seus atributos e métodos. Padrão PEP257
    """
        Cria um objeto ContaCorrente para gerenciar as contas dos clientes.

        Atributos:
            nome (str): Nome do cliente
            cpf (str): CPF do cliente. Deve ser inserido com pontos e traços.
            agencia: Agencia responsável pela conta do cliente
            num_conta: Número da conta corrente do cliente
            saldo: Saldo disponível na conta do cliente
            limite: Limite de cheque especial daquele cliente
            transacoes: Lista com o histórico de transações do cliente
    """

    @staticmethod
    def _data_hora():
        fuso_BR = pytz.timezone('Brazil/East')
        horario_BR = datetime.now(fuso_BR)
        return horario_BR.strftime('%d/%m/%y - %H:%M:%S')

    def __init__(self, nome, cpf, agencia, num_conta): # primeiro define-se o método __init__ para incluir os atributos da classe
        self._nome = nome # atributos com _ para informar que ele só deverá ser alterado por meio de métodos
        self._cpf = cpf
        self._saldo = 0
        self._limite = None
        self._agencia = agencia
        self._num_conta = num_conta
        self._transacoes = []
        self.cartoes = []

# uma linha de espaço entre os métodos
    def consultar_saldo(self): # os demais métodos iniciam com letra minúscula e pode-se utilizar snake_case
        print(f'Seu saldo atual é de R$ {self._saldo:,.2f}.')

    def depositar(self, valor_deposito):
        self._saldo += valor_deposito
        self._transacoes.append(f'Depósito de R$ {valor_deposito:,.2f}. Saldo atual: R$ {self._saldo:,.2f}, {ContaCorrente._data_hora()}')

    def _limite_conta(self): # iniciar o método com _ quando quiser informar que o método é estático
        self._limite = -1000
        return self._limite

    def sacar(self, valor_saque):
        if self._saldo - valor_saque < self._limite_conta():
            print('Você não tem saldo suficiente para realizar este saque')
            self.consultar_saldo()
        else:
            self._saldo -= valor_saque
            self.consultar_saldo()
            self._transacoes.append(f'Saque de R$ {-valor_saque:,.2f}. Saldo atual R$ {self._saldo:,.2f}, {ContaCorrente._data_hora()}')

    def consultar_limite_cheque_especial(self):
        print(f'Seu limite de cheque especial é de R${self._limite_conta():,.2f}')

    def historico_de_transacoes(self):
        print(f'Histórico de transações {self._nome}')
        for transacao in self._transacoes:
            print(transacao)

    def transferir(self, valor, conta_destino):
        self._saldo -= valor
        self._transacoes.append(f'Saque de R$ {-valor:,.2f}. Saldo atual R$ {self._saldo:,.2f}, {ContaCorrente._data_hora()}')
        conta_destino._saldo += valor
        conta_destino._transacoes.append(f'Depósito de R$ {valor:,.2f}. Saldo atual: R$ {conta_destino._saldo:,.2f}, {ContaCorrente._data_hora()}')

class CartaoCredito:


    @staticmethod
    def _data_hora():
        fuso_BR = pytz.timezone('Brazil/East')
        horario_BR = datetime.now(fuso_BR)
        return horario_BR

    def __init__(self, titular, conta_corrente):
        self.numero = randint(1000000000000000, 9999999999999999)
        self.titular = titular
        self.validade = f'{CartaoCredito._data_hora().month}/{CartaoCredito._data_hora().year + 4}'
        self.cod_seguranca = f'{randint(0,9)}{randint(0,9)}{randint(0,9)}'
        self.limite = 1000
        self.conta_corrente = conta_corrente
        conta_corrente.cartoes.append(self) # adicionando o objeto cartão a conta corrente 'self'


# duas linhas ao final do último método
conta_Guilherme = ContaCorrente("Guilherme", "165.654.987-63", 1069, 32145)

cartao_Guilherme = CartaoCredito('Guilherme', conta_Guilherme)

print(cartao_Guilherme.conta_corrente._num_conta)

print(cartao_Guilherme.validade)

print(cartao_Guilherme.numero)

print(cartao_Guilherme.cod_seguranca)