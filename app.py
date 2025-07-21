# -*- coding: utf-8 -*-
"""
Una aplicación web con Streamlit para mostrar el catálogo de CAPRICORNO.
Versión con diseño de tarjetas, título personalizado y datos de contacto corregidos.

Para ejecutar esta aplicación:
1. Instala Streamlit: pip install streamlit
2. Guarda este código en un archivo, por ejemplo, `app.py`.
3. Crea una carpeta llamada `imagenes` y guarda ahí las fotos de tus productos.
4. Actualiza las rutas de las imágenes en la lista de `productos`.
5. Ejecuta el siguiente comando en tu terminal: streamlit run app.py
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
    # ¡IMPORTANTE! Aquí es donde debes poner las rutas a TUS propias imágenes.
    # He actualizado los ejemplos para que veas cómo se hace con una carpeta local "imagenes".
    productos = [
        {
            "nombre": "Pijama de Algodón 'Noches de Ensueño'",
            "descripcion": "Pijama de dos piezas, 100% algodón pima para garantizar la máxima suavidad y frescura.",
            "precio": "COP $89,900",
            "imagen": "imagenes/pijamaalgodon.jpg", # <- CAMBIA ESTO
            "categoria": "Pijamas"
        },
        {
            "nombre": "Pijama de Satén 'Lujo y Confort'",
            "descripcion": "Elegante y sedosa pijama de satén. Perfecta para sentirte cómoda y sofisticada en casa.",
            "precio": "COP $120,500",
            "imagen": "imagenes/pijamasaten.jpg", # <- CAMBIA ESTO
            "categoria": "Pijamas"
        },
        {
            "nombre": "Pijama Térmica 'Abrazo de Oso'",
            "descripcion": "Ideal para las noches frías. Fabricada en tela polar que te mantendrá siempre abrigada.",
            "precio": "COP $150,000",
            "imagen": "imagenes/pijamatermica.jpg", # <- CAMBIA ESTO
            "categoria": "Pijamas"
        },
        {
            "nombre": "Medias de Lana 'Pies Calentitos'",
            "descripcion": "Pack de 3 pares de medias gruesas de lana. ¡El complemento perfecto para tu pijama!",
            "precio": "COP $35,000",
            "imagen": "imagenes/mediaslana.jpg", # <- CAMBIA ESTO
            "categoria": "Medias"
        },
        {
            "nombre": "Medias Tobilleras 'Paso Ligero'",
            "descripcion": "Pack de 5 pares de medias tobilleras de algodón en colores variados. Perfectas para el día a día.",
            "precio": "COP $28,000",
            "imagen": "imagenes/mediastobilleras.jpg", # <- CAMBIA ESTO
            "categoria": "Medias"
        },
        {
            "nombre": "Medias Divertidas 'Diseños Únicos'",
            "descripcion": "Dale un toque de alegría a tus pies con nuestros diseños exclusivos. ¡Colecciónalas todas!",
            "precio": "COP $15,000",
            "imagen": "imagenes/mediasdivertidas.jpg", # <- CAMBIA ESTO
            "categoria": "Medias"
        }
    ]

    # --- Sección de Pijamas ---
    st.header("Nuestras Pijamas")
    pijamas = [p for p in productos if p["categoria"] == "Pijamas"]
    cols_pijamas = st.columns(3)
    for i, producto in enumerate(pijamas):
        with cols_pijamas[i % 3]:
            with st.container(border=True):
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
            with st.container(border=True):
                st.image(producto["imagen"], caption=producto["nombre"], use_container_width=True)
                st.subheader(producto["nombre"])
                st.write(producto["descripcion"])
                st.markdown(f"**Precio:** <span style='color: #28B463; font-weight: bold;'>{producto['precio']}</span>", unsafe_allow_html=True)
                if st.button(f"Comprar {producto['nombre']}", key=f"media_{i}"):
                    st.toast(f"¡'{producto['nombre']}' añadido al carrito!", icon="🛒")

    # --- Pie de Página ---
    st.markdown("---")
    st.markdown("### ¿Tienes alguna pregunta?")
    # **CORRECCIÓN**: Enlace de Instagram actualizado.
    st.markdown("Contáctanos por WhatsApp: [+57 312 561 4349](https://wa.me/573125614349) o síguenos en Instagram [@capricornio](https://instagram.com/capricornio).")


if __name__ == "__main__":
    main()
