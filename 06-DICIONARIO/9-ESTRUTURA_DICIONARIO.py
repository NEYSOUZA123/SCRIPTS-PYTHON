# Set

# Estrutura:

# meu_set = {valor,valor,valor}

# Observação

# Não pode ter valores duplicados
# Não tem ordem fixa

set_produtos = {'arroz', 'feijao', 'macarrao', 'atum', 'azeite'}

print(set_produtos)

# Aplicação Bem Util:
# 1 quantidade de clientes que estiveram na loja


cpf_clientes = {'078.355.605.50', '394.284.605.59', '378.805.605.20', '998.650.980.30','078.355.605.50'}

se_cpf_cliente = set(cpf_clientes)
print(len(se_cpf_cliente))
