import json
import os
import openpyxl
from openpyxl.styles import Font, PatternFill, Alignment, Border, Side
from openpyxl.utils import get_column_letter

# List of modules
modules_meta = [
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

# We will populate all 25 modules dictionary
raw_modules_data = {}

