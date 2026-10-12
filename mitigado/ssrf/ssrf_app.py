import ipaddress
import socket
from urllib.parse import urlparse

from flask import Flask, request, jsonify
import requests

app = Flask(__name__)

# Únicos destinos internos autorizados
SERVICIOS_PERMITIDOS = {("127.0.0.1", 6000)}


def es_ip_no_enrutable(ip_str):
    ip = ipaddress.ip_address(ip_str)
    return ip.is_private or ip.is_loopback or ip.is_link_local or ip.is_reserved


def destino_autorizado(url):
    partes = urlparse(url)
    if partes.scheme != "http":
        return False
    host = partes.hostname
    puerto = partes.port or 80
    try:
        ip_resuelta = socket.gethostbyname(host)
    except socket.gaierror:
        return False
    # Solo pasa si la ip resuelta ya está en la lista permitida
    return (ip_resuelta, puerto) in SERVICIOS_PERMITIDOS


@app.route("/verificar-stock")
def verificar_stock():
    producto_id = request.args.get("producto_id", "")
    if not producto_id:
        return "Falta el parámetro 'producto_id'", 400

    # El destino ya no lo decide el cliente
    url_interna = f"http://127.0.0.1:6000/stock/{producto_id}"

    if not destino_autorizado(url_interna):
        return "Solicitud rechazada", 403

    # Nunca sigue redirecciones automáticas
    respuesta = requests.get(url_interna, timeout=5, allow_redirects=False)

    # Arma su propia respuesta en vez de reenviar la cruda
    datos = respuesta.json()
    return jsonify({"producto_id": datos.get("producto_id"), "stock": datos.get("stock")})


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)


# curl localhost:5000/verificar-stock?producto_id=42
# curl localhost:5000/verificar-stock?servicio=http://127.0.0.1:6000/admin/panel
