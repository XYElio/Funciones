import streamlit as st

#CSS
def set_page_config():
    st.set_page_config(
        page_title="Funciones",
        page_icon="💻",
        layout="wide"
    )
    
    # CSS personalizado para el fondo y estilo general
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

# Funciones para los ejercicios
def saludar(nombre):
    return f"Hola, {nombre}"

def sumar(a, b):
    return a + b

def calcular_area_triangulo(base, altura):
    return 0.5 * base * altura

def calcular_precio_final(precio_original, descuento=10, impuesto=16):
    precio_con_descuento = precio_original * (1 - descuento/100)
    return precio_con_descuento * (1 + impuesto/100)

def sumar_lista(numeros):
    return sum(numeros)

def producto(nombre, cantidad=1, precio=10):
    return f"Producto: {nombre}, Cantidad: {cantidad}, Precio total: ${cantidad * precio}"

def numeros_pares_e_impares(numeros):
    pares = [num for num in numeros if num % 2 == 0]
    impares = [num for num in numeros if num % 2 != 0]
    return pares, impares

def multiplicar_todos(*args):
    return 1 if not args else args[0] if len(args) == 1 else args[0] * multiplicar_todos(*args[1:])

def informacion_personal(**kwargs):
    return "\n".join([f"{k}: {v}" for k, v in kwargs.items()])

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

# Funciones para la interfaz de usuario
def ui_saludo_simple():
    st.header("Bienvenida")
    nombre = st.text_input("Escribe tu nombre")
    if nombre:
        st.write(saludar(nombre))

def ui_suma_dos_numeros():
    st.header("Suma de dos números")
    a = st.number_input("Primer número", value=0.0, step=1.0)
    b = st.number_input("Segundo número", value=0.0, step=1.0)
    st.write(f"El resultado de la suma es: {sumar(a, b)}")

def ui_area_triangulo():
    st.header("Cálculo del área de un triángulo")
    base = st.number_input("Base del triángulo", min_value=0.0, step=1.0)
    altura = st.number_input("Altura del triángulo", min_value=0.0, step=1.0)
    st.write(f"El área calculada del triángulo es: {calcular_area_triangulo(base, altura)}")

def ui_calculadora_descuento():
    st.header("Calculadora de precio con descuento")
    precio = st.number_input("Precio original", min_value=0.0, step=1.0)
    descuento = st.number_input("Porcentaje de descuento", min_value=0.0, max_value=100.0, value=10.0, step=1.0)
    impuesto = st.number_input("Porcentaje de impuesto", min_value=0.0, max_value=100.0, value=16.0, step=1.0)
    st.write(f"El precio final calculado es: ${calcular_precio_final(precio, descuento, impuesto):.2f}")

def ui_suma_lista():
    st.header("Suma de valores en una lista")
    numeros = st.text_input("Ingresa los números separados por comas")
    if numeros:
        lista_numeros = [float(num.strip()) for num in numeros.split(',')]
        st.write(f"La suma de la lista es: {sumar_lista(lista_numeros)}")

def ui_producto_valores_predeterminados():
    st.header("Detalles de producto")
    nombre_producto = st.text_input("Nombre del producto")
    cantidad = st.number_input("Cantidad", min_value=1, value=1, step=1)
    precio = st.number_input("Precio por unidad", min_value=0.0, value=10.0, step=1.0)
    if nombre_producto:
        st.write(producto(nombre_producto, cantidad, precio))

def ui_numeros_pares_impares():
    st.header("Números pares e impares")
    numeros = st.text_input("Lista de enteros separados por comas")
    if numeros:
        lista_numeros = [int(float(num.strip())) for num in numeros.split(',')]
        pares, impares = numeros_pares_e_impares(lista_numeros)
        st.write(f"Números pares encontrados: {pares}")
        st.write(f"Números impares encontrados: {impares}")

def ui_multiplicacion_args():
    st.header("Multiplicación de valores múltiples")
    numeros = st.text_input("Lista de números (separados por comas)")
    if numeros:
        lista_numeros = [float(num.strip()) for num in numeros.split(',')]
        st.write(f"El resultado de la multiplicación es: {multiplicar_todos(*lista_numeros)}")

def ui_informacion_personal_kwargs():
    st.header("Recopilación de datos personales")
    nombre = st.text_input("Nombre completo")
    edad = st.number_input("Edad", min_value=0, value=0, step=1)
    ciudad = st.text_input("Ciudad")
    profesion = st.text_input("Profesión")
    if st.button("Mostrar información"):
        info = informacion_personal(nombre=nombre, edad=edad, ciudad=ciudad, profesion=profesion)
        st.write(info)

def ui_calculadora_flexible():
    st.header("Calculadora")
    a = st.number_input("Primer número", value=0.0, step=1.0)
    b = st.number_input("Segundo número", value=0.0, step=1.0)
    operacion = st.selectbox("Operación", ["Suma", "Resta", "Multiplicacion", "Division"])
    resultado = calculadora_flexible(a, b, operacion)
    st.write(f"El resultado de la operación es: {resultado}")

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

    # Contenedor principal con clase CSS
    with st.container():
        st.markdown('<div class="main-content">', unsafe_allow_html=True)
        
        if ejercicio in ejercicios:
            ejercicios[ejercicio]()
        else:
            st.error("Ejercicio no encontrado")
        
        st.markdown('</div>', unsafe_allow_html=True)

if __name__ == "__main__":
    main()