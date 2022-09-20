import sys


def txt_importer(path_file):
    if not path_file.endswith(".txt"):
        print("Formato inválido", file=sys.stderr)

    try:
        with open(path_file, mode="r") as file:
            reading = file.read()
            return reading.splitlines()
    except Exception:
        print(f"Arquivo {path_file} não encontrado", file=sys.stderr)
