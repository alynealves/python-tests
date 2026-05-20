total_creditos = 0.0
total_debitos = 0.0
linhas_com_erro = 0

# Abrindo o arquivo de entrada
with open('exemplo-1_entrada.csv', 'r', encoding='utf-8') as arquivo:
    
    # Ignora o cabeçalho
    next(arquivo)

    # Percorre cada linha do arquivo
    for linha in arquivo:
        try:
            # Remove espaços/quebra de linha e separa os dados
            dados = linha.strip().split(';')

            # Pegando as informações da linha
            data = dados[0]
            descricao = dados[1]
            valor = float(dados[2])  # Pode gerar ValueError
            tipo = dados[3]

            # Soma os valores conforme o tipo
            if tipo == 'C':
                total_creditos += valor
            elif tipo == 'D':
                total_debitos += valor

        except ValueError:
            # Conta erro se não conseguir converter para float
            linhas_com_erro += 1

# Calcula o saldo final
saldo_final = total_creditos - total_debitos

# Cria o relatório
with open('relatorio_financeiro.txt', 'w', encoding='utf-8') as relatorio:
    relatorio.write(f'Total de receitas: {total_creditos:.2f}\n')
    relatorio.write(f'Total de despesas: {total_debitos:.2f}\n')
    relatorio.write(f'Saldo final: {saldo_final:.2f}\n')
    relatorio.write(f'Linhas com falha: {linhas_com_erro}\n')