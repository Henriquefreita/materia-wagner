def contar_fruta():
    frutas = ["maçã", "banana", "laranja", "uva", "manga", "abacaxi", "morango", "kiwi", "melancia", "pêssego"]
    fruta_usuario = input("Digite o nome de uma fruta: ")
    contagem = frutas.count(fruta_usuario)
    print(f"A fruta '{fruta_usuario}' aparece {contagem} vez(es) na lista.")
contar_fruta()
