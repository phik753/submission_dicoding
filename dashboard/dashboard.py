import streamlit as st
import matplotlib.pyplot as plt
import seaborn as sns
import pandas as pd

# Set Streamlit page configuration
st.set_page_config(page_title="Bike Rental Analysis Dashboard", layout="wide")

# Title
st.title("Bike Rental Analysis Dashboard")

# Dashboard sections
st.header("Exploratory Data Analysis")

# Load the data
day_df = pd.read_csv("https://raw.githubusercontent.com/phik753/submission_dicoding/refs/heads/main/day_df_akhir.csv")
hour_df = pd.read_csv("https://raw.githubusercontent.com/phik753/submission_dicoding/refs/heads/main/hour_df_akhir.csv")

# Visualization 1: Rata-rata jumlah penggunaan sepeda tiap jam
st.subheader("1. Rata-rata jumlah penggunaan sepeda tiap jam")
fig1, ax1 = plt.subplots(figsize=(10, 6))
sns.lineplot(data=hour_df.groupby('hr')['cnt'].mean().reset_index(), x='hr', y='cnt', marker='o', ax=ax1)
ax1.set_title("Rata-rata Penggunaan Sepeda pada Jam Berbeda")
ax1.set_xlabel("Jam")
ax1.set_ylabel("Rata-rata Jumlah Sewa Sepeda (cnt)")
ax1.set_xticks(range(0, 24))
st.pyplot(fig1)

# Visualization 2: Rata-rata jumlah penggunaan sepeda berdasarkan cuaca
st.subheader("2. Rata-rata jumlah penggunaan sepeda berdasarkan cuaca")
weather_avg = hour_df.groupby('weathersit')['cnt'].mean()
fig2, ax2 = plt.subplots(figsize=(10, 5))
sns.barplot(x=weather_avg.index, y=weather_avg.values, ax=ax2)
ax2.set_title("Rata-rata Penggunaan Sepeda Berdasarkan Kondisi Cuaca")
ax2.set_xlabel("Kondisi Cuaca (1: Cerah, 2: Berawan, 3: Hujan Ringan/Snow, 4: Hujan Lebat/Snow Tebal)")
ax2.set_ylabel("Rata-rata Jumlah Sewa Sepeda")
ax2.set_xticks([0, 1, 2, 3])
ax2.set_xticklabels(['Cerah', 'Berawan', 'Hujan Ringan', 'Hujan Lebat'])
st.pyplot(fig2)

# Visualization 3: Rata-rata jumlah penggunaan sepeda tiap bulan
st.subheader("3. Rata-rata jumlah penggunaan sepeda tiap bulan")
month_avg = hour_df.groupby('mnth')['cnt'].mean()
fig3, ax3 = plt.subplots(figsize=(10, 6))
sns.barplot(x=month_avg.index, y=month_avg.values, ax=ax3)
ax3.set_title("Rata-rata Penggunaan Sepeda per Bulan")
ax3.set_xlabel("Bulan (1: Jan, 12: Dec)")
ax3.set_ylabel("Rata-rata Jumlah Sewa Sepeda")
ax3.set_xticks(range(1, 13))
ax3.set_xticklabels(['Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun', 'Jul', 'Aug', 'Sep', 'Oct', 'Nov', 'Dec'])
st.pyplot(fig3)

# Visualization 4: Perbedaan jumlah pengguna sepeda berdasarkan tipe pengguna
st.subheader("4. Perbedaan jumlah pengguna sepeda berdasarkan tipe pengguna")
registered_avg = hour_df['registered'].mean()
casual_avg = hour_df['casual'].mean()
fig4, ax4 = plt.subplots(figsize=(8, 5))
sns.barplot(x=['Terdaftar', 'Kasual'], y=[registered_avg, casual_avg], ax=ax4)
ax4.set_title("Rata-rata Penggunaan Sepeda oleh Pengguna Terdaftar vs Kasual")
ax4.set_xlabel("Tipe Pengguna")
ax4.set_ylabel("Rata-rata Jumlah Sewa Sepeda")
st.pyplot(fig4)

# Conclusion Section
st.header("Kesimpulan")
st.write("""
**1. Jumlah pesewa sepeda tertinggi rata-rata ada pada jam 17 atau 5 sore yaitu sebanyak 400 lebih, dan rata-rata paling sedikit pada pukul 4.**  
**2. Rata-rata jumlah pesewa sepeda paling banyak ada pada saat cuacanya cerah yaitu 200 lebih, dan paling sedikit saat cuaca hujan lebat yaitu lebih dari 50.**  
**3. Rata-rata jumlah pesewa sepeda paling banyak ada pada bulan Mei dan Agustus.**  
**4. Perbedaan jumlah pesewa yang terdaftar jauh lebih banyak dibanding yang kasual.**
""")

