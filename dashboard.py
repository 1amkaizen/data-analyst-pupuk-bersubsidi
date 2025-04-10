import streamlit as st
import pandas as pd
import plotly.express as px
import plotly.graph_objects as go

# ========== JUDUL ==========
st.title("📊 Dashboard Penyaluran Pupuk Bersubsidi")

# ========== LOAD DATA ==========
df = pd.read_csv('data_final.csv')

# ========== VISUAL 1: BOXPLOT ==========
st.subheader("📦 Distribusi Volume per Jenis Pupuk")
fig1 = px.box(df, x='jenis_pupuk', y='volume', color='jenis_pupuk', template='plotly_white')
fig1.update_layout(xaxis_tickangle=-45)
st.plotly_chart(fig1)

# ========== VISUAL 2: TREN NASIONAL ==========
st.subheader("📈 Tren Volume Pupuk Nasional per Tahun")
df_nasional = df.groupby('tahun')['volume'].sum().reset_index()
fig2 = px.line(df_nasional, x='tahun', y='volume', markers=True, template='plotly_white')
st.plotly_chart(fig2)

# ========== VISUAL 3: TREN PER KOTA (TOP 10) ==========
st.subheader("🏙️ Tren Penyaluran Pupuk Top 10 Kota/Kabupaten")
top_kota = df.groupby('nama_kabupaten_kota')['volume'].sum().nlargest(10).index
filtered = df[df['nama_kabupaten_kota'].isin(top_kota)]
filtered_line = filtered.groupby(['tahun', 'nama_kabupaten_kota'])['volume'].sum().reset_index()
fig3 = px.line(filtered_line, x='tahun', y='volume', color='nama_kabupaten_kota', markers=True, template='plotly_white')
fig3.update_layout(legend_title_text='Kabupaten/Kota', legend=dict(x=1.02, y=1))
st.plotly_chart(fig3)

# ========== VISUAL 4: TOP 10 KAB UREA ==========
st.subheader("🌾 Top 10 Kabupaten/Kota Penerima UREA Terbanyak")
top10_urea = df[df['jenis_pupuk'] == 'UREA'].groupby('nama_kabupaten_kota')['volume'].sum().nlargest(10).reset_index()
fig4 = px.bar(top10_urea, x='volume', y='nama_kabupaten_kota', orientation='h', color='volume',
              color_continuous_scale='Blues', template='plotly_white')
fig4.update_layout(yaxis=dict(autorange="reversed"))
st.plotly_chart(fig4)

# ========== VISUAL 5: KENAIKAN TERTINGGI ==========
st.subheader("📈 Kota/Kabupaten dengan Kenaikan Volume Terbesar (YoY)")
top_rise = df.sort_values('delta', ascending=False).dropna(subset=['delta']).head(1)
top_kabupaten = top_rise['nama_kabupaten_kota'].values[0]
top_data = df[df['nama_kabupaten_kota'] == top_kabupaten].groupby('tahun')['volume'].sum().reset_index()
fig5 = px.line(top_data, x='tahun', y='volume', title=f'Tren Volume di {top_kabupaten}', markers=True, template='plotly_white')
st.plotly_chart(fig5)

# ========== VISUAL 6: CLUSTER STATS ==========
st.subheader("🎯 Rata-Rata Volume Pupuk per Cluster")
cluster_stats = df.groupby(['cluster', 'jenis_pupuk'])['volume'].mean().reset_index()
fig6 = px.bar(cluster_stats, x='jenis_pupuk', y='volume', color='cluster', barmode='group', template='plotly_white')
fig6.update_layout(title='Rata-rata Volume Pupuk per Cluster')
st.plotly_chart(fig6)

# ========== VISUAL 7: PROPHET FORECAST ==========
st.subheader("🔮 Forecast Volume Nasional (Prophet)")

# Load forecast hasil Prophet
forecast = pd.read_csv('forecast_result.csv')  # simpan hasil forecast sebelumnya

fig7 = go.Figure()
fig7.add_trace(go.Scatter(x=forecast['ds'], y=forecast['yhat'], mode='lines', name='Prediksi', line=dict(color='royalblue')))
fig7.add_trace(go.Scatter(
    x=forecast['ds'].tolist() + forecast['ds'][::-1].tolist(),
    y=forecast['yhat_upper'].tolist() + forecast['yhat_lower'][::-1].tolist(),
    fill='toself', fillcolor='rgba(173,216,230,0.3)', line=dict(color='rgba(255,255,255,0)'),
    hoverinfo="skip", showlegend=True, name='Rentang Prediksi'))
fig7.update_layout(title='Forecast Volume Pupuk Nasional', xaxis_title='Tahun', yaxis_title='Volume (TON)', template='plotly_white')
st.plotly_chart(fig7)
