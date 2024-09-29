<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Reporte de Proyecto Streamlit</title>
    <style>
        body {
            font-family: Arial, sans-serif;
            line-height: 1.6;
            margin: 20px;
            background-color: #f4f4f4;
        }
        h1, h2, h3 {
            color: #4e54c8;
        }
        code {
            background-color: #e7e7e7;
            padding: 5px;
            border-radius: 5px;
        }
        .exercise {
            background-color: #ffffff;
            padding: 15px;
            margin: 10px 0;
            border: 1px solid #ddd;
            border-radius: 5px;
        }
    </style>
</head>
<body>
    <h1>Reporte de Proyecto: Ejercicios de Python con Streamlit</h1>

    <h2>Funcionalidad del Código</h2>
    <p>
        Este proyecto está diseñado para mostrar diversos ejercicios de Python utilizando la biblioteca Streamlit para crear una interfaz de usuario interactiva. El programa incluye funciones para realizar cálculos matemáticos simples, manipulación de listas y gestión de datos personales. Cada ejercicio es accesible a través de un menú lateral que permite al usuario seleccionar qué función desea utilizar.
    </p>
    
    <h2>Decoración y Estilo</h2>
    <p>
        Se han implementado estilos CSS personalizados para mejorar la apariencia de la aplicación. Esto incluye un fondo con un degradado, colores de texto específicos, estilos para botones y campos de entrada, y un tamaño de fuente ajustado para una mejor legibilidad.
    </p>

    <h2>Descripción de Ejercicios</h2>
    
    <div class="exercise">
        <h3>1. Función de Saludo Simple</h3>
        <p>La función <code>saludar()</code> recibe un nombre como parámetro y devuelve un saludo personalizado.</p>
        <p><code>Ejemplo:</code> <code>saludar("Juan")</code> devuelve <code>"Hola, Juan"</code>.</p>
    </div>

    <div class="exercise">
        <h3>2. Suma de Dos Números</h3>
        <p>La función <code>sumar()</code> recibe dos números y devuelve su suma.</p>
        <p><code>Ejemplo:</code> <code>sumar(2, 3)</code> devuelve <code>5</code>.</p>
    </div>

    <div class="exercise">
        <h3>3. Área de un Triángulo</h3>
        <p>La función <code>calcular_area_triangulo()</code> toma la base y la altura de un triángulo y devuelve su área.</p>
        <p><code>Ejemplo:</code> <code>calcular_area_triangulo(4, 5)</code> devuelve <code>10</code>.</p>
    </div>

    <div class="exercise">
        <h3>4. Calculadora de Descuento</h3>
        <p>La función <code>calcular_precio_final()</code> calcula el precio final después de aplicar un descuento y un impuesto.</p>
        <p><code>Ejemplo:</code> <code>calcular_precio_final(100, 10, 16)</code> devuelve <code>104</code>.</p>
    </div>

    <div class="exercise">
        <h3>5. Suma de una Lista de Números</h3>
        <p>La función <code>sumar_lista()</code> recibe una lista de números y devuelve la suma total de sus elementos.</p>
        <p><code>Ejemplo:</code> <code>sumar_lista([1, 2, 3])</code> devuelve <code>6</code>.</p>
    </div>

    <div class="exercise">
        <h3>6. Funciones con Valores Predeterminados</h3>
        <p>La función <code>producto()</code> devuelve el precio total de un producto basado en el nombre, cantidad y precio por unidad.</p>
        <p><code>Ejemplo:</code> <code>producto("Manzanas", 3, 2)</code> devuelve <code>"Producto: Manzanas, Cantidad: 3, Precio total: $6"</code>.</p>
    </div>

    <div class="exercise">
        <h3>7. Números Pares e Impares</h3>
        <p>La función <code>numeros_pares_e_impares()</code> separa una lista de números en pares e impares.</p>
        <p><code>Ejemplo:</code> <code>numeros_pares_e_impares([1, 2, 3, 4])</code> devuelve <code>([2, 4], [1, 3])</code>.</p>
    </div>

    <div class="exercise">
        <h3>8. Multiplicación con *args</h3>
        <p>La función <code>multiplicar_todos()</code> recibe múltiples números y devuelve su producto.</p>
        <p><code>Ejemplo:</code> <code>multiplicar_todos(2, 3, 4)</code> devuelve <code>24</code>.</p>
    </div>

    <div class="exercise">
        <h3>9. Información de una Persona con **kwargs</h3>
        <p>La función <code>informacion_personal()</code> recopila datos personales en un formato clave:valor.</p>
        <p><code>Ejemplo:</code> <code>informacion_personal(nombre="Juan", edad=30)</code> devuelve <code>"nombre: Juan\nedad: 30"</code>.</p>
    </div>

    <div class="exercise">
        <h3>10. Calculadora Flexible</h3>
        <p>La función <code>calculadora_flexible()</code> realiza operaciones matemáticas básicas (suma, resta, multiplicación, división) según la operación seleccionada.</p>
        <p><code>Ejemplo:</code> <code>calculadora_flexible(10, 5, "Resta")</code> devuelve <code>5</code>.</p>
    </div>

    <h2>Conclusiones</h2>
    <p>
        Este proyecto demuestra el uso de funciones en Python para llevar a cabo diversas tareas matemáticas y de manipulación de datos. La implementación de una interfaz de usuario con Streamlit permite que los usuarios interactúen fácilmente con cada función y obtengan resultados instantáneos.
    </p>
</body>
</html>
