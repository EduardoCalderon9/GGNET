import streamlit as st
import requests
from openai import OpenAI

key = st.text_input('OpenAI API Key')
client = OpenAI(api_key=key) 


st.title('GGNET')
st.header('Manejo de APIs de Facebook, LinkedIn y ChatGPT')



selection = st.selectbox('Seleccionar', ['Envio de Correos', 'Creacion de Anuncios'])
print('render')
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
    content_placeholder = st.empty()
    generate_content = st.button('Generar Contenido', key=5)
    ad_title = title_placeholder.text_input('Titulo del Anuncio')
    ad_content = content_placeholder.text_area('Contenido del Anuncio')
    if generate_title:
        completion = client.chat.completions.create(
        model="gpt-3.5-turbo",
        messages=[
            {"role": "system", "content": "Generas textos para correos y anuncios para una empresa llamada GGNET. GGNET es una empresa que ofrece distintos servicios en la nube, estos incluyen Hosting confiable y seguro; Imágenes de Ubuntu, Debian, CentOs y demás sistemas operativos; Migraciones, Snapshots, Almacenamiento, Balanceadores de carga , Dominios y SSL. GGNET tambien ofrece servicios en la nube ofrecen el servicio de desarrollo de software que incluye desarrollo web, movil y de escritorio, ademas de capacitaciones y seguimiento de proyectos de software. El slogan de la empresa es 'Tu aliado estrategico en tecnologia' "},
            {"role": "user", "content": "Escribe el titulo para un post en linkedIn sobre los servicios de desarrollo de software. El titulo debe ser conciso debe incluir emojis."}

        ]
        )
        ad_title = title_placeholder.text_input('Titulo del Anuncio', value=completion.choices[0].message.content, key=6)
    if generate_content:
        completion_content= client.chat.completions.create(
        model="gpt-3.5-turbo",
        messages=[
            {"role": "system", "content": "Generas textos para correos y anuncios para una empresa llamada GGNET. GGNET es una empresa que ofrece distintos servicios en la nube, estos incluyen Hosting confiable y seguro; Imágenes de Ubuntu, Debian, CentOs y demás sistemas operativos; Migraciones, Snapshots, Almacenamiento, Balanceadores de carga , Dominios y SSL. GGNET tambien ofrece servicios en la nube ofrecen el servicio de desarrollo de software que incluye desarrollo web, movil y de escritorio, ademas de capacitaciones y seguimiento de proyectos de software. El slogan de la empresa es 'Tu aliado estrategico en tecnologia' "},
            {"role": "user", "content": "Escribe el texto para un post en linkedIn sobre los servicios de desarrollo de software. El texto no debe ser muy largo y debe incluir emojis."}
        ]
        )
   
        ad_content = content_placeholder.text_area('Contenido del Anuncio', value=completion_content.choices[0].message.content.replace('\n', '  \n'), key=8)


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
        linkedInRequest = requests.post('https://api.linkedin.com/rest/posts?oauth2_access_token=AQVRSeKjU8njn_XWZ93Jad8mBf31qpiZyWc996DR17eGk-cfKV084Qs3OpdulIXGKPweU4M6YeeoIrg7SzXhNqcETaoqkyF763mUxXwd9zosH17FpVA_zNbGBzliCpCIH_VEHA9botL4rm9hmEAx02KznliNlNcHHFIzMU5Uap3lmpyd9yzy9VaB2myVlVAA_Nx65UOamJPbLnd_674uTBl86W2b1mFildud53r2RDwR8kvCGlDb-OWPAoN5KQGkSseCzRzXp4pLHrfJSES3K7WubHBedS2rsyZU-AkLPMN3zXu-28ChwTjYswRZSALZLV4d9yGfk6VRc_-cfHTh77qVNzakdg',
                    {
                    "author": "urn:li:organization:100145909",
                    "commentary": f'{ad_title}\n\n{ad_content}',
                    "visibility": "PUBLIC",
                    "distribution": {
                        "feedDistribution": "MAIN_FEED",
                        "targetEntities": [],
                        "thirdPartyDistributionChannels": []
                    },
                    "lifecycleState": "PUBLISHED",
                    "isReshareDisabledByAuthor": False
                    })
        print(linkedInRequest)
        st.success('El anuncio fue enviado y esta en espera de aprobación')
