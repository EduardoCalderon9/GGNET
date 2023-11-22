import streamlit as st
import requests
from openai import OpenAI
import json

st.set_page_config(layout="wide")
st.title('GGNET')
st.header('Manejo de APIs de Facebook, LinkedIn y ChatGPT')
query_params = st.experimental_get_query_params()

if 'title' not in st.session_state:
    st.session_state['title'] = ''

if 'content' not in st.session_state:
    st.session_state['content'] = ''


#with st.sidebar:
#    st.text('a')


cloud_tab, internet_tab = st.tabs(['Cloud', 'Internet'])
with cloud_tab:
    with st.expander("Configuración"):
        key = st.text_input("OpenAI API Key")
        st.caption("Por seguridad debes introducir tu llave del API de OpenAI de forma manual. Si no sabes como obtenerla consulta 'Obtener llave de OpenAI'")
        ggnet_description = st.text_area(label='Descripcion de GGNET', value="Generas textos para correos y anuncios para una empresa llamada GGNET.  \nGGNET es una empresa que ofrece distintos servicios en la nube, estos incluyen Hosting confiable y seguro; Imágenes de Ubuntu, Debian, CentOS y demás sistemas operativos; Migraciones, Snapshots, Almacenamiento, Balanceadores de carga, Dominios y SSL.  \nGGNET también ofrece servicios en la nube ofrecen el servicio de desarrollo de software que incluye desarrollo web, móvil y de escritorio, además de capacitaciones y seguimiento de proyectos de software.  \nEl slogan de la empresa es 'Tu aliado estratégico en tecnología' ")
        st.caption("Esta descripción le explica a ChatGPT que es GGNET y que servicios ofrece. Para mejores resultados esta debe ser lo mas detallada posible.")

    if key:
        client = OpenAI(api_key=key) 
    selection = st.selectbox('Seleccionar', ['Envio de Correos', 'Creacion de Anuncios', 'Peticion Personalizada'])
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
        ad_topic = st.text_input('Describir tema del anuncio')
        indications = st.text_input('Indicaciones adicionales:')

        title_placeholder= st.empty()
        generate_title = st.button('Generar Titulo', key=3)

        content_placeholder = st.empty()
        generate_content = st.button('Generar Contenido', key=5)

        ad_title = st.text_input('Titulo del Anuncio', value=st.session_state.title.replace('\n', '  \n'), key=6)
        ad_content = st.text_area('Contenido del Anuncio', value=st.session_state.content.replace('\n', '  \n'), key=8)


        if generate_title:
            completion = client.chat.completions.create(
            model="gpt-3.5-turbo",
            messages=[
                {"role": "system", "content": ggnet_description},
                {"role": "user", "content": f"Escribe el titulo para un post en {app} sobre {ad_topic}. {indications}"}
            ]
            )
            st.session_state.title = completion.choices[0].message.content
            #ad_title = title_placeholder.text_input('Titulo del Anuncio', value=st.session_state.title.replace('\n', '  \n'), key=6)
        if generate_content:
            completion_content= client.chat.completions.create(
            model="gpt-3.5-turbo",
            messages=[
                {"role": "system", "content": ggnet_description},
                {"role": "user", "content": f"Escribe el contenido para un post en {app} sobre {ad_topic}. {indications}"}
            ]
            )
            st.session_state.content = completion_content.choices[0].message.content
    
            #ad_content = content_placeholder.text_area('Contenido del Anuncio', value=st.session_state.content.replace('\n', '  \n'), key=8)


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
        a={ "author": "urn:li:organization:100145909",
                        "commentary": 'a',
                        "visibility": "PUBLIC",
                        "distribution": json.dumps(obj={
                            "feedDistribution": "MAIN_FEED",
                            "targetEntities": [],
                            "thirdPartyDistributionChannels": []
                        }),
                        "lifecycleState": "PUBLISHED"
                        }
        if b:
            url = "https://api.linkedin.com/rest/posts?oauth2_access_token=AQVRSeKjU8njn_XWZ93Jad8mBf31qpiZyWc996DR17eGk-cfKV084Qs3OpdulIXGKPweU4M6YeeoIrg7SzXhNqcETaoqkyF763mUxXwd9zosH17FpVA_zNbGBzliCpCIH_VEHA9botL4rm9hmEAx02KznliNlNcHHFIzMU5Uap3lmpyd9yzy9VaB2myVlVAA_Nx65UOamJPbLnd_674uTBl86W2b1mFildud53r2RDwR8kvCGlDb-OWPAoN5KQGkSseCzRzXp4pLHrfJSES3K7WubHBedS2rsyZU-AkLPMN3zXu-28ChwTjYswRZSALZLV4d9yGfk6VRc_-cfHTh77qVNzakdg"

            payload = json.dumps({
            "author": "urn:li:organization:100145909",
            "commentary": f"{ad_title}\n\n{ad_content}",
            "visibility": "PUBLIC",
            "distribution": {
                "feedDistribution": "MAIN_FEED",
                "targetEntities": [],
                "thirdPartyDistributionChannels": []
            },
            "lifecycleState": "PUBLISHED",
            "isReshareDisabledByAuthor": False
            })
            headers = {
            'Linkedin-Version': '202304',
            'Content-Type': 'application/json'
            }

            response = requests.request("POST", url, headers=headers, data=payload)

            print(response.text)

            print(response.content)
            st.success('El anuncio fue enviado y esta en espera de aprobación')


