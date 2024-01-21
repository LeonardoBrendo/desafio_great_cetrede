from flask import Flask, jsonify
import psycopg2
from psycopg2 import pool
from flask_cors import CORS

app = Flask(__name__)
CORS(app)

db_params = {
    'dbname': 'postgres',
    'user': 'postgres',
    'password': '######',
    'host': 'localhost',
    'port': '5432'
}
connection_pool = psycopg2.pool.SimpleConnectionPool(1, 1000, **db_params)

def get_connection():
    return connection_pool.getconn()

@app.route("/")
def hello_world():
    return "<p>Seja bem-vindo a API das escolas</p>"

@app.route('/api/escola/<int:id_escola>', methods=['GET'])
def get_escola_by_id(id_escola):
    conn = get_connection()
    cur = conn.cursor()
    
    cur.execute('SELECT * FROM escola WHERE "ID_ESCOLA" = %s;', (id_escola,))
    escola = cur.fetchone()
   
    cur.close()
    conn.close()
   
    if escola:
        return jsonify(
            {'ID_ESCOLA': escola[6], 
             'NU_ANO_SAEB': escola[0],
             'CO_UF': escola[1],
             'SG_UF': escola[2],
             'NO_UF': escola[3],
             'CO_MUNICIPIO':escola[4],
             'NO_MUNICIPIO': escola[5],
             'NO_ESCOLA': escola[7],
             'TP_TIPO_REDE': escola[8],
             'TP_LOCALIZACAO': escola[9],
             'TP_CAPITAL': escola[10],
             'QTD_ALUNOS_INSE': escola[11],
             'MEDIA_INSE': escola[12],
             'INSE_CLASSIFICACAO': escola[13],
             'PC_NIVEL_1': escola[14],
             'PC_NIVEL_2': escola[15],
             'PC_NIVEL_3': escola[16],
             'PC_NIVEL_4': escola[17],
             'PC_NIVEL_5': escola[18],
             'PC_NIVEL_6': escola[19],
             'PC_NIVEL_7': escola[20],
             'PC_NIVEL_8': escola[21],
             }
        )
    else:
        return jsonify({'Mensagem': 'Escola não encontrada'}), 404

@app.route('/api/escolas', methods=['GET'])
def get_all_escolas():
    conn = get_connection()
    cur = conn.cursor()

    cur.execute('SELECT * FROM escola;')
    escolas = cur.fetchall()

    cur.close()
    conn.close()

    escolas_list = []
    for escola in escolas:
        escolas_list.append({
            'ID_ESCOLA': escola[6],
            'NU_ANO_SAEB': escola[0],
            'CO_UF': escola[1],
            'SG_UF': escola[2],
            'NO_UF': escola[3],
            'CO_MUNICIPIO': escola[4],
            'NO_MUNICIPIO': escola[5],
            'NO_ESCOLA': escola[7],
            'TP_TIPO_REDE': escola[8],
            'TP_LOCALIZACAO': escola[9],
            'TP_CAPITAL': escola[10],
            'QTD_ALUNOS_INSE': escola[11],
            'MEDIA_INSE': escola[12],
            'INSE_CLASSIFICACAO': escola[13],
            'PC_NIVEL_1': escola[14],
            'PC_NIVEL_2': escola[15],
            'PC_NIVEL_3': escola[16],
            'PC_NIVEL_4': escola[17],
            'PC_NIVEL_5': escola[18],
            'PC_NIVEL_6': escola[19],
            'PC_NIVEL_7': escola[20],
            'PC_NIVEL_8': escola[21],
        })

    return jsonify(escolas_list)

