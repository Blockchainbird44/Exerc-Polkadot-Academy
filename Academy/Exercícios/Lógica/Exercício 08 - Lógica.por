programa {
  funcao inicio() {
    inteiro ano

  escreva("-----------------------------------------\n")
  escreva("             � ano bissexto?              \n")
  escreva("-----------------------------------------\n")

  escreva("Digite o ano para saber se � bissexto: ")
  leia(ano)

  se (ano % 4 ==0) {
        se (ano % 400 == 0){
          se (ano % 100 != 0){
          }
        }
        escreva("Legal, este ano � bissexto!")
  }senao {
        escreva ("Este ano n�o � bissexto!")
  }
  }
}
