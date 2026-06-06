import joblib
import pandas as pd
import streamlit as st
from css import load_css
import time

st.set_page_config(
    page_title="Mundial 2026 Predictor",
    page_icon="🏆",
    layout="centered"
)

st.title("Mundial 2026 Predictor")
st.caption("Simulación basada en ELO + ML")

# styles.py
st.markdown(load_css(), unsafe_allow_html=True)

st.markdown(
    """
    <div class="footer">
        © 2026 · By Jennifer Páramo
    </div>
    """,
    unsafe_allow_html=True
)

model = joblib.load("models/model.pkl")
scaler = joblib.load("models/scaler.pkl")
feature_cols = joblib.load("models/features.pkl")
elo_dict = joblib.load("models/elo_dict.pkl")

df_teams = pd.read_csv("data/processed/world_cup_teams.csv")

df_teams["team_key"] = df_teams["team_key"].str.strip()
df_teams["team_name"] = df_teams["team_name"].str.strip()

teams = sorted(df_teams["team_key"].tolist())
display_dict = dict(zip(df_teams["team_key"], df_teams["team_name"]))

team_a = st.selectbox("Equipo A", teams, format_func=lambda x: display_dict.get(x, x), index=None, placeholder="Selecciona un equipo")

team_b = st.selectbox("Equipo B", teams, format_func=lambda x: display_dict.get(x, x), index=None, placeholder="Selecciona un equipo")

if st.button("Predecir"):
    
    if not team_a or not team_b:
        st.warning("Selecciona ambos equipos")
        st.stop()

    if team_a not in elo_dict:
        st.error(f"¡Lo siento! no encontré equipo: {display_dict.get(team_a, team_a)}. Prueba otro")
        st.stop()
    
    if team_b not in elo_dict:
        st.error(f"¡Lo siento! no encontré equipo: {display_dict.get(team_b, team_b)}. Prueba otro")
        st.stop()

    neutral = 1
    tournament = "FIFA World Cup"

    elo_a = elo_dict[team_a]
    elo_b = elo_dict[team_b]
    elo_diff = elo_a - elo_b

    X = pd.DataFrame(0, columns=feature_cols, index=[0])
    X["elo_diff"] = elo_diff
    X["neutral"] = neutral

    tournament_col = f"tournament_{tournament}"
    if tournament_col in X.columns:
        X[tournament_col] = 1

    X_scaled = scaler.transform(X)
    probs = model.predict_proba(X_scaled)[0]
    
    team_a_win = probs[2]
    draw = probs[1]
    team_b_win = probs[0]

    st.subheader(f"{display_dict.get(team_a, team_a)} vs {display_dict.get(team_b, team_b)}")
    col1, col2, col3 = st.columns(3)
    col1.metric(f"{display_dict.get(team_a, team_a)} gana", f"{team_a_win*100:.1f}%")
    col2.metric("Empate", f"{draw*100:.1f}%")
    col3.metric(f"{display_dict.get(team_b, team_b)} gana", f"{team_b_win*100:.1f}%")