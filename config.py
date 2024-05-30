SECRET_KEY = 'racionais'

#CONFIGURAÇÃO DO BANCOS DE DADOS.
SQLALCHEMY_DATABASE_URI = \
    '{SGBD}://{usuario}:{senha}@{servidor}/{database}'.format(
        SGBD = 'mysql+mysqlconnector',
        usuario = 'root',
        senha = 'dapontepraca',
        servidor = 'localhost',
        database = 'lista_tarefas'
    )
