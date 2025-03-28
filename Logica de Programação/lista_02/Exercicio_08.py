valor_compra = float(input("Digite o valor total da compra: "))
opcao_pagamento = input("Escolha a forma de pagamento (à vista, 3 parcelas, 5 parcelas, 10 parcelas): ")

if opcao_pagamento.lower() == 'à vista':
    valor_final = valor_compra * 0.95
    print(f"Pagamento à vista - Valor total: R${valor_final:.2f}")
elif opcao_pagamento == '3 parcelas':
    valor_final = valor_compra
    print(f"Pagamento em 3 parcelas - Valor total: R${valor_final:.2f} | Valor da parcela: R${valor_final/3:.2f}")
elif opcao_pagamento == '5 parcelas':
    valor_final = valor_compra * 1.02
    print(f"Pagamento em 5 parcelas - Valor total: R${valor_final:.2f} | Valor da parcela: R${valor_final/5:.2f}")
elif opcao_pagamento == '10 parcelas':
    valor_final = valor_compra * 1.08
    print(f"Pagamento em 10 parcelas - Valor total: R${valor_final:.2f} | Valor da parcela: R${valor_final/10:.2f}")
else:
    print("Opção de pagamento inválida. Por favor, escolha entre 'à vista', '3 parcelas', '5 parcelas' ou '10 parcelas'.")