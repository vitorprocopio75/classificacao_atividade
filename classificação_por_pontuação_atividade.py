# Programa para classificar o nível de inteligência artificial com base na pontuação

# Solicita o nome do sistema de IA
nome_ia = input("Informe o nome do sistema de IA: ")

# Solicita a pontuação de performance
try:
    pontuacao = float(input(f"Qual a pontuação de performance de {nome_ia}? (0 a 100): "))
    
    # Valida a pontuação
    if pontuacao < 0:
        print("Erro: Pontuação inválida! ❌")
    elif pontuacao > 100:
        print("Erro: IA fora da escala! ⚠️")
    else:
        # Classificação baseada na pontuação
        if pontuacao < 40:
            classificacao = "IA em Treinamento 🍼"
            mensagem_recompensa = "🔁 Continue alimentando os dados para melhorar a performance."
        elif 40 <= pontuacao <= 69.9:
            classificacao = "IA Intermediária 🧠"
            mensagem_recompensa = ""
        elif 70 <= pontuacao <= 89.9:
            classificacao = "IA Otimizada 🚀"
            mensagem_recompensa = ""
        else:
            classificacao = "IA Avançada (nível Skynet) 🤯"
            mensagem_recompensa = "⚡ Iniciando protocolo de expansão neural..."
        
        # Exibe o resultado formatado
        print(f"\nSistema: {nome_ia}")
        print(f"Pontuação: {pontuacao:.1f}")
        print(f"Classificação: {classificacao}")
        
        if mensagem_recompensa:
            print(mensagem_recompensa)

except ValueError:
    print("Erro: Pontuação inválida! ❌ Digite um número válido.")
