print("Programa de Investimentos")

meta_fundo = float(input("Qual a Meta do Fundo"))

rendimentos = float(input("Qual o Rendimento do fundo"))

if rendimentos > meta_fundo:
   if rendimentos > 0.20:
      taxa = 0.04
      print("Sua taxa e igual a {}%".format(taxa))
   else:
      taxa = 0.02
      print("Sua taxa e igua a {}%".format(taxa))

else:
    taxa = 0
    print("A taxa e igua a {}%".format(taxa))



