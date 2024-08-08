programa {
  funcao inicio() {
    inteiro num, contador = 0

    escreva("         CONTADOR DE POSITIVOS            \n")
    escreva("******************************************\n")

    para (inteiro i = 1; i <= 5; i++){

      escreva("Digite o ", i, "º número: ")
      leia (num)

      se (num > 0 ){

        contador++
      }
    }
    escreva ("Você digitou um total de ", contador, " números positivos.")
  }
}
