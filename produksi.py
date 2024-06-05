import pandas as pd
import matplotlib.pyplot as plt

# Baca file CSV dengan pemisah ';'
df = pd.read_csv('D:\Patricia\data_produksi-20240605T014522Z-001\data_produksi\produksi_data.csv', delimiter=';')

# Tampilkan beberapa baris pertama untuk memastikan data telah terbaca dengan benar
print("Data Preview:")
print(df.head())

# Periksa nama kolom yang ada dalam DataFrame
print("Kolom yang tersedia:", df.columns)

# Menghitung total penjualan per nama barang
total_penjualan_per_barang = df.groupby('Nama Barang')['Jumlah'].sum()

# Tampilkan hasil perhitungan total penjualan per nama barang
print("Total Penjualan per Nama Barang:")
print(total_penjualan_per_barang)

# Menghitung total penjualan secara keseluruhan
total_penjualan_keseluruhan = df['Jumlah'].sum()

# Tampilkan hasil perhitungan total penjualan secara keseluruhan
print("\nTotal Penjualan Keseluruhan:", total_penjualan_keseluruhan)

# Buat histogram dari kolom 'Harga Total (Rp)'
# Pastikan nama kolom sesuai dengan yang ada di file CSV
if 'Harga Total (Rp)' in df.columns:
    plt.hist(df['Harga Total (Rp)'], bins=5, edgecolor='black')
    plt.xlabel('Harga Total (Rp)')
    plt.ylabel('Frekuensi')
    plt.title('Distribusi Harga Total')
    plt.show()
else:
    print("Kolom 'Harga Total (Rp)' tidak ditemukan dalam data.")

# Plotting Histogram untuk Harga Total (Rp)
plt.figure(figsize=(10, 5))
plt.hist(df['Harga Total (Rp)'], bins=5, edgecolor='black')
plt.title('Histogram Harga Total (Rp)')
plt.xlabel('Harga Total (Rp)')
plt.ylabel('Frekuensi')
plt.grid(True)
plt.show()

# Plotting Scatter Plot untuk Harga Satuan (Rp) vs Jumlah
plt.figure(figsize=(10, 5))
plt.scatter(df['Harga Satuan (Rp)'], df['Jumlah'], c='blue', marker='o')
plt.title('Scatter Plot Harga Satuan (Rp) vs Jumlah')
plt.xlabel('Harga Satuan (Rp)')
plt.ylabel('Jumlah')
plt.grid(True)
plt.show()

# Plotting Bar Plot untuk Metode Pembayaran
metode_counts = df['Metode Pembayaran'].value_counts()
plt.figure(figsize=(10, 5))
metode_counts.plot(kind='bar', color='skyblue')
plt.title('Bar Plot Metode Pembayaran')
plt.xlabel('Metode Pembayaran')
plt.ylabel('Jumlah')
plt.xticks(rotation=45)
plt.grid(axis='y')
plt.show()

# Plotting Scatter Plot untuk total penjualan per nama barang
plt.figure(figsize=(10, 5))
plt.scatter(total_penjualan_per_barang.index, total_penjualan_per_barang.values, c='blue', marker='o')
plt.title('Scatter Plot Total Penjualan per Nama Barang')
plt.xlabel('Nama Barang')
plt.ylabel('Total Penjualan')
plt.xticks(rotation=45)
plt.grid(True)
plt.show()