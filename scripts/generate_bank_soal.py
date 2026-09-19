import json
import os
import pandas as pd
import openpyxl
from openpyxl.styles import Font, PatternFill, Alignment, Border, Side
from openpyxl.utils import get_column_letter

# Generate 300 Questions across 25 modules
# 100 Pilihan Ganda (PG001 - PG100)
# 100 Isian Singkat / Komputasi (IS001 - IS100)
# 100 Essay / Studi Kasus (ES001 - ES100)

raw_questions = []

# Module definition helper
modules = [
    (1, "Eksplorasi & Skala Pengukuran Data", "Buku 1"),
    (2, "Ukuran Pemusatan, Penyebaran & Deteksi Outlier", "Buku 1"),
    (3, "Visualisasi Data & Tabel Kontingensi", "Buku 1"),
    (4, "Pengujian Asumsi Diagnostik Statistik", "Buku 1"),
    (5, "Analisis Korelasi & Feature Selection", "Buku 1"),
    (6, "Regresi Linier Sederhana & Berganda", "Buku 1"),
    (7, "Regresi Logistik Biner & Klasifikasi", "Buku 1"),
    (8, "Reduksi Dimensi (PCA & Faktor)", "Buku 1"),
    (9, "Analisis Klaster K-Means & Hierarkis", "Buku 1"),
    (10, "Market Basket Analysis & Association Rules", "Buku 1"),
    (11, "Teori Probabilitas & Distribusi", "Buku 1"),
    (12, "Studi Kasus 1: Risiko Kredit Fintech", "Buku 1"),
    (13, "Studi Kasus 2: Segmentasi & Rekomendasi E-Commerce", "Buku 1"),
    (14, "Studi Kasus 3: A/B Testing Kinerja Sistem", "Buku 1"),
    (15, "Metrik SDLC, Defect Density & Sampling", "Buku 2"),
    (16, "Pengukuran Usabilitas: SUS & TAM", "Buku 2"),
    (17, "Uji Validitas Butir & Reliabilitas Cronbach's Alpha", "Buku 2"),
    (18, "Uji Kesepakatan Evaluator QA (Cohen's Kappa)", "Buku 2"),
    (19, "Weighted & Fleiss' Kappa Multi-Pakar", "Buku 2"),
    (20, "Eksperimen Software t-Test & Mann-Whitney U", "Buku 2"),
    (21, "Analisis Varians (ANOVA) Interaksi UI/UX", "Buku 2"),
    (22, "Pemodelan Keandalan Software (SRE Kaplan-Meier)", "Buku 2"),
    (23, "Pemodelan Retensi & Churn Pengguna (Cox Hazard)", "Buku 2"),
    (24, "Studi Kasus 4: Usabilitas SIM Kampus", "Buku 2"),
    (25, "Studi Kasus 5: Game Edukasi Metode MDA", "Buku 2")
]

# Database construction
pg_items = []
is_items = []
es_items = []

