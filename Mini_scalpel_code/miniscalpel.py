#!/usr/bin/env python3
"""
Mini-Scalpel: Menu-driven File Carving Tool (TXT / JSON / PDF)
Allows selecting file types, carving data, viewing results, or exiting.
"""

import csv
import json
from pathlib import Path
import PyPDF2

def carve_txt(path, pattern):
    with path.open("r", encoding="utf-8") as f:
        return [line.strip() for line in f if pattern.lower() in line.lower()]

def carve_json(path, pattern):
    matches = []
    data = json.loads(path.read_text(encoding="utf-8"))
    def search(obj):
        if isinstance(obj, dict):
            for k, v in obj.items():
                if pattern.lower() in str(k).lower() or pattern.lower() in str(v).lower():
                    matches.append(f"{k}: {v}")
                search(v)
        elif isinstance(obj, list):
            for item in obj:
                search(item)
    search(data)
    return matches

def carve_pdf(path, pattern):
    matches = []
    with open(path, "rb") as f:
        reader = PyPDF2.PdfReader(f)
        for page_num, page in enumerate(reader.pages, 1):
            text = page.extract_text()
            if text and pattern.lower() in text.lower():
                matches.append(f"Page {page_num}:\n{text.strip()}")
    return matches

def save_matches(matches):
    output_dir = Path("carved_output")
    output_dir.mkdir(exist_ok=True)
    files = []
    for i, m in enumerate(matches, 1):
        outfile = output_dir / f"carved_{i}.txt"
        outfile.write_text(m, encoding="utf-8")
        files.append(outfile)
    return files

def view_carved_docs():
    folder = Path("carved_output")
    if not folder.exists() or not any(folder.iterdir()):
        print("No carved documents found.")
        return
    for f in folder.iterdir():
        print(f"\n--- {f.name} ---")
        print(f.read_text(encoding="utf-8"))
        print("----------------")

def main():
    while True:
        print("\n=== Mini-Scalpel Menu ===")
        print("1. Carve TXT file")
        print("2. Carve JSON file")
        print("3. Carve PDF file")
        print("4. View carved documents")
        print("5. Exit")
        choice = input("Select an option (1-5): ").strip()

        if choice == "1":
            file_path = Path(input("Enter TXT file path: "))
            pattern = input("Enter pattern to search: ")
            if file_path.exists():
                matches = carve_txt(file_path, pattern)
                if matches:
                    save_matches(matches)
                    print(f"Found {len(matches)} matches in {file_path.name}.")
                else:
                    print("No matches found.")
            else:
                print("File does not exist.")

        elif choice == "2":
            file_path = Path(input("Enter JSON file path: "))
            pattern = input("Enter pattern to search: ")
            if file_path.exists():
                matches = carve_json(file_path, pattern)
                if matches:
                    save_matches(matches)
                    print(f"Found {len(matches)} matches in {file_path.name}.")
                else:
                    print("No matches found.")
            else:
                print("File does not exist.")

        elif choice == "3":
            file_path = Path(input("Enter PDF file path: "))
            pattern = input("Enter pattern to search: ")
            if file_path.exists():
                matches = carve_pdf(file_path, pattern)
                if matches:
                    save_matches(matches)
                    print(f"Found {len(matches)} matches in {file_path.name}.")
                else:
                    print("No matches found.")
            else:
                print("File does not exist.")

        elif choice == "4":
            view_carved_docs()

        elif choice == "5":
            print("Exiting program. Goodbye!")
            break

        else:
            print("Invalid option. Please select 1-5.")

if __name__ == "__main__":
    main()
