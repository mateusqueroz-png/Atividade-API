from conexao import conectar


def criar_tabela():
    conexao, cursor = conectar()
    if conexao:
        try:
            cursor.execute("""
                CREATE TABLE IF NOT EXISTS movies (
                    id SERIAL PRIMARY KEY,
                    avaliacao REAL
                    )
                """)
            conexao.commit()
        except Exception as erro:
            print(f"Erro ao criar a tabela: {erro}")
        finally:
            cursor.close()
            conexao.close()

criar_tabela()


def criar_filme(titulo, avaliacao):
    conexao, cursor = conectar()
    if conexao:
        try:
            cursor.execute(
                "INSERT INTO movies (titulo, genero, ano, avaliacao) VALUES (%s, %s, %s, %s)",
                (titulo,avaliacao)
            )
            conexao.commit()
        except Exception as erro:
            print(f"Erro ao inserir filme: {erro}")
        finally:
            cursor.close()
            conexao.close()

def listar_movies():
    conexao, cursor = conectar()
    if conexao:
        try:
            cursor.execute(
                "SELECT * FROM movies ORDER BY id"
            )
            return cursor.fetchall()
        except Exception as erro:
            print(f"Erro ao listar: {erro}")
            return []
        finally:
            cursor.close()
            conexao.close()


def atualizar_movies(id_produto, nova_avaliacao):
    conexao, cursor = conectar()
    if conexao:
        try:
            cursor.execute(
                "UPDATE movies SET avaliacao = %s WHERE id = %s",
                (nova_avaliacao, id_produto)
            )
            conexao.commit()
        except Exception as erro:
            print(f"Erro ao atualizar a nota do produto: {erro}")
        finally:
            cursor.close()
            conexao.close()


def deletar_movie(id_movie):
    conexao, cursor = conectar()
    if conexao:
        try:
            cursor.execute(
                "DELETE FROM movies WHERE id = %s", (id_movie,)
            )
            conexao.commit()
        except Exception as erro:
            print(f"Erro ao deletar produto: {erro}")
        finally:
            cursor.close()
            conexao.close()

deletar_movie(1)




def buscar_movies(id_produto):
    conexao, cursor = conectar()
    if conexao:
        try:
            cursor.execute(
                "SELECT * FROM movies ORDER BY id = %s",(id_produto)
            )
            return cursor.fetchall()
        except Exception as erro:
            print(f"Erro ao listar: {erro}")
            return []
        finally:
            cursor.close()
            conexao.close()
