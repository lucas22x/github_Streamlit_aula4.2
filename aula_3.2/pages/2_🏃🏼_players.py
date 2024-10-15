
import streamlit as st

st.set_page_config(
    page_title="Players",
    page_icon="🏃‍♂️",
    layout="wide"
)

# capturando o dataframe da sessão carregado na página home
df_data = st.session_state["data"]

clubes = df_data["Club"].unique() # pegando os valore únicos da coluna Club
club = st.sidebar.selectbox("Clube", clubes) # colocando um selectbox na sidebar para escolher o clube

df_players = df_data[(df_data["Club"] == club)] # pegando o valor da primeira seleçao e filtrando o dataframe
players = df_players["Name"].unique() # pegando os valore únicos da coluna Name
player = st.sidebar.selectbox("Jogador", players) # colocando um selectbox na sidebar para escolher o jogador

player_stats = df_data[df_data["Name"] == player].iloc[0] # pegando as estatísticas do jogador selecionado

st.image(player_stats["Photo"]) # capturando a imagem do jogador
st.title(player_stats["Name"]) # colocando o nome do jogador na tela

st.markdown(f"**Clube:** {player_stats['Club']}") # texto com o nome do clube
st.markdown(f"**Posição:** {player_stats['Position']}") # texto com a posição do jogador

col1, col2, col3, col4,col5,col6 = st.columns(6) # dividindo em 4 colunas
col1.markdown(f"**Idade:** {player_stats['Age']}") # texto com a idade do jogador
col2.markdown(f"**Altura:** {player_stats['Height(cm.)'] / 100}") # texto com a altura do jogador
col3.markdown(f"**Peso:** {player_stats['Weight(lbs.)']*0.453:.2f}") # texto com o peso do jogador
st.divider() # colocando uma linha divisória

st.subheader(f"Overall {player_stats['Overall']}") # texto com o overall do jogador
st.progress(int(player_stats["Overall"])) # barra de progresso (de 0 a 100) com o overall do jogador

col1, col2, col3, col4,col5 = st.columns(5)
col1.metric(label="Valor de mercado", value=f"£ {player_stats['Value(£)']:,}") # metrica com o valor de mercado do jogador
col2.metric(label="Remuneração semanal", value=f"£ {player_stats['Wage(£)']:,}") # metrica com a remuneração semanal do jogador
col3.metric(label="Cláusula de rescisão", value=f"£ {player_stats['Release Clause(£)']:,}") # metrica com a cláusula de rescisão do jogador








