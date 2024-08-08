programa {
  funcao inicio() {
    inteiro num, fatorial = 1

    escreva("                 Descubra o fatorial                        \n")
    escreva("------------------------------------------------------------\n")

    faca{
      escreva("Digite um número maior que zero para o cálculo fatorial: ")
      leia (num)
    } enquanto (num < 1)
      

    para (inteiro i = 1; i <= num; i++){
      fatorial = fatorial * i

    }
    
    escreva("O resultado de ", num, "! é: ", fatorial )
  }
}
