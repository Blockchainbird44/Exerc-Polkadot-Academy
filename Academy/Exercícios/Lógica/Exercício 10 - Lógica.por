programa {
  funcao inicio() {
    inteiro num, contador = 0

    escreva("         CONTADOR DE POSITIVOS            \n")
    escreva("******************************************\n")

    para (inteiro i = 1; i <= 5; i++){

      escreva("Digite o ", i, "� n�mero: ")
      leia (num)

      se (num > 0 ){

        contador++
      }
    }
    escreva ("Voc� digitou um total de ", contador, " n�meros positivos.")
  }
}