# Populate detailed, rigorous items for all 25 modules (4 PG, 4 IS, 4 ES per module)
for mod_id, mod_name, book in modules:
    # Modul 1
    if mod_id == 1:
        pg_items.extend([
            {
                "id": "PG001", "modul_id": 1, "modul": mod_name, "buku": book,
                "soal": "Variabel 'status_pembayaran' dengan nilai ('Lunas', 'Pending', 'Gagal') dalam basis data transaksi e-commerce termasuk ke dalam skala pengukuran:",
                "opsi": {"A": "Nominal", "B": "Ordinal", "C": "Interval", "D": "Rasio", "E": "Diskrit Kontinu"},
                "kunci": "A",
                "pembahasan": "Status pembayaran adalah label kategori kualitatif murni tanpa peringkat hierarki alami antar kategorinya, sehingga berskala Nominal."
            },
            {
                "id": "PG002", "modul_id": 1, "modul": mod_name, "buku": book,
                "soal": "Teknik rekayasa fitur (feature engineering) yang paling tepat untuk menangani variabel kategori berskala Nominal dengan 3 kelas pada model Regresi Linier adalah:",
                "opsi": {"A": "StandardScaler", "B": "One-Hot Encoding (pd.get_dummies)", "C": "Integer Label Encoding (1, 2, 3)", "D": "MinMaxScaler", "E": "Log Transformation"},
                "kunci": "B",
                "pembahasan": "Data Nominal wajib diubah menjadi kolom biner menggunakan One-Hot Encoding untuk menghindari asumsi urutan numerik semu oleh model linier."
            },
            {
                "id": "PG003", "modul_id": 1, "modul": mod_name, "buku": book,
                "soal": "Perbedaan fundamental antara skala Interval dan skala Rasio terletak pada keberadaan:",
                "opsi": {"A": "Urutan peringkat", "B": "Titik Nol Mutlak sejati", "C": "Jarak antar nilai yang konstan", "D": "Kemampuan dihitung frekuensinya", "E": "Label kategori"},
                "kunci": "B",
                "pembahasan": "Skala Rasio memiliki nilai nol mutlak sejati (0 berarti ketiadaan atribut, misal latensi 0 ms), sedangkan skala Interval memiliki titik nol arbitrer (seperti 0 derajat Celsius)."
            },
            {
                "id": "PG004", "modul_id": 1, "modul": mod_name, "buku": book,
                "soal": "Tingkat keparahan bug perangkat lunak dengan kategori 'Low', 'Medium', 'High', 'Critical' diukur dalam skala:",
                "opsi": {"A": "Nominal", "B": "Ordinal", "C": "Interval", "D": "Rasio", "E": "Metrik Kontinu"},
                "kunci": "B",
                "pembahasan": "Tingkat keparahan memiliki urutan tingkatan hierarki yang jelas (Critical > High > Medium > Low), namun jarak perbedaan kuantitatif antar tingkatannya tidak terukur secara konstan, sehingga merupakan skala Ordinal."
            }
        ])
        is_items.extend([
            {
                "id": "IS001", "modul_id": 1, "modul": mod_name, "buku": book,
                "soal": "Jika sebuah variabel kategori nominal memiliki k = 5 kategori unik, berapa jumlah kolom biner minimum yang dihasilkan untuk menghindari jebakan multikolinearitas (dummy variable trap)?",
                "kunci": "4 kolom (k - 1)",
                "pembahasan": "Untuk menghindari multikolinearitas sempurna (dummy variable trap) pada model regresi linier, jumlah kolom dummy yang digunakan adalah k - 1 (yaitu 5 - 1 = 4 kolom)."
            },
            {
                "id": "IS002", "modul_id": 1, "modul": mod_name, "buku": book,
                "soal": "Sebutkan nama fungsi pustaka Pandas dalam Python yang digunakan untuk melakukan One-Hot Encoding secara otomatis pada DataFrame!",
                "kunci": "pd.get_dummies()",
                "pembahasan": "Fungsi pd.get_dummies() dalam Pandas digunakan untuk mengonversi variabel kategorikal menjadi indikator/dummy variabel biner (0 atau 1)."
            },
            {
                "id": "IS003", "modul_id": 1, "modul": mod_name, "buku": book,
                "soal": "Operasi pemusatan statistik manakah yang HANYA sah digunakan pada variabel data berskala Nominal?",
                "kunci": "Modus (Mode)",
                "pembahasan": "Pada data Nominal, operasi matematika aritmetika (+, -, *, /) dan pemeringkatan tidak sah, sehingga satu-satunya ukuran pemusatan yang sah adalah Modus (kategori dengan frekuensi kemunculan terbanyak)."
            },
            {
                "id": "IS004", "modul_id": 1, "modul": mod_name, "buku": book,
                "soal": "Variabel 'waktu eksekusi query basis data' dalam satuan milidetik (ms) diklasifikasikan ke dalam skala pengukuran apa?",
                "kunci": "Skala Rasio",
                "pembahasan": "Waktu eksekusi memiliki jarak konstan dan titik nol mutlak (0 ms berarti query selesai secara instan/tidak membutuhkan waktu), serta perbandingan kelipatan sah (200 ms = 2x 100 ms)."
            }
        ])
        es_items.extend([
            {
                "id": "ES001", "modul_id": 1, "modul": mod_name, "buku": book,
                "soal": "Jelaskan hierarki 4 skala pengukuran data menurut Stanley Smith Stevens (1946) dan berikan masing-masing 2 contoh konkret penerapannya dalam rekayasa perangkat lunak!",
                "kunci": "Jawaban komprehensif mencakup:\n1. Nominal: Label kategori tanpa urutan (contoh: status autentikasi JWT 'Valid/Expired/Invalid', tipe sistem operasi 'Linux/Windows/macOS').\n2. Ordinal: Kategori berjenjang ranking (contoh: prioritas backlog Jira 'P1/P2/P3', tingkat kepuasan SUS 'Low/Medium/High').\n3. Interval: Jarak konstan tanpa nol mutlak (contoh: timestamp epoch selisih waktu, skor suhu CPU Celsius).\n4. Rasio: Jarak konstan dengan nol sejati (contoh: throughput request per second, ukuran memori RAM terpakai dalam MB).",
                "rubrik": "Bobot 100: Penjelasan 4 skala lengkap (40%), 2 contoh software engineering per skala valid (40%), ketepatan analisis matematis (20%)."
            },
            {
                "id": "ES002", "modul_id": 1, "modul": mod_name, "buku": book,
                "soal": "Mengapa menerapkan Integer Label Encoding (misal: 1 untuk 'Credit Card', 2 untuk 'E-Wallet', 3 untuk 'Bank Transfer') pada model Regresi Linier atau Neural Network dianggap sebagai anti-pattern rekayasa data? Jelaskan dampak matematisnya!",
                "kunci": "Karena Integer Encoding memaksakan relasi matematis berurutan (Bank Transfer = 3 > E-Wallet = 2 > Credit Card = 1) dan mengasumsikan selisih aritmetika (3 - 2 = 2 - 1). Model linier akan mengalikan bobot koefisien beta dengan angka 1, 2, 3 tersebut, seolah-olah Bank Transfer bernilai 3 kali lipat dari Credit Card, yang menyebabkan model mengalami bias interpretasi yang salah terhadap fitur nominal murni.",
                "rubrik": "Bobot 100: Analisis dampak matematis bobot model (50%), penjelasan distorsi urutan ordinal semu (30%), solusi alternatif menggunakan One-Hot Encoding (20%)."
            },
            {
                "id": "ES003", "modul_id": 1, "modul": mod_name, "buku": book,
                "soal": "Diberikan skema tabel transaksi sistem e-commerce: 'user_id', 'device_type', 'star_rating', 'checkout_time_sec', 'total_payment_idr'. Tentukan skala pengukuran masing-masing kolom dan tentukan ukuran pemusatan statistik yang sah untuk tiap kolom!",
                "kunci": "1. user_id: Nominal -> Ukuran pemusatan: Modus (ID transaksi terbanyak).\n2. device_type: Nominal -> Modus.\n3. star_rating (1-5): Ordinal -> Median dan Modus.\n4. checkout_time_sec: Rasio -> Mean, Median, Modus (Semua rata-rata sah).\n5. total_payment_idr: Rasio -> Mean, Median, Modus.",
                "rubrik": "Bobot 100: Ketepatan klasifikasi skala 5 kolom (50%), ketepatan penentuan ukuran pemusatan yang sah (50%)."
            },
            {
                "id": "ES004", "modul_id": 1, "modul": mod_name, "buku": book,
                "soal": "Jelaskan konsep 'Dummy Variable Trap' dalam konteks One-Hot Encoding dan tunjukkan secara matematis bagaimana multikolinearitas sempurna terjadi jika k dummy variables digunakan bersamaan dengan konstanta intercept!",
                "kunci": "Dummy Variable Trap adalah kondisi multikolinearitas sempurna di mana satu variabel dummy dapat diprediksi secara linier sempurna dari kombinasi variabel dummy lainnya. Jika terdapat k dummy (D1, D2, ..., Dk), maka D1 + D2 + ... + Dk = 1 = Konstanta Intercept. Akibatnya, matriks X^T X menjadi singular (determinan = 0) dan tidak memiliki invers, sehingga persamaan OLS beta = (X^T X)^(-1) X^T Y tidak dapat dihitung secara unik. Solusinya adalah membuang 1 kolom referensi (drop_first=True, menggunakan k - 1 dummy).",
                "rubrik": "Bobot 100: Penjelasan konsep matematis singularitas matriks OLS (50%), pembuktian linier D1+...+Dk=1 (30%), solusi drop_first=True (20%)."
            }
        ])

print("Populated Module 1...")
