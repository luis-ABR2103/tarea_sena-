import os

import MySQLdb
from flask import Flask, jsonify
from flask_mysqldb import MySQL
from Config import Config
from Routes import CargarRutas
from flask_cors import CORS 

app = Flask(__name__)
# blueprint
CORS(app)
app.config.from_object(Config) 
mysql = MySQL(app)

app.mysql = mysql    
CargarRutas(app)



# Errores de la base de datos que no atrapa cada controlador
# (por ejemplo, borrar una persona que todavía es aprendiz).
@app.errorhandler(MySQLdb.IntegrityError)
def error_integridad(e):
    return jsonify({
        "mensaje": "No se puede completar: el registro está relacionado con otros datos o ya existe",
        "detalle": str(e),
    }), 409


@app.errorhandler(MySQLdb.DataError)
@app.errorhandler(MySQLdb.OperationalError)
def error_datos(e):
    codigo = e.args[0] if e.args else None
    # 2002/2003/2005/2006/2013: no se pudo conectar o se perdió la conexión con Aiven
    if codigo in (2002, 2003, 2005, 2006, 2013):
        return jsonify({"mensaje": "No hay conexión con la base de datos, intenta de nuevo", "detalle": str(e)}), 503
    return jsonify({"mensaje": "Datos no válidos para la base de datos", "detalle": str(e)}), 400


# En Render la API se inicia con gunicorn; esto solo se ejecuta con "python app.py"
if __name__ == "__main__":
    app.run(debug=True, port=int(os.getenv("PORT", 5000)), host="0.0.0.0")
