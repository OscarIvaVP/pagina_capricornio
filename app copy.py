# -*- coding: utf-8 -*-
"""
Una aplicación web sencilla con Streamlit para mostrar un catálogo de pijamas y medias.
Versión con diseño mejorado usando contenedores.

Para ejecutar esta aplicación:
1. Instala Streamlit: pip install streamlit
2. Guarda este código en un archivo, por ejemplo, `app.py`.
3. Ejecuta el siguiente comando en tu terminal: streamlit run app.py
"""

import streamlit as st

def main():
    """
    Función principal que construye la página web del catálogo.
    """

    # --- Configuración de la Página ---
    st.set_page_config(
        page_title="Catálogo CAPRICORNO",
        page_icon="♑",
        layout="wide"
    )

    # --- Contenido del Catálogo ---
    st.markdown("<h1 style='text-align: center; font-size: 4em; font-weight: bold;'>CAPRICORNO</h1>", unsafe_allow_html=True)
    st.markdown("<h2 style='text-align: center;'>Catálogo</h2>", unsafe_allow_html=True)
    st.markdown("---")


    # --- Lista de Productos ---
    # Usamos una lista de diccionarios para almacenar la información de cada producto.
    # Esto facilita agregar, eliminar o modificar productos en el futuro.
    # Las URLs de las imágenes son de un servicio de placeholders. ¡Recuerda cambiarlas por tus propias fotos!
    productos = [
        {
            "nombre": "Pijama de Algodón 'Noches de Ensueño'",
            "descripcion": "Pijama de dos piezas, 100% algodón pima para garantizar la máxima suavidad y frescura.",
            "precio": "COP $89,900",
            "imagen": "productos/pijamaalgodon.jpg",
            "categoria": "Pijamas"
        },
        {
            "nombre": "Pijama de Satén 'Lujo y Confort'",
            "descripcion": "Elegante y sedosa pijama de satén. Perfecta para sentirte cómoda y sofisticada en casa.",
            "precio": "COP $120,500",
            "imagen": "productos/pijamasaten.png",
            "categoria": "Pijamas"
        },
        {
            "nombre": "Pijama Térmica 'Abrazo de Oso'",
            "descripcion": "Ideal para las noches frías. Fabricada en tela polar que te mantendrá siempre abrigada.",
            "precio": "COP $150,000",
            "imagen": "productos/pijamatermica.jpg",
            "categoria": "Pijamas"
        },
        {
            "nombre": "Medias de Lana 'Pies Calentitos'",
            "descripcion": "Pack de 3 pares de medias gruesas de lana. ¡El complemento perfecto para tu pijama!",
            "precio": "COP $35,000",
            "imagen": "productos/mediaslana.png",
            "categoria": "Medias"
        },
        {
            "nombre": "Medias Tobilleras 'Paso Ligero'",
            "descripcion": "Pack de 5 pares de medias tobilleras de algodón en colores variados. Perfectas para el día a día.",
            "precio": "COP $28,000",
            "imagen": "productos/mediastobilleras.png",
            "categoria": "Medias"
        },
        {
            "nombre": "Medias Divertidas 'Diseños Únicos'",
            "descripcion": "Dale un toque de alegría a tus pies con nuestros diseños exclusivos. ¡Colecciónalas todas!",
            "precio": "COP $15,000",
            "imagen": "productos/mediasdisenos.png",
            "categoria": "Medias"
        }
    ]

    # --- Sección de Pijamas ---
    st.header("Nuestras Pijamas")
    pijamas = [p for p in productos if p["categoria"] == "Pijamas"]
    cols_pijamas = st.columns(3)
    for i, producto in enumerate(pijamas):
        with cols_pijamas[i % 3]:
            # **CAMBIO**: Usamos un contenedor con borde para crear un efecto de "tarjeta".
            with st.container(border=True):
                # **CORRECCIÓN**: Cambiamos use_column_width por use_container_width.
                st.image(producto["imagen"], caption=producto["nombre"], use_container_width=True)
                st.subheader(producto["nombre"])
                st.write(producto["descripcion"])
                st.markdown(f"**Precio:** <span style='color: #28B463; font-weight: bold;'>{producto['precio']}</span>", unsafe_allow_html=True)
                if st.button(f"Comprar {producto['nombre']}", key=f"pijama_{i}"):
                    st.toast(f"¡'{producto['nombre']}' añadido al carrito!", icon="🛒")


    st.markdown("---")

    # --- Sección de Medias ---
    st.header("Nuestras Medias")
    medias = [p for p in productos if p["categoria"] == "Medias"]
    cols_medias = st.columns(3)
    for i, producto in enumerate(medias):
        with cols_medias[i % 3]:
            # **CAMBIO**: Usamos un contenedor con borde para crear un efecto de "tarjeta".
            with st.container(border=True):
                # **CORRECCIÓN**: Cambiamos use_column_width por use_container_width.
                st.image(producto["imagen"], caption=producto["nombre"], use_container_width=True)
                st.subheader(producto["nombre"])
                st.write(producto["descripcion"])
                st.markdown(f"**Precio:** <span style='color: #28B463; font-weight: bold;'>{producto['precio']}</span>", unsafe_allow_html=True)
                if st.button(f"Comprar {producto['nombre']}", key=f"media_{i}"):
                    st.toast(f"¡'{producto['nombre']}' añadido al carrito!", icon="🛒")

    # --- Pie de Página ---
    st.markdown("---")
    st.markdown("### ¿Tienes alguna pregunta?")
    st.markdown("Contáctanos por WhatsApp: [+57 312 561 4349](https://wa.me/5731256614349) o síguenos en Instagram [@DulcesSuenosPijamas](https://instagram.com).")


if __name__ == "__main__":
    main()
