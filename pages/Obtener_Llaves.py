import streamlit as st

st.write('Para modificar llaves o tokens de acceso para la aplicacion debes ir a https://share.streamlit.io/  en donde se encuentra un listado con las aplicaciones de streamlit')
st.write('En la seccion \'Secretos\' en configuracion de la aplicacion se encuentran todas las variables de entorno que no deben mostrarse publicamente')
st.write('Aqui debes agregar tu llave de OpenAI, ademas tambien pueden agregar tokens de acceso para Facebook y LinkedIn')
st.image('secrets.png')

facebook, linkedin, openai = st.tabs(['Facebook', 'LinkedIn', 'OpenAI'])

with openai:
    st.title('¿Como obtener llave del API de OpenAI?')

    st.write('Para obtener una llave del API de OpenAI y utilizarla para generar textos debes iniciar navegando a https://platform.openai.com/api-keys')

    st.write('Selecciona la opcion de crear nueva llave secreta, dale un nombre a tu nueva llave si deseas y selecciona crear nueva llave.')
    st.image('generate_key.png')
    st.image('key_modal.png')
    st.write('Despues de que la llave sea creada deberas guardarla en algun lugar seguro ya que OpenAI ya no volvera a mostrartela.')
    st.image('new_key.png')

with facebook:
    st.title('¿Como obtener token de acceso para el API de Facebook')

    st.write('Para obtener un token para el API de Meta debes iniciar navegando a https://developers.facebook.com/apps/')

    st.write('Selecciona la aplicacion de GGNET.')
    st.image('meta_app.png')
    st.write('En el menu superior coloca el cursor sobre la opción de \'Herramientas\' y selecciona el Explorador de Graph API.')
    st.image('tool.png')
    st.write('Copia el token que se muestra en esta pagina. Este es un token con expiracion de aproximadamente una hora en el siguiente paso se usara para crear uno con tiempo de expiración de 2 meses.')
    st.image('default_token.png')
    st.write('En el menu superior coloca el cursor sobre la opción de \'Herramientas\' y ahora selecciona el token debugger.')
    st.image('debug.png')
    st.write('Ingresa el token que obtuviste en el paso anterior y selecciona la opcion de extender token al final de la pagina.')
    st.image('extend_token.png')



with linkedin:
    st.title('¿Como obtener token de acceso para el API de LinkedIn')

    st.write('Para obtener una llave del API de LinkedIn y utilizarla para manejar publicaciones debes iniciar navegando a https://www.linkedin.com/developers/tools/oauth')

    st.write('Selecciona la opcion de crear token')
    st.image('linkedin_token.png')
    st.write('Selecciona la aplicaciòn GGNET.')
    st.image('select.png')
    st.write('Selecciona los permisos para el token.')
    st.image('permissions.png')
    st.write('Por ultimo usa el boton de generar token para obtenerlo.')
