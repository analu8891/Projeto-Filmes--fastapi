# pip install stremlit requests
import streamlit as st
import requests

# URL da API fastapi
API_URL = "http://127.0.0.1:8000"

st.title("Gerenciador de filmes")

menu = st.sidebar.radio("Menu", 
                        ["Listar filmes", "Cadastrar filmes"]
    )
if menu == "Listar filmes":
    st.subheader("Todos os filmes")
    response = requests.get(f"{API_URL}/filmes")
    if response.status_code == 200:
        filmes = response.json().get("filmes", [])
    else:
        st.error("Erro ao conectar com a API.")