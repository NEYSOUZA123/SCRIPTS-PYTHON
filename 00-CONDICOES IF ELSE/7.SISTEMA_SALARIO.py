# Calcular Salario funcionario

valor_horasteclado = int(input('Qual o valor da hora'))

salario_horas = int(input('Quantidade de Horas Trabalhada:'))

valor_hora = salario_horas * valor_horasteclado



inss = valor_hora * 0.10

fgts = valor_hora * 0.11

if valor_hora <= 900:
    desconto_ir = valor_hora * 0.00
    salario = valor_hora- inss - desconto_ir
    desconto_ir = int (desconto_ir)
    print('Nao ha desconto de imposto de renda, seu salario esta abaixo do teto. Salario a receber: R${:.2f}\n'
          'DESCONTOS - INSS: R${:.2f} reais, FGTS: R${:.2f},Imposto de renda isento. '.format(salario, inss, fgts))
elif valor_hora <= 1100:
    desconto_ir = valor_hora * 0.05
    salario = valor_hora - inss - desconto_ir
    desconto_ir = int (desconto_ir)
    print('Salario a receber: R${:.2f}\n'
          'DESCONTOS - INSS: R${:.2f} reais, FGTS: R${:.2f},Imposto de renda sobre 5%. desconto imposto de renda R${}. '.format(salario, inss, fgts,desconto_ir))

elif valor_hora <= 2500:
    desconto_ir = valor_hora * 0.10
    salario = valor_hora - inss - desconto_ir
    desconto_ir = int(desconto_ir)
    print('Salario a receber: R${:.2f}\n'
          'DESCONTOS - INSS: R${:.2f} reais, FGTS: R${:.2f},Imposto de renda sobre 10%. desconto imposto de renda R${}. '.format(
        salario, inss, fgts, desconto_ir))
elif valor_hora > 2500:
    desconto_ir = valor_hora * 0.20
    salario = valor_hora - inss - desconto_ir
    desconto_ir = int(desconto_ir)
    print('Salario a receber: R${:.2f}\n'
          'DESCONTOS - INSS: R${:.2f} reais, FGTS: R${:.2f},Imposto de renda sobre 20%. desconto imposto de renda R${}. '.format(
        salario, inss, fgts, desconto_ir))














