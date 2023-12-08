import streamlit as st

st.write('Para publicar una aplicación de Python en streamlit debes subirla a un repositorio en GitHub que incluya un archivo main de python y un archivo requirements.txt que describe las librerias que utiliza el script.')
st.write('El archivo requirements.txt se puede generar con la libreria [pipreqs](https://pypi.org/project/pipreqs/).')
st.write('Primero debes ir a https://share.streamlit.io/')
st.write('Deberas ingresar con una cuenta de GitHub para conectar tus repositorios.')
st.image('streamlit_share.png')
st.write('Una vez hayas ingresado, selecciona la opcion de nueva aplicación.')
st.write('Se te mostrara un formulario en donde deberas elegir el repositorio en el que se encuentra tu proyecto de streamlit, la rama de la cual deseas publicar, el archivo main y un nombre para la url.')
st.image('deploy.png')

st.write('Por ultimo deberas seleccionar la opción \'Deploy\' para publicar tu aplicación.')