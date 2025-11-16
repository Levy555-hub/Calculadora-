print("1- Somar dois valores")
print("2- Multiplicar dois valores")
print("3- dividir dois numeros")
print("4- Subtrair dois numeros")

opc = input(" Qual você precisa ?:")
 
if  opc == "1":
 n1 = float(input(" Primeiro valor:"))
 n2 = float(input(" Segundo valor:"))
 print(" O valor da soma é:", n1 + n2)
 
elif  opc == "2":
 n1 = float(input(" Primeiro valor"))
 n2 = float(input(" Segundo valor"))
 print("O valor da Multiplição é:", n1 * n2)

elif opc == "3":
 n1 = float(input(" Primeiro valor"))
 n2 = float(input("Segundo valor"))
 print(" O valor da Divisão é:", n1 // n2)
 
elif  opc  ==  "4": 
  n1 = float(input(" Primeiro valor"))
  n2 = float(input(" Segundo valor"))

else:
	print(" a opção que você escolheu não existe")