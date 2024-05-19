import pymysql

# Dados de acesso ao banco de dados
DB_HOST = 'localhost'  # Endereço do banco de dados
DB_USER = 'root'  # Usuário do banco de dados
DB_PASSWORD = '7890_6543'  # Senha do banco de dados
DB_NAME = 'infinito'  # Nome do banco de dados

conexao = pymysql.connect(host=DB_HOST, user=DB_USER, password=DB_PASSWORD, database=DB_NAME)

def atualiza_banco_via_id(tabela, coluna, novo_dado, id):
    """
    Atualiza um dado na tabela do banco de dados pelo ID.

    Args:
        tabela (str): Nome da tabela onde ocorrerá a atualização.
        coluna (str): Nome da coluna que será atualizada.
        novo_dado (str): Novo valor a ser atribuído à coluna.
        id (int): ID do registro que será atualizado.

    Returns:
        None
    """
    try:
        with conexao.cursor() as cursor:
            # Query SQL para atualizar o dado na tabela pelo ID
            sql = f"UPDATE `{DB_NAME}`.`{tabela}` SET `{coluna}` = %s WHERE (`cadastro_id` = %s);"
            cursor.execute(sql, (novo_dado, id))
        conexao.commit()  # Confirmar a atualização no banco de dados
    except pymysql.Error as e:
        print(f"Erro ao atualizar banco: {e}")

def autenticar_usuario(email, senha):
    """
    Verifica se o e-mail e senha correspondem a um usuário cadastrado.

    Args:
        email (str): E-mail do usuário a ser autenticado.
        senha (str): Senha do usuário a ser autenticado.

    Returns:
        bool: True se a autenticação for bem-sucedida, False caso contrário.
    """
    try:
        with conexao.cursor() as cursor:
            # Consulta SQL para verificar autenticação
            sql = f"SELECT * FROM `cadastro` WHERE `cadastro_email` = %s AND `cadastro_senha` = %s"
            cursor.execute(sql, (email, senha))
            resultado = cursor.fetchone()
            return resultado is not None
    except pymysql.Error as e:
        print(f"Erro ao autenticar usuário: {e}")
        return False

def mostrar_tabela(tabela):
    """
    Retorna todos os dados de uma tabela do banco de dados.

    Args:
        tabela (str): Nome da tabela a ser consultada.

    Returns:
        tuple: Tupla contendo os dados da tabela.
    """
    try:
        with conexao.cursor() as cursor:
            sql = f"SELECT * FROM `{DB_NAME}`.`{tabela}`;"
            cursor.execute(sql)
            resultados = cursor.fetchall()
            return resultados
    except pymysql.Error as e:
        print(f"Erro ao mostrar tabela: {e}")

def inserir_dados_em_tabela(tabela, campos_colunas, linha):
    """
    Insere dados em uma tabela do banco de dados.

    Args:
        tabela (str): Nome da tabela onde os dados serão inseridos.
        campos_colunas (str): Nomes das colunas separados por vírgula.
        linha (str): Valores correspondentes aos campos separados por vírgula.

    Returns:
        None
    """
    try:
        with conexao.cursor() as cursor:
            # Query SQL para inserir os dados na tabela
            sql = f"INSERT INTO `{DB_NAME}`.`{tabela}` ({campos_colunas}) VALUES ({linha})"
            cursor.execute(sql)
        conexao.commit()  # Confirmar a inserção no banco de dados
    except pymysql.Error as e:
        print(f"Erro ao inserir dados na tabela: {e}")
