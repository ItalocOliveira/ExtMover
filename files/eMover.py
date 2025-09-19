import os
import shutil
from colorama import Fore, Back, Style
from time import sleep

from functions.index import loading, verifyPath, undo

executing: bool = True

print('\n')
print('Welcome to ExtMover.')
print('This script was created to make it easier to move, copy, and sort a large number of files on your computer, avoiding duplicates.')

# Aviso de precaução
print(Fore.RED)
print(Back.BLACK + "ATTENTION!")
print("MAKE SURE TO TYPE THE CORRECT BOTH ORIGIN AND DESTINATION PATH.\nTHE SAME GOES TO EXTENSION TYPES(.TXT .JPEG .MP3...)")
print(Style.RESET_ALL)

while (executing):

    arquivos_processados = []

    # Obtendo caminho de origem e destino
    caminho_origem = verifyPath("Type the ORIGIN files path: ")
    caminho_destino = verifyPath("Type the DESTINATION path: ")
    extensao_procurada = str(input("Type the file's extension type you want to move or copy: ")).lower()

    print(Fore.YELLOW)
    print("\n--- Defined paths ---")
    print(f"Origin: {caminho_origem}")
    print(f"Destination: {caminho_destino}")
    print(f"Extension: {extensao_procurada}")
    print("---------------------\n")
    print(Style.RESET_ALL)

    while(True):
        try:
            moveOrCopy = int(input("[0] Move files to destination\n[1] Copy files to destination\n"))

            if moveOrCopy in [0, 1]:
                if moveOrCopy == 1:
                    moveOrCopy == True
                else:
                    moveOrCopy == False
                break
            else:
                print("❌ Invalid option. Try again...\n")
        except ValueError:
            print("❌ Invalid value. Try again...\n")

    print("Working on it", end="")
    loading(3, 0.5)

    arquivos_processados_contagem = 0

    # Percorrendo recursivamente os diretórios e arquivos a partir do caminho de origem
    for pasta_atual, _, arquivos in os.walk(caminho_origem):
        sleep(0.4)
        print(f"📂 Current directory: {pasta_atual}")
        print(f"📃 Files contained: {arquivos}")

        # Verifica se há pelo menos 1 arquivo com a extensão desejada na pasta_atual
        existe_arquivo = any(arquivo.endswith(extensao_procurada) for arquivo in arquivos)
        if not existe_arquivo:
            continue

        for arquivo in arquivos:
            if arquivo.lower().endswith(f"{extensao_procurada}"):

                origem = os.path.join(pasta_atual, arquivo)
                destino = os.path.join(caminho_destino, arquivo)

                # Verificando se o nome do arquivo já existe no destino
                if os.path.exists(destino):
                    print(f"❗The file '{arquivo}' already exists on destiny. Skiping...")
                    continue

                # Ação de mover
                if not moveOrCopy:
                    try:
                        os.rename(origem, destino)
                        arquivos_processados.append(("move", origem, destino))
                        arquivos_processados_contagem += 1
                        print(f"🔧 Transferring: {arquivo}...")
                    except (FileNotFoundError, PermissionError, OSError) as error:
                        print(f"\n❌ Error trying to transfer '{arquivo}': {error}")

                # Ação de copiar
                if moveOrCopy:
                    try:
                        shutil.copy2(origem, destino)
                        arquivos_processados.append(("copy", origem, destino))
                        arquivos_processados_contagem += 1
                        print(f"©️ Copying: {arquivo}...\n", end="")
                    except (FileNotFoundError, PermissionError, OSError) as error:
                        print(f"\n❌ Error trying to copy '{arquivo}': {error}")

    if arquivos_processados_contagem == 0:
        print("\nNo files with the specified extension were found to be processed.")
    else:
        print(f"\n✅ Process completed! {arquivos_processados} files processed.")

        while(True):
            try:
                desfazer = int(input("\nUndo latest operation?\n[0] Yes\n[1] No\n"))

                if desfazer in [0, 1]:
                    if desfazer == 1:
                        break
                    else:
                        undo(arquivos_processados)
                        break
                else:
                    print("❌ Opção inválida. Tente novamente...\n")
            except ValueError:
                print("❌ Valor inválido. Tente novamente...\n")

    print("")
    while(True):
        try:
            choice = int(input('Move another file type?\n[0] Yes\n[1] No\n'))

            if choice in [0, 1]:
                if choice == 1:
                    executing = False
                break
            else:
                print("❌ Invalid option. Try again...\n")
        except ValueError:
            print("❌ Invalid value. Try again...\n")

print("\nThanks for using ExtMover! See ya next time...")
sleep(1)






