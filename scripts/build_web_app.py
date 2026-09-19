import json

with open("/Users/ridwanilyas/Documents/Unjani/Statistika/bank_soal_300.json", "r", encoding="utf-8") as f:
    data = json.load(f)

json_str = json.dumps(data, ensure_ascii=False)

html_content = f"""<!DOCTYPE html>
<html lang="id">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Bank Latihan 300 Soal - Statistika Komputasi</title>
    <!-- Tailwind CSS CDN -->
    <script src="https://cdn.tailwindcss.com"></script>
    <!-- SheetJS (xlsx.full.min.js) for Excel Export -->
    <script src="https://cdnjs.cloudflare.com/ajax/libs/xlsx/0.18.5/xlsx.full.min.js"></script>
    <!-- Lucide Icons -->
    <script src="https://unpkg.com/lucide@latest"></script>
    <style>
        @import url('https://fonts.googleapis.com/css2?family=Plus+Jakarta+Sans:wght@300;400;500;600;700;800&display=swap');
        body {{
            font-family: 'Plus Jakarta Sans', sans-serif;
            background-color: #F8FAFC;
        }}
        .tab-active {{
            background-color: #1A365D;
            color: #FFFFFF;
            border-color: #1A365D;
        }}
        .option-selected-correct {{
            background-color: #DCFCE7 !important;
            border-color: #22C55E !important;
            color: #15803D !important;
        }}
        .option-selected-wrong {{
            background-color: #FEE2E2 !important;
            border-color: #EF4444 !important;
            color: #B91C1C !important;
        }}
    </style>
</head>
<body class="text-slate-800 antialiased min-h-screen flex flex-col">

    <!-- Header Section -->
    <header class="bg-gradient-to-r from-slate-900 via-blue-950 to-slate-900 text-white shadow-xl border-b border-blue-800/40 sticky top-0 z-50">
        <div class="max-w-7xl mx-auto px-4 sm:px-6 lg:px-8 py-4">
            <div class="flex flex-col md:flex-row md:items-center md:justify-between gap-4">
                <div>
                    <div class="flex items-center gap-2">
                        <span class="px-2.5 py-0.5 rounded-full text-xs font-semibold bg-emerald-500/20 text-emerald-300 border border-emerald-500/30">OBE Kurikulum</span>
                        <span class="px-2.5 py-0.5 rounded-full text-xs font-semibold bg-blue-500/20 text-blue-300 border border-blue-500/30">300 Soal Terintegrasi</span>
                    </div>
                    <h1 class="text-2xl sm:text-3xl font-extrabold tracking-tight mt-1 text-white flex items-center gap-2">
                        <span>📊 Bank Latihan Soal Statistika Komputasi</span>
                    </h1>
                    <p class="text-slate-300 text-xs sm:text-sm mt-0.5">
                        Teknik Informatika • Universitas Jenderal Achmad Yani • Dr. Ridwan Ilyas, S.Kom., M.T.
                    </p>
                </div>
                <!-- Export Excel Button -->
                <div class="flex items-center gap-3">
                    <button onclick="exportToExcel()" class="inline-flex items-center gap-2 px-5 py-2.5 rounded-xl font-bold text-sm bg-emerald-600 hover:bg-emerald-500 active:scale-95 transition-all text-white shadow-lg shadow-emerald-900/30 border border-emerald-400/40">
                        <i data-lucide="file-spreadsheet" class="w-5 h-5"></i>
                        <span>Export ke Excel (.xlsx)</span>
                    </button>
                    <a href="latihan_soal_300_statistika_komputasi.xlsx" download class="hidden sm:inline-flex items-center gap-2 px-4 py-2.5 rounded-xl font-semibold text-sm bg-slate-800 hover:bg-slate-700 text-slate-200 border border-slate-600 transition-all">
                        <i data-lucide="download" class="w-4 h-4"></i>
                        <span>File Langsung</span>
                    </a>
                </div>
            </div>
        </div>
    </header>

    <!-- Main Content Container -->
    <main class="max-w-7xl mx-auto px-4 sm:px-6 lg:px-8 py-8 flex-1 w-full">
        
        <!-- Summary Stats Banner -->
        <div class="grid grid-cols-2 sm:grid-cols-4 gap-4 mb-6">
            <div class="bg-white p-4 rounded-2xl border border-slate-200 shadow-sm flex items-center gap-3">
                <div class="w-10 h-10 rounded-xl bg-blue-100 text-blue-800 flex items-center justify-center font-bold">
                    <i data-lucide="layers" class="w-5 h-5"></i>
                </div>
                <div>
                    <div class="text-xs text-slate-500 font-medium">Total Bank Soal</div>
                    <div class="text-xl font-extrabold text-slate-900">300 Soal</div>
                </div>
            </div>
            <div class="bg-white p-4 rounded-2xl border border-slate-200 shadow-sm flex items-center gap-3">
                <div class="w-10 h-10 rounded-xl bg-indigo-100 text-indigo-800 flex items-center justify-center font-bold">
                    <i data-lucide="check-circle-2" class="w-5 h-5"></i>
                </div>
                <div>
                    <div class="text-xs text-slate-500 font-medium">Pilihan Ganda</div>
                    <div class="text-xl font-extrabold text-indigo-900">100 Butir</div>
                </div>
            </div>
            <div class="bg-white p-4 rounded-2xl border border-slate-200 shadow-sm flex items-center gap-3">
                <div class="w-10 h-10 rounded-xl bg-teal-100 text-teal-800 flex items-center justify-center font-bold">
                    <i data-lucide="edit-3" class="w-5 h-5"></i>
                </div>
                <div>
                    <div class="text-xs text-slate-500 font-medium">Isian & Kasus</div>
                    <div class="text-xl font-extrabold text-teal-900">100 Soal</div>
                </div>
            </div>
            <div class="bg-white p-4 rounded-2xl border border-slate-200 shadow-sm flex items-center gap-3">
                <div class="w-10 h-10 rounded-xl bg-amber-100 text-amber-800 flex items-center justify-center font-bold">
                    <i data-lucide="file-text" class="w-5 h-5"></i>
                </div>
                <div>
                    <div class="text-xs text-slate-500 font-medium">Essay Analisis</div>
                    <div class="text-xl font-extrabold text-amber-900">100 Kasus</div>
                </div>
            </div>
        </div>

        <!-- Controls & Filters Card -->
        <div class="bg-white p-5 rounded-2xl border border-slate-200 shadow-sm mb-8 space-y-4">
            <!-- Tabs Row -->
            <div class="flex flex-wrap items-center gap-2 border-b border-slate-100 pb-4">
                <button onclick="setTab('all')" id="tab-all" class="px-4 py-2 rounded-xl text-xs sm:text-sm font-bold border transition-all tab-active">
                    📚 Semua Soal (300)
                </button>
                <button onclick="setTab('pg')" id="tab-pg" class="px-4 py-2 rounded-xl text-xs sm:text-sm font-bold border border-slate-200 text-slate-600 hover:bg-slate-50 transition-all">
                    🔘 100 Pilihan Ganda
                </button>
                <button onclick="setTab('is')" id="tab-is" class="px-4 py-2 rounded-xl text-xs sm:text-sm font-bold border border-slate-200 text-slate-600 hover:bg-slate-50 transition-all">
                    ✍️ 100 Isian Singkat
                </button>
                <button onclick="setTab('es')" id="tab-es" class="px-4 py-2 rounded-xl text-xs sm:text-sm font-bold border border-slate-200 text-slate-600 hover:bg-slate-50 transition-all">
                    📝 100 Soal Essay
                </button>
                <button onclick="setTab('ans')" id="tab-ans" class="px-4 py-2 rounded-xl text-xs sm:text-sm font-bold border border-amber-300 text-amber-800 bg-amber-50 hover:bg-amber-100 transition-all ml-auto">
                    🔑 Kunci & Pembahasan Terpisah
                </button>
            </div>

            <!-- Search & Filters -->
            <div class="grid grid-cols-1 md:grid-cols-12 gap-3">
                <div class="md:col-span-5 relative">
                    <i data-lucide="search" class="w-4 h-4 text-slate-400 absolute left-3.5 top-3.5"></i>
                    <input type="text" id="searchInput" oninput="renderQuestions()" placeholder="Cari kata kunci soal, rumus, modul, atau konsep..." class="w-full pl-10 pr-4 py-2 text-sm rounded-xl border border-slate-200 focus:outline-none focus:ring-2 focus:ring-blue-600 focus:border-transparent bg-slate-50/50">
                </div>
                <div class="md:col-span-3">
                    <select id="bookFilter" onchange="renderQuestions()" class="w-full px-3 py-2 text-sm rounded-xl border border-slate-200 focus:outline-none focus:ring-2 focus:ring-blue-600 bg-slate-50/50">
                        <option value="all">📖 Semua Buku Kurikulum</option>
                        <option value="Buku 1">Buku 1: Sains Data (Modul 01 - 14)</option>
                        <option value="Buku 2">Buku 2: Software Engineering (Modul 15 - 25)</option>
                    </select>
                </div>
                <div class="md:col-span-4">
                    <select id="moduleFilter" onchange="renderQuestions()" class="w-full px-3 py-2 text-sm rounded-xl border border-slate-200 focus:outline-none focus:ring-2 focus:ring-blue-600 bg-slate-50/50">
                        <option value="all">🏷️ Semua 25 Modul Praktikum</option>
                        <!-- Populated dynamically -->
                    </select>
                </div>
            </div>

            <!-- Global Actions -->
            <div class="flex flex-wrap items-center justify-between text-xs text-slate-500 pt-2 border-t border-slate-100">
                <span id="resultCount" class="font-medium text-slate-600">Menampilkan 300 soal</span>
                <div class="flex items-center gap-2">
                    <button onclick="toggleAllAnswers(true)" class="text-blue-700 hover:underline font-semibold flex items-center gap-1">
                        <i data-lucide="eye" class="w-3.5 h-3.5"></i> Buka Semua Kunci
                    </button>
                    <span>•</span>
                    <button onclick="toggleAllAnswers(false)" class="text-slate-600 hover:underline font-semibold flex items-center gap-1">
                        <i data-lucide="eye-off" class="w-3.5 h-3.5"></i> Tutup Semua Kunci
                    </button>
                </div>
            </div>
        </div>

        <!-- Questions List Container -->
        <div id="questionsContainer" class="space-y-4">
            <!-- Dynamic Content Injected Here -->
        </div>

    </main>

    <!-- Footer -->
    <footer class="bg-slate-900 text-slate-400 py-6 border-t border-slate-800 text-center text-xs mt-12">
        <div class="max-w-7xl mx-auto px-4 flex flex-col sm:flex-row items-center justify-between gap-2">
            <p>© 2026 Statistika Komputasi • Program Studi Teknik Informatika • UNJANI</p>
            <p>Disusun oleh: <strong>Dr. Ridwan Ilyas, S.Kom., M.T.</strong></p>
        </div>
    </footer>

    <!-- Application JavaScript Engine -->
    <script>
        const BANK_DATA = {json_str};

        let currentTab = 'all';
        let moduleList = [];

        // Initialize
        document.addEventListener('DOMContentLoaded', () => {{
            populateModuleDropdown();
            renderQuestions();
            lucide.createIcons();
        }});

        function populateModuleDropdown() {{
            const select = document.getElementById('moduleFilter');
            const modules = new Map();
            
            [...BANK_DATA.pilihan_ganda, ...BANK_DATA.isian_singkat, ...BANK_DATA.essay].forEach(q => {{
                if (!modules.has(q.modul_id)) {{
                    modules.set(q.modul_id, `Modul ${{q.modul_id < 10 ? '0' : ''}}${{q.modul_id}}: ${{q.modul}} (${{q.buku}})`);
                }}
            }});

            const sortedKeys = Array.from(modules.keys()).sort((a, b) => a - b);
            sortedKeys.forEach(mId => {{
                const opt = document.createElement('option');
                opt.value = mId;
                opt.textContent = modules.get(mId);
                select.appendChild(opt);
            }});
        }}

        function setTab(tab) {{
            currentTab = tab;
            ['all', 'pg', 'is', 'es', 'ans'].forEach(t => {{
                const btn = document.getElementById(`tab-${{t}}`);
                if (t === tab) {{
                    btn.className = "px-4 py-2 rounded-xl text-xs sm:text-sm font-bold border transition-all tab-active shadow-sm";
                }} else {{
                    btn.className = "px-4 py-2 rounded-xl text-xs sm:text-sm font-bold border border-slate-200 text-slate-600 hover:bg-slate-50 transition-all";
                }}
            }});
            renderQuestions();
        }}

        function getFilteredQuestions() {{
            const search = document.getElementById('searchInput').value.toLowerCase();
            const book = document.getElementById('bookFilter').value;
            const module = document.getElementById('moduleFilter').value;

            let list = [];

            if (currentTab === 'all' || currentTab === 'ans') {{
                list = [
                    ...BANK_DATA.pilihan_ganda.map(q => ({{ ...q, type: 'PG', typeLabel: 'Pilihan Ganda' }})),
                    ...BANK_DATA.isian_singkat.map(q => ({{ ...q, type: 'IS', typeLabel: 'Isian Singkat' }})),
                    ...BANK_DATA.essay.map(q => ({{ ...q, type: 'ES', typeLabel: 'Essay Analisis' }}))
                ];
            }} else if (currentTab === 'pg') {{
                list = BANK_DATA.pilihan_ganda.map(q => ({{ ...q, type: 'PG', typeLabel: 'Pilihan Ganda' }}));
            }} else if (currentTab === 'is') {{
                list = BANK_DATA.isian_singkat.map(q => ({{ ...q, type: 'IS', typeLabel: 'Isian Singkat' }}));
            }} else if (currentTab === 'es') {{
                list = BANK_DATA.essay.map(q => ({{ ...q, type: 'ES', typeLabel: 'Essay Analisis' }}));
            }}

            return list.filter(q => {{
                const matchSearch = q.soal.toLowerCase().includes(search) || 
                                    q.modul.toLowerCase().includes(search) || 
                                    q.id.toLowerCase().includes(search) ||
                                    (q.pembahasan && q.pembahasan.toLowerCase().includes(search)) ||
                                    (q.rubrik && q.rubrik.toLowerCase().includes(search));
                
                const matchBook = (book === 'all') || (q.buku === book);
                const matchModule = (module === 'all') || (q.modul_id.toString() === module);

                return matchSearch && matchBook && matchModule;
            }});
        }}

        function renderQuestions() {{
            const container = document.getElementById('questionsContainer');
            const questions = getFilteredQuestions();
            document.getElementById('resultCount').textContent = `Menampilkan ${{questions.length}} dari 300 soal`;

            if (questions.length === 0) {{
                container.innerHTML = `
                    <div class="bg-white p-12 rounded-2xl text-center border border-slate-200">
                        <i data-lucide="help-circle" class="w-12 h-12 text-slate-300 mx-auto mb-3"></i>
                        <h3 class="text-base font-bold text-slate-700">Tidak ada soal yang cocok</h3>
                        <p class="text-xs text-slate-500 mt-1">Coba ubah kata kunci pencarian atau reset filter buku dan modul.</p>
                    </div>
                `;
                lucide.createIcons();
                return;
            }}

            // If TAB ANSWERS ONLY: Render Key Table / Cards
            if (currentTab === 'ans') {{
                let html = `
                    <div class="bg-amber-50/70 border border-amber-200 p-4 rounded-2xl mb-4 flex items-center justify-between">
                        <div class="flex items-center gap-3">
                            <div class="w-8 h-8 rounded-lg bg-amber-500 text-white flex items-center justify-center font-bold">
                                <i data-lucide="key" class="w-4 h-4"></i>
                            </div>
                            <div>
                                <h4 class="text-sm font-bold text-amber-900">Lembar Kunci Jawaban & Pembahasan Terpisah</h4>
                                <p class="text-xs text-amber-700">Memuat solusi eksak dan rubrik penilaian untuk seluruh ${{questions.length}} soal.</p>
                            </div>
                        </div>
                    </div>
                `;

                questions.forEach((q, idx) => {{
                    html += `
                        <div class="bg-white p-5 rounded-2xl border border-slate-200 shadow-sm space-y-3">
                            <div class="flex items-center justify-between gap-2 border-b border-slate-100 pb-2">
                                <div class="flex items-center gap-2">
                                    <span class="px-2.5 py-1 rounded-md text-xs font-bold bg-slate-900 text-white">${{q.id}}</span>
                                    <span class="px-2 py-0.5 rounded text-[11px] font-semibold ${{q.type==='PG' ? 'bg-indigo-100 text-indigo-800' : q.type==='IS' ? 'bg-teal-100 text-teal-800' : 'bg-amber-100 text-amber-800'}}">${{q.typeLabel}}</span>
                                    <span class="text-xs text-slate-500 font-medium">${{q.buku}} • Modul ${{q.modul_id < 10 ? '0' : ''}}${{q.modul_id}}: ${{q.modul}}</span>
                                </div>
                            </div>
                            <div class="text-xs text-slate-600 line-clamp-2">
                                <strong>Soal:</strong> ${{q.soal}}
                            </div>
                            <div class="p-3.5 bg-emerald-50 border border-emerald-200 rounded-xl">
                                <div class="text-xs font-bold text-emerald-900 flex items-center gap-1.5 mb-1">
                                    <i data-lucide="check" class="w-4 h-4 text-emerald-600"></i>
                                    <span>Kunci Jawaban / Solusi:</span>
                                </div>
                                <div class="text-sm font-extrabold text-emerald-800 whitespace-pre-line">
                                    ${{q.type === 'PG' ? `${{q.kunci}}. ${{q.opsi[q.kunci]}}` : q.kunci}}
                                </div>
                            </div>
                            <div class="p-3.5 bg-slate-50 border border-slate-200 rounded-xl text-xs text-slate-700 space-y-1">
                                <div class="font-bold text-slate-800 flex items-center gap-1.5">
                                    <i data-lucide="info" class="w-4 h-4 text-blue-600"></i>
                                    <span>${{q.rubrik ? 'Rubrik Penilaian:' : 'Pembahasan Konseptual:'}}</span>
                                </div>
                                <div class="whitespace-pre-line text-slate-600 leading-relaxed">
                                    ${{q.rubrik || q.pembahasan}}
                                </div>
                            </div>
                        </div>
                    `;
                }});
                container.innerHTML = html;
                lucide.createIcons();
                return;
            }}

            // Normal Question Practice Cards
            let html = '';
            questions.forEach((q, idx) => {{
                const isPG = q.type === 'PG';
                const isIS = q.type === 'IS';
                const isES = q.type === 'ES';

                html += `
                    <div class="bg-white p-5 rounded-2xl border border-slate-200 shadow-sm transition-all hover:border-slate-300 space-y-4" id="card-${{q.id}}">
                        <!-- Top Metadata -->
                        <div class="flex flex-wrap items-center justify-between gap-2 border-b border-slate-100 pb-3">
                            <div class="flex items-center gap-2">
                                <span class="px-2.5 py-1 rounded-md text-xs font-bold bg-slate-900 text-white">${{q.id}}</span>
                                <span class="px-2 py-0.5 rounded text-[11px] font-semibold ${{isPG ? 'bg-indigo-100 text-indigo-800' : isIS ? 'bg-teal-100 text-teal-800' : 'bg-amber-100 text-amber-800'}}">${{q.typeLabel}}</span>
                                <span class="text-xs text-slate-500 font-medium">${{q.buku}} • Modul ${{q.modul_id < 10 ? '0' : ''}}${{q.modul_id}}: ${{q.modul}}</span>
                            </div>
                            <button onclick="toggleAnswer('${{q.id}}')" class="text-xs font-semibold text-blue-700 hover:text-blue-900 bg-blue-50 hover:bg-blue-100 px-3 py-1.5 rounded-lg border border-blue-200/60 transition-all flex items-center gap-1">
                                <i data-lucide="eye" class="w-3.5 h-3.5"></i>
                                <span id="btn-text-${{q.id}}">Lihat Kunci</span>
                            </button>
                        </div>

                        <!-- Question Statement -->
                        <div class="text-sm sm:text-base font-semibold text-slate-800 leading-relaxed whitespace-pre-line">
                            ${{q.soal}}
                        </div>

                        <!-- PG Options (Interactive) -->
                        ${{isPG ? `
                            <div class="grid grid-cols-1 gap-2 pt-1">
                                ${{Object.entries(q.opsi).map(([optKey, optVal]) => `
                                    <button onclick="checkOption('${{q.id}}', '${{optKey}}', '${{q.kunci}}')" id="opt-${{q.id}}-${{optKey}}" class="option-btn text-left px-4 py-2.5 rounded-xl border border-slate-200 text-xs sm:text-sm font-medium hover:bg-slate-50 transition-all flex items-start gap-3">
                                        <span class="w-5 h-5 rounded-full bg-slate-100 text-slate-700 font-bold flex items-center justify-center text-xs flex-shrink-0 mt-0.5">${{optKey}}</span>
                                        <span class="text-slate-700">${{optVal}}</span>
                                    </button>
                                `).join('')}}
                            </div>
                        ` : ''}}

                        <!-- Expandable Answer Key & Explanation -->
                        <div id="ans-${{q.id}}" class="hidden p-4 bg-slate-50/80 border border-slate-200 rounded-xl text-xs space-y-2 mt-2">
                            <div class="flex items-center gap-1.5 text-emerald-800 font-bold">
                                <i data-lucide="check-circle" class="w-4 h-4 text-emerald-600"></i>
                                <span>Kunci Jawaban:</span>
                                <span class="bg-emerald-100 text-emerald-900 px-2 py-0.5 rounded font-extrabold text-sm ml-1">
                                    ${{isPG ? `${{q.kunci}}. ${{q.opsi[q.kunci]}}` : q.kunci}}
                                </span>
                            </div>
                            <div class="text-slate-600 leading-relaxed whitespace-pre-line pt-1 border-t border-slate-200/60">
                                <strong>${{q.rubrik ? 'Rubrik Penilaian:' : 'Pembahasan:'}}</strong><br>
                                ${{q.rubrik || q.pembahasan}}
                            </div>
                        </div>

                    </div>
                `;
            }});

            container.innerHTML = html;
            lucide.createIcons();
        }}

        function checkOption(qId, selectedKey, correctKey) {{
            const buttons = document.querySelectorAll(`[id^="opt-${{qId}}-"]`);
            buttons.forEach(btn => {{
                btn.classList.remove('option-selected-correct', 'option-selected-wrong');
            }});

            const selectedBtn = document.getElementById(`opt-${{qId}}-${{selectedKey}}`);
            const correctBtn = document.getElementById(`opt-${{qId}}-${{correctKey}}`);

            if (selectedKey === correctKey) {{
                selectedBtn.classList.add('option-selected-correct');
            }} else {{
                selectedBtn.classList.add('option-selected-wrong');
                correctBtn.classList.add('option-selected-correct');
            }}

            // Automatically reveal explanation
            const ansDiv = document.getElementById(`ans-${{qId}}`);
            const btnText = document.getElementById(`btn-text-${{qId}}`);
            ansDiv.classList.remove('hidden');
            btnText.textContent = 'Tutup Kunci';
        }}

        function toggleAnswer(qId) {{
            const ansDiv = document.getElementById(`ans-${{qId}}`);
            const btnText = document.getElementById(`btn-text-${{qId}}`);
            if (ansDiv.classList.contains('hidden')) {{
                ansDiv.classList.remove('hidden');
                btnText.textContent = 'Tutup Kunci';
            }} else {{
                ansDiv.classList.add('hidden');
                btnText.textContent = 'Lihat Kunci';
            }}
        }}

        function toggleAllAnswers(show) {{
            const allAnsDivs = document.querySelectorAll('[id^="ans-"]');
            const allBtnTexts = document.querySelectorAll('[id^="btn-text-"]');
            allAnsDivs.forEach(div => {{
                if (show) div.classList.remove('hidden');
                else div.classList.add('hidden');
            }});
            allBtnTexts.forEach(btn => {{
                btn.textContent = show ? 'Tutup Kunci' : 'Lihat Kunci';
            }});
        }}

        // Client-side Excel Export using SheetJS
        function exportToExcel() {{
            const wb = XLSX.utils.book_new();

            // 1. Panduan Sheet
            const guideData = [
                ["BANK SOAL 300 STATISTIKA KOMPUTASI (OBE TEKNIK INFORMATIKA)"],
                ["Mata Kuliah: Statistika Komputasi | Penyusun: Dr. Ridwan Ilyas, S.Kom., M.T. | UNJANI"],
                [],
                ["Struktur Bank Soal:"],
                ["1. Bagian I: 100 Soal Pilihan Ganda (PG001 - PG100)"],
                ["2. Bagian II: 100 Soal Isian Singkat & Kasus Komputasi (IS001 - IS100)"],
                ["3. Bagian III: 100 Soal Essay & Studi Kasus Analisis (ES001 - ES100)"],
                ["4. Bagian IV: Kunci Jawaban & Pembahasan Lengkap (Terpisah pada Sheet ke-5)"],
                [],
                ["No", "Buku", "Modul ID", "Nama Modul", "Pilihan Ganda", "Isian Singkat", "Essay", "Total Soal"]
            ];
            
            for (let m = 1; m <= 25; m++) {{
                const pgSample = BANK_DATA.pilihan_ganda.find(q => q.modul_id === m);
                guideData.push([m, pgSample.buku, `Modul ${{m < 10 ? '0' : ''}}${{m}}`, pgSample.modul, 4, 4, 4, 12]);
            }}
            guideData.push(["Total", "", "", "TOTAL KESELURUHAN BANK SOAL", 100, 100, 100, 300]);
            const wsGuide = XLSX.utils.aoa_to_sheet(guideData);
            XLSX.utils.book_append_sheet(wb, wsGuide, "Panduan & Distribusi");

            // 2. PG Sheet (Soal Only)
            const pgRows = BANK_DATA.pilihan_ganda.map((q, idx) => ({{
                "No": idx + 1,
                "Kode Soal": q.id,
                "Buku": q.buku,
                "Modul ID": `Modul ${{q.modul_id < 10 ? '0' : ''}}${{q.modul_id}}`,
                "Nama Modul": q.modul,
                "Pertanyaan / Kasus": q.soal,
                "Pilihan A": q.opsi.A || "",
                "Pilihan B": q.opsi.B || "",
                "Pilihan C": q.opsi.C || "",
                "Pilihan D": q.opsi.D || "",
                "Pilihan E": q.opsi.E || ""
            }}));
            const wsPG = XLSX.utils.json_to_sheet(pgRows);
            XLSX.utils.book_append_sheet(wb, wsPG, "100 Pilihan Ganda");

            // 3. IS Sheet (Soal Only)
            const isRows = BANK_DATA.isian_singkat.map((q, idx) => ({{
                "No": idx + 1,
                "Kode Soal": q.id,
                "Buku": q.buku,
                "Modul ID": `Modul ${{q.modul_id < 10 ? '0' : ''}}${{q.modul_id}}`,
                "Nama Modul": q.modul,
                "Pertanyaan / Kasus Komputasi": q.soal
            }}));
            const wsIS = XLSX.utils.json_to_sheet(isRows);
            XLSX.utils.book_append_sheet(wb, wsIS, "100 Isian Singkat");

            // 4. ES Sheet (Soal Only)
            const esRows = BANK_DATA.essay.map((q, idx) => ({{
                "No": idx + 1,
                "Kode Soal": q.id,
                "Buku": q.buku,
                "Modul ID": `Modul ${{q.modul_id < 10 ? '0' : ''}}${{q.modul_id}}`,
                "Nama Modul": q.modul,
                "Kasus & Instruksi Soal Essay": q.soal
            }}));
            const wsES = XLSX.utils.json_to_sheet(esRows);
            XLSX.utils.book_append_sheet(wb, wsES, "100 Soal Essay");

            // 5. Kunci Jawaban & Pembahasan (Terpisah)
            const ansRows = [];
            let counter = 1;
            BANK_DATA.pilihan_ganda.forEach(q => {{
                ansRows.push({{
                    "No": counter++,
                    "Kode Soal": q.id,
                    "Tipe Soal": "Pilihan Ganda",
                    "Buku": q.buku,
                    "Modul ID": `Modul ${{q.modul_id < 10 ? '0' : ''}}${{q.modul_id}}`,
                    "Nama Modul": q.modul,
                    "Kunci Jawaban": `${{q.kunci}}. ${{q.opsi[q.kunci]}}`,
                    "Pembahasan / Rubrik": q.pembahasan
                }});
            }});
            BANK_DATA.isian_singkat.forEach(q => {{
                ansRows.push({{
                    "No": counter++,
                    "Kode Soal": q.id,
                    "Tipe Soal": "Isian Singkat",
                    "Buku": q.buku,
                    "Modul ID": `Modul ${{q.modul_id < 10 ? '0' : ''}}${{q.modul_id}}`,
                    "Nama Modul": q.modul,
                    "Kunci Jawaban": q.kunci,
                    "Pembahasan / Rubrik": q.pembahasan
                }});
            }});
            BANK_DATA.essay.forEach(q => {{
                ansRows.push({{
                    "No": counter++,
                    "Kode Soal": q.id,
                    "Tipe Soal": "Essay Analisis",
                    "Buku": q.buku,
                    "Modul ID": `Modul ${{q.modul_id < 10 ? '0' : ''}}${{q.modul_id}}`,
                    "Nama Modul": q.modul,
                    "Kunci Jawaban": q.kunci,
                    "Pembahasan / Rubrik": q.rubrik
                }});
            }});
            const wsAns = XLSX.utils.json_to_sheet(ansRows);
            XLSX.utils.book_append_sheet(wb, wsAns, "Kunci Jawaban & Pembahasan");

            // Save File
            XLSX.writeFile(wb, "latihan_soal_300_statistika_komputasi.xlsx");
        }}
    </script>
</body>
</html>
"""

with open("/Users/ridwanilyas/Documents/Unjani/Statistika/latihan_soal_300_statistika_komputasi.html", "w", encoding="utf-8") as f:
    f.write(html_content)

print("Web Application successfully created: latihan_soal_300_statistika_komputasi.html")
