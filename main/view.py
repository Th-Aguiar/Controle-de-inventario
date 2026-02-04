import sqlite3 as lite
import os
#----------CONFIGURAÇÃO--------------
#Obtendo o diretorio para evitar erros no programa
diretorioAtual = os.path.dirname(os.path.abspath(__file__))
caminhoBanco = os.path.join(diretorioAtual, 'dados.db')

def criarConexao():
    #cria e retorna uma conexao com o banco de dados
    con = None
    try:
        con = lite.connect(caminhoBanco)
    except lite.Error as e:
        print(f'Ops! Erro ao conectar: {e}')
    return con


def criarTabelas():
    con = criarConexao()
    if con:
        try:
            cursor = con.cursor()
            query = "CREATE TABLE IF NOT EXISTS inventario (id INTEGER PRIMARY KEY AUTOINCREMENT,nome TEXT NOT NULL,local TEXT,descricao TEXT,marca TEXT,data_compra DATE,valor DECIMAL,serie TEXT)"
        
            cursor.execute(query)
            con.commit()

            print("Tabela 'inventario' verificada/criada com sucesso!")
        except lite.Error as e:
            print(f'Erro ao criar tabela: {e}')
        finally:
            con.close()

#Verificar quais tabelas existem
def verificarTabelas():
    con = criarConexao()
    if con:
        cursor = con.cursor()
        # Esta query consulta a tabela mestre do SQLite que guarda os nomes de todas as tabelas
        cursor.execute("SELECT name FROM sqlite_master WHERE type='table';")
        tabelas = cursor.fetchall()

        print("Tabelas encontradas no banco: ")
        for t in tabelas:
            print(f'- {t[0]}')

        con.close()


#-----------------CRUD-------------------------

def inserirItem(listaDados):
    """
    lista_dados: deve ser uma lista ou tupla com os valores
    ex: ['Notebook', 'Escritório', 'Dell G15']
    """
    con = criarConexao()
    if con:
        try:
            cursor = con.cursor()
            query = 'INSERT INTO inventario(nome,local,descricao,marca,data_compra_valor,serie) VALUES (?,?,?,?,?,?,?)' 
            cursor.execute(query, listaDados)
            con.commit() # Salva as alterações no banco, Muita gente esquece disso! No SQLite (e no MySQL), quando você altera dados (INSERT, UPDATE, DELETE), você precisa dar o "commit" para confirmar que a alteração é permanente.
            print("Dados inseridos com sucesso!")
        except lite.Error as e:
            print(f'Erro ao inserir o dado: {e}')
        finally:
            con.close()# Garante que a conexão feche sempre

def excluirItem(idItem):
    con = criarConexao()
    if con:
        try:
            cursor = con.cursor()
            query = "DELETE FROM inventario WHERE id = ? "
            # Note a vírgula após id_item: (id_item,) 
            # Isso transforma o número em uma tupla, que é o que o SQLite ama.
            cursor.execute(query, (idItem,))
            con.commit()
            print('Dado deletado com sucesso!')
        except lite.Error as e:
            print(f'Erro ao deletar o dado: {e}')
        finally:
            con.close()

def atualizarItem(listaDados):
    """
    listaDados deve conter os valores novos e, POR ÚLTIMO, o ID do item.
    Ex: [nome, local, descricao, marca, data, valor, serie, id]
    """
    con = criarConexao()
    if con:
        try:
            cursor = con.cursor()
            query = "UPDATE inventario SET nome=?, local=?, descricao=?, marca=?, data_compra=?, valor=?, serie=? WHERE id=?"
            cursor.execute(query, listaDados)
            con.commit()
            print('Dados atualizados com sucesso')
        except lite.Error as e:
            print(f'Erro ao atualizar os dados: {e}')
        finally:
            con.close()

def verItens():
    """Retorna todos os registros da tabela."""
    con = criarConexao()
    dados = []
    if con:
        try:
            cursor = con.cursor()
            cursor.execute('SELECT * FROM inventario')
            dados = cursor.fetchall()
        except lite.Error as e:
            print(f"Erro ao buscar dados: {e}")
        finally:
            con.close()
    return dados

#Testar codigo
#if __name__ == "__main__":

