def study_schedule(start_time=[], end_time=[], target_time=[]):
    # qual o melhor horário para disponibilizar os conteúdos?
    # Quando o contador retornado pela função for o maior.
    contador = 0

    # no caso de os arrays estarem vazios:
    if not target_time or not start_time or not end_time:
        return contador

    # percorrer os arrays para somar quantas vezes o valor pretendido (target_time)
    # aparece e assim pode ser contado += 1

    # para cada elemento (indice) no tamanho array de saída (end_time - quantas vezes)
    for indice in range(len(end_time)):
        if start_time[indice] <= target_time <= end_time[indice]:
            contador += 1
            print(
                f"contador na volta {indice}: {contador}, quem é o target: {target_time}"
            )

    print(f"array entrada: {start_time} e array saida: {end_time}")
    print(f"contador fora do loop? {contador}")
    return contador
