# 🩺 MediScan

**MediScan** is a Python-based OCR project that extracts structured data—such as **patient details** and **prescription information**—from PDF medical documents. The project includes an intelligent backend built with **FastAPI** and an interactive frontend using **Streamlit**.

<div align="center">
  <img src="https://github.com/Mohamed-Imran-94/MediScan/blob/main/MediScan%20-%20Working%20video.webm" width="700" alt="MediScan Demo">
</div>

---

## 📌 Table of Contents

1. [What is OCR?](#what-is-ocr)
2. [Why this Project?](#why-this-project)
3. [Key Features](#key-features)
4. [Tech Stack](#tech-stack)
5. [How It Works](#how-it-works)
6. [Directory Structure](#directory-structure)
7. [Installation & Setup](#installation--setup)
8. [What I Learned](#what-i-learned)
9. [Challenges Faced](#challenges-faced)

---

## 📖 What is OCR?

**OCR** (Optical Character Recognition) is a technology that converts scanned documents and images into editable, machine-readable text. It powers document digitization, automated data entry, and intelligent search.

OCR is widely used in:

- Healthcare for extracting medical records
- Banking for check and form processing
- Retail, education, and accessibility applications
- NLP & document AI tasks

---

## 🔍 Why this Project?

While studying Python and backend development, I built this project for three reasons:

1. 🧠 To apply **Computer Vision** (OCR) in a **real-world healthcare scenario**
2. 💡 To improve modular programming and text parsing skills using **Python OOP and RegEx**
3. 🚀 To build and expose a production-style backend using **FastAPI**, a modern async API framework

---

## ✨ Key Features

- Extracts fields like **Patient Name**, **Address**, **Medicines**, **Dosage**, and **Refill Info**
- Handles scanned or digital **PDF prescriptions** and **medical forms**
- Clean JSON output for further use in databases or health platforms
- Modular backend logic with switchable parsers (`PatientDetailsParser`, `PrescriptionParser`)
- **Streamlit frontend** to upload and visualize results
- Fully offline and privacy-safe (no cloud required)

---

## 🛠 Tech Stack

| Component       | Technology       |
|----------------|------------------|
| OCR Engine      | Tesseract OCR     |
| Image Conversion | pdf2image + Poppler |
| Image Preprocessing | OpenCV2           |
| Backend API     | FastAPI            |
| Frontend UI     | Streamlit          |
| Parsing Logic   | Python (Regex, OOP) |
| Testing         | Pytest             |
| API Testing     | Postman            |

---

## 🔁 How It Works

1. ✅ **PDF ➜ Image** using `pdf2image` and Poppler
2. 🎨 **Image ➜ Preprocessing** (adaptive thresholding with OpenCV)
3. 🔤 **Image ➜ Text** using `pytesseract` (Tesseract OCR)
4. 🔎 **Text ➜ Field Extraction** using `regex` and `parsers`
5. 🌐 **FastAPI Backend** processes incoming PDFs and returns structured JSON
6. 🖥 **Streamlit Frontend** provides file upload and result preview

```mermaid
flowchart LR
    A[PDF File] --> B[pdf2image]
    B --> C[OpenCV Preprocessing]
    C --> D[Tesseract OCR]
    D --> E[Regex Parsers]
    E --> F[JSON Output]
    F --> G[Streamlit UI / API Response]



MediScan/
├── backend/
│   ├── src/
│   │   ├── extractor.py
│   │   ├── parser_prescription.py
│   │   ├── parser_patient_details.py
│   │   ├── utils.py
│   │   └── main.py  ← FastAPI server
│   ├── tests/
│   │   └── test_prescription_parser.py
│   ├── uploads/
│   └── resources/
│       ├── prescription/
│       └── patient_details/
│
├── frontend/
│   └── app.py  ← Streamlit frontend
│
├── Notebooks/
│   ├── 01_prescription_parser.ipynb
│   ├── 02_patient_details_parser.ipynb
│   └── 03_RegEx.ipynb
│
├── reference/
│   └── tesseract_papar_by_google.pdf
├── requirements.txt
└── README.md