@app.route('/api/escolas_sguf/<string:uf>', methods=['GET'])
def get_escola_by_sguf(uf):
    conn = get_connection()
    cur = conn.cursor()

    cur.execute('SELECT * FROM escola WHERE "SG_UF" = %s;', (uf,))
    escolas = cur.fetchall()

    cur.close()
    conn.close()

    escolas_list = []
    for escola in escolas:
        escolas_list.append({
            'ID_ESCOLA': escola[6],
            'NU_ANO_SAEB': escola[0],
            'CO_UF': escola[1],
            'SG_UF': escola[2],
            'NO_UF': escola[3],
            'CO_MUNICIPIO': escola[4],
            'NO_MUNICIPIO': escola[5],
            'NO_ESCOLA': escola[7],
            'TP_TIPO_REDE': escola[8],
            'TP_LOCALIZACAO': escola[9],
            'TP_CAPITAL': escola[10],
            'QTD_ALUNOS_INSE': escola[11],
            'MEDIA_INSE': escola[12],
            'INSE_CLASSIFICACAO': escola[13],
            'PC_NIVEL_1': escola[14],
            'PC_NIVEL_2': escola[15],
            'PC_NIVEL_3': escola[16],
            'PC_NIVEL_4': escola[17],
            'PC_NIVEL_5': escola[18],
            'PC_NIVEL_6': escola[19],
            'PC_NIVEL_7': escola[20],
            'PC_NIVEL_8': escola[21],
        })

    return jsonify(escolas_list)

@app.route('/api/escolas_couf/<int:uf>', methods=['GET'])
def get_escola_by_couf(uf):
    conn = get_connection()
    cur = conn.cursor()

    cur.execute('SELECT * FROM escola WHERE "CO_UF" = %s;', (uf,))
    escolas = cur.fetchall()

    cur.close()
    conn.close()

    escolas_list = []
    for escola in escolas:
        escolas_list.append({
            'ID_ESCOLA': escola[6],
            'NU_ANO_SAEB': escola[0],
            'CO_UF': escola[1],
            'SG_UF': escola[2],
            'NO_UF': escola[3],
            'CO_MUNICIPIO': escola[4],
            'NO_MUNICIPIO': escola[5],
            'NO_ESCOLA': escola[7],
            'TP_TIPO_REDE': escola[8],
            'TP_LOCALIZACAO': escola[9],
            'TP_CAPITAL': escola[10],
            'QTD_ALUNOS_INSE': escola[11],
            'MEDIA_INSE': escola[12],
            'INSE_CLASSIFICACAO': escola[13],
            'PC_NIVEL_1': escola[14],
            'PC_NIVEL_2': escola[15],
            'PC_NIVEL_3': escola[16],
            'PC_NIVEL_4': escola[17],
            'PC_NIVEL_5': escola[18],
            'PC_NIVEL_6': escola[19],
            'PC_NIVEL_7': escola[20],
            'PC_NIVEL_8': escola[21],
        })

    return jsonify(escolas_list)

@app.route("/api/quantidade_por_classificacao/<string:estado>", methods=['GET'])
def quantidade_por_classificacao(estado):
    conn = get_connection()
    cur = conn.cursor()

    cur.execute('SELECT "INSE_CLASSIFICACAO", COUNT(*) FROM escola WHERE "SG_UF" = %s GROUP BY "INSE_CLASSIFICACAO";', (estado,))
    resultado = cur.fetchall()

    cur.close()
    conn.close()

    classificacoes = [{"classificacao": row[0], "quantidade": row[1]} for row in resultado]

    return jsonify(classificacoes)

@app.route('/media_inse/<uf>', methods=['GET'])
def calcular_media_inse(uf):
    conn = get_connection()
    cur = conn.cursor()

    with conn.cursor() as cur:
        cur.execute('SELECT AVG ("MEDIA_INSE") FROM escola WHERE "SG_UF" = %s;', (uf,))
        resultado = cur.fetchone()

    conn.close()

    if resultado[0] is not None:
        media_inse = resultado[0]
    else:
        media_inse = 0

    return jsonify({"media_inse": media_inse})

@app.route('/pc_nivel_1/<uf>', methods=['GET'])
def calcular_pc_nivel_1(uf):
    conn = get_connection()
    cur = conn.cursor()

    with conn.cursor() as cur:
        cur.execute('SELECT AVG ("PC_NIVEL_1") FROM escola WHERE "SG_UF" = %s;', (uf,))
        resultado = cur.fetchone()

    conn.close()

    if resultado[0] is not None:
        pc_nivel_1 = resultado[0]
    else:
        pc_nivel_1 = 0

    return jsonify({"pc_nivel_1": pc_nivel_1})

