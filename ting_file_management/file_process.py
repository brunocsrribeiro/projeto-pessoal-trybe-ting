import sys
from ting_file_management.file_management import txt_importer


def process(path_file, instance):
    for file in instance.data:
        if file["nome_do_arquivo"] is path_file:
            return None

    output_structure = {
        "nome_do_arquivo": path_file,
        "qtd_linhas": len(txt_importer(path_file)),
        "linhas_do_arquivo": txt_importer(path_file)
    }

    instance.enqueue(output_structure)
    print(output_structure, file=sys.stdout)


def remove(instance):
    if not instance:
        return print("Não há elementos", file=sys.stdout)

    first_file_remove = instance.dequeue()
    print(
        f"Arquivo {first_file_remove['nome_do_arquivo']} removido com sucesso",
        file=sys.stdout
    )


def file_metadata(instance, position):
    try:
        print(instance.search(position), file=sys.stdout)
    except IndexError:
        print("Posição inválida", file=sys.stderr)
