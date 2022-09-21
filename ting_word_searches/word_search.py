def exists_word(word, instance):
    exist = list()

    for i in instance.data:
        occurrences = list()

        for words, rows in enumerate(i['linhas_do_arquivo']):
            if word.lower() in rows.lower():
                occurrences.append({"linha": words + 1})

        if len(occurrences) > 0:
            exist.append(
                {
                    "palavra": word,
                    "arquivo": i['nome_do_arquivo'],
                    "ocorrencias": occurrences,
                }
            )

    return exist


def search_by_word(word, instance):
    exist = list()

    for i in instance.data:
        occurrences = list()

        for words, rows in enumerate(i['linhas_do_arquivo']):
            if word.lower() in rows.lower():
                occurrences.append(
                    {"linha": words + 1, "conteudo": rows}
                )

        if len(occurrences) > 0:
            exist.append(
                {
                    "palavra": word,
                    "arquivo": i['nome_do_arquivo'],
                    "ocorrencias": occurrences,
                }
            )

    return exist
