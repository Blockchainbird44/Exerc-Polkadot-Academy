programa {
  funcao inicio() {
    inteiro num

    escreva("   ***   TABUADA   ***    \n")

    escreva("Insira o número para o qual deseja a tabuada: ")
    leia (num)
    
    escreva("O resultado é: \n")

    para (inteiro  i= 1; i<=10; i++){
      escreva(num, " x ", i, " = ", num * i, "\n")
    }

  }
}
