


import streamlit as st

st.set_page_config(
    page_title="Teams", # título da página
    page_icon="⚽", # 
    layout="wide"
)

# capturando o dataframe da sessão carregado na página home
df_data = st.session_state["data"]

clubes = df_data["Club"].unique() # pegando os valore únicos da coluna Club
club = st.sidebar.selectbox("Clube", clubes) # colocando um selectbox na sidebar para escolher o clube

# pegando o valor da primeira seleçao e filtrando o dataframe
df_filtered = df_data[(df_data["Club"] == club)].set_index("Name") # colocando o Name como índice

st.image(df_filtered.iloc[0]["Club Logo"]) # capturando a logo do clube
st.markdown(f"## {club}") # colocando o nome do clube na tela

columns = ["Age", "Photo", "Flag", "Overall", 'Value(£)', 'Wage(£)', 'Joined', 
           'Height(cm.)', 'Weight(lbs.)',
           'Contract Valid Until', 'Release Clause(£)']

st.dataframe(df_filtered[columns],
             column_config={
                 "Overall": st.column_config.ProgressColumn(   # colocando uma barra de progresso na coluna Overall
                     "Overall",  # renomeando a coluna a ser formatada
                     format="%d", # formato do valor da barra de progresso (inteiro) 
                     min_value=0,  # valor mínimo
                     max_value=100 # valor máximo
                 ),
                 "Wage(£)": st.column_config.ProgressColumn( # colocando uma barra de progresso na coluna Wage(£)
                     "Weekly Wage", # renomeando a coluna a ser formatada     
                     format="£%f",  # formato do valor da barra de progresso (moeda)
                     min_value=0,  # valor mínimo
                     max_value=df_filtered["Wage(£)"].max() # valor máximo (o maior valor da coluna)
                 ),
                "Photo": st.column_config.ImageColumn(), # capturando as imagens da coluna Photo
                "Flag": st.column_config.ImageColumn("Country"), # capturando as imagens da coluna Flag e renomeando para Country  
             })