with internet_tab:
    with st.expander("Configuración"):
        key = st.text_input("OpenAI API Key", key='fd')
        st.caption("Por seguridad debes introducir tu llave del API de OpenAI de forma manual. Si no sabes como obtenerla consulta 'Obtener llave de OpenAI'")
        ggnet_description = st.text_area(label='Descripcion de GGNET', value="Generas textos para correos y anuncios para una empresa llamada GGNET.  \nGGNET es una empresa que ofrece planes de internet para tres condominios (Colinas del Norte, Colinas del Norte 2 y El Fiscal). \nEl slogan de la empresa es 'Tu aliado estratégico en tecnología' ")
        st.caption("Esta descripción le explica a ChatGPT que es GGNET y que servicios ofrece. Para mejores resultados esta debe ser lo mas detallada posible.")

    if key:
        client = OpenAI(api_key=key) 
    selection = st.selectbox('Seleccionar', ['Envio de Correos', 'Creacion de Anuncios', 'Peticion Personalizada'], key='select')
    print('render')
    if selection == 'Envio de Correos':
        destinatario = st.text_input('Ingrese un destinatario', key=898)
        placeholder = st.empty()
        input = placeholder.text_area('Contenido del Correo', key='area')
        generate_text = st.button('Generar Contenido', key=22)
        if generate_text:
            input = placeholder.text_area('Contenido del Correo', value='🚀💻 ¡GGNet: tu aliado tecnológico para el éxito empresarial! 💡🌐\n\nEn GGNet entendemos que la tecnología es fundamental para el crecimiento y el éxito de tu empresa. Por eso, ofrecemos una amplia gama de servicios de consultoría y soluciones de infraestructura de TI 🔧🌐, para que puedas aprovechar al máximo todo el potencial de la era digital.', key=1)

    if selection == 'Creacion de Anuncios':
        app = st.selectbox('Seleccionar red social', ['Facebook', 'LinkedIn'])
        ad_topic = st.text_input('Describir tema del anuncio')
        indications = st.text_input('Indicaciones adicionales:')

        title_placeholder= st.empty()
        generate_title = st.button('Generar Titulo', key=32)

        content_placeholder = st.empty()
        generate_content = st.button('Generar Contenido', key=52)

        ad_title = title_placeholder.text_input('Titulo del Anuncio', key=42)
        ad_content = content_placeholder.text_area('Contenido del Anuncio', key=000)


        if generate_title:
            completion = client.chat.completions.create(
            model="gpt-3.5-turbo",
            messages=[
                {"role": "system", "content": ggnet_description},
                {"role": "user", "content": f"Escribe el titulo para un post en {app} sobre {ad_topic}. {indications}"}
            ]
            )
            ad_title = title_placeholder.text_input('Titulo del Anuncio', value=completion.choices[0].message.content, key=62)
        if generate_content:
            completion_content= client.chat.completions.create(
            model="gpt-3.5-turbo",
            messages=[
                {"role": "system", "content": ggnet_description},
                {"role": "user", "content": f"Escribe el contenido para un post en {app} sobre {ad_topic}. {indications}"}
            ]
            )
    
            ad_content = content_placeholder.text_area('Contenido del Anuncio', value=completion_content.choices[0].message.content.replace('\n', '  \n'), key=82)


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
                        data={
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
                        }, 
                        headers={'LinkedIn-Version': '202304', 'Linkedin-Version': '202304'})
            print(linkedInRequest)
            st.success('El anuncio fue enviado y esta en espera de aprobación')
