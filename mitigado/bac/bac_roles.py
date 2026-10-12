from flask import Flask, session, jsonify, render_template_string

app = Flask(__name__)
app.secret_key = "clave_secreta_que_debe_ser_larga"

# HTML básico
HTML_TEMPLATE = """
<!DOCTYPE html>
<html>
<head><title>Panel Seguro con Roles</title></head>
<body>
    <h2>Panel Seguro (Tu rol actual: {{ rol }})</h2>
    <p><a href="/user">Ir al panel de usuario</a></p>
    <!-- <p><a href="/admin">Intentar entrar al panel de administración</a></p> -->
</body>
</html>
"""

@app.route("/")
def index():
    # Usuario normal logueado
    session["user_id"] = "101"
    session["rol"] = "usuario"
    return render_template_string(HTML_TEMPLATE, rol=session["rol"])

@app.route("/user")
def user_dashboard():
    return jsonify({
        "mensaje": "Bienvenido al panel general de usuario",
        "rol_actual": session.get("rol")
    })

# Ruta mitigada. Verificación estricta del rol en el servidor
@app.route("/admin")
def admin_panel():
    rol_actual = session.get("rol")
    
    # 1. Comprobar autenticación y rol
    if rol_actual != "administrador":
        return jsonify({
            "error": "Acceso denegado (403 Forbidden). Se requieren permisos de administrador."
        }), 403
    
    # 2. Solo llega aquí si el usuario es administrador
    return jsonify({
        "mensaje": "Panel de administración",
        "datos_secretos": "Claves de API del sistema y configuración maestra"
    })

if __name__ == "__main__":
    app.run(port=5000)