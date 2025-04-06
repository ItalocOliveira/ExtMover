import os
from colorama import Fore, Back, Style
from time import sleep


def loading(qnt, delay):
    for _ in range(qnt):
        print(".", end="", flush=True)
        sleep(delay)
    print("")

print(Style.RESET_ALL)
print(Fore.RED)
print(Back.BLACK + "ATENÇÃO:")
print("TENHA CERTEZA DE DIGITAR O CAMINHO DE DESTINO E O TIPO DE ARQUIVO CORRETAMENTE(INCLUI-SE PONTUAÇÕES COMO: .TXT .JPEG .MP3...)")
print(Style.RESET_ALL)

# Obtendo caminho de origem e destino
caminho_original = os.path.normpath(str(input("Digite o caminho da pasta em que o programa buscará arquivos: ")))
caminho_destino = str(input("Digite o caminho de destino para onde irão os arquivos: "))
extensao_procurada = str(input("Digite a extensão do arquivo que gostaria que o programa rastreasse: ")).lower()

# Percorrendo recursivamente os diretórios e arquivos a partir do caminho especificado pelo usuário
loading(3, 0.5)
for pasta_atual, _, arquivos in os.walk(caminho_original):
    sleep(0.4)
    print("")
    print(f"Pasta da vez: {pasta_atual}")
    print(f"Arquivos contidos: {arquivos}")
    print("")

    # Verifica se há pelo menos 1 arquivo com a extensão desejada na pasta_atual
    existe_arquivo = any(arquivo.endswith(extensao_procurada) for arquivo in arquivos)
    if not existe_arquivo:
        continue

    for arquivo in arquivos:
        if arquivo.endswith(f"{extensao_procurada}"):
            print(f"Lendo: {arquivo}", end="")

            # Verificando se o nome do arquivo já existe no destino
            destino_arquivo_da_vez = os.path.join(caminho_destino, arquivo)
            if os.path.exists(destino_arquivo_da_vez):
                print(f"\n⚠️  Arquivo '{arquivo}' já existe no destino. Pulando...\n")
                continue

            # Verificando se foi possível mover o arquivo
            try:
                origem= os.path.join(pasta_atual, arquivo)
                destino = os.path.join(caminho_destino, arquivo)
                os.rename(origem, destino)
                print("")
                print(f"Tranferindo: {arquivo}...", end="")
            except (FileNotFoundError, PermissionError, OSError) as error:
                print(f"\n❌ Erro ao mover o arquivo '{arquivo}': {error}")







