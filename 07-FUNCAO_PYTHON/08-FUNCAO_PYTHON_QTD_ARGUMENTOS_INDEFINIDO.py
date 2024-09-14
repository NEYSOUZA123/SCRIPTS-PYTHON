# Quantidade Indefinidas de Argumentos

### Utilidade:

# Quando você quer permitir uma quantidade indefinida de argumentos, usa o * para isso.

### Estrutura:

def minha_soma(*numeros):
    print(numeros)
    soma = 0
    for numero in numeros:
        soma += numero
        return soma
    
print(minha_soma(10*50*30+90+58)) 



# --------------------------------Exemplo 02----------------------------------------------------


# Define uma função chamada preco_final que recebe um preço inicial e quaisquer argumentos adicionais utilizando **adicionais.
def preco_final(preco, **adicionais):
    # Exibe o dicionário contendo os argumentos adicionais passados para a função.
    print(adicionais)
    
    # Verifica se o argumento 'desconto' foi passado.
    if 'desconto' in adicionais:
        # Aplica o desconto ao preço inicial.
        preco *= (1 - adicionais['desconto'])
        
        # Verifica se o argumento 'garantia_extra' foi passado.
        if 'garantia_extra' in adicionais:
            # Adiciona o custo da garantia extra ao preço.
            preco += adicionais['garantia_extra']
            
            # Verifica se o argumento 'imposto' foi passado.
            if 'imposto' in adicionais: 
                # Aplica o imposto ao preço final.
                preco *= (1 + adicionais['imposto'])
                
                # Retorna o preço final após aplicar desconto, garantia extra, e imposto.
                return preco

# Chama a função preco_final com um preço inicial de 900, um desconto de 10%, uma garantia extra de 100, e um imposto de 30%.
print(preco_final(900, desconto=0.1, garantia_extra=100, imposto=0.3))
