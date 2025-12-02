from getapi import consultar_filme

if __name__ == "__main__":
    nome = input("Digite o nome do filme: ")
    resultado = consultar_filme(nome)
    
    if "erro" in resultado:
        print(f"ERRO: {resultado['erro']}")
    else:
        print(f"Titulo: {resultado['titulo']}")
        print(f"Ano: {resultado['ano']}")
        print(f"Sinopse: {resultado['sinopse']}")
