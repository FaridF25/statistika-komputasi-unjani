# Modul 06 - 10

def load_part2(add_module):
    # Modul 06: Regresi Linier Sederhana & Berganda
    add_module(
        6, "Regresi Linier Sederhana & Berganda", "Buku 1",
        [
            ("Dalam pemodelan Regresi Linier Ordinary Least Squares (OLS), metode penaksiran parameter beta dilakukan dengan meminimalkan:",
             {"A": "Jumlah absolut galat (Sum of Absolute Errors)", "B": "Jumlah kuadrat residual (Sum of Squared Residuals / SSE)", "C": "Nilai rata-rata target Y", "D": "Nilai koefisien korelasi r", "E": "Derajat kebebasan regresi"}, "B",
             "Prinsip OLS adalah mencari garis regresi yang meminimalkan jumlah kuadrat selisih antara nilai aktual Y dengan nilai prediksi (SSE = sum(e_i²))."),
            ("Koefisien Determinasi (R²) mengukur proporsi variabilitas variabel dependen Y yang dapat dijelaskan oleh:",
             {"A": "Variabel independen X dalam model", "B": "Galat acak residual", "C": "Ukuran sampel n", "D": "Nilai rata-rata populasi", "E": "Intersept beta_0 semata"}, "A",
             "R² = SSR / SST mengukur persentase variasi total variabel terikat Y yang mampu diterangkan secara linier oleh himpunan fitur prediktor X."),
            ("Uji signifikansi simultan untuk menguji apakah seluruh variabel prediktor secara bersama-sama berpengaruh signifikan terhadap variabel target Y adalah:",
             {"A": "Uji-t parsial", "B": "Uji-F ANOVA Regresi", "C": "Uji Chi-Square", "D": "Uji Shapiro-Wilk", "E": "Uji Mann-Whitney"}, "B",
             "Uji-F (F-test for overall significance) menguji hipotesis H0: beta_1 = beta_2 = ... = beta_k = 0 secara simultan."),
            ("Mengapa metrik Adjusted R-Squared (R²_adj) lebih diutamakan daripada R² standar dalam mengevaluasi model Regresi Linier Berganda?",
             {"A": "Karena nilainya selalu lebih besar dari R²", "B": "Karena memberikan penalti terhadap penambahan variabel prediktor baru yang tidak informatif", "C": "Karena tidak memerlukan perhitungan residual", "D": "Karena selalu bernilai antara 0 dan 100", "E": "Karena dapat digunakan pada data kategorikal murni"}, "B",
             "R² standar selalu meningkat jika fitur baru ditambahkan meskipun tidak berguna. Adjusted R² memasukkan faktor penalti derajat kebebasan n - k - 1 sehingga hanya meningkat jika fitur baru benar-benar menambah kekuatan prediksi.")
        ],
        [
            ("Diberikan persamaan regresi linier biaya proyek software: Y = 25 + 1.8 * LOC + 15 * Team. Berapakah estimasi biaya Y (Juta IDR) jika LOC = 50 KLOC dan Team = 4 orang?",
             "Y = 175 Juta IDR", "Y = 25 + (1.8 * 50) + (15 * 4) = 25 + 90 + 60 = 175 Juta IDR."),
            ("Sebutkan rumus matematis untuk menghitung residual ke-i (e_i) dari model regresi!",
             "e_i = Y_i - Y_hat_i (Aktual - Prediksi)", "Residual adalah selisih antara nilai observasi aktual Y_i dengan nilai estimasi model Y_hat_i."),
            ("Jika nilai Total Sum of Squares (SST) = 500 dan Sum of Squared Errors (SSE) = 50, berapakah nilai R² model regresi tersebut?",
             "R² = 0.90 (atau 90%)", "R² = 1 - (SSE / SST) = 1 - (50 / 500) = 1 - 0.10 = 0.90."),
            ("Uji hipotesis statistik apakah yang digunakan untuk menguji signifikansi pengaruh masing-masing koefisien prediktor beta_j secara individual/parsial?",
             "Uji-t Parsial (Partial t-Test)", "Uji-t dengan statistik t = beta_j / SE(beta_j) digunakan untuk menguji apakah koefisien individual signifikan secara parsial (H0: beta_j = 0).")
        ],
        [
            ("Jelaskan secara analitis turunan matematis persamaan matriks OLS beta_hat = (X^T X)^(-1) X^T Y dalam regresi linier berganda dan jelaskan kondisi apa yang menyebabkan matriks (X^T X) tidak dapat diinverskan!",
             "Model matriks: Y = X beta + e. Fungsi objektif SSE(beta) = e^T e = (Y - X beta)^T (Y - X beta) = Y^T Y - 2 beta^T X^T Y + beta^T X^T X beta.\nUntuk meminimalkan SSE, lakukan turunan parsial terhadap vektor beta dan samakan dengan nol: d(SSE)/d(beta) = -2 X^T Y + 2 X^T X beta = 0 => X^T X beta = X^T Y.\nJika matriks (X^T X) non-singular (invertible), maka solusi estimator OLS unik adalah: beta_hat = (X^T X)^(-1) X^T Y.\nKondisi Tidak Dapat Diinverskan: Terjadi jika matriks X tidak berderajat penuh (rank deficient), yaitu ketika terdapat multikolinearitas sempurna antar kolom fitur independen atau jumlah fitur prediktor p melebihi jumlah sampel observasi n (p > n).",
             "Bobot 100: Langkah turunan matriks OLS lengkap (50%), penjelasan kondisi singularitas rank deficient & p > n (50%)."),
            ("Sebuah tim DevOps membangun model regresi linier untuk memprediksi Latensi API (ms) berdasarkan Throughput (req/s) dan Utilisasi RAM (GB). Hasil summary statsmodels menunjukkan: R² = 0.92, F-stat p-value = 1.2e-15, namun p-value uji-t untuk Throughput = 0.42 dan RAM = 0.38. Jelaskan anomali statistik apa yang sedang terjadi, mengapa hal ini terjadi, dan bagaimana solusinya!",
             "Anomali: Paradoks Multikolinearitas Ekstrem (Multicollinearity Paradox). Model keseluruhan sangat signifikan (F-test p < 0.001, R² sangat tinggi 92%), namun tidak ada satupun koefisien individu yang signifikan secara parsial (p-value t-test > 0.05).\nPenyebab: Throughput dan Utilisasi RAM saling berkorelasi sangat tinggi (hampir sempurna, r ~ 0.98). Hal ini menyebabkan standar error koefisien meledak (inflated SE), sehingga t-statistic (beta/SE) anjlok dan gagal menolak H0 pada uji-t individual.\nSolusi: 1) Cek nilai VIF pada kedua prediktor. 2) Buang salah satu prediktor yang redundan (misal drop RAM). 3) Terapkan PCA untuk mereduksi kedua fitur menjadi 1 komponen utama beban kerja. 4) Gunakan Ridge Regression untuk menstabilkan estimasi bobot.",
             "Bobot 100: Identifikasi anomali paradoks multikolinearitas tepat (35%), penjelasan mekanisme inflasi standar error (35%), 3 solusi rekayasa data konkret (30%)."),
            ("Jelaskan 3 plot diagnostik residual yang wajib diperiksa setelah membangun model regresi linier OLS, serta jelaskan pola visual apa yang mengindikasikan adanya pelanggaran asumsi homoskedastisitas dan linearitas!",
             "1. Residual vs Fitted Plot: Menguji linearitas dan homoskedastisitas. Jika terdapat pelanggaran linearitas, residual membentuk pola lengkungan kurva parabolik (U-shape). Jika terjadi heteroskedastisitas (varians tidak konstan), sebaran residual melebar menyerupai bentuk corong/kipas (funnel shape) seiring bertambahnya nilai prediksi.\n2. Normal Q-Q Plot: Menguji normalitas residual. Jika titik-titik menyimpang jauh dari garis lurus 45 derajat (membentuk kurva S), residual tidak normal.\n3. Residual vs Leverage Plot (Cook's Distance): Mengidentifikasi titik observasi yang memiliki pengaruh ekstrem (high leverage outliers) yang dapat merusak stabilitas garis regresi.",
             "Bobot 100: Penjelasan 3 plot diagnostik (40%), pola visual corong heteroskedastisitas (30%), pola lengkung non-linearitas & Cook's distance (30%)."),
            ("Diberikan tabel ANOVA regresi dengan data: Derajat kebebasan Regresi df1 = 3, Residual df2 = 96. Nilai Sum of Squares Regresi SSR = 1800, Sum of Squares Error SSE = 600. Hitunglah: (a) Mean Square Regression (MSR) & Mean Square Error (MSE), (b) Nilai F-hitung model, (c) Koefisien determinasi R²!",
             "(a) MSR = SSR / df1 = 1800 / 3 = 600.\nMSE = SSE / df2 = 600 / 96 = 6.25.\n(b) F-hitung = MSR / MSE = 600 / 6.25 = 96.0.\n(c) SST = SSR + SSE = 1800 + 600 = 2400. R² = SSR / SST = 1800 / 2400 = 0.75 (atau 75%).",
             "Bobot 100: Perhitungan MSR dan MSE tepat (35%), perhitungan F-hitung tepat (35%), perhitungan R² tepat (30%).")
        ]
    )

    # Modul 07: Regresi Logistik Biner & Klasifikasi
    add_module(
        7, "Regresi Logistik Biner & Klasifikasi", "Buku 1",
        [
            ("Fungsi matematika yang digunakan dalam Regresi Logistik untuk memetakan nilai kombinasi linier (-tak hingga s.d. +tak hingga) menjadi nilai probabilitas (0 s.d. 1) adalah:",
             {"A": "Fungsi ReLU", "B": "Fungsi Sigmoid (Logistik)", "C": "Fungsi Tangen Hiperbolik (Tanh)", "D": "Fungsi Linear Step", "E": "Fungsi Polinomial Orde 3"}, "B",
             "Fungsi Sigmoid sigma(z) = 1 / (1 + e^(-z)) memetakan input kontinu bilangan riil menjadi probabilitas pada rentang (0, 1)."),
            ("Jika nilai koefisien regresi logistik untuk variabel 'riwayat_kredit_buruk' adalah beta = 1.3863, maka nilai Odds Ratio (OR = exp(beta)) adalah:",
             {"A": "0.25 kali", "B": "1.38 kali", "C": "4.00 kali", "D": "10.00 kali", "E": "-4.00 kali"}, "C",
             "Odds Ratio dihitung dengan eksponensial koefisien: OR = exp(1.3863) = 4.00, artinya nasabah dengan riwayat kredit buruk memiliki peluang gagal bayar 4 kali lipat lebih tinggi dibanding nasabah baik."),
            ("Fungsi kerugian (loss function) yang dioptimalkan menggunakan Maximum Likelihood Estimation (MLE) pada regresi logistik biner adalah:",
             {"A": "Mean Squared Error (MSE)", "B": "Binary Cross-Entropy (Log-Loss)", "C": "Huber Loss", "D": "Hinge Loss", "E": "Mean Absolute Percentage Error"}, "B",
             "Binary Cross-Entropy (Log-Loss) diturunkan dari fungsi likelihood Bernoulli dan digunakan untuk mengukur penalti kesalahan probabilitas prediksi klasifikasi biner."),
            ("Kurva ROC (Receiver Operating Characteristic) menggambarkan hubungan trade-off antara:",
             {"A": "Precision dan Recall", "B": "True Positive Rate (Sensitivity) dan False Positive Rate (1 - Specificity)", "C": "Accuracy dan F1-Score", "D": "Mean dan Standar Deviasi", "E": "Support dan Confidence"}, "B",
             "Kurva ROC memetakan True Positive Rate (TPR / Sensitivity) pada sumbu-Y terhadap False Positive Rate (FPR / 1 - Specificity) pada sumbu-X pada berbagai variasi nilai ambang batas (threshold).")
        ],
        [
            ("Tuliskan formula fungsi logit (log-odds) dalam regresi logistik biner!",
             "logit(p) = ln(p / (1 - p)) = beta_0 + beta_1*X_1 + ... + beta_k*X_k", "Fungsi logit adalah logaritma natural dari odds rasio peluang sukses p terhadap peluang gagal (1 - p)."),
            ("Jika probabilitas seorang nasabah mengalami default kredit adalah p = 0.80, berapakah nilai Odds nasabah tersebut?",
             "Odds = 4.0 (atau 4 banding 1)", "Odds = p / (1 - p) = 0.80 / (1 - 0.80) = 0.80 / 0.20 = 4.0."),
            ("Berapakah nilai metrik Area Under the ROC Curve (ROC-AUC) untuk model klasifikasi yang setara dengan tebakan acak murni (random guess)?",
             "AUC = 0.50", "Model acak murni menghasilkan garis diagonal dengan luas area di bawah kurva (ROC-AUC) sebesar 0.50, sedangkan model sempurna memiliki AUC = 1.0."),
            ("Sebutkan metrik evaluasi klasifikasi yang mengukur proporsi prediksi positif yang benar-benar bernilai positif (True Positives / (True Positives + False Positives))!",
             "Precision (Presisi)", "Presisi mengukur ketepatan model saat memprediksi kelas positif: TP / (TP + FP).")
        ],
        [
            ("Jelaskan perbedaan mendasar antara model Regresi Linier dan Regresi Logistik dalam hal: (a) Tipe variabel target, (b) Bentuk kurva fungsi pemetaan, (c) Metode optimasi estimasi parameter, dan (d) Interpretasi koefisien!",
             "(a) Variabel Target: Regresi Linier kontinu (-inf s.d. +inf); Regresi Logistik kategorikal biner (0 atau 1) / probabilitas [0, 1].\n(b) Bentuk Kurva: Regresi Linier garis lurus linier tak terbatas; Regresi Logistik kurva non-linier berbentuk 'S' (Sigmoid) yang asimtotik pada 0 dan 1.\n(c) Metode Optimasi: Regresi Linier menggunakan Ordinary Least Squares (OLS) dengan solusi analitik tertutup; Regresi Logistik menggunakan Maximum Likelihood Estimation (MLE) / Gradient Descent numerik iteratif (Log-Loss).\n(d) Interpretasi Koefisien: Regresi Linier: beta_j adalah perubahan rata-rata absolut unit Y untuk setiap kenaikan 1 unit X_j; Regresi Logistik: beta_j adalah perubahan log-odds, dan exp(beta_j) adalah Odds Ratio (kelipatan peluang rasio).",
             "Bobot 100: Penjelasan 4 dimensi komparasi lengkap dan akurat (masing-masing 25%)."),
            ("Diberikan Confusion Matrix dari model deteksi serangan siber IDS (Intrusion Detection System): True Positive (TP) = 90, False Positive (FP) = 10, False Negative (FN) = 30, True Negative (TN) = 870. Hitunglah: (a) Accuracy, (b) Precision, (c) Recall (Sensitivity), (d) F1-Score, dan (e) Jelaskan mengapa pada data tidak seimbang (imbalanced data), Accuracy dapat menjadi metrik yang menyesatkan!",
             "(a) Total N = 90 + 10 + 30 + 870 = 1000. Accuracy = (TP + TN) / Total = (90 + 870) / 1000 = 960 / 1000 = 96.0%.\n(b) Precision = TP / (TP + FP) = 90 / (90 + 10) = 90 / 100 = 90.0%.\n(c) Recall = TP / (TP + FN) = 90 / (90 + 30) = 90 / 120 = 75.0%.\n(d) F1-Score = 2 * (Precision * Recall) / (Precision + Recall) = 2 * (0.90 * 0.75) / (0.90 + 0.75) = 1.35 / 1.65 = 81.82%.\n(e) Jebakan Accuracy: Data sangat timpang (900 normal vs 100 serangan). Jika model bodoh selalu memprediksi 'Normal' untuk semua data, akurasi tetap tinggi 90%, padahal model gagal menangkap 100% serangan siber. F1-Score dan Recall lebih representatif untuk mendeteksi bahaya FN.",
             "Bobot 100: Perhitungan 4 metrik tepat (50%), analisis jebakan akurasi pada imbalanced data (50%)."),
            ("Jelaskan konsep penyesuaian ambang batas probabilitas (Classification Threshold Tuning) dalam sistem credit scoring fintech: Kapan kita harus menurunkan threshold dari 0.50 ke 0.30, dan apa konsekuensinya terhadap Precision dan Recall?",
             "Threshold default adalah 0.50. Jika probabilitas default p >= 0.50, nasabah ditolak. Dalam credit scoring, kerugian finansial akibat meloloskan nasabah macet (False Negative) jauh lebih besar daripada menolak nasabah baik (False Positive).\n- Menurunkan Threshold ke 0.30: Model menjadi lebih agresif dan konservatif. Nasabah dengan risiko 30% saja sudah ditolak.\n- Konsekuensi: Recall meningkat (lebih banyak nasabah macet yang berhasil dicegat/dideteksi), namun Precision menurun (lebih banyak nasabah baik yang salah tolak / FP meningkat).",
             "Bobot 100: Penjelasan trade-off biaya finansial FN vs FP (40%), analisis dampak penurunan threshold (30%), dinamika Precision-Recall (30%)."),
            ("Tuliskan skrip Python (menggunakan Scikit-Learn) untuk melatih model LogisticRegression, melakukan prediksi probabilitas, menghitung metrik classification_report, serta memplot kurva ROC dan skor ROC-AUC!",
             "Skrip Python:\nfrom sklearn.linear_model import LogisticRegression\nfrom sklearn.metrics import classification_report, roc_curve, roc_auc_score\nimport matplotlib.pyplot as plt\n# 1. Training\nmodel = LogisticRegression(max_iter=1000)\nmodel.fit(X_train, y_train)\n# 2. Prediksi & Laporan\ny_pred = model.predict(X_test)\ny_proba = model.predict_proba(X_test)[:, 1]\nprint(classification_report(y_test, y_pred))\n# 3. ROC-AUC\nauc_score = roc_auc_score(y_test, y_proba)\nfpr, tpr, _ = roc_curve(y_test, y_proba)\nplt.figure(figsize=(7,5))\nplt.plot(fpr, tpr, label=f'ROC Curve (AUC = {auc_score:.3f})', color='darkorange', lw=2)\nplt.plot([0,1], [0,1], 'k--')\nplt.xlabel('False Positive Rate'); plt.ylabel('True Positive Rate'); plt.title('Kurva ROC Klasifikasi')\nplt.legend(); plt.show()",
             "Bobot 100: Sintaks LogisticRegression dan predict_proba tepat (30%), classification_report tepat (30%), pembuatan plot ROC-AUC lengkap (40%).")
        ]
    )

    # Modul 08: Reduksi Dimensi (PCA & Faktor)
    add_module(
        8, "Reduksi Dimensi (PCA & Faktor)", "Buku 1",
        [
            ("Tujuan utama dari teknik Principal Component Analysis (PCA) dalam rekayasa data adalah:",
             {"A": "Mengelompokkan data ke dalam k cluster", "B": "Mereduksi dimensi fitur dengan mempertahankan varians informasi maksimum tanpa saling berkorelasi", "C": "Memprediksi target kategorikal secara biner", "D": "Menghilangkan seluruh data pencilan", "E": "Mengubah data diskrit menjadi kontinu"}, "B",
             "PCA mentransformasikan himpunan variabel yang berkorelasi menjadi himpunan variabel baru yang saling ortogonal (tidak berkorelasi) yang disebut Principal Components dengan memaksimalkan varians data."),
            ("Dalam dekomposisi nilai eigen (Eigenvalue Decomposition) pada PCA, nilai eigen (eigenvalue / lambda_i) merepresentasikan:",
             {"A": "Jumlah baris observasi data", "B": "Besarnya varians data yang dijelaskan oleh komponen utama ke-i", "C": "Arah vektor komponen utama di ruang berdimensi tinggi", "D": "Tingkat signifikansi p-value korelasi", "E": "Jumlah fitur kategorikal yang dibuang"}, "B",
             "Nilai eigen mengukur magnitudo varians yang diserap oleh sumbu komponen utama terkait, sedangkan vektor eigen (eigenvector) menentukan arah rotasi geometris sumbu tersebut."),
            ("Menurut Kriteria Kaiser (Kaiser Rule), komponen utama (PC) yang layak dipertahankan untuk analisis lanjutan adalah komponen yang memiliki:",
             {"A": "Eigenvalue < 0.5", "B": "Eigenvalue >= 1.0", "C": "Cumulative Variance = 50%", "D": "Vektor eigen bernilai negatif", "E": "Nilai korelasi = 0"}, "B",
             "Kriteria Kaiser menyatakan bahwa pada data terstandarisasi (StandardScaler), satu komponen utama baru hanya bermakna jika mampu menjelaskan varians setidaknya setara dengan satu variabel asli (Eigenvalue >= 1.0)."),
            ("Tahap pra-pemrosesan data yang WAJIB dilakukan sebelum menerapkan algoritma PCA adalah:",
             {"A": "One-Hot Encoding tanpa drop_first", "B": "Standardisasi fitur (Z-score scaling / mean=0, std=1)", "C": "Menghapus seluruh nilai median", "D": "Membuat tabel kontingensi", "E": "Uji Chi-Square independensi"}, "B",
             "PCA sangat sensitif terhadap skala satuan data. Jika data tidak distandarisasi, variabel dengan rentang nilai besar (misal gaji jutaan rupiah) akan mendominasi komponen utama secara keliru dibanding variabel berskala kecil.")
        ],
        [
            ("Jika 3 komponen utama pertama memiliki rasio varians terjelaskan: PC1 = 45%, PC2 = 25%, PC3 = 15%, berapakah nilai varians kumulatif dari ketiga komponen tersebut?",
             "Varians Kumulatif = 85.0%", "Varians Kumulatif = 45% + 25% + 15% = 85.0%."),
            ("Sebutkan nama diagram visual grafik garis yang digunakan untuk menentukan 'titik siku' (elbow point) pemotongan jumlah komponen utama PCA berdasarkan nilai eigen!",
             "Scree Plot", "Scree Plot memetakan nomor komponen utama pada sumbu-X terhadap nilai eigen pada sumbu-Y untuk mengidentifikasi titik siku retensi komponen."),
            ("Apakah sifat matematis dari hubungan korelasi antara komponen utama PC-1 dan PC-2 hasil transformasi PCA?",
             "Ortogonal / Tidak berkorelasi sama sekali (r = 0)", "Seluruh komponen utama hasil PCA saling ortogonal secara geometris dan memiliki korelasi linier nol (uncorrelated)."),
            ("Sebutkan nama visualisasi gabungan 2D yang memetakan skor observasi sampel sekaligus vektor loading fitur asli dalam ruang PCA!",
             "PCA Biplot", "Biplot menampilkan sebaran titik data sampel bersamaan dengan panah vektor loading fitur untuk menginterpretasikan kontribusi variabel asli terhadap PC1 dan PC2.")
        ],
        [
            ("Jelaskan langkah-langkah algoritma PCA secara sistematis mulai dari matriks data mentah X berukuran n x p hingga diperoleh matriks proyeksi tereduksi Z berukuran n x k (k < p)!",
             "1. Standardisasi Data: Hitung Z-score untuk setiap fitur agar mean = 0 dan varians = 1: X_std = (X - mu) / sigma.\n2. Matriks Kovarians: Hitung matriks kovarians/korelasi C = (1 / (n - 1)) * X_std^T X_std berukuran p x p.\n3. Dekomposisi Spektral: Hitung nilai eigen (lambda_1, lambda_2, ..., lambda_p) dan vektor eigen ortonormal (v_1, v_2, ..., v_p) dari matriks C sehingga C v_i = lambda_i v_i.\n4. Pengurutan & Seleksi: Urutkan pasangan nilai eigen dari terbesar ke terkecil. Pilih k vektor eigen teratas berdasarkan Kriteria Kaiser (lambda >= 1.0) atau ambang varians kumulatif (misal >= 80%), membentuk matriks bobot W berukuran p x k.\n5. Proyeksi Dimensi: Transformasikan data asli ke ruang baru: Z = X_std * W berukuran n x k.",
             "Bobot 100: Langkah standardisasi dan matriks kovarians (30%), dekomposisi nilai/vektor eigen (40%), seleksi k dan proyeksi matriks Z (30%)."),
            ("Sebuah sistem e-commerce mengumpulkan 10 fitur perilaku pengguna aplikasi. Analisis PCA menghasilkan 10 nilai eigen: [3.8, 2.2, 1.4, 0.9, 0.6, 0.4, 0.3, 0.2, 0.1, 0.1]. (a) Berdasarkan Kriteria Kaiser, berapa jumlah komponen utama yang harus dipertahankan? (b) Berapakah persentase total varians yang dapat dijelaskan oleh komponen-komponen yang terpilih tersebut?",
             "(a) Berdasarkan Kriteria Kaiser (Eigenvalue >= 1.0), komponen yang memenuhi syarat adalah PC1 (3.8), PC2 (2.2), dan PC3 (1.4). Maka jumlah komponen yang dipertahankan adalah 3 komponen utama (k = 3).\n(b) Total sum of eigenvalues = 3.8 + 2.2 + 1.4 + 0.9 + 0.6 + 0.4 + 0.3 + 0.2 + 0.1 + 0.1 = 10.0.\nVarians yang dijelaskan oleh 3 komponen terpilih = 3.8 + 2.2 + 1.4 = 7.4.\nPersentase Varians Terjelaskan = (7.4 / 10.0) * 100% = 74.0%.",
             "Bobot 100: Penentuan k berdasarkan Kriteria Kaiser tepat (50%), perhitungan persentase varians kumulatif tepat (50%)."),
            ("Jelaskan perbedaan mendasar antara Principal Component Analysis (PCA) dan Exploratory Factor Analysis (EFA) dalam metodologi analisis multivariat!",
             "1. Tujuan & Filosofi: PCA adalah teknik reduksi dimensi murni yang bertujuan merangkum varians total (varians unik + varians bersama) menjadi kombinasi linier ortogonal. EFA bertujuan mengidentifikasi variabel laten (faktor tersembunyi yang tidak teramati secara langsung) yang mendasari korelasi antar variabel teramati (hanya memodelkan common variance).\n2. Arah Hubungan: Pada PCA, komponen dibentuk dari variabel teramati (variabel -> PC). Pada EFA, faktor laten diasumsikan menyebabkan timbulnya respon pada variabel teramati (Faktor Laten -> Variabel Teramati + Error Term).\n3. Rotasi: PCA tidak memerlukan rotasi faktor untuk retensi varians maksimal; EFA sering menggunakan rotasi (seperti Varimax atau Promax) untuk memudahkan interpretasi makna faktor laten.",
             "Bobot 100: Perbandingan tujuan PCA vs EFA (40%), arah hubungan kausal laten vs komposit linier (30%), aspek pemodelan varians & rotasi (30%)."),
            ("Tuliskan kode Python lengkap menggunakan PCA dari Scikit-Learn untuk: (1) Menstandarisasi fitur numerik, (2) Mengekstrak 2 komponen utama, (3) Menampilkan explained_variance_ratio_, dan (4) Membuat scatter plot 2D proyeksi data dengan warna label cluster!",
             "Kode Python:\nimport pandas as pd, matplotlib.pyplot as plt, seaborn as sns\nfrom sklearn.preprocessing import StandardScaler\nfrom sklearn.decomposition import PCA\n# 1. Standardisasi\nscaler = StandardScaler()\nX_scaled = scaler.fit_transform(df_features)\n# 2. PCA 2D\npca = PCA(n_components=2)\nX_pca = pca.fit_transform(X_scaled)\nprint(f'Explained Variance Ratio: {pca.explained_variance_ratio_ * 100}')\n# 3. DataFrame Proyeksi\ndf_pca = pd.DataFrame(X_pca, columns=['PC1', 'PC2'])\ndf_pca['label'] = df['label']\n# 4. Scatter Plot\nplt.figure(figsize=(8,6))\nsns.scatterplot(data=df_pca, x='PC1', y='PC2', hue='label', palette='Set1', s=70)\nplt.title(f'Proyeksi 2D PCA (Total Varians: {sum(pca.explained_variance_ratio_)*100:.1f}%)')\nplt.xlabel(f'PC1 ({pca.explained_variance_ratio_[0]*100:.1f}%)')\nplt.ylabel(f'PC2 ({pca.explained_variance_ratio_[1]*100:.1f}%)')\nplt.show()",
             "Bobot 100: Sintaks StandardScaler & PCA tepat (35%), ekstraksi variance ratio tepat (30%), visualisasi scatterplot 2D rapi (35%).")
        ]
    )

    # Modul 09: Analisis Klaster K-Means & Hierarkis
    add_module(
        9, "Analisis Klaster K-Means & Hierarkis", "Buku 1",
        [
            ("Algoritma K-Means Clustering bekerja dengan cara meminimalkan fungsi objektif WCSS, yaitu:",
             {"A": "Within-Cluster Sum of Squares (Jumlah kuadrat jarak data ke pusat centroid)", "B": "Between-Cluster Sum of Squares", "C": "Jumlah nilai korelasi Pearson", "D": "Nilai Silhouette Coefficient maksimum", "E": "Jarak Manhattan antar observasi terjauh"}, "A",
             "K-Means meminimalkan Within-Cluster Sum of Squares (WCSS / Inersia) yang merupakan total kuadrat jarak Euclidean antara setiap titik data dengan titik pusat cluster (centroid) terdekatnya."),
            ("Metode grafis yang digunakan untuk menentukan jumlah klaster k optimal pada K-Means dengan mencari titik perlambatan penurunan inersia adalah:",
             {"A": "Scree Plot", "B": "Metode Siku (Elbow Method)", "C": "Dendrogram", "D": "Boxplot", "E": "Kurva ROC"}, "B",
             "Metode Elbow memetakan jumlah k klaster terhadap WCSS/Inersia untuk menemukan titik siku di mana penambahan k tidak lagi menurunkan WCSS secara signifikan."),
            ("Rentang nilai Silhouette Coefficient (s) berkisar antara:",
             {"A": "0 hingga 100", "B": "-1.0 hingga +1.0", "C": "0 hingga +1.0", "D": "-tak hingga hingga +tak hingga", "E": "1 hingga k"}, "B",
             "Silhouette Coefficient bernilai dari -1.0 (salah penempatan cluster) hingga +1.0 (cluster sangat terpisah padat dan terdefinisi dengan sangat baik). Nilai mendekati 0 berarti cluster saling tumpang tindih."),
            ("Diagram pohon visual yang digunakan untuk menggambarkan proses penggabungan bertahap pada Klasterisasi Hierarki Aglomeratif disebut:",
             {"A": "Histogram", "B": "Dendrogram", "C": "Violin Plot", "D": "Scatter Matrix", "E": "Contingency Tree"}, "B",
             "Dendrogram adalah diagram pohon bercabang yang memvisualisasikan hierarki penggabungan cluster dari tingkat observasi individual hingga membentuk satu cluster tunggal.")
        ],
        [
            ("Formula jarak metrik apakah yang paling umum digunakan pada algoritma K-Means standar untuk mengukur jarak antara titik x dan centroid c?",
             "Jarak Euclidean (Euclidean Distance)", "Jarak Euclidean d(x, c) = sqrt(sum((x_i - c_i)^2)) adalah metrik jarak default pada K-Means."),
            ("Jika nilai Silhouette Score suatu hasil klasterisasi adalah s = 0.75, bagaimanakah interpretasi kualitas struktur klaster tersebut?",
             "Struktur klaster kuat / sangat baik (Strong cluster structure)", "Skor s >= 0.70 mengindikasikan bahwa data terkelompok secara sangat solid dan terpisah jelas dari cluster tetangga."),
            ("Apakah kelemahan utama algoritma K-Means terhadap inisialisasi titik centroid awal acak, dan teknik apa yang digunakan untuk mengatasinya?",
             "K-Means sensitif terhadap inisialisasi centroid awal (dapat terjebak di local optima). Diatasi dengan algoritma 'k-means++'",
             "Inisialisasi acak dapat menyebabkan hasil suboptimal. Solusinya menggunakan inisialisasi cerdas 'k-means++' yang menyebarkan titik centroid awal sejauh mungkin satu sama lain."),
            ("Sebutkan metode linkage pada Hierarchical Clustering yang menghitung jarak antar klaster berdasarkan jarak rata-rata seluruh pasangan titik data!",
             "Average Linkage", "Average Linkage mengukur jarak rata-rata antara semua anggota cluster A dengan semua anggota cluster B.")
        ],
        [
            ("Jelaskan secara mendalam siklus iterasi algoritma K-Means Clustering mulai dari inisialisasi hingga konvergensi, dan sebutkan 3 kondisi penghentian iterasi (stopping criteria)!",
             "Siklus Iterasi K-Means:\n1. Inisialisasi: Tentukan jumlah k cluster dan pilih k titik centroid awal (menggunakan metode k-means++).\n2. Tahap Assignment: Hitung jarak Euclidean setiap titik data x_i ke seluruh k centroid. Tetapkan titik x_i ke cluster dengan centroid terdekat: c_i = argmin ||x_i - mu_j||^2.\n3. Tahap Update: Hitung ulang posisi koordinat setiap centroid mu_j sebagai nilai rata-rata (mean) aritmetika dari seluruh titik data yang menjadi anggotanya: mu_j = (1 / |S_j|) * sum_{x in S_j} x.\n4. Evaluasi & Pengulangan: Ulangi langkah 2 dan 3 secara iteratif.\nKondisi Penghentian (Stopping Criteria):\n1) Posisi koordinat centroid tidak lagi mengalami pergeseran (perubahan < toleransi epsilon).\n2) Tidak ada lagi titik data yang berpindah keanggotaan cluster antar iterasi.\n3) Jumlah iterasi maksimum yang ditentukan (max_iter, misal 300) telah tercapai.",
             "Bobot 100: Penjelasan 4 tahap siklus K-Means lengkap (50%), 3 kondisi penghentian iterasi akurat (50%)."),
            ("Jelaskan secara matematis cara menghitung Silhouette Coefficient untuk sebuah titik data i: s(i) = (b(i) - a(i)) / max(a(i), b(i)), dan jelaskan interpretasi jika s(i) mendekati +1, 0, dan -1!",
             "Komponen Perhitungan:\n1. a(i) [Intra-cluster distance]: Rata-rata jarak titik i ke seluruh titik lain yang berada di dalam klaster yang sama dengan i (mengukur kepadatan/kohesi internal klaster).\n2. b(i) [Nearest-cluster distance]: Rata-rata jarak titik i ke seluruh titik pada klaster tetangga terdekat yang bukan klaster i (mengukur derajat pemisahan/separasi).\n3. Formula: s(i) = (b(i) - a(i)) / max(a(i), b(i)).\nInterpretasi Nilai:\n- s(i) mendekati +1: a(i) << b(i). Titik i sangat dekat dengan anggotanya dan sangat jauh dari klaster lain (penempatan klaster ideal/sempurna).\n- s(i) mendekati 0: a(i) ~ b(i). Titik i berada di perbatasan tumpang tindih antara dua klaster.\n- s(i) mendekati -1: a(i) >> b(i). Titik i lebih dekat ke klaster tetangga dibanding klasternya sendiri (salah penempatan klaster / misclassified).",
             "Bobot 100: Definisi matematis a(i) dan b(i) tepat (40%), formula s(i) tepat (20%), interpretasi nilai +1, 0, -1 detail (40%)."),
            ("Bandingkan kelebihan dan kekurangan algoritma K-Means Clustering vs Agglomerative Hierarchical Clustering untuk segmentasi 500.000 pengguna aplikasi e-commerce!",
             "K-Means Clustering: Kelebihan: Kompleksitas komputasi linier O(n * k * I), sangat cepat dan mampu memproses dataset raksasa (500.000 user). Kekurangan: Wajib menentukan k di awal, mengasumsikan bentuk klaster bulat (spherical) dengan ukuran seragam, sensitif terhadap outlier dan inisialisasi awal. Hierarchical Clustering: Kelebihan: Tidak memerlukan input k di awal, menghasilkan dendrogram hierarkis yang sangat informatif untuk analisis taksonomi bisnis, mampu menangani bentuk klaster arbitrary. Kekurangan: Kompleksitas komputasi waktu O(n²) atau O(n³) dan memori O(n²), sehingga TIDAK LAYAK dan akan mengalami Out-Of-Memory (OOM) pada 500.000 baris data.\nKesimpulan Rekayasa: Gunakan K-Means (atau Mini-Batch K-Means) untuk segmentasi 500.000 pengguna.",
             "Bobot 100: Analisis kelebihan & kekurangan K-Means (35%), analisis Hierarchical Clustering (35%), justifikasi skalabilitas komputasi Big Data (30%)."),
            ("Tuliskan skrip Python lengkap untuk melakukan klasterisasi K-Means: (1) Standardisasi data, (2) Loop pencarian k optimal dari k=2 hingga k=8 menggunakan Silhouette Score, (3) Melatih model K-Means pada k terbaik, dan (4) Menampilkan nilai centroid profil tiap klaster!",
             "Skrip Python:\nimport pandas as pd, numpy as np\nfrom sklearn.preprocessing import StandardScaler\nfrom sklearn.cluster import KMeans\nfrom sklearn.metrics import silhouette_score\n# 1. Standardisasi\nscaler = StandardScaler()\nX_scaled = scaler.fit_transform(df_features)\n# 2. Pencarian k Optimal\nbest_k, best_score = 2, -1\nfor k in range(2, 9):\n    km = KMeans(n_clusters=k, init='k-means++', random_state=42, n_init=10)\n    labels = km.fit_predict(X_scaled)\n    score = silhouette_score(X_scaled, labels)\n    print(f'k = {k}, Silhouette Score = {score:.4f}')\n    if score > best_score:\n        best_k, best_score = k, score\nprint(f'\\n>> k Optimal Terpilih: k = {best_k} (Score: {best_score:.4f})')\n# 3. Model Final & Centroid\nfinal_km = KMeans(n_clusters=best_k, init='k-means++', random_state=42, n_init=10)\ndf_features['cluster'] = final_km.fit_predict(X_scaled)\n# 4. Profil Centroid Skala Asli\ncentroid_profil = df_features.groupby('cluster').mean()\nprint('\\n=== Profil Rata-rata Centroid Tiap Cluster ===')\ndisplay(centroid_profil.round(2))",
             "Bobot 100: Pipeline StandardScaler tepat (25%), iterasi pencarian k via silhouette_score tepat (35%), pelatihan model final dan agregasi centroid profil tepat (40%).")
        ]
    )

    # Modul 10: Market Basket Analysis & Association Rules
    add_module(
        10, "Market Basket Analysis & Association Rules", "Buku 1",
        [
            ("Dalam algoritma asosiasi Apriori, metrik 'Support' dari aturan asosiasi {A} -> {B} mengukur:",
             {"A": "Peluang bersyarat transaksi membeli B jika membeli A", "B": "Proporsi transaksi dalam basis data yang memuat item A dan B secara bersamaan", "C": "Rasio peningkatan peluang pembelian B akibat promosi A", "D": "Jumlah item unik dalam keranjang", "E": "Waktu eksekusi algoritma keranjang belanja"}, "B",
             "Support(A -> B) = P(A intersek B) = Frekuensi(A dan B) / Total Transaksi N. Mengukur seberapa sering kombinasi itemset A dan B muncul bersama di database."),
            ("Metrik 'Confidence' pada aturan asosiasi {A} -> {B} dihitung dengan rumus:",
             {"A": "Support(A intersek B) / Support(A)", "B": "Support(A intersek B) / Support(B)", "C": "Support(A) * Support(B)", "D": "Support(A) + Support(B)", "E": "Support(A intersek B) / Total Transaksi"}, "A",
             "Confidence(A -> B) = P(B | A) = Support(A intersek B) / Support(A). Mengukur probabilitas bersyarat transaksi memuat item B jika diketahui transaksi memuat item A."),
            ("Nilai metrik Lift Ratio > 1.0 pada aturan asosiasi {Mouse} -> {Keyboard} mengindikasikan bahwa:",
             {"A": "Pembelian Mouse dan Keyboard saling independen", "B": "Pembelian Mouse berkorelasi positif dan meningkatkan kecenderungan pembelian Keyboard", "C": "Pembelian Mouse menurunkan peluang pembelian Keyboard", "D": "Aturan asosiasi tidak valid", "E": "Kedua item tidak pernah dibeli bersama"}, "B",
             "Lift(A -> B) = Confidence(A -> B) / Support(B). Nilai Lift > 1.0 membuktikan adanya hubungan asosiasi positif di atas ekspektasi kebetulan acak (cross-selling yang efektif)."),
            ("Prinsip Monotonik (Apriori Property / Downward Closure Property) menyatakan bahwa:",
             {"A": "Semua itemset memiliki nilai support yang sama", "B": "Jika sebuah itemset bersifat frequent, maka seluruh subset dari itemset tersebut pasti frequent", "C": "Itemset berukuran besar selalu memiliki confidence lebih tinggi", "D": "Confidence selalu lebih besar daripada Support", "E": "Lift ratio berbanding lurus dengan jumlah transaksi"}, "B",
             "Prinsip Apriori: 'Jika itemset I sering muncul (frequent), maka semua subset dari I pasti frequent'. Konsekuensinya: Jika suatu itemset infrequent, seluruh superset-nya dapat langsung dipangkas (pruned) untuk menghemat komputasi.")
        ],
        [
            ("Dari 1.000 transaksi toko online, terdapat 200 transaksi yang memuat 'Kopi' dan 150 transaksi memuat 'Kopi' dan 'Gula' bersamaan. Berapakah nilai Confidence aturan {Kopi} -> {Gula}?",
             "Confidence = 0.75 (atau 75%)", "Confidence = Support(Kopi & Gula) / Support(Kopi) = 150 / 200 = 0.75 (75%)."),
            ("Jika Support(A & B) = 0.10, Support(A) = 0.20, dan Support(B) = 0.25, berapakah nilai Lift Ratio aturan {A} -> {B}?",
             "Lift Ratio = 2.0", "Confidence = 0.10 / 0.20 = 0.50. Lift = Confidence / Support(B) = 0.50 / 0.25 = 2.0."),
            ("Sebutkan pustaka populer Python yang menyediakan fungsi apriori dan association_rules untuk Market Basket Analysis!",
             "MLxtend (mlxtend.frequent_patterns)", "Pustaka MLxtend menyediakan modul apriori, fpgrowth, dan association_rules."),
            ("Format representasi matriks biner (0 atau 1 / True atau False) di mana baris adalah ID transaksi dan kolom adalah daftar seluruh produk disebut format apa?",
             "One-Hot Encoded Transaction Matrix / Basket Matrix", "Data transaksi daftar belanja harus diubah menjadi matriks biner boolean sebelum diproses oleh algoritma Apriori.")
        ],
        [
            ("Diberikan basis data transaksi minimarket berisi 10 transaksi:\n- T1: {Roti, Selai, Susu}\n- T2: {Roti, Mentega}\n- T3: {Susu, Keju}\n- T4: {Roti, Selai, Mentega}\n- T5: {Roti, Susu}\n- T6: {Roti, Selai}\n- T7: {Susu, Mentega}\n- T8: {Roti, Selai, Keju}\n- T9: {Roti, Mentega, Keju}\n- T10: {Roti, Selai, Susu, Mentega}\nHitunglah: (a) Support({Roti}), Support({Selai}), dan Support({Roti, Selai}), (b) Confidence aturan {Roti} -> {Selai}, (c) Lift Ratio aturan {Roti} -> {Selai}, dan (d) Berikan rekomendasi penataan produk rak toko berdasarkan nilai Lift tersebut!",
             "(a) Total N = 10 transaksi.\n- Frekuensi Roti = 8 (T1, T2, T4, T5, T6, T8, T9, T10) -> Support(Roti) = 8/10 = 0.80 (80%).\n- Frekuensi Selai = 5 (T1, T4, T6, T8, T10) -> Support(Selai) = 5/10 = 0.50 (50%).\n- Frekuensi {Roti, Selai} = 5 (T1, T4, T6, T8, T10) -> Support(Roti, Selai) = 5/10 = 0.50 (50%).\n(b) Confidence({Roti} -> {Selai}) = Support(Roti, Selai) / Support(Roti) = 0.50 / 0.80 = 0.625 (62.5%).\n(c) Lift({Roti} -> {Selai}) = Confidence / Support(Selai) = 0.625 / 0.50 = 1.25.\n(d) Rekomendasi: Karena Lift Ratio = 1.25 > 1.0, terdapat asosiasi positif nyata. Disarankan meletakkan Selai berdampingan dengan Roti atau membuat paket bundling promosi 'Beli Roti Diskon Selai' untuk mendorong cross-selling.",
             "Bobot 100: Perhitungan Support 3 itemset tepat (30%), perhitungan Confidence tepat (25%), perhitungan Lift tepat (25%), rekomendasi bisnis tepat (20%)."),
            ("Jelaskan bagaimana 'Prinsip Monotonik Apriori' (Apriori Downward Closure Property) secara dramatis mampu memangkas ruang pencarian kombinasi itemset (Search Space Pruning) pada transaksi Big Data dengan ribuan produk!",
             "Jika sebuah toko memiliki m produk unik, ruang pencarian kombinasi itemset berukuran 2^m - 1 (eksponensial). Untuk m = 1.000 produk, pencarian brute-force mustahil dilakukan.\nPrinsip Apriori: 'Jika sebuah itemset I tidak sering muncul (infrequent, Support < min_support), maka seluruh superset dari I dipastikan tidak frequent'.\nMekanisme Pruning: Algoritma bekerja secara level-wise (k-itemsets). Jika itemset 2-elemen {A, B} memiliki Support < min_support, maka algoritma langsung memangkas (prune) dan tidak akan pernah menguji semua kombinasi superset 3-elemen {A, B, C}, {A, B, D}, dst. Ini mereduksi miliaran kalkulasi menjadi ribuan iterasi efisien.",
             "Bobot 100: Penjelasan kompleksitas eksponensial 2^m (30%), formulasi aturan downward closure (40%), mekanisme pruning level-wise (30%)."),
            ("Jelaskan perbedaan interpretasi antara metrik Confidence dan metrik Lift Ratio: Mengapa aturan asosiasi dengan Confidence tinggi (misal 80%) belum tentu merupakan aturan asosiasi yang baik jika Lift Ratio-nya <= 1.0? Berikan contoh kasus!",
             "Confidence P(B | A) hanya mengukur seberapa sering B dibeli saat A dibeli, namun mengabaikan seberapa populer B secara umum di seluruh populasi. Lift membandingkan Confidence terhadap peluang dasar Support(B).\nContoh Kasus: Misalkan produk 'Beras' sangat populer dan dibeli oleh 90% seluruh pengunjung toko (Support(Beras) = 0.90). Aturan {Cokelat} -> {Beras} menghasilkan Confidence = 80%. Angka 80% tampak sangat tinggi.\nNamun Lift = Confidence / Support(Beras) = 0.80 / 0.90 = 0.888 (< 1.0).\nInterpretasi: Pembelian Cokelat sebenarnya justru MENURUNKAN peluang pembelian Beras dari 90% menjadi 80% (asosiasi negatif/substitusi). Mengandalkan Confidence semata akan menghasilkan keputusan bisnis bundling yang keliru.",
             "Bobot 100: Analisis kelemahan Confidence murni (40%), contoh kasus numerik komparasi Lift < 1.0 (40%), kesimpulan rekayasa rekomendasi (20%)."),
            ("Tuliskan kode Python lengkap menggunakan pustaka mlxtend untuk: (1) Mengubah list transaksi belanja menjadi matriks One-Hot TransactionEncoder, (2) Mengekstrak frequent itemsets dengan min_support = 0.05 menggunakan apriori, dan (3) Menghasilkan association rules yang memiliki metric='lift' dengan min_threshold = 1.2 diurutkan berdasarkan confidence tertinggi!",
             "Kode Python:\nimport pandas as pd\nfrom mlxtend.preprocessing import TransactionEncoder\nfrom mlxtend.frequent_patterns import apriori, association_rules\n# 1. One-Hot Matrix\nte = TransactionEncoder()\nte_ary = te.fit(dataset_transaksi).transform(dataset_transaksi)\ndf_basket = pd.DataFrame(te_ary, columns=te.columns_)\n# 2. Frequent Itemsets Apriori\nfrequent_itemsets = apriori(df_basket, min_support=0.05, use_colnames=True)\nprint(f'Ditemukan {len(frequent_itemsets)} frequent itemsets.')\n# 3. Association Rules Filtered by Lift >= 1.2\nrules = association_rules(frequent_itemsets, metric='lift', min_threshold=1.2)\nrules_sorted = rules.sort_values(by='confidence', ascending=False)\ndisplay(rules_sorted[['antecedents', 'consequents', 'support', 'confidence', 'lift']].head(10))",
             "Bobot 100: Penggunaan TransactionEncoder tepat (35%), sintaks apriori dengan min_support tepat (30%), association_rules dengan sorting confidence tepat (35%).")
        ]
    )

print("modules_part2.py ready...")
