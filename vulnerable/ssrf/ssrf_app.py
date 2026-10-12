from flask import Flask, request
import requests

app = Flask(__name__)


@app.route("/verificar-stock")
def verificar_stock():
    servicio_url = request.args.get("servicio", "")
    if not servicio_url:
        return "Falta el parámetro 'servicio'", 400

    # Usa la url del cliente sin validarla
    respuesta = requests.get(servicio_url, timeout=5)

    # Reenvía la respuesta cruda del backend
    return respuesta.text


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)


# curl localhost:5000/verificar-stock?servicio=http://127.0.0.1:6000/stock/42
# curl localhost:5000/verificar-stock?servicio=http://127.0.0.1:6000/admin/panel
