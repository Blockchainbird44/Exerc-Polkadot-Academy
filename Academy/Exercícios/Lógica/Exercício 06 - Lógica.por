programa {
  funcao inicio() {
    inteiro num

    escreva("   ***   TABUADA   ***    \n")

    escreva("Insira o n�mero para o qual deseja a tabuada: ")
    leia (num)
    
    escreva("O resultado �: \n")

    para (inteiro  i= 1; i<=10; i++){
      escreva(num, " x ", i, " = ", num * i, "\n")
    }

  }
}
