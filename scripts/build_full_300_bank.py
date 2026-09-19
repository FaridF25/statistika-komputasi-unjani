import json
import os
import openpyxl
from openpyxl.styles import Font, PatternFill, Alignment, Border, Side
from openpyxl.utils import get_column_letter

def get_all_questions():
    pg = []
    is_q = []
    es = []

    # Module 1 to 25 data definition
    mod_data = [
        # MODUL 01
        (1, "Eksplorasi & Skala Pengukuran Data", "Buku 1", [
            ("Variabel 'status_pembayaran' dengan nilai ('Lunas', 'Pending', 'Gagal') dalam basis data transaksi e-commerce termasuk ke dalam skala pengukuran:",
             {"A": "Nominal", "B": "Ordinal", "C": "Interval", "D": "Rasio", "E": "Diskrit Kontinu"}, "A",
             "Status pembayaran adalah label kategori kualitatif murni tanpa peringkat hierarki alami antar kategorinya, sehingga berskala Nominal."),
            ("Teknik rekayasa fitur (feature engineering) yang paling tepat untuk menangani variabel kategori berskala Nominal dengan 3 kelas pada model Regresi Linier adalah:",
             {"A": "StandardScaler", "B": "One-Hot Encoding (pd.get_dummies)", "C": "Integer Label Encoding (1, 2, 3)", "D": "MinMaxScaler", "E": "Log Transformation"}, "B",
             "Data Nominal wajib diubah menjadi kolom biner menggunakan One-Hot Encoding untuk menghindari asumsi urutan numerik semu oleh model linier."),
            ("Perbedaan fundamental antara skala Interval dan skala Rasio terletak pada keberadaan:",
             {"A": "Urutan peringkat", "B": "Titik Nol Mutlak sejati", "C": "Jarak antar nilai yang konstan", "D": "Kemampuan dihitung frekuensinya", "E": "Label kategori"}, "B",
             "Skala Rasio memiliki nilai nol mutlak sejati (0 berarti ketiadaan atribut, misal latensi 0 ms), sedangkan skala Interval memiliki titik nol arbitrer (seperti 0 derajat Celsius)."),
            ("Tingkat keparahan bug perangkat lunak dengan kategori 'Low', 'Medium', 'High', 'Critical' diukur dalam skala:",
             {"A": "Nominal", "B": "Ordinal", "C": "Interval", "D": "Rasio", "E": "Metrik Kontinu"}, "B",
             "Tingkat keparahan memiliki urutan tingkatan hierarki yang jelas (Critical > High > Medium > Low), namun jarak perbedaan kuantitatif antar tingkatannya tidak terukur secara konstan, sehingga merupakan skala Ordinal.")
        ], [
            ("Jika sebuah variabel kategori nominal memiliki k = 5 kategori unik, berapa jumlah kolom biner minimum yang dihasilkan untuk menghindari jebakan multikolinearitas (dummy variable trap)?",
             "4 kolom (k - 1)", "Untuk menghindari multikolinearitas sempurna (dummy variable trap) pada model regresi linier, jumlah kolom dummy yang digunakan adalah k - 1 (yaitu 5 - 1 = 4 kolom)."),
            ("Sebutkan nama fungsi pustaka Pandas dalam Python yang digunakan untuk melakukan One-Hot Encoding secara otomatis pada DataFrame!",
             "pd.get_dummies()", "Fungsi pd.get_dummies() dalam Pandas digunakan untuk mengonversi variabel kategorikal menjadi indikator/dummy variabel biner (0 atau 1)."),
            ("Operasi pemusatan statistik manakah yang HANYA sah digunakan pada variabel data berskala Nominal?",
             "Modus (Mode)", "Pada data Nominal, operasi matematika aritmetika (+, -, *, /) dan pemeringkatan tidak sah, sehingga satu-satunya ukuran pemusatan yang sah adalah Modus (kategori dengan frekuensi kemunculan terbanyak)."),
            ("Variabel 'waktu eksekusi query basis data' dalam satuan milidetik (ms) diklasifikasikan ke dalam skala pengukuran apa?",
             "Skala Rasio", "Waktu eksekusi memiliki jarak konstan dan titik nol mutlak (0 ms berarti query selesai secara instan/tidak membutuhkan waktu), serta perbandingan kelipatan sah (200 ms = 2x 100 ms).")
        ], [
            ("Jelaskan hierarki 4 skala pengukuran data menurut Stanley Smith Stevens (1946) dan berikan masing-masing 2 contoh konkret penerapannya dalam rekayasa perangkat lunak!",
             "1. Nominal: Label kategori tanpa urutan (contoh: status token JWT 'Valid/Expired', arsitektur OS 'Linux/Windows').\n2. Ordinal: Kategori berjenjang ranking (contoh: prioritas backlog Jira 'P1/P2/P3', rating bintang ulasan '1-5').\n3. Interval: Jarak konstan tanpa nol mutlak (contoh: suhu prosesor CPU Celsius, format waktu timestamp kalender).\n4. Rasio: Jarak konstan dengan nol sejati (contoh: latensi API ms, throughput request per second, penggunaan RAM MB).",
             "Bobot 100: Penjelasan 4 skala lengkap (40%), 2 contoh software engineering per skala valid (40%), ketepatan analisis matematis (20%)."),
            ("Mengapa menerapkan Integer Label Encoding pada model Regresi Linier terhadap variabel nominal dianggap sebagai anti-pattern rekayasa data? Jelaskan dampak matematisnya!",
             "Karena Integer Encoding memaksakan relasi matematis berurutan (3 > 2 > 1) dan mengasumsikan selisih aritmetika yang sama (3-2 = 2-1). Model linier akan mengalikan bobot koefisien beta dengan integer buatan tersebut, sehingga model mengasumsikan kategori bernilai 3 memiliki bobot 3 kali lipat dari kategori 1, yang menyebabkan distorsi estimasi dan bias yang fatal.",
             "Bobot 100: Analisis dampak matematis koefisien beta (50%), penjelasan distorsi urutan ordinal semu (30%), solusi One-Hot Encoding (20%)."),
            ("Diberikan skema tabel transaksi sistem e-commerce: 'user_id', 'device_type', 'star_rating', 'checkout_time_sec', 'total_payment_idr'. Tentukan skala pengukuran masing-masing kolom dan tentukan ukuran pemusatan statistik yang sah untuk tiap kolom!",
             "1. user_id: Nominal -> Modus\n2. device_type: Nominal -> Modus\n3. star_rating (1-5): Ordinal -> Median dan Modus\n4. checkout_time_sec: Rasio -> Mean, Median, Modus (Semua rata-rata sah)\n5. total_payment_idr: Rasio -> Mean, Median, Modus.",
             "Bobot 100: Ketepatan klasifikasi skala 5 kolom (50%), ketepatan penentuan ukuran pemusatan yang sah (50%)."),
            ("Jelaskan konsep 'Dummy Variable Trap' dalam konteks One-Hot Encoding dan tunjukkan secara matematis bagaimana multikolinearitas sempurna terjadi jika k dummy variables digunakan bersamaan dengan konstanta intercept!",
             "Dummy Variable Trap adalah kondisi multikolinearitas sempurna di mana satu variabel dummy dapat diprediksi secara linier sempurna dari kombinasi dummy lainnya. Jika terdapat k dummy, maka D1 + D2 + ... + Dk = 1 = Intercept. Akibatnya matriks X^T X menjadi singular (determinan = 0) dan tidak memiliki invers, sehingga persamaan OLS beta = (X^T X)^(-1) X^T Y gagal dihitung secara unik. Solusinya adalah membuang 1 kolom referensi (drop_first=True, k - 1 dummy).",
             "Bobot 100: Penjelasan konsep matematis singularitas matriks OLS (50%), pembuktian linier D1+...+Dk=1 (30%), solusi drop_first=True (20%).")
        ]),

        # MODUL 02
        (2, "Ukuran Pemusatan, Penyebaran & Deteksi Outlier", "Buku 1", [
            ("Pada distribusi data waktu respon server yang menceng ke kanan (positive/right-skewed), urutan nilai pemusatan data yang benar adalah:",
             {"A": "Mean < Median < Modus", "B": "Modus < Median < Mean", "C": "Median < Modus < Mean", "D": "Mean = Median = Modus", "E": "Modus = Mean < Median"}, "B",
             "Pada distribusi menceng ke kanan (right-skewed), ekor data memanjang ke kanan akibat outlier bernilai besar, sehingga Mean tertarik ke nilai terbesar, menghasilkan urutan Modus < Median < Mean."),
            ("Ukuran penyebaran data yang paling tahan (robust) terhadap keberadaan nilai pencilan (outlier) ekstrem adalah:",
             {"A": "Rentang (Range)", "B": "Varians Sampel (s²)", "C": "Rentang Antarkuartil (IQR)", "D": "Standar Deviasi (s)", "E": "Mean Absolute Deviation terhadap Rata-rata"}, "C",
             "Rentang Antarkuartil (IQR = Q3 - Q1) mengukur rentang 50% data di bagian tengah sehingga tidak terpengaruh oleh pencilan ekstrem pada ujung distribusi."),
            ("Berdasarkan metode Pagar Tukey (Tukey's Fences), batas atas (Upper Fence) untuk mendeteksi pencilan dihitung dengan rumus:",
             {"A": "Q3 + 1.5 * IQR", "B": "Q1 - 1.5 * IQR", "C": "Mean + 2 * Std", "D": "Q3 + 3.0 * IQR", "E": "Median + 1.5 * IQR"}, "A",
             "Pagar Tukey mendefinisikan batas atas pencilan sebagai Upper Fence = Q3 + 1.5 * IQR. Nilai yang melebihi batas ini dianggap sebagai pencilan."),
            ("Koreksi Bessel dengan membagi (n - 1) pada perhitungan varians sampel bertujuan untuk:",
             {"A": "Memperbesar nilai varians", "B": "Menghilangkan galat pembulatan", "C": "Menghasilkan penaksir tak bias (unbiased estimator) bagi varians populasi", "D": "Menstandarisasi data ke skala 0 sampai 1", "E": "Mengubah data menjadi distribusi normal"}, "C",
             "Pembagian dengan (n - 1) mengoreksi kecenderungan varians sampel yang meremehkan (underestimate) varians populasi sejati, sehingga menghasilkan unbiased estimator.")
        ], [
            ("Diberikan data latensi 5 server: [20, 22, 25, 28, 150] ms. Berapakah nilai Median dari data tersebut?",
             "25 ms", "Data setelah diurutkan: 20, 22, 25, 28, 150. Nilai tengah (posisi ke-3) adalah 25 ms."),
            ("Jika Kuartil Bawah Q1 = 40 ms dan Kuartil Atas Q3 = 100 ms, berapakah batas bawah (Lower Fence) deteksi outlier Tukey?",
             "-50 ms (atau 0 ms jika batas fisik non-negatif)", "IQR = Q3 - Q1 = 100 - 40 = 60 ms. Lower Fence = Q1 - 1.5 * IQR = 40 - (1.5 * 60) = 40 - 90 = -50 ms."),
            ("Metrik dispersi manakah yang diperoleh dari pembagian standar deviasi dengan rata-rata dikali 100% untuk membandingkan variabilitas lintas variabel beda satuan?",
             "Koefisien Variasi (Coefficient of Variation / CV)", "Formula CV = (s / Mean) * 100%. Digunakan untuk membandingkan dispersi relatif antar variabel dengan satuan berbeda."),
            ("Berapakah nilai persentil data yang ekuivalen dengan Kuartil Atas (Q3)?",
             "Persentil ke-75 (P75)", "Kuartil Atas Q3 memotong 75% data terendah dari distribusi terurut, sehingga ekuivalen dengan Persentil ke-75 (P75).")
        ], [
            ("Jelaskan mengapa metrik rata-rata aritmetika (Mean) sering kali menyesatkan dalam pengukuran Service Level Agreement (SLA) latensi sistem perangkat lunak, dan mengapa industri mengadopsi Persentil P95 atau P99!",
             "Mean sangat sensitif terhadap outlier dan menyamarkan lonjakan latensi ekstrem. Misalkan 950 request selesai dalam 50 ms dan 50 request mengalami timeout 5000 ms. Mean latensi adalah 297.5 ms (terlihat wajar), namun 5% pengguna mengalami freeze fatal. Persentil P95 (50 ms) dan P99 (5000 ms) mampu mendeteksi secara transparan bahwa 1-5% pengguna mengalami gangguan performa parah.",
             "Bobot 100: Penjelasan kelemahan Mean thd outlier (40%), ilustrasi kasus latensi server (30%), urgensi P95/P99 dalam SLA (30%)."),
            ("Buktikan secara konseptual mengapa pembagi (n - 1) pada varians sampel menghasilkan penaksir tak bias (unbiased estimator) dibandingkan pembagi n!",
             "Sampel ditarik dari populasi dan deviasi diukur terhadap rata-rata sampel (X_bar), bukan rata-rata populasi sejati (mu). Karena X_bar dihitung dari sampel itu sendiri, titik data sampel selalu lebih dekat ke X_bar daripada ke mu, sehingga jumlah kuadrat deviasi sum(X_i - X_bar)^2 selalu lebih kecil daripada sum(X_i - mu)^2. Membagi dengan n akan menghasilkan nilai yang terlalu kecil (underestimate). Pengurangan 1 derajat kebebasan (n - 1) mengompensasi hilangnya informasi akibat estimasi mu oleh X_bar, menghasilkan penaksir yang tepat sama dengan ekspektasi varians populasi E[s^2] = sigma^2.",
             "Bobot 100: Penjelasan kedekatan sampel ke X_bar vs mu (40%), konsep kehilangan derajat kebebasan (30%), formulasi ekspektasi E[s^2]=sigma^2 (30%)."),
            ("Diberikan dataset waktu muat halaman (detik): [1.2, 1.4, 1.5, 1.6, 1.8, 2.0, 2.1, 2.3, 2.5, 8.5]. Hitunglah: (a) Mean & Median, (b) Q1, Q3, dan IQR, (c) Lakukan uji Pagar Tukey untuk membuktikan apakah 8.5 detik adalah pencilan!",
             "(a) Total = 24.9, n = 10. Mean = 2.49 detik. Median = (1.8 + 2.0)/2 = 1.90 detik.\n(b) Q1 = 1.5 detik, Q3 = 2.3 detik. IQR = 2.3 - 1.5 = 0.8 detik.\n(c) Upper Fence = Q3 + 1.5 * IQR = 2.3 + (1.5 * 0.8) = 2.3 + 1.2 = 3.5 detik. Karena 8.5 > 3.5 detik, maka nilai 8.5 terbukti secara statistik merupakan pencilan (outlier) ekstrem.",
             "Bobot 100: Ketepatan perhitungan Mean & Median (30%), perhitungan Q1, Q3, IQR (30%), pembuktian Pagar Tukey dan kesimpulan (40%)."),
            ("Jelaskan perbedaan antara Standard Scaler (Z-score normalization) dan Robust Scaler dalam pra-pemrosesan fitur machine learning, serta tentukan kapan masing-masing harus digunakan!",
             "Standard Scaler menggunakan rumus Z = (X - Mean) / Std. Sangat sensitif terhadap outlier karena Mean dan Std terdistorsi oleh nilai ekstrem. Robust Scaler menggunakan rumus X_scaled = (X - Median) / IQR. Menggunakan Median dan IQR yang tahan terhadap outlier. Standard Scaler optimal untuk data yang berdistribusi normal tanpa pencilan, sedangkan Robust Scaler wajib digunakan jika dataset mengandung pencilan ekstrem atau berdistribusi miring (skewed).",
             "Bobot 100: Perbandingan rumus matematis (40%), analisis sensitivitas thd outlier (30%), use-case skenario yang tepat (30%).")
        ]),

        # MODUL 03
        (3, "Visualisasi Data & Tabel Kontingensi", "Buku 1", [
            ("Uji statistik inferensial non-parametrik yang digunakan untuk menguji ada tidaknya hubungan dependensi/asosiasi antara dua variabel kategorikal pada tabel kontingensi adalah:",
             {"A": "Uji-t Dua Sampel", "B": "Uji Chi-Square (Independensi)", "C": "Uji F ANOVA", "D": "Uji Korelasi Pearson", "E": "Uji Durbin-Watson"}, "B",
             "Uji Chi-Square Independensi (Chi-Square Test of Independence) membandingkan frekuensi observasi (O) dengan frekuensi ekspektasi (E) pada tabel kontingensi r x c untuk menguji independensi bivariat."),
            ("Diagram visualisasi yang paling efektif untuk membandingkan distribusi probabilitas kontinu multi-modal antar kelompok kategori sekaligus menampilkan kuartil adalah:",
             {"A": "Pie Chart", "B": "Violin Plot", "C": "Scatter Plot", "D": "Line Chart", "E": "Stacked Bar Chart"}, "B",
             "Violin Plot menggabungkan Boxplot (menampilkan Q1, Median, Q3) dengan Kernel Density Estimation (KDE) yang memperlihatkan kurva densitas probabilitas dan pola multi-modal secara visual."),
            ("Formula frekuensi harapan (Expected Frequency / E_ij) pada sel baris ke-i dan kolom ke-j pada tabel kontingensi dengan total sampel N adalah:",
             {"A": "(Total Baris i * Total Kolom j) / N", "B": "(Total Baris i + Total Kolom j) / N", "C": "O_ij / N", "D": "(O_ij - E_ij)² / N", "E": "Total Baris i / Total Kolom j"}, "A",
             "Frekuensi harapan dihitung dengan rumus E_ij = (Row Total_i * Column Total_j) / Grand Total N berdasarkan asumsi independensi stokastik antar variabel."),
            ("Derajat kebebasan (degrees of freedom / df) pada uji Chi-Square untuk tabel kontingensi berukuran r baris dan c kolom adalah:",
             {"A": "r * c", "B": "(r - 1) * (c - 1)", "C": "r + c - 1", "D": "N - r - c", "E": "(r - 1) + (c - 1)"}, "B",
             "Derajat kebebasan untuk tabel kontingensi r x c adalah df = (r - 1) * (c - 1).")
        ], [
            ("Berapakah derajat kebebasan (df) uji Chi-Square untuk tabel kontingensi berukuran 3 baris x 4 kolom?",
             "df = 6", "df = (r - 1) * (c - 1) = (3 - 1) * (4 - 1) = 2 * 3 = 6."),
            ("Jika total baris ke-1 adalah 50, total kolom ke-2 adalah 40, dan grand total N = 200, berapakah nilai frekuensi harapan E_12?",
             "E_12 = 10", "E_12 = (50 * 40) / 200 = 2000 / 200 = 10."),
            ("Sebutkan fungsi dalam pustaka SciPy Python yang digunakan untuk melakukan uji Chi-Square tabel kontingensi secara otomatis!",
             "scipy.stats.chi2_contingency()", "Fungsi scipy.stats.chi2_contingency() menghitung statistik chi2, p-value, df, dan matriks frekuensi harapan dari tabel kontingensi."),
            ("Apa nama representasi visual grafis 2D yang menggunakan gradasi intensitas warna untuk menampilkan nilai matriks korelasi atau tabel kontingensi?",
             "Heatmap", "Heatmap memvisualisasikan data matriks numerik dengan pemetaan warna gradien untuk memudahkan identifikasi pola konsentrasi data.")
        ], [
            ("Diberikan tabel kontingensi 2x2 evaluasi konversi pengguna berdasarkan metode pembayaran: E-Wallet (Beli=60, Batal=40), Transfer Bank (Beli=30, Batal=70). Hitunglah nilai frekuensi ekspektasi (E), statistik Chi-Square hitung, dan simpulkan apakah ada hubungan signifikan pada alpha = 0.05 (Nilai kritis Chi-Square tabel df=1 adalah 3.841)!",
             "Total E-Wallet = 100, Transfer = 100. Total Beli = 90, Batal = 110. Grand Total N = 200.\nE_11 = (100*90)/200 = 45; E_12 = (100*110)/200 = 55.\nE_21 = (100*90)/200 = 45; E_22 = (100*110)/200 = 55.\nChi2 = (60-45)^2/45 + (40-55)^2/55 + (30-45)^2/45 + (70-55)^2/55 = 225/45 + 225/55 + 225/45 + 225/55 = 5.0 + 4.091 + 5.0 + 4.091 = 18.182.\nKarena Chi2 hitung (18.182) > Chi2 tabel (3.841), tolak H0. Kesimpulan: Terdapat hubungan signifikan antara metode pembayaran dan keputusan konversi pembelian pengguna (p < 0.05).",
             "Bobot 100: Perhitungan frekuensi ekspektasi lengkap (30%), perhitungan nilai Chi-Square hitung tepat (40%), perbandingan dengan nilai kritis dan kesimpulan substantif (30%)."),
            ("Jelaskan asumsi dan syarat kelayakan penggunaan uji Chi-Square tabel kontingensi, serta jelaskan apa solusi komputasi jika frekuensi harapan (Expected Frequency) sel bernilai < 5!",
             "Syarat Chi-Square: 1) Data berupa frekuensi kategorikal independen. 2) Tidak boleh ada sel dengan frekuensi harapan E < 1. 3) Tidak lebih dari 20% sel memiliki E < 5. Jika syarat dilanggar (E < 5): Untuk tabel 2x2, gunakan uji eksak Fisher (Fisher's Exact Test / scipy.stats.fisher_exact). Untuk tabel r x c yang lebih besar, gabungkan (collapse) kategori yang berdekatan atau gunakan simulasi Monte Carlo p-value.",
             "Bobot 100: Penjelasan 3 syarat Chi-Square (40%), identifikasi masalah E < 5 (30%), solusi Fisher Exact Test & collapsing categories (30%)."),
            ("Bandingkan kelebihan dan kekurangan visualisasi Boxplot vs Violin Plot dalam mengeksplorasi performa latensi microservices multivariat!",
             "Boxplot: Kelebihan: Sangat cepat dibaca, menampilkan 5-number summary (Min, Q1, Median, Q3, Max) dan outlier secara tegas. Kekurangan: Tidak dapat memperlihatkan distribusi multi-modal (misal dua puncak beban kerja) atau kepadatan lokal. Violin Plot: Kelebihan: Menampilkan kurva densitas KDE penuh, mampu memperlihatkan distribusi bimodal/multimodal dan bentuk kemiringan secara presisi. Kekurangan: Membutuhkan komputasi KDE dan lebih sulit diinterpretasikan oleh pemangku kepentingan non-teknis.",
             "Bobot 100: Analisis kelebihan-kekurangan Boxplot (40%), analisis Violin Plot (40%), konteks data performa microservice (20%)."),
            ("Rancanglah pipeline kode Python (menggunakan Pandas, Seaborn, dan SciPy) untuk membuat tabel kontingensi proporsi baris (crosstab normalize='index'), heatmap visualisasi, dan uji signifikansi Chi-Square secara otomatis dari DataFrame df dengan kolom 'device_type' dan 'churn_status'!",
             "Kode pipeline:\nimport pandas as pd, seaborn as sns, matplotlib.pyplot as plt, scipy.stats as stats\n# 1. Crosstab Frekuensi & Proporsi\nct_freq = pd.crosstab(df['device_type'], df['churn_status'])\nct_prop = pd.crosstab(df['device_type'], df['churn_status'], normalize='index') * 100\n# 2. Uji Chi-Square\nchi2, p, dof, ex = stats.chi2_contingency(ct_freq)\nprint(f'Chi2: {chi2:.4f}, p-value: {p:.4e}, df: {dof}')\n# 3. Visualisasi Heatmap\nplt.figure(figsize=(8,5))\nsns.heatmap(ct_prop, annot=True, fmt='.1f', cmap='Blues')\nplt.title('Proporsi Churn per Tipe Device (%)')\nplt.show()",
             "Bobot 100: Sintaks pd.crosstab proporsi tepat (30%), eksekusi chi2_contingency tepat (35%), visualisasi sns.heatmap rapi (35%).")
        ])
    ]

    return mod_data

print("Module data blueprint ready...")
