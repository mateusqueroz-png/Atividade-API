import streamlit as st
import requests

API = "http://127.0.0.1:8000/"

st.title("Controle de Estoque")

menu = st.sidebar.selectbox("Menu", ["Listar", "Adicionar", "Atualizar", "Excluir", "Total em Estoque"])

if menu == "Listar":
    r = requests.get(f"{API}/produtos/")
    if r.status_code == 200:
        for p in r.json():
            st.write(p)
    else:
        st.error("Erro ao buscar produtos.")

elif menu == "Adicionar":
    nome = st.text_input("Nome")
    categoria = st.text_input("Categoria")
    preco = st.number_input("Preço", step=0.01)
    quantidade = st.number_input("Quantidade", step=1)
    if st.button("Adicionar"):
        data = {"nome": nome, "categoria": categoria, "preco": preco, "quantidade": quantidade}
        r = requests.post(f"{API}/produtos/", json=data)
        st.success("Produto adicionado.")

elif menu == "Atualizar":
    id = st.number_input("ID", step=1)
    preco = st.number_input("Novo Preço", step=0.01)
    quantidade = st.number_input("Nova Quantidade", step=1)
    if st.button("Atualizar"):
        data = {"preco": preco, "quantidade": quantidade}
        r = requests.put(f"{API}/produtos/{int(id)}", json=data)
        st.success("Produto atualizado.")

elif menu == "Excluir":
    id = st.number_input("ID", step=1)
    if st.button("Excluir"):
        r = requests.delete(f"{API}/produtos/{int(id)}")
        st.success("Produto excluído.")

elif menu == "Total em Estoque":
    r = requests.get(f"{API}/produtos/")
    if r.status_code == 200:
        produtos = r.json()
        total = sum(p["preco"] * p["quantidade"] for p in produtos)
        st.metric("Valor Total do Estoque", f"R$ {total:.2f}")
