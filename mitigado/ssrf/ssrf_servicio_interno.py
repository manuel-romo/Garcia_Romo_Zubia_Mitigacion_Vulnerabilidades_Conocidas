from flask import Flask, jsonify

app = Flask(__name__)


@app.route("/stock/<producto_id>")
def consultar_stock(producto_id):
    # Simula una consulta real a una base de inventario
    return jsonify({"producto_id": producto_id, "stock": 17})


@app.route("/admin/panel")
def panel_admin():
    # Recurso interno que nunca debería ser visible desde fuera
    return jsonify({
        "panel": "ADMINISTRACION INTERNA",
        "usuarios": ["admin", "soporte_ti"],
        "api_key_interna": "SK-INTERNA-9f8e7d6c5b4a",
    })


if __name__ == "__main__":
    # Solo escucha en loopback, simula la red interna
    app.run(host="127.0.0.1", port=6000)
