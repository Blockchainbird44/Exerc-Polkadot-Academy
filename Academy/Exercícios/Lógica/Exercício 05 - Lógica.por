programa {
  funcao inicio() {
    real temp, fahr

    escreva("      Conversor de Temperatua      \n")
    escreva("-------------------------------------\n")

    escreva("Informe a temperatura em °C: ")
    leia (temp)

    fahr = (temp * 1.8)+32
    escreva("A temperatura convertida em Fahrenheit é: ", fahr, "°F")

  }
}
