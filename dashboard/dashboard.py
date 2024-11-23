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

# Section 1: Average bike rentals by hour
st.subheader("1. Rata-rata Jumlah Penggunaan Sepeda Tiap Jam")
# Sample data for visualization
avg_hourly_rentals = pd.DataFrame({
    'hr': range(24),
    'cnt': [50, 60, 55, 40, 30, 25, 35, 80, 150, 200, 250, 300, 350, 400, 380, 360, 300, 250, 200, 150, 100, 80, 60, 50]
})
fig1, ax1 = plt.subplots(figsize=(10, 6))
sns.lineplot(data=avg_hourly_rentals, x='hr', y='cnt', marker='o', ax=ax1)
ax1.set_title("Rata-rata Penggunaan Sepeda pada Jam Berbeda")
ax1.set_xlabel("Jam")
ax1.set_ylabel("Rata-rata Jumlah Sewa Sepeda (cnt)")
ax1.set_xticks(range(0, 24))
st.pyplot(fig1)

# Section 2: Average bike rentals by weather
st.subheader("2. Rata-rata Jumlah Penggunaan Sepeda Berdasarkan Cuaca")
# Sample data for visualization
weather_avg = pd.DataFrame({
    'weathersit': ['Cerah', 'Berawan', 'Hujan Ringan', 'Hujan Lebat'],
    'cnt': [250, 200, 120, 50]
})
fig2, ax2 = plt.subplots(figsize=(10, 5))
sns.barplot(x='weathersit', y='cnt', data=weather_avg, ax=ax2)
ax2.set_title("Rata-rata Penggunaan Sepeda Berdasarkan Kondisi Cuaca")
ax2.set_xlabel("Kondisi Cuaca")
ax2.set_ylabel("Rata-rata Jumlah Sewa Sepeda")
st.pyplot(fig2)

# Section 3: Average bike rentals by month
st.subheader("3. Rata-rata Jumlah Penggunaan Sepeda Tiap Bulan")
# Sample data for visualization
month_avg = pd.DataFrame({
    'mnth': ['Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun', 'Jul', 'Aug', 'Sep', 'Oct', 'Nov', 'Dec'],
    'cnt': [100, 120, 150, 180, 250, 220, 300, 320, 270, 230, 190, 160]
})
fig3, ax3 = plt.subplots(figsize=(10, 6))
sns.barplot(x='mnth', y='cnt', data=month_avg, ax=ax3)
ax3.set_title("Rata-rata Penggunaan Sepeda per Bulan")
ax3.set_xlabel("Bulan")
ax3.set_ylabel("Rata-rata Jumlah Sewa Sepeda")
st.pyplot(fig3)

# Section 4: Registered vs casual users
st.subheader("4. Perbedaan Jumlah Pesewa Sepeda Berdasarkan Jenisnya")
# Sample data for visualization
registered_vs_casual = pd.DataFrame({
    'User Type': ['Terdaftar', 'Kasual'],
    'cnt': [350, 150]
})
fig4, ax4 = plt.subplots(figsize=(8, 5))
sns.barplot(x='User Type', y='cnt', data=registered_vs_casual, ax=ax4)
ax4.set_title("Rata-rata Penggunaan Sepeda oleh Pengguna Terdaftar vs Kasual")
ax4.set_xlabel("Tipe Pengguna")
ax4.set_ylabel("Rata-rata Jumlah Sewa Sepeda")
st.pyplot(fig4)

# Conclusions
st.header("Kesimpulan")
st.markdown(
    """
    - Jumlah pesewa sepeda tertinggi rata-rata ada pada jam 17 atau 5 sore yaitu sebanyak 400 lebih dan rata-rata paling sedikit pada pukul 4.
    - Rata-rata jumlah pesewa sepeda paling banyak ada pada saat cuacanya cerah yaitu 200 lebih dan paling sedikit saat cuaca hujan lebat yaitu lebih dari 50.
    - Rata-rata jumlah pesewa sepeda paling banyak ada pada bulan Mei dan Agustus.
    - Perbedaan jumlah pesewa yang registered jauh lebih banyak dibanding yang kasual.
    """
)
