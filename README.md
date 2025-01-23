#Einfo2024

Projeto desenvolvido durante o evento Einfo na Facape.

## Descrição

Este projeto tem como objetivo colocar em prática a criação de um ambiente utilizando Terraform no Google Cloud. O código está organizado em diferentes arquivos e diretórios para facilitar a manutenção e a escalabilidade.

## Estrutura do Projeto

- `.github/workflows/`: Contém o arquivo de configuração de workflows para integração contínua.
- `templates/`: Contém os templates utilizados no projeto.
- `Dockerfile`: Arquivo de configuração para containerização do projeto.
- `README.md`: Este arquivo README.
- `cloudbuild.yaml`: Arquivo de configuração para construção do ambiente na nuvem.
- `main.py`: Arquivo principal contendo a lógica do projeto.
- `requirements.txt`: Lista de dependências do projeto.
- `test_app.py`: Arquivo de testes unitários.

## Como rodar o projeto

1. Clone este repositório:
    ```sh
    git clone https://github.com/seu-usuario/jujubamundo.git
    ```

2. Navegue até o diretório do projeto:
    ```sh
    cd jujubamundo
    ```

3. Crie um ambiente virtual e ative-o:
    ```sh
    python3 -m venv venv
    source venv/bin/activate  # No Windows use `venv\Scripts\activate`
    ```

4. Instale as dependências:
    ```sh
    pip install -r requirements.txt
    ```

5. Execute o projeto:
    ```sh
    python main.py
    ```

## Testes

Para rodar os testes unitários, execute o seguinte comando:
```sh
pytest test_app.py
