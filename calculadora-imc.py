peso = float(input("Informe o seu peso em kg: "))
altura = float(input("Informe sua altura em metros: " ))

imc = peso / (altura*altura)

if (imc < 18.5):
    print("Abaixo do peso")
elif (imc < 25):
    print("Peso Normal")
elif(imc < 30):
    print("Sobrepeso")
elif(imc < 35):
    print("Obesidade grau 1")
elif(imc < 40):
    print("Obesidade grau 2")
else:
  print("Obesidade grau 3")