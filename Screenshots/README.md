# Author: Ibrahim Aljiez (33712928)
---
# Mini-Scalpel: Simple File Carving Tool

## Overview

Mini-Scalpel is a Python-based file carving tool that allows users to search for patterns within TXT, CSV, JSON, and PDF files. It extracts matching content and saves them as separate output files. The tool also provides a menu-driven interface to carve files, view extracted content, or exit the program.

## Table of Contents
- [Overview](#overview)
- [Features](#features)
- [File Carving Functions](#file-carving-functions)
- [Why this Project?](#why-this-project)
- [Menu Options](#menu-options)
- [Installation](#installation-of-the-pdf-package)
- [How to Run](#how-to-run-the-programe)
- [Supplying a File](#supplying-a-file)
- [Carving Examples](#carving-examples)
- [Viewing Carved Content](#viewing-the-carved-content)
- [Conclusion](#conclusion)
- [Notes](#notes)


## Features

* Pattern search in TXT, CSV, JSON, and PDF files.
* Case-insensitive search.
* Recursive search for nested structures in JSON files.
* Page-wise search in PDF files.
* Saves carved matches in `carved_output/` directory.
* Menu-driven interface for easy operation.
* View carved documents from within the program.

## File Carving Functions

### `carve_txt(path, pattern)`

* Opens a TXT file.
* Returns a list of lines containing the specified pattern (case-insensitive).

### `carve_csv(path, pattern)`

* Opens a CSV file.
* Returns a list of rows (as strings) containing the pattern.

### `carve_json(path, pattern)`

* Reads and parses a JSON file.
* Recursively searches through nested dictionaries and lists.
* Returns a list of key-value pairs matching the pattern.

### `carve_pdf(path, pattern)`

* Opens a PDF in binary mode.
* Reads each page and extracts text.
* Returns a list of pages containing the pattern, including page numbers.

### `save_matches(matches)`

* Saves each match in a separate text file inside the `carved_output/` folder.

### `view_carved_docs()`

* Displays the content of all previously carved documents stored in the `carved_output/` folder.

---

### Why this Project?
Due to my background in digital forensics and the hands-on experience with the Mini-Scalpel tool, this project has been particularly engaging and insightful for me. Exploring file carving, pattern searching, and data extraction allowed me to apply theoretical knowledge in a practical setting, deepening my understanding of forensic techniques and enhancing my interest in the field.

## Menu Options
![The main Interface](interface.png)

1. Carve TXT file.
2. Carve JSON file.
3. Carve PDF file.
4. View carved documents.
5. Exit program.

## Installation of the PDF Package

1. Ensure Python 3 is installed on your system.
2. Install required libraries (PyPDF2 for PDF support):

![Installation command](installation.png)

```bash
pip install PyPDF2
```

## How to run the Program

3. Navigate to the directory containing `miniscalpel.py`.
4. Run the program:

```bash
python miniscalpel.py
```
![Running the program](running.png)


5. Follow the on-screen menu to select a file type, provide file path, and enter the search pattern.

## Supplying a file 
1. Upon the Execution of the program a file must be supplied.
2. choose a file provided
3. Navigate to miniscalpel files for a list of file to be used

![Miniscalpel files provided](mini_scalpel_files.png)

## Carving .TXT File
![Carving a .txt file ](file_supply.png)

## Carving a .JSON File
![Carving a .json file ](json_file.png)

## Carving a .PDF File
![Carving a .pdf file ](pdf_file.png)


## Viewing the carved content 
![output 1 ](carved1.png)
---
![output 2 ](carved2.png)
---

## Conclusion

Mini-Scalpel provides a simple yet effective approach to file carving, making it a useful tool for beginners, students, and anyone exploring digital forensics. By supporting multiple file formats and offering features such as recursive JSON searching and PDF page analysis, it demonstrates the core concepts of pattern-based data extraction. The menu-driven interface ensures that the tool is accessible and easy to operate, while the automatic saving of carved content supports further analysis and documentation. Overall, Mini-Scalpel highlights the importance of efficient file parsing and serves as a solid foundation for more advanced forensic tools in the future.

---
## Notes

* All carved files are saved in the `carved_output/` folder.
* Pattern searches are **case-insensitive**.
* The program handles errors such as missing files or unsupported file types gracefully.
---

**Author:** Ibrahim Aljiez
