import re

nome_arquivo = "banco-temperaturas-julho.txt"

temperaturas = []
temp_minima = float("inf")
temp_maxima = float("-inf")
primeiro_registro_minima = None

contador = 0

with open(nome_arquivo, "r", encoding="utf-8") as arquivo:
    for linha in arquivo:
        contador += 1
        linha = linha.strip()

        if linha == "":
            continue

        # Separa a linha por ';', ',' ou espaços
        partes = re.split(r"[;,\t]+|\s{2,}", linha)
        if len(partes) == 1:
            partes = linha.rsplit(" ", 1)

        if len(partes) >= 2:
            data_hora = partes[0].strip()
            valor_texto = partes[-1].strip().replace(",", ".")

            # Verifica se é um número válido (ignora cabeçalho, se houver)
            if valor_texto.replace(".", "", 1).replace("-", "", 1).isdigit():
                temp = float(valor_texto)
                temperaturas.append(temp)

                if temp > temp_maxima:
                    temp_maxima = temp

                if temp < temp_minima:
                    temp_minima = temp
                    primeiro_registro_minima = data_hora

media = sum(temperaturas) / len(temperaturas)

print()
print(f"Total de linhas: {contador}")
print(f"Média das temperaturas: {media:.2f}")
print(f"Temperatura mínima: {temp_minima}")
print(f"Temperatura máxima: {temp_maxima}")
print(f"Primeiro registro da mínima: {primeiro_registro_minima}")