@app.route('/pc_nivel_2/<uf>', methods=['GET'])
def calcular_pc_nivel_2(uf):
    conn = get_connection()
    cur = conn.cursor()

    with conn.cursor() as cur:
        cur.execute('SELECT AVG ("PC_NIVEL_2") FROM escola WHERE "SG_UF" = %s;', (uf,))
        resultado = cur.fetchone()

    conn.close()

    if resultado[0] is not None:
        pc_nivel_2 = resultado[0]
    else:
        pc_nivel_2 = 0

    return jsonify({"pc_nivel_2": pc_nivel_2})

@app.route('/pc_nivel_3/<uf>', methods=['GET'])
def calcular_pc_nivel_3(uf):
    conn = get_connection()
    cur = conn.cursor()

    with conn.cursor() as cur:
        cur.execute('SELECT AVG ("PC_NIVEL_3") FROM escola WHERE "SG_UF" = %s;', (uf,))
        resultado = cur.fetchone()

    conn.close()

    if resultado[0] is not None:
        pc_nivel_3 = resultado[0]
    else:
        pc_nivel_3 = 0

    return jsonify({"pc_nivel_3": pc_nivel_3})

@app.route('/pc_nivel_4/<uf>', methods=['GET'])
def calcular_pc_nivel_4(uf):
    conn = get_connection()
    cur = conn.cursor()

    with conn.cursor() as cur:
        cur.execute('SELECT AVG ("PC_NIVEL_4") FROM escola WHERE "SG_UF" = %s;', (uf,))
        resultado = cur.fetchone()

    conn.close()

    if resultado[0] is not None:
        pc_nivel_4 = resultado[0]
    else:
        pc_nivel_4 = 0

    return jsonify({"pc_nivel_4": pc_nivel_4})

@app.route('/pc_nivel_5/<uf>', methods=['GET'])
def calcular_pc_nivel_5(uf):
    conn = get_connection()
    cur = conn.cursor()

    with conn.cursor() as cur:
        cur.execute('SELECT AVG ("PC_NIVEL_5") FROM escola WHERE "SG_UF" = %s;', (uf,))
        resultado = cur.fetchone()

    conn.close()

    if resultado[0] is not None:
        pc_nivel_5 = resultado[0]
    else:
        pc_nivel_5 = 0

    return jsonify({"pc_nivel_5": pc_nivel_5})

@app.route('/pc_nivel_6/<uf>', methods=['GET'])
def calcular_pc_nivel_6(uf):
    conn = get_connection()
    cur = conn.cursor()

    with conn.cursor() as cur:
        cur.execute('SELECT AVG ("PC_NIVEL_6") FROM escola WHERE "SG_UF" = %s;', (uf,))
        resultado = cur.fetchone()

    conn.close()

    if resultado[0] is not None:
        pc_nivel_6 = resultado[0]
    else:
        pc_nivel_6 = 0

    return jsonify({"pc_nivel_6": pc_nivel_6})

@app.route('/pc_nivel_7/<uf>', methods=['GET'])
def calcular_pc_nivel_7(uf):
    conn = get_connection()
    cur = conn.cursor()

    with conn.cursor() as cur:
        cur.execute('SELECT AVG ("PC_NIVEL_7") FROM escola WHERE "SG_UF" = %s;', (uf,))
        resultado = cur.fetchone()

    conn.close()

    if resultado[0] is not None:
        pc_nivel_7 = resultado[0]
    else:
        pc_nivel_7 = 0

    return jsonify({"pc_nivel_7": pc_nivel_7})

@app.route('/pc_nivel_8/<uf>', methods=['GET'])
def calcular_pc_nivel_8(uf):
    conn = get_connection()
    cur = conn.cursor()

    with conn.cursor() as cur:
        cur.execute('SELECT AVG ("PC_NIVEL_8") FROM escola WHERE "SG_UF" = %s;', (uf,))
        resultado = cur.fetchone()

    conn.close()

    if resultado[0] is not None:
        pc_nivel_8 = resultado[0]
    else:
        pc_nivel_8 = 0

    return jsonify({"pc_nivel_8": pc_nivel_8})

if __name__ == '__main__':
    app.run(debug=True)