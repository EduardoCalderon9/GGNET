import streamlit as st
import requests
from openai import OpenAI
import json

st.set_page_config(page_title="GGNET", page_icon="📊", layout="wide" )
st.title('GGNET')
st.header('Manejo de APIs de Facebook, LinkedIn y ChatGPT')
query_params = st.experimental_get_query_params()

if 'title' not in st.session_state:
    st.session_state['title'] = ''

if 'content' not in st.session_state:
    st.session_state['content'] = ''

if 'idea' not in st.session_state:
    st.session_state['idea'] = ''

if 'script' not in st.session_state:
    st.session_state['script'] = ''

if 'cloud_custom' not in st.session_state:
    st.session_state['cloud_custom'] = ''

if 'internet_custom' not in st.session_state:
    st.session_state['internet_custom'] = ''

def generate_text(system, user):
    '''Funcion utilizada para generar textos con el modelo gpt 3.5 turbo, el parametro system representa el mensaje de configuracion inicial y user representa la peticion deseada'''
    try:
        completion = client.chat.completions.create(
            model="gpt-3.5-turbo",
            messages=[
                {"role": "system", "content": system},
                {"role": "user", "content": user}
            ]
        )
        return completion.choices[0].message.content.replace('\n', '  \n')
    except:
        print('An exception occurred')
        return 'Ocurrio un error, intentelo mas tarde.'

def generate_title(system, user):
    st.session_state.cloud_title = generate_text(system, user)
    st.session_state.internet_title = generate_text(system, user)

def generate_content(system, user):
    st.session_state.cloud_content = generate_text(system, user)
    st.session_state.internet_content = generate_text(system, user)

def generate_idea(system, user):
    st.session_state.cloud_idea = generate_text(system, user)
    st.session_state.internet_idea = generate_text(system, user)

def generate_script(system, user):
    st.session_state.cloud_script = generate_text(system, user)
    st.session_state.internet_script = generate_text(system, user)

def generate_custom(system, user):
    st.session_state.cloud_custom = generate_text(system, user)
    st.session_state.internet_custom = generate_text(system, user)

