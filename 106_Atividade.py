print("Algoritimo que solicita uma data")

import re

nome_arquivo = "banco-temperaturas-julho.txt"

data_buscada = input("Digite a data (aaaa-mm-dd): ").strip()

temp_minima = float("inf")
temp_maxima = float("-inf")
encontrou_data = False

with open(nome_arquivo, "r", encoding="utf-8") as arquivo:
    for linha in arquivo:
        linha = linha.strip()

        if linha == "":
            continue

        partes = re.split(r"[;,\t]+|\s{2,}", linha)
        if len(partes) == 1:
            partes = linha.rsplit(" ", 1)

        if len(partes) >= 2:
            data_hora = partes[0].strip()
            valor_texto = partes[-1].strip().replace(",", ".")

            if data_hora.startswith(data_buscada):
                if valor_texto.replace(".", "", 1).replace("-", "", 1).isdigit():
                    temp = float(valor_texto)
                    encontrou_data = True

                    if temp < temp_minima:
                        temp_minima = temp

                    if temp > temp_maxima:
                        temp_maxima = temp

print()
if encontrou_data:
    amplitude = temp_maxima - temp_minima
    print(f"Data analisada: {data_buscada}")
    print(f"Temperatura mínima: {temp_minima:.2f}")
    print(f"Temperatura máxima: {temp_maxima:.2f}")
    print(f"Amplitude térmica: {amplitude:.2f}")
else:
    print(f"A data {data_buscada} não foi encontrada no arquivo.")