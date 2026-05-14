# Focus Marketing Solutions Billing Software

A professional Streamlit-based billing and salary voucher software for internal business use.

---

# Features

## Invoice Module
- Create GST invoices
- Add multiple services
- Remove accidental service entries
- Auto GST calculation
- Auto invoice number series
- Editable Word DOCX invoice download

---

## Salary Voucher Module
- Generate salary vouchers
- Aadhaar Number field
- PAN Number field
- Salary amount entry
- Payment mode support
- Transaction ID support

---

## Payment Features
- Cash
- UPI
- Card
- Online
- Bank Transfer

Transaction ID field automatically appears for non-cash payments.

---

## Bill Management
- Search previous bills
- View all bills
- Auto save bills to SQLite database

---

# Project Structure

```plaintext
focus_billing_app/
│
├── app.py
├── database.py
├── billing.db
├── requirements.txt
└── README.md
```

---

# Installation Guide

## Step 1 - Install Python

Download Python:

https://www.python.org/downloads/

IMPORTANT:
Enable:

[x] Add Python to PATH

---

# Step 2 - Create Project Folder

Example:

```bash
mkdir focus_billing_app
```

---

# Step 3 - Copy Files

Copy:
- app.py
- database.py
- requirements.txt

into the folder.

---

# Step 4 - Open Terminal

Open terminal inside project folder.

---

# Step 5 - Create Virtual Environment (Recommended)

## Windows

```bash
python -m venv venv
venv\\Scripts\\activate
```

## Mac/Linux

```bash
python3 -m venv venv
source venv/bin/activate
```

---

# Step 6 - Install Requirements

```bash
pip install -r requirements.txt
```

---

# Step 7 - Run Streamlit App

```bash
streamlit run app.py
```

---

# Step 8 - Open Browser

If browser does not open automatically:

```plaintext
http://localhost:8501
```

---

# Features Included

## Invoice Features
- GST calculation
- Invoice number auto-series
- Service add/remove
- DOCX invoice download

---

## Salary Voucher Features
- Voucher number auto-series
- Aadhaar number
- PAN number
- Salary amount
- Payment tracking

---

## Database Features
- Search bill by number
- View all previous bills
- SQLite local storage

---

# Invoice Number Examples

```plaintext
INV-001
INV-002
INV-003
```

# Salary Voucher Examples

```plaintext
SAL-001
SAL-002
SAL-003
```

---

# Database

SQLite database file:

```plaintext
billing.db
```

This file stores:
- invoices
- salary vouchers
- payment history

---

# Future Upgrade Ideas

- PDF download
- WhatsApp share
- Email invoices
- Company logo
- Revenue dashboard
- GST reports
- Export to Excel
- Multi-user login
- Cloud deployment

---

# Deployment on Streamlit Cloud

## Step 1
Upload project to GitHub

## Step 2
Open:

https://streamlit.io/cloud

---

## Step 3
Connect GitHub Repository

---

## Step 4
Deploy app.py

---

# Author

Focus Marketing Solutions
