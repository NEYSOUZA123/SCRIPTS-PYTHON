 #Exercícios

# Para fazer um treino simples antes de avançarmos em mais functions, vamos criar uma function que resolve 1 "desafio
# simples"

## 1.Function para Cálculo de Carga Tributária

# (Lembrando, não se atente ao funcionamento real da carga tributária, é apenas um exemplo imaginário para treinarmos
# as functions com algo mais prático)

# Imagine que você trabalha no setor contábil de uma grande empresa de Varejo.

# Crie uma function que calcule qual o % de carga tributária que está sendo aplicado sobre um determinado produto,
# dado o preço de venda, o "lucro" e os custos (com exceção do imposto) dele.

preco = 1500
custo = 400
lucro = 785


def cargar_tributario(precoa, custob, lucroc):
    imposto = precoa - custob - lucroc
    carga = imposto / precoa
    return carga


carga_calculada = cargar_tributario(preco, custo, lucro)
print('A carga tributaria foi {:.1%} '.format(carga_calculada))



