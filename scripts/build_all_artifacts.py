import json
import os
import openpyxl
from openpyxl.styles import Font, PatternFill, Alignment, Border, Side
from openpyxl.utils import get_column_letter

from modules_part1 import load_part1
from modules_part2 import load_part2
from modules_part3 import load_part3
from modules_part4 import load_part4
from modules_part5 import load_part5

# Data container
MODULES_DATA = {}

def add_module(mod_id, name, book, pg_list, is_list, es_list):
    MODULES_DATA[mod_id] = {
        "mod_id": mod_id,
        "name": name,
        "book": book,
        "pg": pg_list,
        "is": is_list,
        "es": es_list
    }

# Load all 5 parts
load_part1(add_module)
load_part2(add_module)
load_part3(add_module)
load_part4(add_module)
load_part5(add_module)

print(f"Loaded {len(MODULES_DATA)} modules.")

# Extract 300 questions
all_pg = []
all_is = []
all_es = []

pg_counter = 1
is_counter = 1
es_counter = 1

for m_id in sorted(MODULES_DATA.keys()):
    m = MODULES_DATA[m_id]
    
    # 4 PG
    for q_text, opts, key, exp in m["pg"]:
        all_pg.append({
            "id": f"PG{pg_counter:03d}",
            "modul_id": m["mod_id"],
            "modul": m["name"],
            "buku": m["book"],
            "soal": q_text,
            "opsi": opts,
            "kunci": key,
            "pembahasan": exp
        })
        pg_counter += 1
        
    # 4 IS
    for q_text, key, exp in m["is"]:
        all_is.append({
            "id": f"IS{is_counter:03d}",
            "modul_id": m["mod_id"],
            "modul": m["name"],
            "buku": m["book"],
            "soal": q_text,
            "kunci": key,
            "pembahasan": exp
        })
        is_counter += 1
        
    # 4 ES
    for q_text, key, rubric in m["es"]:
        all_es.append({
            "id": f"ES{es_counter:03d}",
            "modul_id": m["mod_id"],
            "modul": m["name"],
            "buku": m["book"],
            "soal": q_text,
            "kunci": key,
            "rubrik": rubric
        })
        es_counter += 1

print(f"Total PG Questions: {len(all_pg)}")
print(f"Total IS Questions: {len(all_is)}")
print(f"Total ES Questions: {len(all_es)}")
print(f"Grand Total: {len(all_pg) + len(all_is) + len(all_es)} Questions.")

assert len(all_pg) == 100, f"Expected 100 PG, got {len(all_pg)}"
assert len(all_is) == 100, f"Expected 100 IS, got {len(all_is)}"
assert len(all_es) == 100, f"Expected 100 ES, got {len(all_es)}"

# Save to JSON
json_data = {
    "title": "Bank Soal 300 Statistika Komputasi",
    "course": "Statistika Komputasi",
    "total_questions": 300,
    "pilihan_ganda": all_pg,
    "isian_singkat": all_is,
    "essay": all_es
}

with open("/Users/ridwanilyas/Documents/Unjani/Statistika/bank_soal_300.json", "w", encoding="utf-8") as f:
    json.dump(json_data, f, indent=2, ensure_ascii=False)
print("Saved bank_soal_300.json")

