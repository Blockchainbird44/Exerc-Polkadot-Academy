programa 
{inclua biblioteca Matematica --> mat

  funcao inicio() {
    inteiro num1, num2, num3
    real media

    escreva("     C�lculo de M�dia       \n")
    escreva("----------------------------\n")
    escreva("Escreva o primeiro n�mero: ")
    leia (num1)
    escreva("Escreva o sedundo n�mero: ")
    leia (num2)
    escreva("Agora, escreva o terceiro n�mero: ")
    leia (num3)

    media = mat.arredondar(((num1+num2+num3)/3),2)

    escreva("A m�dia dos n�meros digitados �: ", media)
  }
}
