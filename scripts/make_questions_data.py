import json
import os
import openpyxl
from openpyxl.styles import Font, PatternFill, Alignment, Border, Side
from openpyxl.utils import get_column_letter

# Master container for all questions
MODULES_DATA = {}

# We define each module with:
# 'pg': list of (question, options_dict, key, explanation)
# 'is': list of (question, key, explanation)
# 'es': list of (question, model_answer, rubric)

def add_module(mod_id, name, book, pg_list, is_list, es_list):
    MODULES_DATA[mod_id] = {
        "mod_id": mod_id,
        "name": name,
        "book": book,
        "pg": pg_list,
        "is": is_list,
        "es": es_list
    }

print("make_questions_data initialized.")
