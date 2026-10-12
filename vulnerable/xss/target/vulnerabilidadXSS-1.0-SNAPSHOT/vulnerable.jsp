<%@ page contentType="text/html;charset=UTF-8" language="java" %>
<html>
<head>
    <title>Consulta de Empleado - Vulnerable</title>
</head>
<body>
    <h2>Portal de Búsqueda de Empleados</h2>
    
    <form method="GET" action="vulnerable.jsp">
        <label for="eid">Employee ID:</label>
        <input type="text" id="eid" name="eid">
        <button type="submit">Buscar</button>
    </form>

    <hr>

    <% 
        String eid = request.getParameter("eid");
        if (eid != null) {
    %>
        <!-- Vulnerabilidad. Inyección directa sin sanitización -->
        <p>Resultado para Employee ID: <strong><%= eid %></strong></p>
    <% 
        } 
    %>
</body>
</html>