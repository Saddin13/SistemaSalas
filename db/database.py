import pymysql

def conectar_banco():
    return pymysql.connect(
        host="blank",
        user="blank",
        password="12345",
        database="blank"
    )

def obter_professores():
    conn = conectar_banco()
    cursor = conn.cursor()
    cursor.execute("SELECT nome FROM professores")
    professores = [row[0] for row in cursor.fetchall()]
    conn.close()
    return professores

# Outras funções: obter_disciplinas(), obter_turmas(), obter_horarios(), etc.
