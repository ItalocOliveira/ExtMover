import os
from time import sleep


def loading(qnt, delay):
    for _ in range(qnt):
        print(".", end="", flush=True)
        sleep(delay)
    print("")

def verifyPath(message):
    while True:
        caminho_input = input(message)

        if not caminho_input.strip():
            print("❌ Invalid path: Null. Try again.\n")
            continue

        caminho_normalizado = os.path.normpath(caminho_input)

        if not caminho_input.strip():
            print("❌ Invalid path: Null. Try again.\n")
            continue
        if not os.path.exists(caminho_normalizado):
            print(f"❌ Invalid path: Non-existent path '{caminho_normalizado}' . Verify and try again.\n")
            continue
        if not os.path.isdir(caminho_normalizado):
            print(f"❌ Invalid path: Path '{caminho_normalizado}' it's not a directory. Type a directory path.\n")
            continue

        return caminho_normalizado

def undo(files):
    print("\nUndoing latest operation", end="")
    loading(3, 0.3)

    for action in reversed(files):
        action_type, action_origin, action_destination = action

        try:
            if action_type == 'move':
                os.rename(action_destination, action_origin)

            if action_type == 'copy':
                if os.path.exists(action_destination):
                    os.remove(action_destination)
        except (FileNotFoundError, PermissionError, OSError) as error:
            print(f"\n❌ Error occurred trying to undo operation: {error}")
