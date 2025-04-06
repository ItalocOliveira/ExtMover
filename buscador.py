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
print("TENHA CERTEZA DE DIGITAR O CAMINHO DE DESTINO E O TIPO DE ARQUIVO CORRETAMENTE(INCLUI-SE PONTUAÇÕES COMO: .TXT .JPEG)")
print(Style.RESET_ALL)

caminho_inicio = str(input("Digite o caminho de início que o programa lerá: ")).replace("\\", "//")
caminho_destino = str(input("Digite o caminho de destino em que o programa trabalhará: "))
extensao_procurada = str(input("Digite a extensão do arquivo que gostaria que o programa rastreasse: "))

for rota, _, arquivos in os.walk(caminho_inicio):
    sleep(0.4)
    print("")
    print(f"Pasta da vez: {rota}")
    print(f"Arquivos contidos: {arquivos}")
    print("")

    for arquivo in arquivos:
        if arquivo.endswith(f"{extensao_procurada}"):
            print(f"Lendo: {arquivo}", end="")
            # loading(3, 0.2)

            print(f"Tranferindo: {arquivo}", end="")
            # loading(3, 0.2)

            os.rename(f"{rota}//{arquivo}", f"{caminho_destino}//{arquivo}")
            print("")  