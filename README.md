# 📊 Dashboard & Analisis Pupuk Bersubsidi di Jawa Barat

Studi Kasus Data Analyst + Machine Learning**

Repositori ini berisi analisis end-to-end penyaluran pupuk bersubsidi di provinsi Jawa Barat, termasuk visualisasi, prediksi masa depan, clustering wilayah, dan pembuatan dashboard interaktif dengan Streamlit.

---

## 📁 Dataset
Sumber data: `distanhor-od_18713_jml_penyaluran_pupuk_bersubsidi__kabupatenkota_jen_v2_data.csv`

---

## 🔍 Fitur Analisis
- Analisis distribusi & tren per jenis pupuk, kota, dan tahun
- Normalisasi dan encoding fitur
- Regresi untuk prediksi volume (Linear Regression & Random Forest)
- Clustering kota/kabupaten dengan KMeans
- Forecasting volume pupuk nasional dengan Prophet
- Visualisasi interaktif dengan Plotly
- Dashboard interaktif dengan Streamlit

---

## 🚀 Cara Menjalankan

### 1. Clone Repository
```bash
git clone https://github.com/yourusername/data-analyst-pupuk-bersubsidi.git
cd data-analyst-pupuk-bersubsidi
```

### 2. Instalasi Package
```bash
pip install -r requirements.txt
```

### 3. Generate Data Final
```bash
python generate_data_final.py
```

### 4. Jalankan Dashboard
```bash
streamlit run dashboard.py
```

---

## 🧠 File Penting

| File | Fungsi |
|------|--------|
| `generate_data_final.py` | Membuat file `data_final.csv` dari raw data |
| `dashboard.py` | Streamlit dashboard interaktif |
| `forecast_result.csv` | Hasil prediksi Prophet |
| `data_final.csv` | Dataset siap pakai untuk ML & dashboard |
| `notebook_analisis_pupuk.ipynb` | Notebook eksplorasi & modelling *(opsional)* |

---

## 📈 Contoh Output

- 📊 Grafik tren volume pupuk
- 🌾 10 besar penerima UREA
- 🧠 Clustering kabupaten berdasarkan pola penyaluran
- 🔮 Prediksi kebutuhan pupuk hingga 2026

---

## 📚 Teknologi yang Digunakan
- Python (pandas, sklearn, plotly, prophet, streamlit)
- Jupyter Notebook
- GitHub / Kaggle

---

## 🌐 Live Demo

📺 Coba langsung dashboard interaktif hasil analisis ini:

👉 [Klik untuk membuka di Streamlit Cloud](https://data-analyst-pupuk-bersubsidi.streamlit.app/)

**Fitur dalam demo:**
- Visualisasi distribusi dan tren penyaluran pupuk per tahun & kota
- Top 10 kabupaten penerima pupuk jenis UREA
- Clusterisasi kabupaten berdasarkan pola penyaluran
- Prediksi kebutuhan pupuk nasional hingga tahun 2026 (model Prophet)
- Dashboard responsif berbasis Streamlit & Plotly

```
