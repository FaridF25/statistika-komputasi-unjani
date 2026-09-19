# Modul 11 - 14

def load_part3(add_module):
    # Modul 11: Teori Probabilitas & Distribusi
    add_module(
        11, "Teori Probabilitas & Distribusi", "Buku 1",
        [
            ("Teorema Bayes digunakan dalam pemodelan probabilistik komputasi untuk:",
             {"A": "Menghitung nilai rata-rata sampel", "B": "Memperbarui peluang prior hipotesis P(H) menjadi peluang posterior P(H|E) setelah diperoleh bukti data empiris E", "C": "Menentukan jumlah klaster K-Means", "D": "Mengurangi dimensi fitur", "E": "Menguji normalitas data"}, "B",
             "Teorema Bayes P(H|E) = (P(E|H) * P(H)) / P(E) memperbarui keyakinan probabilitas hipotesis (Prior) berdasarkan kemunculan bukti observasi baru (Likelihood & Evidence) menjadi Posterior Probability."),
            ("Distribusi probabilitas diskrit yang digunakan untuk memodelkan banyaknya kedatangan request jaringan atau panggilan API yang terjadi dalam suatu interval waktu tertentu dengan laju konstan lambda adalah:",
             {"A": "Distribusi Normal (Gauss)", "B": "Distribusi Poisson", "C": "Distribusi Binomial", "D": "Distribusi Eksponensial", "E": "Distribusi Uniform Kontinu"}, "B",
             "Distribusi Poisson memodelkan jumlah peristiwa diskrit langka yang terjadi per unit interval waktu/ruang dengan parameter rata-rata laju kedatangan lambda."),
            ("Pada distribusi Normal Standar (Z-Distribution), nilai rata-rata (mu) dan standar deviasi (sigma) berturut-turut adalah:",
             {"A": "mu = 1, sigma = 0", "B": "mu = 0, sigma = 1", "C": "mu = 100, sigma = 15", "D": "mu = 0.5, sigma = 0.5", "E": "mu = -1, sigma = +1"}, "B",
             "Distribusi Normal Baku (Standard Normal) memiliki parameter baku mu = 0 dan varians sigma² = 1 (sigma = 1)."),
            ("Sifat unik 'Memoryless Property' (Ketiadaan Memori) yang menyatakan bahwa peluang kegagalan masa depan tidak bergantung pada berapa lama sistem telah berjalan adalah ciri khas dari distribusi:",
             {"A": "Distribusi Normal", "B": "Distribusi Eksponensial", "C": "Distribusi Poisson", "D": "Distribusi Student's t", "E": "Distribusi Chi-Square"}, "B",
             "Distribusi Eksponensial memiliki sifat Memoryless: P(X > s + t | X > s) = P(X > t). Distribusi ini memodelkan waktu antar-kedatangan peristiwa Poisson kontinu.")
        ],
        [
            ("Jika peluang sebuah paket data hilang (packet loss) adalah p = 0.02, berapakah nilai ekspektasi (rata-rata) jumlah paket yang hilang dari pengiriman n = 500 paket (Distribusi Binomial)?",
             "E[X] = 10 paket", "Formula ekspektasi Binomial E[X] = n * p = 500 * 0.02 = 10 paket."),
            ("Tuliskan formula Teorema Bayes untuk menghitung probabilitas posterior P(A|B)!",
             "P(A|B) = [P(B|A) * P(A)] / P(B)", "Teorema Bayes: Posterior = (Likelihood * Prior) / Total Evidence."),
            ("Pada kurva normal standar Z, berapa persentase total data yang berada di antara Z = -1.96 dan Z = +1.96?",
             "95.0% (atau 95.45% untuk rentang +/- 2 sigma)", "Rentang Z = +/- 1.96 mencakup tepat 95.0% area di bawah kurva normal standar (tingkat kepercayaan 95%)."),
            ("Jika rata-rata kedatangan request API adalah lambda = 4 request per detik, berapakah varians dari jumlah request per detik tersebut (Distribusi Poisson)?",
             "Varians = 4.0", "Pada Distribusi Poisson, nilai varians identik sama dengan nilai rata-ratanya: Var(X) = lambda = 4.0.")
        ],
        [
            ("Sebuah sistem filter email spam mengklasifikasikan email masuk. Diketahui:\n- Peluang email adalah spam: P(Spam) = 0.20, sehingga P(Bukan Spam) = 0.80.\n- Kata 'Hadiah Gratis' muncul pada 70% email spam: P(Kata|Spam) = 0.70.\n- Kata 'Hadiah Gratis' hanya muncul pada 5% email bukan spam: P(Kata|Bukan Spam) = 0.05.\nJika sebuah email baru masuk dan memuat kata 'Hadiah Gratis', hitunglah probabilitas posterior bahwa email tersebut benar-benar SPAM!",
             "Langkah Perhitungan Teorema Bayes:\n1. Hitung Total Evidence P(Kata):\nP(Kata) = [P(Kata|Spam) * P(Spam)] + [P(Kata|Bukan Spam) * P(Bukan Spam)]\nP(Kata) = (0.70 * 0.20) + (0.05 * 0.80) = 0.14 + 0.04 = 0.18 (18.0%).\n2. Hitung Posterior Probability P(Spam|Kata):\nP(Spam|Kata) = [P(Kata|Spam) * P(Spam)] / P(Kata) = 0.14 / 0.18 = 14 / 18 = 0.7778 (77.78%).\nKesimpulan: Peluang email tersebut merupakan spam meningkat drastis dari prior 20.0% menjadi 77.78% setelah terdeteksi memuat kata 'Hadiah Gratis'.",
             "Bobot 100: Perhitungan Total Evidence tepat (40%), perhitungan Posterior Bayes tepat (40%), kesimpulan interpretasi tepat (20%)."),
            ("Jelaskan perbedaan karakteristik matematis antara Distribusi Binomial, Distribusi Poisson, dan Distribusi Eksponensial dalam konteks pemodelan keandalan sistem jaringan komputer!",
             "1. Binomial: Distribusi diskrit untuk menghitung jumlah sukses k dari n percobaan independen biner (sukses/gagal) dengan peluang sukses p konstan. Contoh: Jumlah paket data yang rusak dari 100 paket yang ditransmisikan.\n2. Poisson: Distribusi diskrit untuk menghitung jumlah peristiwa langka yang terjadi dalam interval waktu/ruang kontinu tertentu dengan laju rata-rata lambda konstan. Contoh: Jumlah koneksi baru yang masuk ke web server per detik.\n3. Eksponensial: Distribusi kontinu untuk memodelkan durasi waktu tunggu antar-peristiwa Poisson atau waktu hingga terjadinya kegagalan pertama (Time to Failure) dengan laju kegagalan lambda konstan. Bersifat memoryless.",
             "Bobot 100: Karakteristik Binomial (35%), karakteristik Poisson (35%), karakteristik Eksponensial & memoryless (30%)."),
            ("Waktu respon suatu database berdistribusi normal dengan rata-rata mu = 120 ms dan standar deviasi sigma = 20 ms. (a) Berapa probabilitas query database selesai dalam waktu kurang dari 150 ms? (b) Jika Service Level Agreement (SLA) menetapkan batas atas latensi pada 99% query tercepat, berapa ambang batas latensi SLA tersebut? (Diketahui: Z_0.9332 = 1.5, Z_0.99 = 2.326)!",
             "(a) Standarisasi Z-score untuk X = 150 ms:\nZ = (150 - 120) / 20 = 30 / 20 = +1.5.\nProbabilitas P(X < 150) = P(Z < 1.5) = 0.9332 (93.32%).\n(b) Ambang Batas SLA Persentil ke-99:\nZ = 2.326. Rumus X = mu + (Z * sigma) = 120 + (2.326 * 20) = 120 + 46.52 = 166.52 ms.\nKesimpulan SLA: Batas maksimum waktu respon yang dapat ditoleransi untuk 99% query adalah 166.52 ms.",
             "Bobot 100: Perhitungan Z-score dan probabilitas bagian a tepat (50%), perhitungan batas latensi persentil ke-99 SLA tepat (50%)."),
            ("Jelaskan konsep 'The Law of Large Numbers' (Hukum Bilangan Besar) dan 'Central Limit Theorem' (Teorema Limit Pusat) serta jelaskan signifikansinya dalam komputasi simulasi Monte Carlo!",
             "1. Law of Large Numbers (LLN): Menyatakan bahwa jika suatu eksperimen acak diulang dalam jumlah yang sangat besar (n -> tak hingga), rata-rata sampel X_bar akan konvergen secara pasti menuju nilai harapan matematis populasi mu.\n2. Central Limit Theorem (CLT): Menyatakan bahwa distribusi rata-rata sampel dari sembarang populasi (dengan bentuk distribusi apapun, asalkan memiliki varians terhingga) akan mendekati distribusi normal seiring bertambahnya ukuran sampel (umumnya n >= 30).\n3. Signifikansi Monte Carlo: Memungkinkan algoritma simulasi komputasi memprediksi sistem stokastik yang sangat kompleks (misal: estimasi risiko beban server atau integral dimensi tinggi) dengan mengambil sampel acak jutaan kali: LLN menjamin akurasi konvergensi nilai estimasi, dan CLT menyediakan batas interval kepercayaan (confidence interval) bagi galat estimasi.",
             "Bobot 100: Penjelasan LLN (35%), penjelasan CLT (35%), signifikansi komputasi simulasi Monte Carlo (30%).")
        ]
    )

    # Modul 12: Studi Kasus 1: Risiko Kredit Fintech
    add_module(
        12, "Studi Kasus 1: Risiko Kredit Fintech", "Buku 1",
        [
            ("Dalam pemodelan Credit Scoring pada platform Fintech P2P Lending, variabel target biner 'default' (1 = gagal bayar, 0 = lancar) paling tepat dimodelkan menggunakan algoritma:",
             {"A": "Regresi Linier OLS", "B": "Regresi Logistik Biner dengan Tuning Probabilitas", "C": "K-Means Clustering", "D": "Apriori Association Rules", "E": "PCA Reduksi Dimensi"}, "B",
             "Regresi Logistik menghasilkan estimasi probabilitas default P(Y=1) yang dapat dikalibrasi ambang batasnya (threshold tuning) sesuai dengan profil toleransi risiko finansial perusahaan."),
            ("Dampak finansial dari kesalahan False Negative (FN / memprediksi nasabah macet sebagai nasabah lancar) dibandingkan False Positive (FP / menolak nasabah baik) dalam bisnis fintech adalah:",
             {"A": "FN merugikan biaya kehilangan pokok pinjaman (Loss of Principal), yang jauh lebih mahal daripada FP yang hanya kehilangan potensi bunga (Opportunity Cost)", "B": "FP selalu lebih berbahaya daripada FN", "C": "Biaya FN dan FP selalu identik sama", "D": "FN meningkatkan margin keuntungan perusahaan", "E": "FP menyebabkan sistem basis data macet"}, "A",
             "False Negative menyebabkan kredit macet total (kehilangan modal pokok pinjaman), sedangkan False Positive hanya kehilangan potensi keuntungan bunga kredit (opportunity cost)."),
            ("Metrik evaluasi kurva yang paling ideal untuk membandingkan kinerja model credit scoring tanpa tergantung pada pemilihan ambang batas tunggal (threshold-independent) adalah:",
             {"A": "Accuracy Score", "B": "Area Under the ROC Curve (ROC-AUC)", "C": "Sum of Squared Errors", "D": "Within-Cluster Sum of Squares", "E": "Chi-Square p-value"}, "B",
             "ROC-AUC mengevaluasi kemampuan pemeringkatan dan diskriminasi model dalam memisahkan kelas berisiko tinggi dan rendah di seluruh spektrum ambang batas probabilitas."),
            ("Jika model credit scoring menghasilkan koefisien logistik beta = -0.05 untuk variabel 'pendapatan_bulanan_juta' (OR = exp(-0.05) = 0.951), artinya:",
             {"A": "Setiap kenaikan pendapatan 1 juta rupiah menurunkan risiko odds default kredit sebesar 4.9%", "B": "Pendapatan tidak berpengaruh terhadap risiko", "C": "Pendapatan meningkatkan risiko gagal bayar", "D": "Nasabah berpendapatan tinggi pasti gagal bayar", "E": "Model mengalami overfitting"}, "A",
             "Odds Ratio = 0.951 (< 1.0) menunjukkan efek protektif: setiap kenaikan pendapatan 1 juta rupiah menurunkan odds gagal bayar sebesar (1 - 0.951) = 4.9%.")
        ],
        [
            ("Jika sebuah platform fintech ingin meminimalkan risiko kredit macet (False Negative) secara agresif, apakah ambang batas probabilitas (threshold) harus dinaikkan atau diturunkan dari 0.50?",
             "Diturunkan (misal ke 0.30 atau 0.25)", "Menurunkan threshold menyebabkan model lebih ketat menolak pengajuan kredit yang memiliki indikasi risiko default rendah-menengah."),
            ("Tuliskan formula perhitungan Specificity (Tingkat Ketepatan Kelas Negatif / Nasabah Lancar) dari Confusion Matrix!",
             "Specificity = TN / (TN + FP)", "Specificity mengukur proporsi nasabah lancar (aktual negatif) yang berhasil diprediksi secara tepat sebagai lancar (True Negatives)."),
            ("Sebutkan nama matriks biaya dalam analisis keputusan data science yang menetapkan bobot kerugian moneter riil untuk setiap sel Confusion Matrix (TP, FP, TN, FN)!",
             "Cost-Loss Matrix / Financial Cost Matrix", "Matriks Biaya Finansial mengalikan jumlah prediksi pada Confusion Matrix dengan nilai kerugian finansial moneter aktual."),
            ("Jika nilai ROC-AUC sebuah model credit scoring adalah 0.92, bagaimana predikat kualitas pemisahan risiko model tersebut?",
             "Sangat Baik / Luar Biasa (Outstanding Discrimination)", "Nilai ROC-AUC 0.90 - 1.00 dikategorikan sebagai model dengan diskriminasi luar biasa (outstanding/excellent).")
        ],
        [
            ("Sebuah fintech UMKM menguji model credit scoring pada 1.000 pengajuan pinjaman dengan rata-rata pinjaman Rp 10.000.000. Matriks biaya menetapkan: Kerugian False Negative (kredit macet total) = Rp 10.000.000 per nasabah; Kerugian False Positive (kehilangan margin bunga 15%) = Rp 1.500.000 per nasabah. Dua model diuji:\n- Model A (Threshold 0.50): TP = 80, FP = 20, FN = 20, TN = 880.\n- Model B (Threshold 0.30): TP = 95, FP = 60, FN = 5, TN = 840.\nHitunglah total kerugian finansial untuk masing-masing model dan tentukan model mana yang paling menguntungkan bagi bisnis fintech!",
             "Perhitungan Biaya Finansial:\n1. Model A:\n- Biaya FN = 20 nasabah * Rp 10.000.000 = Rp 200.000.000\n- Biaya FP = 20 nasabah * Rp 1.500.000 = Rp 30.000.000\n- Total Kerugian Finansial Model A = Rp 230.000.000.\n2. Model B:\n- Biaya FN = 5 nasabah * Rp 10.000.000 = Rp 50.000.000\n- Biaya FP = 60 nasabah * Rp 1.500.000 = Rp 90.000.000\n- Total Kerugian Finansial Model B = Rp 140.000.000.\nKesimpulan Keputusan Bisnis:\nModel B (Threshold 0.30) jauh lebih menguntungkan karena mampu menghemat kerugian finansial sebesar Rp 90.000.000 (Rp 230 juta - Rp 140 juta) dengan menekan angka kredit macet secara drastis.",
             "Bobot 100: Perhitungan biaya Model A tepat (35%), perhitungan biaya Model B tepat (35%), perbandingan finansial & kesimpulan bisnis tepat (30%)."),
            ("Jelaskan rancangan arsitektur pipeline data science end-to-end untuk sistem otomatisasi Credit Scoring UMKM berbasis Machine Learning di lingkungan cloud production!",
             "Pipeline End-to-End:\n1. Data Ingestion & Validation: Mengambil data historis UMKM (laporan mutasi rekening bank, omzet e-commerce, riwayat transaksi payment gateway, usia bisnis). Validasi skema data & deteksi missing values.\n2. Feature Engineering & Preprocessing: Imputasi median, One-Hot Encoding fitur kategorikal (sektor usaha), penskalaan fitur numerik (RobustScaler), penghapusan multikolinearitas (VIF filtering).\n3. Model Training & Cross-Validation: Melatih model ensemble/regresi logistik dengan stratifikasi 5-Fold Cross Validation. Optimasi hyperparameter.\n4. Threshold Calibration: Mengalibrasi ambang batas probabilitas menggunakan matriks biaya finansial untuk meminimalkan expected loss.\n5. Model Serving API: Menerapkan model sebagai RESTful API (FastAPI / Docker di Kubernetes) untuk inferensi credit scoring real-time saat pengguna mengajukan pinjaman.\n6. Monitoring & Drift Detection: Memonitor metrik ROC-AUC harian dan mendeteksi data drift / concept drift seiring perubahan kondisi ekonomi makro.",
             "Bobot 100: Penjelasan ingestion & preprocessing (30%), training & kalibrasi threshold (35%), serving API & drift monitoring (35%)."),
            ("Jelaskan mengapa masalah ketidakseimbangan kelas (Class Imbalance) sangat umum terjadi pada dataset kredit perbankan (misal: 97% lancar, 3% macet), dan jelaskan 3 teknik rekayasa data untuk mengatasinya!",
             "Penyebab: Mayoritas nasabah perbankan adalah nasabah baik yang membayar tepat waktu, sehingga kasus gagal bayar (default) adalah peristiwa langka (rare event).\nMasalah: Model cenderung bias memprediksi semua nasabah sebagai 'Lancar' untuk mencapai akurasi 97%, padahal gagal total mendeteksi nasabah macet.\n3 Teknik Solusi:\n1. SMOTE (Synthetic Minority Over-sampling Technique): Membuat data sintetis baru untuk kelas minoritas (gagal bayar) berdasarkan interpolasi k-tetangga terdekat.\n2. Class Weighting / Cost-Sensitive Learning: Memberikan bobot penalti loss function yang jauh lebih berat pada kesalahan kelas minoritas (misal class_weight='balanced' pada Logistic Regression).\n3. Random Under-sampling: Mengurangi jumlah sampel kelas mayoritas secara proporsional agar rasio dataset lebih berimbang.",
             "Bobot 100: Analisis penyebab & bahaya class imbalance (40%), penjelasan 3 teknik penanganan SMOTE, Class Weighting, Under-sampling (60%)."),
            ("Rancang skrip Python untuk mencari ambang batas probabilitas optimal (Optimal Decision Threshold) dari model regresi logistik yang meminimalkan total financial loss berdasarkan fungsi biaya kustom!",
             "Skrip Python:\nimport numpy as np\ndef find_optimal_threshold(y_true, y_proba, cost_fn=10000000, cost_fp=1500000):\n    thresholds = np.linspace(0.01, 0.99, 100)\n    best_thresh, min_loss = 0.50, float('inf')\n    for th in thresholds:\n        y_pred = (y_proba >= th).astype(int)\n        fn = np.sum((y_true == 1) & (y_pred == 0))\n        fp = np.sum((y_true == 0) & (y_pred == 1))\n        total_loss = (fn * cost_fn) + (fp * cost_fp)\n        if total_loss < min_loss:\n            min_loss = total_loss\n            best_thresh = th\n    print(f'Optimal Threshold: {best_thresh:.3f} | Minimum Financial Loss: Rp {min_loss:,.0f}')\n    return best_thresh",
             "Bobot 100: Logika loop threshold linspace tepat (35%), formulasi penghitungan FN dan FP tepat (35%), optimasi pencarian minimum loss valid (30%).")
        ]
    )

    # Modul 13: Studi Kasus 2: Segmentasi & Rekomendasi E-Commerce
    add_module(
        13, "Studi Kasus 2: Segmentasi & Rekomendasi E-Commerce", "Buku 1",
        [
            ("Dalam arsitektur sistem rekomendasi e-commerce hibrida, integrasi antara algoritma K-Means dan Algoritma Apriori bertujuan untuk:",
             {"A": "Menghitung nilai regresi linier biaya server", "B": "Mensegmentasi pengguna ke dalam persona klaster perilaku, lalu menerapkan aturan asosiasi produk yang relevan per segmen", "C": "Mereduksi dimensi teks ulasan pengguna", "D": "Mengenkripsi token transaksi", "E": "Menguji kesepakatan penilai QA"}, "B",
             "Segmentasi persona membagi audiens menjadi kelompok homogen (misal: 'Tech Enthusiast', 'Diskon Hunter'), kemudian Market Basket Analysis diterapkan pada tiap klaster untuk menghasilkan rekomendasi bundling yang sangat personal."),
            ("Metode normalisasi data numerik yang mengubah nilai fitur ke dalam rentang skala seragam [0, 1] menggunakan nilai minimum dan maksimum adalah:",
             {"A": "StandardScaler (Z-Score)", "B": "MinMaxScaler", "C": "RobustScaler", "D": "Log Transform", "E": "Box-Cox Scaling"}, "B",
             "MinMaxScaler mengonversi fitur dengan rumus X_norm = (X - X_min) / (X_max - X_min) sehingga seluruh fitur bernilai pada domain tertutup [0, 1]."),
            ("Fitur perilaku berikut manakah yang paling informatif untuk membentuk segmentasi persona pelanggan pada model RFM (Recency, Frequency, Monetary)?",
             {"A": "Jumlah hari sejak transaksi terakhir, total transaksi per tahun, dan total nilai belanja moneter", "B": "Alamat IP pengguna dan tipe browser", "C": "Warna tema aplikasi yang dipilih", "D": "Nomor rekening bank pelanggan", "E": "Versi kernel sistem operasi"}, "A",
             "Model RFM adalah standar analitik e-commerce yang mengombinasikan Recency (kebaruan transaksi), Frequency (frekuensi belanja), dan Monetary (total perputaran uang belanja)."),
            ("Metrik asosiasi yang digunakan untuk menyaring aturan rekomendasi bundling produk agar hanya menampilkan produk yang benar-benar dibeli secara signifikan bersamaan di atas kebetulan acak adalah:",
             {"A": "Lift Ratio >= 1.20 dan Confidence >= 60%", "B": "Support = 100%", "C": "Koefisien Pearson r = 0", "D": "P-value Shapiro-Wilk = 0.50", "E": "Inersia WCSS minimum"}, "A",
             "Kombinasi Lift Ratio > 1.20 dan Confidence tinggi menjamin bahwa aturan bundling memiliki kekuatan asosiasi positif yang nyata dan tingkat kepastian pembelian yang tinggi.")
        ],
        [
            ("Tuliskan formula matematis transformasi Min-Max Normalization untuk menstandarisasi fitur X ke rentang [0, 1]!",
             "X_norm = (X - X_min) / (X_max - X_min)", "Min-Max scaler membagi selisih nilai terhadap minimum dengan rentang data (Range)."),
            ("Sebutkan 3 dimensi utama dalam model segmentasi pelanggan RFM!",
             "Recency (Kebaruan), Frequency (Frekuensi), Monetary (Nilai Moneter Belanja)", "Model RFM mengevaluasi kapan transaksi terakhir terjadi, seberapa sering belanja, dan berapa total uang yang dibelanjakan."),
            ("Jika klaster pelanggan 'Sultan / High-Spender' memiliki rata-rata belanja tinggi namun frekuensi rendah, strategi promosi apa yang paling efektif?",
             "Penawaran produk premium / eksklusif dan program loyalitas VIP", "Segmen high-monetary merespon sangat baik terhadap produk eksklusif bernilai tinggi dan pelayanan VIP concierge."),
            ("Apakah fungsi dari visualisasi Radar Chart (Spider Plot) dalam interpretasi persona klaster pelanggan?",
             "Menampilkan profil kekuatan multivariat rata-rata fitur tiap klaster secara visual 360 derajat", "Radar Chart membandingkan karakteristik rata-rata tiap segmen pada berbagai dimensi fitur secara simultan.")
        ],
        [
            ("Rancanglah konsep sistem analitik e-commerce yang menggabungkan Analisis Klaster (K-Means) untuk segmentasi persona pembeli dengan Market Basket Analysis (Apriori) untuk mesin rekomendasi cross-selling yang dipersonalisasi!",
             "Konsep Desain Sistem:\n1. Pengumpulan Data Perilaku: Ekstraksi fitur transaksi pelanggan (Frekuensi belanja, Rata-rata keranjang belanja, Diskon sensitivity, Rasio browsing kategori gadget/fashion).\n2. Segmentasi K-Means: Data dinormalisasi (StandardScaler), k optimal ditentukan via Silhouette Score. Terbentuk persona: Klaster 1 ('Budget Hunters'), Klaster 2 ('Tech Gadget Lovers'), Klaster 3 ('Family Shoppers').\n3. Pemisahan Transaksi per Klaster: Basis data transaksi dipartisi berdasarkan keanggotaan klaster pengguna.\n4. Mining Association Rules per Klaster: Algoritma Apriori dijalankan secara terpisah pada masing-masing partisi transaksi. Hasilnya:\n- Klaster Tech: {Laptop} -> {Mechanical Keyboard, Mouse Gaming} (Lift 2.5).\n- Klaster Budget: {Minyak Goreng} -> {Gula Pasir Diskon} (Lift 1.8).\n5. Serving Engine Real-Time: Saat user login, sistem mengidentifikasi ID klasternya dan menampilkan widget 'Rekomendasi Khusus Untuk Anda' yang ditenagai oleh aturan asosiasi spesifik klasternya.",
             "Bobot 100: Integrasi arsitektur K-Means + Apriori jelas (40%), segmentasi persona realistis (30%), pipeline inferensi rekomendasi real-time (30%)."),
            ("Diberikan profil centroid 3 klaster pelanggan e-commerce (skala 1 - 10): \n- Klaster 1: Income = 8.5, Spending = 9.2, Tech_Savvy = 8.8, Promo_Sensitivity = 2.1.\n- Klaster 2: Income = 4.2, Spending = 3.5, Tech_Savvy = 4.0, Promo_Sensitivity = 9.5.\n- Klaster 3: Income = 6.0, Spending = 5.8, Tech_Savvy = 3.2, Promo_Sensitivity = 6.0.\nBerikan penamaan persona bisnis yang tepat untuk masing-masing klaster dan rancang strategi pemasaran digital yang spesifik untuk tiap klaster!",
             "1. Klaster 1: Persona 'Tech-Savvy Affluent / Sultan Digital'. Karakteristik: Pendapatan dan belanja sangat tinggi, melek teknologi tinggi, tidak peduli promo diskon. Strategi: Tawarkan gadget flagship terbaru, program membership eksklusif, dan opsi pengiriman same-day instan.\n2. Klaster 2: Persona 'Bargain Hunters / Pemburu Diskon'. Karakteristik: Pendapatan dan belanja rendah, sangat sensitif terhadap promo dan voucher gratis ongkir. Strategi: Kampanye Flash Sale berkala, promo bundling 'Beli 2 Gratis 1', dan voucher cashback koin.\n3. Klaster 3: Persona 'Mainstream Pragmatic / Pelanggan Reguler'. Karakteristik: Pendapatan dan belanja moderat, respon sedang terhadap promo. Strategi: Program poin loyalitas bertingkat, email newsletter berkala rekomendasi produk terlaris.",
             "Bobot 100: Penamaan persona 3 klaster tepat (40%), analisis karakteristik centroid tepat (30%), perancangan strategi bisnis relevan (30%)."),
            ("Jelaskan mengapa metrik Silhouette Coefficient lebih dapat diandalkan dibandingkan metode Elbow (Inersia WCSS) semata dalam menentukan jumlah k klaster optimal untuk data segmentasi e-commerce!",
             "Kelemahan Metode Elbow (WCSS): 1) Penentuan titik siku bersifat sangat subjektif dan visual (sering kali tidak terdapat titik patahan siku yang tegas / kurva melengkung mulus). 2) Inersia selalu menurun secara monotonik seiring penambahan k hingga k = N (WCSS = 0), sehingga tidak mengevaluasi apakah klaster baru benar-benar bermakna.\nKeunggulan Silhouette Coefficient: 1) Memberikan skor metrik kuantitatif eksak dan objektif pada rentang [-1, +1]. 2) Mengombinasikan evaluasi kekompakan internal klaster (kohesi intra-cluster a(i)) sekaligus derajat pemisahan dari klaster lain (separasi inter-cluster b(i)). Titik puncak nilai Silhouette langsung menunjukkan k optimal dengan pemisahan klaster terbaik.",
             "Bobot 100: Analisis kelemahan metode Elbow (40%), analisis keunggulan Silhouette Coefficient (40%), justifikasi matematis kohesi vs separasi (20%)."),
            ("Rancang skrip Python untuk memproses dataset transaksi e-commerce, mengelompokkan pengguna dengan K-Means k=3, dan mengekstrak matriks profil demografi & perilaku belanja per klaster menggunakan groupby!",
             "Skrip Python:\nimport pandas as pd\nfrom sklearn.preprocessing import StandardScaler\nfrom sklearn.cluster import KMeans\n# 1. Scaling Fitur RFM\nfeatures = ['recency_days', 'purchase_frequency', 'monetary_total_k', 'promo_usage_count']\nX = df_customers[features]\nscaler = StandardScaler()\nX_scaled = scaler.fit_transform(X)\n# 2. K-Means Clustering\nkm = KMeans(n_clusters=3, random_state=42, n_init=10)\ndf_customers['cluster_id'] = km.fit_predict(X_scaled)\n# 3. Profil Centroid Skala Asli\ncluster_profile = df_customers.groupby('cluster_id')[features].agg(['mean', 'median', 'count'])\nprint('=== Matriks Profil Persona Pelanggan E-Commerce ===')\ndisplay(cluster_profile.round(2))",
             "Bobot 100: Penskalaan fitur tepat (30%), eksekusi KMeans tepat (35%), agregasi groupby multi-fungsi mean, median, count tepat (35%).")
        ]
    )

    # Modul 14: Studi Kasus 3: A/B Testing Kinerja Sistem
    add_module(
        14, "Studi Kasus 3: A/B Testing Kinerja Sistem", "Buku 1",
        [
            ("Dalam eksperimen A/B Testing optimasi halaman checkout e-commerce, pengujian komparasi metrik rasio konversi biner (Checkout Sukses vs Batal) antar Varian Kontrol dan Varian Optimasi dianalisis menggunakan:",
             {"A": "Uji-t Satu Sampel", "B": "Uji Chi-Square Dua Sampel Independen (atau Uji Z Dua Proporsi)", "C": "Regresi Linier OLS", "D": "K-Means Clustering", "E": "PCA Decomposition"}, "B",
             "Metrik konversi adalah data kategorikal biner (proporsi sukses), sehingga pengujian signifikansi perbedaan rasio antar dua varian menggunakan Uji Chi-Square 2x2 atau Uji Z Dua Proporsi."),
            ("Uji-t Dua Sampel Welch (Welch's t-Test) lebih diutamakan dibandingkan Student's t-Test standar saat menguji perbedaan waktu muat halaman (latency) karena:",
             {"A": "Tidak memerlukan data berukuran besar", "B": "Mampu menangani kondisi di mana varians kedua kelompok tidak homogen (varians tidak sama)", "C": "Selalu menghasilkan p-value = 0", "D": "Hanya dapat digunakan pada data kategorikal", "E": "Menghitung median bukan mean"}, "B",
             "Welch's t-Test mengoreksi derajat kebebasan untuk mengatasi pelanggaran asumsi homogenitas varians (heteroskedastisitas) antar dua kelompok eksperimen."),
            ("Kesalahan Tipe I (Type I Error / False Positive) dalam eksperimen A/B Testing sistem didefinisikan sebagai:",
             {"A": "Menolak hipotesis nol (H0) padahal sebenarnya tidak ada perbedaan performa nyata antar varian", "B": "Gagal menolak H0 padahal sebenarnya ada perbaikan nyata", "C": "Salah menghitung rata-rata", "D": "Ukuran sampel terlalu besar", "E": "Waktu testing terlalu lama"}, "A",
             "Type I Error (alpha) adalah kesalahan 'False Positive', yaitu menyimpulkan bahwa Varian B lebih baik daripada Varian A padahal perbedaannya hanyalah fluktuasi acak semata."),
            ("Tingkat kekuatan statistik (Statistical Power = 1 - beta) standar industri yang direkomendasikan dalam perancangan ukuran sampel A/B Testing adalah setidaknya:",
             {"A": "20%", "B": "50%", "C": "80% (0.80)", "D": "99.9%", "E": "5%"}, "C",
             "Power statistik 80% (beta = 0.20) adalah standar emas industri yang menjamin probabilitas 80% bahwa eksperimen mampu mendeteksi efek perbaikan nyata (Minimum Detectable Effect / MDE) jika efek tersebut memang ada.")
        ],
        [
            ("Apakah hipotesis nol (H0) pada uji A/B Testing perbandingan rasio konversi antara Varian A (p_A) dan Varian B (p_B)?",
             "H0: p_A = p_B (Tidak ada perbedaan rasio konversi antara Varian A dan B)", "H0 selalu mengasumsikan ketiadaan efek atau perbedaan performa antar varian."),
            ("Jika Varian A memiliki rasio konversi 10.0% dan Varian B memiliki konversi 12.0%, berapakah persentase peningkatan relatif (Relative Uplift) dari Varian B?",
             "Relative Uplift = +20.0%", "Uplift = ((12.0 - 10.0) / 10.0) * 100% = (2.0 / 10.0) * 100% = +20.0%."),
            ("Sebutkan fenomena bias di mana pengguna baru menunjukkan ketertarikan sesaat terhadap antarmuka baru semata-mata karena hal baru, bukan karena desainnya lebih unggul!",
             "Novelty Effect (Efek Kebaruan)", "Novelty Effect adalah lonjakan performa artifisial sesaat pada antarmuka baru yang akan mereda kembali ke kondisi normal setelah beberapa minggu."),
            ("Fungsi dalam pustaka SciPy Python manakah yang digunakan untuk menghitung Welch's t-Test secara langsung dengan argumen equal_var=False?",
             "scipy.stats.ttest_ind(data_a, data_b, equal_var=False)", "Argumen equal_var=False mengaktifkan perhitungan uji-t Welch tanpa asumsi kesamaan varians.")
        ],
        [
            ("Sebuah tim rekayasa web melakukan A/B Testing redesain tombol Checkout pada 10.000 pengunjung per varian:\n- Varian A (Kontrol): 1.200 checkout sukses dari 10.000 pengunjung (Konversi = 12.0%).\n- Varian B (Redesain): 1.400 checkout sukses dari 10.000 pengunjung (Konversi = 14.0%).\nHitunglah: (a) Nilai standar error perbedaan proporsi, (b) Nilai Z-hitung (atau Chi-Square hitung), (c) Ujilah pada alpha = 0.05 apakah peningkatan konversi signifikan secara statistik (Nilai kritis Z_0.05 = 1.96)!",
             "Langkah Uji Z Dua Proporsi:\n1. Proporsi Gabungan (Pooled Proportion p_pool):\np_pool = (1200 + 1400) / (10000 + 10000) = 2600 / 20000 = 0.13.\nq_pool = 1 - 0.13 = 0.87.\n2. Standar Error Perbedaan Proporsi (SE):\nSE = sqrt( p_pool * q_pool * (1/n_A + 1/n_B) ) = sqrt( 0.13 * 0.87 * (1/10000 + 1/10000) )\nSE = sqrt( 0.1131 * 0.0002 ) = sqrt( 0.00002262 ) = 0.004756.\n3. Nilai Statistik Z-Hitung:\nZ = (p_B - p_A) / SE = (0.14 - 0.12) / 0.004756 = 0.02 / 0.004756 = +4.205.\n4. Kesimpulan Statistik:\nKarena Z-hitung (+4.205) > Z-kritis (+1.96), tolak H0 (p-value < 0.0001). Kesimpulan: Peningkatan rasio konversi Varian B sebesar +2.0% absolut (atau +16.67% relatif) adalah SIGNIFIKAN NYATA secara statistik. Tim produk direkomendasikan merilis Varian B ke 100% pengguna produksi.",
             "Bobot 100: Perhitungan pooled proportion & standard error tepat (40%), perhitungan Z-hitung tepat (35%), kesimpulan dan rekomendasi rilis tepat (25%)."),
            ("Jelaskan 3 jebakan metodologis (Common Pitfalls) yang sering merusak validitas kesimpulan eksperimen A/B Testing dalam rekayasa perangkat lunak, serta bagaimana cara mitigasinya!",
             "1. Peeking Problem (Mengintip Data Berulang Kali): Memeriksa p-value setiap jam dan menghentikan pengujian segera setelah p < 0.05. Ini melipatgandakan False Positive Rate secara dramatis. Mitigasi: Tentukan ukuran sampel dan durasi testing di awal (Fixed-horizon testing) atau gunakan Sequential Testing.\n2. Novelty Effect & Primacy Effect: Pengguna lama bingung dengan UI baru (Primacy Effect) atau pengguna antusias sesaat dengan UI baru (Novelty Effect). Mitigasi: Jalankan eksperimen minimal 2 minggu penuh (mencakup siklus weekday dan weekend) hingga efek kebaruan stabil.\n3. Sample Ratio Mismatch (SRM): Alokasi trafik aktual menyimpang dari rasio 50:50 yang direncanakan (misal 45:55) akibat kegagalan routing load balancer atau bot filtering. Mitigasi: Selalu jalankan uji Chi-Square Goodness-of-Fit pada jumlah trafik sebelum menganalisis metrik konversi.",
             "Bobot 100: Penjelasan Peeking Problem (35%), Novelty Effect (35%), Sample Ratio Mismatch (30%)."),
            ("Jelaskan faktor-faktor yang menentukan perhitungan Ukuran Sampel Minimum (Minimum Sample Size) yang dibutuhkan sebelum eksperimen A/B Testing diluncurkan!",
             "Faktor-faktor Penentu Ukuran Sampel:\n1. Baseline Conversion Rate (p): Tingkat konversi awal Varian Kontrol A saat ini.\n2. Minimum Detectable Effect (MDE / delta): Besaran perbaikan terkecil yang ingin dideteksi secara andal (misal kenaikan +1.0%). Semakin kecil MDE yang ingin dideteksi, semakin besar ukuran sampel yang dibutuhkan (skala kuadratik).\n3. Tingkat Signifikansi (alpha / Type I Error): Probabilitas menolak H0 saat tidak ada efek (biasanya 5% / alpha = 0.05, Z_alpha/2 = 1.96).\n4. Kekuatan Statistik (Statistical Power = 1 - beta / Type II Error): Probabilitas mendeteksi efek jika memang ada (biasanya 80% / beta = 0.20, Z_beta = 0.84).\nFormula Sampel n per varian: n = [2 * (Z_alpha/2 + Z_beta)² * p * (1 - p)] / (MDE)².",
             "Bobot 100: Penjelasan 4 faktor baseline, MDE, alpha, beta lengkap (60%), formulasi matematis ukuran sampel (40%)."),
            ("Rancang skrip Python lengkap untuk menganalisis data eksperimen A/B Testing: (1) Uji beda rata-rata Page Load Time menggunakan Welch's t-Test, (2) Uji rasio konversi menggunakan Chi-Square crosstab, dan (3) Membuat visualisasi KDE plot latensi dan Bar plot rasio konversi!",
             "Skrip Python:\nimport pandas as pd, scipy.stats as stats, matplotlib.pyplot as plt, seaborn as sns\n# 1. Welch t-Test Latensi\nlat_a = df[df['variant']=='A']['load_time_sec']\nlat_b = df[df['variant']=='B']['load_time_sec']\nt_stat, p_t = stats.ttest_ind(lat_a, lat_b, equal_var=False)\nprint(f'Welch t-Test: t = {t_stat:.4f}, p-value = {p_t:.4e}')\n# 2. Chi-Square Konversi\nct = pd.crosstab(df['variant'], df['converted'])\nchi2, p_chi2, _, _ = stats.chi2_contingency(ct)\nprint(f'Chi-Square Konversi: Chi2 = {chi2:.4f}, p-value = {p_chi2:.4e}')\n# 3. Visualisasi 2 Subplot\nfig, axes = plt.subplots(1, 2, figsize=(14, 5))\nsns.kdeplot(data=df, x='load_time_sec', hue='variant', fill=True, ax=axes[0])\naxes[0].set_title('Distribusi Latensi (KDE Plot)')\nconv_rates = df.groupby('variant')['converted'].mean() * 100\nconv_rates.plot(kind='bar', color=['#1A365D', '#EA580C'], ax=axes[1])\naxes[1].set_title('Rasio Konversi (%)'); axes[1].set_ylabel('Conversion Rate (%)')\nplt.tight_layout(); plt.show()",
             "Bobot 100: Eksekusi Welch t-test tepat (30%), eksekusi Chi-Square konversi tepat (35%), visualisasi 2 subplot rapi (35%).")
        ]
    )

print("modules_part3.py ready...")
