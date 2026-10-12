from flask import Flask, session, jsonify, render_template_string

app = Flask(__name__)
app.secret_key = "clave_secreta"

# HTML básico
HTML_TEMPLATE = """
<!DOCTYPE html>
<html>
<head><title>Panel con Roles</title></head>
<body>
    <h2>Bienvenido, usuario regular</h2>
    <p>Opciones disponibles en tu interfaz:</p>
    <p><a href="/user">Ir al panel de usuario</a></p>
    
    <!-- El enlace a /admin está oculto en la interfaz, pero la ruta existe -->
</body>
</html>
"""

@app.route("/")
def index():
    # Simulación de entrada con un usuario de rol 'usuario'
    session["user_id"] = "101"
    session["rol"] = "usuario"
    return render_template_string(HTML_TEMPLATE)

@app.route("/user")
def user_dashboard():
    return jsonify({
        "mensaje": "Bienvenido al panel general de usuario",
        "tu_rol": session.get("rol")
    })

# Ruta vulnerable. No verifica si el rol es 'administrador'
@app.route("/admin")
def admin_panel():
    # El servidor asume que si alguien llegó a este punto es porque tiene permiso
    return jsonify({
        "mensaje": "¡ACCESO DE ADMINISTRADOR CONCEDIDO!",
        "datos_secretos": "Claves de API del sistema, logs y base de datos maestra"
    })

if __name__ == "__main__":
    app.run(port=5000)