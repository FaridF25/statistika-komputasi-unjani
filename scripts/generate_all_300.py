import json
import os
import openpyxl
from openpyxl.styles import Font, PatternFill, Alignment, Border, Side
from openpyxl.utils import get_column_letter

# Build complete 300 question dataset
print("Building 300 Questions for Statistika Komputasi...")

# Data structures
all_pg = []
all_is = []
all_es = []

