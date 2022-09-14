from ContasBancos import ContaCorrente, CartaoCredito

# duas linhas ao final do último método
conta_Guilherme = ContaCorrente("Guilherme", "165.654.987-63", 1069, 32145)

cartao_Guilherme = CartaoCredito('Guilherme', conta_Guilherme)

print(vars(conta_Guilherme))
print(conta_Guilherme.__dict__)