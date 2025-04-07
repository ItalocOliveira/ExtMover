# 🗃️ Buscador e Movimentador de Arquivos

Este script em Python tem como objetivo buscar, de forma recursiva, arquivos com uma extensão específica dentro de um diretório informado pelo usuário, e transferi-los para um outro diretório de destino.

---

## 🚀 Funcionalidade

- O usuário informa:
  - O **caminho da pasta de origem** (onde os arquivos serão buscados).
  - O **caminho da pasta de destino** (onde os arquivos serão movidos).
  - A **extensão dos arquivos desejados** (ex: `.txt`, `.jpg`, `.mp3`, etc).

- O script:
  - Percorre todas as subpastas do diretório de origem.
  - Identifica arquivos que possuem a extensão informada.
  - Move esses arquivos para o diretório de destino.
  - **Evita sobrescrever** arquivos já existentes no destino.
  - Apresenta mensagens de status amigáveis durante a execução.

---

## 🧠 Tecnologias e Bibliotecas

- **Python 3.x**
- [`os`](https://docs.python.org/3/library/os.html) — para manipulação de caminhos e arquivos.
- [`colorama`](https://pypi.org/project/colorama/) — para estilização do terminal.
- [`time`](https://docs.python.org/3/library/time.html) — para simulação de carregamento e delays.

---

## 💻 Como utilizar

1. Instale as dependências (caso não tenha o `colorama`):
   ```bash
   pip install colorama

---

## 📑 Explicação detalhada do código

A explicação técnica detalhada de cada função está disponível [neste PDF](docs/explicacao_detalhada.pdf). Caso prefira uma leitura rápida, veja abaixo os principais pontos:

- ### Função loading(qnt, delay)
    - Exibe um "loading" simples com `.` repetidos.
    - `qnt`: número de pontos a exibir.
    - `delay`: tempo de espera entre cada ponto.
