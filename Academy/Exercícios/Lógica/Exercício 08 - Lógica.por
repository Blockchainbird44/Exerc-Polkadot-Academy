programa {
  funcao inicio() {
    inteiro ano

  escreva("-----------------------------------------\n")
  escreva("             É ano bissexto?              \n")
  escreva("-----------------------------------------\n")

  escreva("Digite o ano para saber se é bissexto: ")
  leia(ano)

  se (ano % 4 ==0) {
        se (ano % 400 == 0){
          se (ano % 100 != 0){
          }
        }
        escreva("Legal, este ano é bissexto!")
  }senao {
        escreva ("Este ano não é bissexto!")
  }
  }
}
