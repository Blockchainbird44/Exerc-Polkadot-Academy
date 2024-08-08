programa 
{inclua biblioteca Matematica --> mat

  funcao inicio() {
    inteiro num1, num2, num3
    real media

    escreva("     Cálculo de Média       \n")
    escreva("----------------------------\n")
    escreva("Escreva o primeiro número: ")
    leia (num1)
    escreva("Escreva o sedundo número: ")
    leia (num2)
    escreva("Agora, escreva o terceiro número: ")
    leia (num3)

    media = mat.arredondar(((num1+num2+num3)/3),2)

    escreva("A média dos números digitados é: ", media)
  }
}
