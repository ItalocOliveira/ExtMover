# 🗃️ Buscador e Movimentador de Arquivos

Este script em Python tem como objetivo buscar, de forma recursiva, arquivos com uma extensão específica dentro de um diretório informado pelo usuário, e transferi-los para um outro diretório de destino, **com a opção de mover ou copiar os arquivos**.

---

## 🚀 Funcionalidade

- O usuário informa:
  - O **caminho da pasta de origem** (onde os arquivos serão buscados).
  - O **caminho da pasta de destino** (onde os arquivos serão transferidos).
  - A **extensão dos arquivos desejados** (ex: `.txt`, `.jpg`, `.mp3`, etc).
  - Se deseja **mover** (`0`) ou **copiar** (`1`) os arquivos.

- O script:
  - Percorre todas as subpastas do diretório de origem.
  - Identifica arquivos com a extensão informada.
  - **Move** ou **copia** os arquivos para o destino conforme a escolha do usuário.
  - **Evita sobrescrever** arquivos já existentes no destino.
  - Exibe mensagens informativas sobre o progresso da execução.

---

## 🧠 Tecnologias e Bibliotecas

- **Python 3.x**
- [`os`](https://docs.python.org/3/library/os.html) — manipulação de diretórios e arquivos.
- [`shutil`](https://docs.python.org/3/library/shutil.html) — para cópia de arquivos com metadados.
- [`colorama`](https://pypi.org/project/colorama/) — estilização colorida no terminal.
- [`time`](https://docs.python.org/3/library/time.html) — delays e carregamento.

---

## 💻 Como utilizar

1. Instale a biblioteca `colorama` (caso ainda não tenha):
   ```bash
   pip install colorama


## 📑 Explicação detalhada do código

A explicação técnica detalhada de cada função está disponível [neste PDF](docs/explicacao_detalhada.pdf). Caso prefira uma leitura rápida, veja abaixo os principais pontos:

- ### Função loading(qnt, delay)
    - Exibe um "loading" simples com `.` repetidos.
    - `qnt`: número de pontos a exibir.
    - `delay`: tempo de espera entre cada ponto.
