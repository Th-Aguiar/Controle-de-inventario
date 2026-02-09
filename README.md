# 📦 Sistema de Controle de Inventário

Este é um aplicativo desktop moderno desenvolvido em **Python** para o gerenciamento eficiente de itens e ativos. Ele permite o controle completo de um inventário, desde o cadastro até o acompanhamento financeiro dos itens.



## 🛠️ Tecnologias Utilizadas

- **Linguagem:** Python 3.x
- **Interface Gráfica:** Tkinter (Customizado com temas `ttk`)
- **Banco de Dados:** SQLite3 (Persistência local)
- **Bibliotecas Auxiliares:**
  - `Pillow`: Para manipulação e exibição da logo.
  - `tkcalendar`: Para seleção de datas intuitiva.
  - `os`: Para gerenciamento de caminhos e diretórios.

## ✨ Funcionalidades

- **CRUD Completo:**
  - **Inserir:** Adiciona novos itens com detalhes como localização, descrição, marca e valor.
  - **Visualizar:** Tabela dinâmica que lista todos os itens cadastrados.
  - **Atualizar:** Permite carregar dados de um item selecionado para edição rápida.
  - **Deletar:** Remove itens do sistema com confirmação de segurança.
- **Dashboard Financeiro:** Cálculo automático do valor total acumulado no inventário e contagem de itens em tempo real.
- **Interface Responsiva:** Tabela (Treeview) que se ajusta ao tamanho da janela.

## 🚀 Como Executar o Projeto

### 1. Pré-requisitos
Certifique-se de ter o Python instalado. Instale as dependências necessárias via terminal:

```bash
pip install pillow tkcalendar

/meu-projeto
├── assets/
│   └── logo.png
├── main.py
└── view.py

python main.py

### Dicas Extras para o Portfólio:

1.  **Imagens:** O GitHub renderiza imagens no README. Tire um print da sua aplicação funcionando e coloque-o na pasta do projeto. No README, você pode referenciá-lo com `![App Screenshot](screenshot.png)`.
2.  **Requirements.txt:** É uma boa prática criar este arquivo. No terminal, digite:
    `pip freeze > requirements.txt`
    Isso permitirá que outros instalem tudo com `pip install -r requirements.txt`.
3.  **Refatoração Futura:** Se quiser impressionar ainda mais, futuramente você pode aplicar **Programação Orientada a Objetos (POO)** no `main.py`, transformando a janela em uma classe. Isso mostra que você entende padrões de projeto avançados.

**Deseja que eu te ajude a criar o arquivo `requirements.txt` ou prefere uma sugestão de como organizar as pastas para o primeiro "Push" no GitHub?**

```
## Desenvolvido por THIAGO DE OLIVEIRA AGUIAR
