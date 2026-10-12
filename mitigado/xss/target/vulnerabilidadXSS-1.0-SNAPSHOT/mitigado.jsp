<%@ page contentType="text/html;charset=UTF-8" language="java" %>
<%@ taglib prefix="c" uri="http://java.sun.com/jsp/jstl/core" %>
<%
    // Cabecera de seguridad CSP (Defensa en profundidad contra XSS)
    response.setHeader(
        "Content-Security-Policy",
        "default-src 'self'; script-src 'self'; object-src 'none'; base-uri 'self';"
    );
%>
<html>
<head>
    <title>Consulta de Empleado - Seguro con JSTL y CSP</title>
</head>
<body>
    <h2>Portal de Búsqueda de Empleados</h2>
    
    <form method="GET" action="protegido-jstl.jsp">
        <label for="eid">Employee ID:</label>
        <input type="text" id="eid" name="eid">
        <button type="submit">Buscar</button>
    </form>

    <hr>

    <c:if test="${not empty param.eid}">
        <p>Resultado para Employee ID: <strong><c:out value="${param.eid}"/></strong></p>
    </c:if>
</body>
</html>