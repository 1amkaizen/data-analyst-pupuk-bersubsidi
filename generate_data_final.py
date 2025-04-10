# generate_data_final.py
import pandas as pd
from sklearn.preprocessing import LabelEncoder, MinMaxScaler, StandardScaler
from sklearn.cluster import KMeans

# === 1. Load Data ===
df = pd.read_csv("distanhor-od_18713_jml_penyaluran_pupuk_bersubsidi__kabupatenkota_jen_v2_data.csv")

# === 2. Label Encoding jenis_pupuk ===
le = LabelEncoder()
df['jenis_pupuk_encoded'] = le.fit_transform(df['jenis_pupuk'])

# === 3. Normalisasi & Standardisasi ===
min_max_scaler = MinMaxScaler()
standard_scaler = StandardScaler()

df['volume_normalized'] = min_max_scaler.fit_transform(df[['volume']])
df['volume_standardized'] = standard_scaler.fit_transform(df[['volume']])

# === 4. Hitung delta (YoY) ===
delta_df = df.groupby(['nama_kabupaten_kota', 'tahun'])['volume'].sum().reset_index()
delta_df.sort_values(by=['nama_kabupaten_kota', 'tahun'], inplace=True)
delta_df['delta'] = delta_df.groupby('nama_kabupaten_kota')['volume'].diff()

# Gabungkan ke df utama
df = df.merge(
    delta_df[['nama_kabupaten_kota', 'tahun', 'delta']],
    on=['nama_kabupaten_kota', 'tahun'],
    how='left'
)

# === 5. Clustering KMeans berdasarkan volume per jenis pupuk ===
pivot_df = df.pivot_table(
    index='nama_kabupaten_kota',
    columns='jenis_pupuk',
    values='volume',
    aggfunc='sum',
    fill_value=0
).reset_index()

X_clustering = pivot_df.drop(columns='nama_kabupaten_kota')
X_scaled = StandardScaler().fit_transform(X_clustering)

kmeans = KMeans(n_clusters=3, random_state=42)
pivot_df['cluster'] = kmeans.fit_predict(X_scaled)

# Gabungkan cluster ke df
df = df.merge(
    pivot_df[['nama_kabupaten_kota', 'cluster']],
    on='nama_kabupaten_kota',
    how='left'
)

# === 6. Simpan file akhir ===
df.to_csv("data_final.csv", index=False)
print("✅ data_final.csv berhasil dibuat.")
