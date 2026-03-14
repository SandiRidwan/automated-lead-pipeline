import pandas as pd
import datetime

# 1. Menyiapkan Dummy Data (Alamat asli di US agar API Roofle tidak error)
data = {
    'Name': [
        'Sandi Test - Mountain View', 
        'Sandi Test - Cupertino', 
        'Sandi Test - New York', 
        'Sandi Test - Chicago', 
        'Sandi Test - Torrance'
    ],
    'Address': [
        '1600 Amphitheatre Pkwy, Mountain View, CA 94043', 
        '1 Infinite Loop, Cupertino, CA 95014', 
        '350 Fifth Avenue, New York, NY 10118', 
        '233 S Wacker Dr, Chicago, IL 60606', 
        '20100 S Western Ave, Torrance, CA 90501'
    ],
    'Email': [
        'test1@example.com', 
        'test2@example.com', 
        'test3@example.com', 
        'test4@example.com', 
        'test5@example.com'
    ],
    'Phone': [
        '1234567890', 
        '0987654321', 
        '1122334455', 
        '5566778899', 
        '9988776655'
    ]
}

# 2. Membuat DataFrame
df = pd.DataFrame(data)

# 3. Menambahkan Kolom Sistem (System Columns) untuk Otomasi Make.com
# Kolom ini penting agar sistem tahu baris mana yang sudah diproses
df['Status'] = 'Pending'
df['Estimate_Link'] = ''  # Akan diisi otomatis oleh Make.com
df['Last_Updated'] = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")

# 4. Menyimpan langsung ke format CSV
file_name = 'Master_Roofing_Leads.csv'
df.to_csv(file_name, index=False)

print(f"✅ Berhasil! File '{file_name}' telah dibuat.")
print("Silakan upload file ini ke Google Sheets kamu untuk memulai testing Make.com.")