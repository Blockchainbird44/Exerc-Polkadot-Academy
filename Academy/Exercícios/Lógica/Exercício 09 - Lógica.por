programa {
  funcao inicio() {
    inteiro num, fatorial = 1

    escreva("                 Descubra o fatorial                        \n")
    escreva("------------------------------------------------------------\n")

    faca{
      escreva("Digite um n�mero maior que zero para o c�lculo fatorial: ")
      leia (num)
    } enquanto (num < 1)
      

    para (inteiro i = 1; i <= num; i++){
      fatorial = fatorial * i

    }
    
    escreva("O resultado de ", num, "! �: ", fatorial )
  }
}
