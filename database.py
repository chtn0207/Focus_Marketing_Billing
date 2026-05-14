import sqlite3

DB_NAME = "billing.db"

# -----------------------------------
# CREATE DATABASE TABLE
# -----------------------------------

def init_db():

    conn = sqlite3.connect(DB_NAME)

    cursor = conn.cursor()

    cursor.execute("""
    CREATE TABLE IF NOT EXISTS bills (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        document_number TEXT,
        document_type TEXT,
        customer_name TEXT,
        invoice_date TEXT,
        payment_mode TEXT,
        transaction_id TEXT,
        total_amount REAL,
        data TEXT
    )
    """)

    conn.commit()

    conn.close()

# -----------------------------------
# GET NEXT DOCUMENT NUMBER
# -----------------------------------

def get_next_number(document_type):

    conn = sqlite3.connect(DB_NAME)

    cursor = conn.cursor()

    prefix = "INV" if document_type == "Invoice" else "SAL"

    cursor.execute(
        "SELECT COUNT(*) FROM bills WHERE document_type=?",
        (document_type,)
    )

    count = cursor.fetchone()[0] + 1

    conn.close()

    return f"{prefix}-{count:03d}"

# -----------------------------------
# SAVE BILL
# -----------------------------------

def save_bill(
    document_number,
    document_type,
    customer_name,
    invoice_date,
    payment_mode,
    transaction_id,
    total_amount,
    data
):

    conn = sqlite3.connect(DB_NAME)

    cursor = conn.cursor()

    cursor.execute("""
    INSERT INTO bills (
        document_number,
        document_type,
        customer_name,
        invoice_date,
        payment_mode,
        transaction_id,
        total_amount,
        data
    )
    VALUES (?, ?, ?, ?, ?, ?, ?, ?)
    """, (
        document_number,
        document_type,
        customer_name,
        invoice_date,
        payment_mode,
        transaction_id,
        total_amount,
        data
    ))

    conn.commit()

    conn.close()

# -----------------------------------
# GET ALL BILLS
# -----------------------------------

def get_all_bills():

    conn = sqlite3.connect(DB_NAME)

    cursor = conn.cursor()

    cursor.execute("""
    SELECT
        document_number,
        document_type,
        customer_name,
        invoice_date,
        payment_mode,
        total_amount
    FROM bills
    ORDER BY id DESC
    """)

    rows = cursor.fetchall()

    conn.close()

    return rows

# -----------------------------------
# SEARCH BILL
# -----------------------------------

def search_bill(document_number):

    conn = sqlite3.connect(DB_NAME)

    cursor = conn.cursor()

    cursor.execute("""
    SELECT *
    FROM bills
    WHERE document_number=?
    """, (document_number,))

    row = cursor.fetchone()

    conn.close()

    return row
