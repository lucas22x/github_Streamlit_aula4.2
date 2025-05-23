

# oi
# referente a (( 7 - Criando Aplicativos Web com Streamlit\codigos_das_aulas\aula_3.2 ))


import os
# os.system('cls')  # nao utilizar para poder ver o localhost do streamlit no terminal
import streamlit as st
import pandas as pd
from pathlib import Path
from datetime import datetime 
import webbrowser
import openai  # nao tem por padrao no cloud do streamlit

# executando
# //////////////////////////////////////////////////////////////
# digitar no terminal o comando abaixo para ((acessar a pasta)) onde esta o arquivo 1_🏠_home.py
#   1- considerando que esta em :  PS C:\1_EstudosPython\codigos_Aplicacoes_IA> 
#   2- entao digita no terminal:
#       cd "7 - Criando Aplicativos Web com Streamlit\codigos_das_aulas\aula_3.2" 

# ou 1-digita no terminal ( cd\ ) para ir para a raiz                                
#    2- verifica o caminho ate a pasta onde o arquivo esta com o codigo :
#            caminho = Path(os.path.dirname(__file__))
#    3- digita no terminal cd "caminho ate a pasta onde esta o arquivo"

# digitar no terminal o comando abaixo para executar o arquivo 1_🏠_home.py (vai abrir no navegador)    
#     streamlit run 1_🏠_home.py
# //////////////////////////////////////////////////////////////
st.set_page_config(
    page_title="Home",
    page_icon="🏡",
    layout="wide"
)

# nao funciona na cloue do streamlit ------------------
# aqui so acha nesse PC onde foi criado o projeto
# caminho = Path('C:\\1_EstudosPython\\codigos_Aplicacoes_IA\\7 - Criando Aplicativos Web com Streamlit\\codigos_das_aulas\\aula_3.2\\datasets')
# caminho_arquivo_1 = caminho / 'CLEAN_FIFA23_official_data.csv'

# assim funciona na cloue do streamlit ----------------
# para rodar e achar o arquivo em qualquer PC
# pois sera enviado a claud do stremalit e tem que achar o arquivo la
caminho = Path(os.path.dirname(__file__)) / 'datasets' # endereço da pasta (seja qual for) onde esta o arquivo atual + pasta datasets (que esta dentro da pasta do arquivo atual)
caminho_arquivo_1 = caminho / 'CLEAN_FIFA23_official_data.csv'


# garantir que o DataFrame seja carregado e processado apenas uma vez por sessão
if "data" not in st.session_state: # verificando se a sessao tem o dataframe
    # configurando o dataframe com funçoes do pandas
    df_data = pd.read_csv(caminho_arquivo_1, index_col=0) # abrindo o arquivo csv e colocando a coluna 0 como index
    df_data = df_data[df_data["Contract Valid Until"] >= datetime.today().year] # filtrando a coluna "Contract Valid Until" para valores maiores ou iguais ao ano atual
    df_data = df_data[df_data["Value(£)"] > 0] # filtrando a coluna "Value(£)" para valores maiores que 0
    df_data = df_data.sort_values(by="Overall", ascending=False) # ordenando a coluna "Overall" de forma decrescente
    # colocando o dataframe na sessao para ser utilizado em outras paginas  
    st.session_state["data"] = df_data # colocando o dataframe na sessao para ser utilizado em outras paginas


st.markdown("# FIFA23 OFFICIAL DATASET! ⚽️") # colocando texto na tela
st.sidebar.markdown("Desenvolvido por [Asimov Academy](https://asimov.academy)")

# nao funciona na cloue do streamlit ------------------
# btn = st.button("Acesse os dados no Kaggle") # colocando botao na tela
# if btn: # vinculando o botao a um link
#     webbrowser.open_new_tab("https://www.kaggle.com/datasets/kevwesophia/fifa23-official-datasetclean-data")

# assim funciona na cloue do streamlit ----------------
btn = st.link_button(
    "Acesse os dados no Kaggle",  # colocando botao na tela
    "https://www.kaggle.com/datasets/kevwesophia/fifa23-official-datasetclean-data" # vinculando o botao a um link
    ) 



st.markdown(   # colocando texto na tela
    """
    O conjunto de dados
    de jogadores de futebol de 2017 a 2023 fornece informações 
    abrangentes sobre jogadores de futebol profissionais.
    O conjunto de dados contém uma ampla gama de atributos, incluindo dados demográficos 
    do jogador, características físicas, estatísticas de jogo, detalhes do contrato e 
    afiliações de clubes. 
    
    Com **mais de 17.000 registros**, este conjunto de dados oferece um recurso valioso para 
    analistas de futebol, pesquisadores e entusiastas interessados em explorar vários 
    aspectos do mundo do futebol, pois permite estudar atributos de jogadores, métricas de 
    desempenho, avaliação de mercado, análise de clubes, posicionamento de jogadores e 
    desenvolvimento do jogador ao longo do tempo.
"""
)





