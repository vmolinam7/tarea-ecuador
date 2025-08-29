import streamlit as st

# Configuración de página
st.set_page_config(
    page_title="Economía Digital en Ecuador",
    page_icon="💻",
    layout="wide"
)

# Menú lateral para navegación
st.sidebar.title("Navegación")
section = st.sidebar.radio("Ir a:", ["Inicio", "Diagnóstico", "Propuestas", "Ingeniero en Software", "Conclusiones", "Recursos"])

# Inicio
if section == "Inicio":
    st.title("💻 Economía Digital y Realidad Nacional Actual - Ecuador")
    st.image("https://upload.wikimedia.org/wikipedia/commons/thumb/e/e8/Flag_of_Ecuador.svg/320px-Flag_of_Ecuador.svg.png", width=200)
    st.write("Esta aplicación presenta un análisis sobre la economía digital en Ecuador y el papel del ingeniero en software en su desarrollo.")

# Diagnóstico
elif section == "Diagnóstico":
    st.header("📊 1. Diagnóstico de la Situación")
    st.subheader("Estado Actual de la Economía Digital en Ecuador")
    st.write("""
    - Ecuador ha avanzado en la adopción de tecnologías digitales, con un 60% de los hogares conectados a Internet.
    - Habilidades Digitales Limitadas: Ocupa el puesto 98 de 141 países en el índice de habilidades digitales.
    - Infraestructura y Conectividad: Brechas en cobertura de Internet, especialmente en áreas rurales.
    - Marco Regulatorio Insuficiente: Leyes no totalmente actualizadas para comercio electrónico y protección de datos.
    """)

    st.subheader("Comparativa con Otros Países")
    st.write("""
    - En comparación con España, Ecuador ha experimentado un crecimiento del 69% en el uso de herramientas digitales.
    - La implementación efectiva del comercio electrónico y la digitalización empresarial aún está en desarrollo.
    """)

# Propuestas
elif section == "Propuestas":
    st.header("💡 2. Propuestas de Soluciones")
    st.subheader("Fortalecimiento de la Educación y Capacitación Digital")
    st.write("""
    - Implementación de Programas de Formación en programación, ciberseguridad y análisis de datos.
    - Colaboración con Instituciones Académicas: Crear centros de innovación y laboratorios de desarrollo de software.
    """)

    st.subheader("Modernización del Marco Regulatorio")
    st.write("""
    - Actualización de Legislaciones: Reformar la Ley de Comercio Electrónico y proteger datos personales.
    - Fomento de la Competencia Justa: Evitar monopolios y promover innovación.
    """)

    st.subheader("Impulso a la Innovación y Desarrollo de Software")
    st.write("""
    - Creación de Ecosistemas de Innovación: Hubs tecnológicos y parques industriales digitales.
    - Apoyo a Startups Tecnológicas: Incentivos fiscales y financieros a soluciones digitales.
    """)

# Ingeniero en Software
elif section == "Ingeniero en Software":
    st.header("👨‍💻 3. Papel del Ingeniero en Software Ecuatoriano")
    st.write("""
    - Desarrollo de Soluciones Locales: Apps y plataformas digitales adaptadas a necesidades ecuatorianas.
    - Transformación Digital de Sectores Productivos: Automatización, gestión empresarial y análisis de datos.
    - Promoción de la Inclusión Digital: Facilitar acceso a servicios digitales en comunidades rurales.
    """)

    st.subheader("Propuestas para el País")
    st.write("""
    - Establecimiento de Políticas de Apoyo: Reconocer e impulsar al ingeniero de software.
    - Fomento de Investigación y Desarrollo (I+D): Financiamiento estatal y colaboración privada.
    - Creación de Redes Profesionales: Conectar ingenieros, empresas y organismos gubernamentales.
    """)

# Conclusiones
elif section == "Conclusiones":
    st.header("✅ 4. Conclusiones")
    st.write("""
    - Necesidad de una Transformación Digital Integral: Educación, infraestructura, regulación e innovación.
    - Rol Fundamental del Ingeniero en Software: Clave para competitividad y bienestar social.
    - Compromiso Gubernamental y Privado: Trabajo conjunto para un entorno favorable para la economía digital.
    """)

# Recursos
elif section == "Recursos":
    st.header("📺 Recurso adicional")
    st.write("Video sobre Economía Digital en Ecuador:")
    st.video("https://www.youtube.com/watch?v=bN-CSkOJ_8o")  # video embebido
