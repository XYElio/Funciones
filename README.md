# Aplicación Python Streamlit
### Visita la Aplicación Web Aquí:

🔗 **[Funciones de la Aplicación](https://xfunciones-app-1.streamlit.app)**

## Resumen

Este informe analiza una aplicación Python que utiliza Streamlit para crear una interfaz web interactiva para varias funciones matemáticas y de procesamiento de datos. La aplicación consta de varios componentes clave:

1. Funciones principales para procesamiento de datos y cálculos
2. Funciones de interfaz de usuario (UI) que utilizan Streamlit para entrada y salida
3. Una función principal que configura la página y gestiona el flujo general de la aplicación
4. CSS personalizado para estilizar la aplicación

## Análisis de Funciones Principales

### 1. Saludo Simple

```python
def saludar(nombre):
    return f"Hola, {nombre}"
```

Esta función toma un nombre como entrada y devuelve una cadena de saludo. Demuestra el formateo básico de cadenas en Python.

### 2. Suma de Dos Números

```python
def sumar(a, b):
    return a + b
```

Una función de suma simple que toma dos números y devuelve su suma. Muestra operaciones aritméticas básicas en Python.

### 3. Área de un Triángulo

```python
def calcular_area_triangulo(base, altura):
    return 0.5 * base * altura
```

Esta función calcula el área de un triángulo dada su base y altura. Demuestra el uso de fórmulas matemáticas en funciones Python.

### 4. Calculadora de Descuento

```python
def calcular_precio_final(precio_original, descuento=10, impuesto=16):
    precio_con_descuento = precio_original * (1 - descuento/100)
    return precio_con_descuento * (1 + impuesto/100)
```

Esta función calcula el precio final de un producto después de aplicar un descuento e impuesto. Muestra el uso de parámetros por defecto y cálculos más complejos.

### 5. Suma de una Lista

```python
def sumar_lista(numeros):
    return sum(numeros)
```

Esta función suma todos los números en una lista dada. Demuestra el uso de la función incorporada `sum()` de Python.

### 6. Información de Producto

```python
def producto(nombre, cantidad=1, precio=10):
    return f"Producto: {nombre}, Cantidad: {cantidad}, Precio total: ${cantidad * precio}"
```

Esta función crea una cadena con información del producto. Muestra el uso de parámetros por defecto y formateo de cadenas.

### 7. Números Pares e Impares

```python
def numeros_pares_e_impares(numeros):
    pares = [num for num in numeros if num % 2 == 0]
    impares = [num for num in numeros if num % 2 != 0]
    return pares, impares
```

Esta función separa una lista de números en números pares e impares. Demuestra el uso de comprensiones de lista en Python.

### 8. Multiplicación con *args

```python
def multiplicar_todos(*args):
    return 1 if not args else args[0] if len(args) == 1 else args[0] * multiplicar_todos(*args[1:])
```

Esta función multiplica un número arbitrario de argumentos. Muestra el uso de `*args` y llamadas a funciones recursivas.

### 9. Información Personal con **kwargs

```python
def informacion_personal(**kwargs):
    return "\n".join([f"{k}: {v}" for k, v in kwargs.items()])
```

Esta función crea una cadena con información personal a partir de argumentos de palabras clave. Demuestra el uso de `**kwargs` y operaciones de diccionario.

### 10. Calculadora Flexible

```python
def calculadora_flexible(a, b, operacion="suma"):
    match operacion:
        case "Suma":
            return a + b
        case "Resta":
            return a - b
        case "Multiplicacion":
            return a * b
        case "Division":
            return a / b if b != 0 else "Error: División por cero"
        case _:
            return "Operación no válida"
```

Esta función realiza diferentes operaciones aritméticas según la entrada. Muestra el uso de la declaración `match` de Python para el control de flujo.

## Funciones de Interfaz de Usuario

La aplicación utiliza Streamlit para crear una interfaz web interactiva. Cada función de UI corresponde a una de las funciones principales y proporciona campos de entrada y visualización de salida utilizando componentes de Streamlit. Por ejemplo:

```python
def ui_saludo_simple():
    st.header("Bienvenida")
    nombre = st.text_input("Escribe tu nombre")
    if nombre:
        st.write(saludar(nombre))
```

Esta función crea un campo de entrada de texto para el nombre del usuario y muestra el saludo utilizando la función `saludar()`.

## Función Principal y Estructura de la Aplicación

La función `main()` configura la estructura general de la aplicación:

```python
def main():
    set_page_config()
    st.title("Ejercicios de Python con Streamlit")

    ejercicios = {
        "1. Saludo 👋": ui_saludo_simple,
        "2. Calculadora de suma 🧮": ui_suma_dos_numeros,
        "3. Calculadora de área triangular 📐": ui_area_triangulo,
        "4. Calculadora de precios con descuento 💰": ui_calculadora_descuento,
        "5. Suma de una lista 📊": ui_suma_lista,
        "6. Información de producto 🛒": ui_producto_valores_predeterminados,
        "7. Números pares e impares 🔢": ui_numeros_pares_impares,
        "8. Multiplicación múltiple ✖️": ui_multiplicacion_args,
        "9. Formulario de datos personales 📝": ui_informacion_personal_kwargs,
        "10. Calculadora 🖩": ui_calculadora_flexible
    }

    ejercicio = st.sidebar.selectbox("Selecciona un ejercicio", list(ejercicios.keys()))

    with st.container():
        st.markdown('<div class="main-content">', unsafe_allow_html=True)
        
        if ejercicio in ejercicios:
            ejercicios[ejercicio]()
        else:
            st.error("Ejercicio no encontrado")
        
        st.markdown('</div>', unsafe_allow_html=True)
```

Esta función:
1. Configura la página
2. Crea una barra lateral con un menú desplegable para seleccionar diferentes ejercicios
3. Muestra el ejercicio seleccionado en el área de contenido principal

## Estilización CSS

La aplicación utiliza CSS personalizado para estilizar la interfaz de Streamlit:

```python
def set_page_config():
    st.set_page_config(
        page_title="Funciones",
        page_icon="💻",
        layout="wide"
    )
    
    st.markdown("""
    <style>
    .stApp {
        background: linear-gradient(to right, #4e54c8, #8f94fb);
        color: white;
    }
                
    *{
        font-family: Arial, sans-serif;  
    }
                
    p {
        font-size: 18px !important;  
    }
                
    .stButton>button {
        background-color: #4CAF50;
        color: white;
    }
                
    .stTextInput>div>div>input,
    .stNumberInput>div>div>input,
    .stSelectbox>div>div>select {
        background-color: rgba(255, 255, 255, 0.1);
        color: white;
    }
    </style>
    """, unsafe_allow_html=True)
```

Este CSS:
- Establece un fondo degradado para la aplicación
- Define la familia y el tamaño de fuente para los elementos de texto
- Estiliza los botones y campos de entrada para una mejor visibilidad sobre el fondo degradado

## Conclusión

Esta aplicación Python demuestra el uso de Streamlit para crear una interfaz web interactiva para varias funciones matemáticas y de procesamiento de datos. Muestra varios conceptos de programación en Python, incluyendo definiciones de funciones, manejo de parámetros, comprensiones de lista y estructuras de control. El uso de Streamlit permite la creación fácil de interfaces de usuario basadas en web, mientras que el CSS personalizado mejora el atractivo visual de la aplicación.
