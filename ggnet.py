import streamlit as st

st.title('GGNET')
st.header('Manejo de APIs de Facebook, LinkedIn y ChatGPT')

selection = st.selectbox('Seleccionar', ['Envio de Correos', 'Creacion de Anuncios'])

if selection == 'Envio de Correos':
    destinatario = st.text_input('Ingrese un destinatario')
    placeholder = st.empty()
    input = placeholder.text_area('Contenido del Correo')
    generate_text = st.button('Generar Contenido', key=2)
    if generate_text:
        input = placeholder.text_area('Contenido del Correo', value='🚀💻 ¡GGNet: tu aliado tecnológico para el éxito empresarial! 💡🌐\n\nEn GGNet entendemos que la tecnología es fundamental para el crecimiento y el éxito de tu empresa. Por eso, ofrecemos una amplia gama de servicios de consultoría y soluciones de infraestructura de TI 🔧🌐, para que puedas aprovechar al máximo todo el potencial de la era digital.', key=1)

if selection == 'Creacion de Anuncios':
    app = st.selectbox('Seleccionar red social', ['Facebook', 'LinkedIn'])

    ad_topic = st.selectbox('Seleccionar tema del anuncio', ['Cloud Hosting', 'Desarrollo de Software', 'Capacitaciones', 'Plan especifico'])
    title_placeholder= st.empty()
    generate_title = st.button('Generar Titulo', key=3)
    description_placeholder= st.empty()
    generate_description= st.button('Generar Descripcion', key=4)
    content_placeholder = st.empty()
    generate_content = st.button('Generar Contenido', key=5)
    ad_title = title_placeholder.text_input('Titulo del Anuncio')
    ad_description = description_placeholder.text_area('Descripcion del Anuncio')
    ad_content = content_placeholder.text_area('Contenido del Anuncio')
    if generate_title:
        ad_title = title_placeholder.text_input('Titulo del Anuncio', value='GGNET, tu aliado en tecnologia.', key=6)
    if generate_description:
        ad_description = description_placeholder.text_area('Descripcion del Anuncio', value='Descubre el futuro de tu negocio con GGNet. Ofrecemos servicios de nube de última generación, soporte técnico 24/7 y desarrollo de software personalizado. Desde la nube hasta soluciones a medida, estamos listos para impulsar tu éxito. ¡Contáctanos hoy!', key=7)
    if generate_content:
        ad_content = content_placeholder.text_area('Contenido del Anuncio', value='🚀💻 ¡GGNet: tu aliado tecnológico para el éxito empresarial! 💡🌐\n\nEn GGNet entendemos que la tecnología es fundamental para el crecimiento y el éxito de tu empresa. Por eso, ofrecemos una amplia gama de servicios de consultoría y soluciones de infraestructura de TI 🔧🌐, para que puedas aprovechar al máximo todo el potencial de la era digital.', key=8)


    if app == 'Facebook':
        m = st.markdown("""
        <style>
        div.stButton > button:first-child {
            background-color: rgb(66 ,103 ,178);
            color: rgb(255 ,255 ,255);
        }
        </style>""", unsafe_allow_html=True)
    else:
        m = st.markdown("""
        <style> 
        div.stButton > button:first-child {
            background-color: rgb(0, 119, 181);
            color: rgb(255 ,255 ,255);
        }
        </style>""", unsafe_allow_html=True)
    b = st.button("Publicar Anuncio")
    if b:
        st.success('El anuncio fue enviado y esta en espera de aprobación')