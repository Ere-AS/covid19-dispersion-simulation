import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt

st.set_page_config(page_title="COVID-19 Simulation Dashboard", layout="wide")
st.title("📊 COVID-19 Dispersion Simulation Dashboard")

uploaded_file = st.file_uploader("Upload the simulation CSV file (resultado_simulacion.csv):", type=["csv"])

if uploaded_file is not None:
    df = pd.read_csv(uploaded_file)

    st.subheader("📈 Time Series of Population States")
    fig, ax = plt.subplots(figsize=(12, 6))
    for col in ['sanos', 'infectados', 'recuperados', 'muertos']:
        ax.plot(df['día'], df[col], label=col)
    ax.set_xlabel("Día")
    ax.set_ylabel("Número de personas")
    ax.set_title("Evolución de la pandemia en la simulación")
    ax.grid(True)
    ax.legend()
    st.pyplot(fig)

    st.subheader("📊 Final Population Distribution")
    final_counts = df.iloc[-1][['sanos', 'infectados', 'recuperados', 'muertos']]
    fig2, ax2 = plt.subplots()
    final_counts.plot(kind='bar', color=['#3b82f6', '#ef4444', '#22c55e', '#fefefe'], ax=ax2)
    ax2.set_title("Estado final de la población")
    ax2.set_ylabel("Cantidad")
    ax2.set_xticklabels(final_counts.index, rotation=0)
    st.pyplot(fig2)

    st.subheader("📂 Datos crudos")
    st.dataframe(df)

else:
    st.info("Por favor sube un archivo CSV generado por la simulación para visualizar los resultados.")