cloud_tab, internet_tab = st.tabs(['Cloud', 'Internet'])
with cloud_tab:
    with st.expander("Configuración"):
        ggnet_description = st.text_area(label='Descripcion de GGNET', value="Generas textos para correos y anuncios para una empresa llamada GGNET.  \nGGNET es una empresa que ofrece distintos servicios en la nube, estos incluyen Hosting confiable y seguro; Imágenes de Ubuntu, Debian, CentOS y demás sistemas operativos; Migraciones, Snapshots, Almacenamiento, Balanceadores de carga, Dominios y SSL.  \nGGNET también ofrece servicios en la nube ofrecen el servicio de desarrollo de software que incluye desarrollo web, móvil y de escritorio, además de capacitaciones y seguimiento de proyectos de software.  \nEl slogan de la empresa es 'Tu aliado estratégico en tecnología' ")
        st.caption("Esta descripción le explica a ChatGPT que es GGNET y que servicios ofrece. Para mejores resultados esta debe ser lo mas detallada posible.")
    
    client = OpenAI(api_key=st.secrets['OPENAI_KEY']) 
    selection = st.selectbox('Seleccionar funcion', ['Creacion de Anuncios','Ideas para videos', 'Petición Personalizada'], key='cloud_select')

    if selection == 'Petición Personalizada':
        req = st.text_input('Petición', key='cloud_req')
        generate_script = st.button('Generar Respuesta', key='cloud_gen_custom', on_click=generate_custom, args=[ggnet_description, req])
        cloud_custom = st.text_area('Respuesta', key='cloud_custom')


    if selection == 'Ideas para videos':
        ad_topic = st.text_input('Describir tema del video', key='cloud_video_topic')
        custom = st.text_input('Indicaciones adicionales:', key='cloud_video_custom')
        duration = st.text_input('Cuanto deseas que dure el video:', key='cloud_video_duration')
        st.divider()
        script = st.text_area('Guión del Anuncio', key='cloud_script')
        generate_script = st.button('Generar Guión', key='cloud_gen_script', on_click=generate_script, args=[ggnet_description, f"Escribe un guion para un anuncio de video sobre {ad_topic} con una duración de {duration}. {custom}"])

        idea = st.text_area('Idea Visual', key='cloud_idea')
        generate_idea = st.button('Generar idea', key='gen_cloud_idea', on_click=generate_idea, args=[ggnet_description, f"Dame una idea sobre lo que podria mostrar en un video sobre {ad_topic}. {custom}"])

    if selection == 'Creacion de Anuncios':
        app = st.selectbox('Seleccionar red social', ['Facebook', 'LinkedIn'], key='cloud_app')
        ad_topic = st.text_input('Describir tema del anuncio', key='cloud_topic')
        custom = st.text_input('Indicaciones adicionales:', key='cloud_custom')

        st.divider()
        ad_title = st.text_input('Titulo del Anuncio', key='cloud_title')
        title_button = st.button('Generar Titulo', key='cloud_title_btn', on_click=generate_title, args=[ggnet_description, f"Escribe el titulo para un post en {app} sobre {ad_topic}. {custom}"])

        ad_content = st.text_area('Contenido del Anuncio', key='cloud_content')
        content_button = st.button('Generar Contenido', key='cloud_content_btn', on_click=generate_content, args=[ggnet_description, f"Escribe el contenido para un post en {app} sobre {ad_topic}. {custom}"])


        if app == 'Facebook':
            st.markdown("""
            <style>
            div.stButton > button:first-child {
                background-color: rgb(66 ,103 ,178);
                color: rgb(255 ,255 ,255);
            }
            </style>""", unsafe_allow_html=True)
        else:
            st.markdown("""
            <style> 
            div.stButton > button:first-child {
                background-color: rgb(0, 119, 181);
                color: rgb(255 ,255 ,255);
            }
            </style>""", unsafe_allow_html=True)
        publish = st.button("Publicar Anuncio", key='cloud_post')
       
        if publish:
            url = f"https://api.linkedin.com/rest/posts?oauth2_access_token={st.secrets['CLOUD_LINKEDIN_TOKEN']}"

            payload = json.dumps({
            "author": f"urn:li:organization:{st.secrets['CLOUD_LINKEDIN_AUTHOR']}",
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
            st.success('El anuncio fue enviado y esta en espera de aprobación')


with internet_tab:
    with st.expander("Configuración"):
        ggnet_description = st.text_area(label='Descripcion de GGNET', value="Generas textos para correos y anuncios para una empresa llamada GGNET.  \nGGNET es una empresa que ofrece planes de internet para tres condominios (Colinas del Norte, Colinas del Norte 2 y El Fiscal).  \nAdemas de los planes de internet, GGNET tambien ofrece una aplicación de streaming  \nEl slogan de la empresa es 'Tu aliado estratégico en tecnología' ")
        st.caption("Esta descripción le explica a ChatGPT que es GGNET y que servicios ofrece. Para mejores resultados esta debe ser lo mas detallada posible.")

    client = OpenAI(api_key=st.secrets['OPENAI_KEY']) 
    selection = st.selectbox('Seleccionar funcion', ['Creacion de Anuncios', 'Ideas para videos', 'Petición Personalizada'], key='internet_select')
   
    if selection == 'Petición Personalizada':
        req = st.text_input('Petición', key='cloud_req')
        st.divider()
        cloud_custom = st.text_area('Respuesta', key='cloud_custom')
        generate_script = st.button('Generar Respuesta', key='cloud_gen_custom', on_click=generate_custom, args=[ggnet_description, {req}])


    if selection == 'Ideas para videos':
        ad_topic = st.text_input('Describir tema del video', key='internet_video_topic')
        custom = st.text_input('Indicaciones adicionales:', key='internet_video_custom')
        duration = st.text_input('Cuanto deseas que dure el video:', key='internet_video_duration')
        st.divider()
        script = st.text_area('Guión del Anuncio', key='internet_script')
        generate_script = st.button('Generar Guión', key='internet_gen_script', on_click=generate_script, args=[ggnet_description, f"Escribe un guion para un anuncio de video sobre {ad_topic} con una duración de {duration}. {custom}"])

        idea = st.text_area('Idea Visual', key='internet_idea')
        generate_idea = st.button('Generar idea', key='gen_internet_idea', on_click=generate_idea, args=[ggnet_description, f"Dame una idea sobre lo que podria mostrar en un video sobre {ad_topic}. {custom}"])

    if selection == 'Creacion de Anuncios':
        app = st.selectbox('Seleccionar red social', ['Facebook', 'LinkedIn'], key='internet_app')
        ad_topic = st.text_input('Describir tema del anuncio', key='internet_topic')
        custom = st.text_input('Indicaciones adicionales:', key='internet_custom')

        st.divider()
        ad_title = st.text_input('Titulo del Anuncio', key='internet_title')
        title_button = st.button('Generar Titulo', key='internet_title_btn', on_click=generate_title, args=[ggnet_description, f"Escribe el titulo para un post en {app} sobre {ad_topic}. {custom}"])

        ad_content = st.text_area('Contenido del Anuncio', key='internet_content')
        content_button = st.button('Generar Contenido', key='internet_content_btn', on_click=generate_content, args=[ggnet_description, f"Escribe el contenido para un post en {app} sobre {ad_topic}. {custom}"])


        if app == 'Facebook':
            st.markdown("""
            <style>
            div.stButton > button:first-child {
                background-color: rgb(66 ,103 ,178);
                color: rgb(255 ,255 ,255);
            }
            </style>""", unsafe_allow_html=True)
        else:
            st.markdown("""
            <style> 
            div.stButton > button:first-child {
                background-color: rgb(0, 119, 181);
                color: rgb(255 ,255 ,255);
            }
            </style>""", unsafe_allow_html=True)
        publish = st.button("Publicar Anuncio", key='internet_post')
       
        if publish:
            url = f"https://api.linkedin.com/rest/posts?oauth2_access_token={st.secrets['INTERNET_LINKEDIN_TOKEN']}"

            payload = json.dumps({
            "author": f"urn:li:organization:{st.secrets['INTERNET_LINKEDIN_AUTHOR']}",
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

            st.success('El anuncio fue enviado y esta en espera de aprobación')
