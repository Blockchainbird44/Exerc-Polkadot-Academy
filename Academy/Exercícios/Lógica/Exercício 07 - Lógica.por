programa {
  funcao inicio() {
    inteiro num

    escreva("------------------------------------------------------\n")
    escreva("                Contagem Regressiva               \n")
    escreva("------------------------------------------------------\n")
    escreva("Digite um número para iniciar a contagem regressiva: ")
    leia (num)

    escreva("> Iniciando a contagem...\n")
    para (inteiro i = num; i >= 0; i--){
      escreva (i, "\n")
    }
    escreva("Contagem regressiva completa!")
  }
}
