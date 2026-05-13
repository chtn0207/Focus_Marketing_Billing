import streamlit as st
import pandas as pd
from datetime import datetime
from docx import Document
import io

# -----------------------------------
# PAGE CONFIG
# -----------------------------------

st.set_page_config(
    page_title="Focus Marketing Billing Software",
    layout="wide"
)

st.title("Focus Marketing Consultant - Billing Software")

st.markdown("---")

# -----------------------------------
# SESSION STATE
# -----------------------------------

if "invoice_items" not in st.session_state:
    st.session_state.invoice_items = []

# -----------------------------------
# COMPANY GST PLACEHOLDER
# -----------------------------------

company_gst_number = "GSTIN: 29AHHPP6093J1ZN"

# -----------------------------------
# INVOICE DETAILS
# -----------------------------------

col1, col2 = st.columns(2)

with col1:

    invoice_number = st.text_input(
        "Invoice Number",
        value=f"INV-{datetime.now().strftime('%Y%m%d%H%M')}"
    )

    client_name = st.text_input("Client Name")

    company_name = st.text_input("Company Name")

    client_address = st.text_area("Client Address")

    client_gst = st.text_input(
        "Client GST Number (Optional)"
    )

with col2:

    invoice_date = st.date_input("Invoice Date")

    payment_mode = st.selectbox(
        "Payment Mode",
        ["Cash", "UPI", "Bank Transfer", "Card"]
    )

    gst_percentage = st.number_input(
        "GST %",
        min_value=0.0,
        value=18.0
    )

    remarks = st.text_area("Remarks")

# -----------------------------------
# SERVICES SECTION
# -----------------------------------

st.markdown("## Services")

with st.form("service_form"):

    col1, col2, col3 = st.columns(3)

    with col1:
        description = st.text_input(
            "Service Description"
        )

    with col2:
        quantity = st.number_input(
            "Quantity",
            min_value=1,
            value=1
        )

    with col3:
        rate = st.number_input(
            "Rate",
            min_value=0.0,
            value=0.0
        )

    add_service = st.form_submit_button(
        "Add Service"
    )

    if add_service:

        if description.strip() == "":
            st.warning(
                "Please enter service description"
            )

        else:

            amount = quantity * rate

            st.session_state.invoice_items.append({
                "Description": description,
                "Quantity": quantity,
                "Rate": rate,
                "Amount": amount
            })

            st.success(
                "Service Added Successfully"
            )

# -----------------------------------
# DISPLAY SERVICES
# -----------------------------------

if len(st.session_state.invoice_items) > 0:

    df = pd.DataFrame(
        st.session_state.invoice_items
    )

    st.markdown("### Added Services")

    # Display Table
    st.dataframe(
        df,
        use_container_width=True
    )

    # -----------------------------------
    # REMOVE SERVICE
    # -----------------------------------

    st.markdown("### Remove Service")

    remove_options = [
        f"{idx + 1}. {item['Description']}"
        for idx, item in enumerate(
            st.session_state.invoice_items
        )
    ]

    selected_item = st.selectbox(
        "Select Service to Remove",
        remove_options
    )

    if st.button("Remove Selected Service"):

        selected_index = remove_options.index(
            selected_item
        )

        st.session_state.invoice_items.pop(
            selected_index
        )

        st.success(
            "Service Removed Successfully"
        )

        st.rerun()

    # -----------------------------------
    # CALCULATIONS
    # -----------------------------------

    subtotal = df["Amount"].sum()

    gst_amount = subtotal * (
        gst_percentage / 100
    )

    total_amount = subtotal + gst_amount

    # -----------------------------------
    # SUMMARY
    # -----------------------------------

    st.markdown("---")

    st.subheader("Invoice Summary")

    col1, col2, col3 = st.columns(3)

    with col1:
        st.metric(
            "Subtotal",
            f"₹ {subtotal:,.2f}"
        )

    with col2:
        st.metric(
            "GST",
            f"₹ {gst_amount:,.2f}"
        )

    with col3:
        st.metric(
            "Total Amount",
            f"₹ {total_amount:,.2f}"
        )

    # -----------------------------------
    # GENERATE DOCX
    # -----------------------------------

    if st.button("Generate Invoice DOCX"):

        doc = Document()

        # -----------------------------------
        # HEADER
        # -----------------------------------

        heading = doc.add_heading(
            "FOCUS MARKETING CONSULTANT",
            level=1
        )

        heading.alignment = 1

        title = doc.add_paragraph()

        title.add_run(
            "INVOICE / BILL"
        ).bold = True

        # -----------------------------------
        # COMPANY DETAILS
        # -----------------------------------

        doc.add_paragraph(
            "Focus Marketing Consultant"
        )

        doc.add_paragraph(
            company_gst_number
        )

        # -----------------------------------
        # INVOICE DETAILS
        # -----------------------------------

        doc.add_paragraph(
            f"Invoice Number: {invoice_number}"
        )

        doc.add_paragraph(
            f"Invoice Date: {invoice_date}"
        )

        # -----------------------------------
        # CLIENT DETAILS
        # -----------------------------------

        doc.add_heading(
            "Client Details",
            level=2
        )

        doc.add_paragraph(
            f"Client Name: {client_name}"
        )

        doc.add_paragraph(
            f"Company Name: {company_name}"
        )

        doc.add_paragraph(
            f"Address: {client_address}"
        )

        if client_gst.strip() != "":

            doc.add_paragraph(
                f"Client GST Number: {client_gst}"
            )

        # -----------------------------------
        # SERVICES TABLE
        # -----------------------------------

        doc.add_heading(
            "Services",
            level=2
        )

        table = doc.add_table(
            rows=1,
            cols=5
        )

        table.style = "Table Grid"

        hdr_cells = table.rows[0].cells

        hdr_cells[0].text = "Sl No"
        hdr_cells[1].text = "Description"
        hdr_cells[2].text = "Quantity"
        hdr_cells[3].text = "Rate"
        hdr_cells[4].text = "Amount"

        for idx, item in enumerate(
            st.session_state.invoice_items,
            start=1
        ):

            row_cells = table.add_row().cells

            row_cells[0].text = str(idx)

            row_cells[1].text = item["Description"]

            row_cells[2].text = str(item["Quantity"])

            row_cells[3].text = (
                f"₹ {item['Rate']:,.2f}"
            )

            row_cells[4].text = (
                f"₹ {item['Amount']:,.2f}"
            )

        # -----------------------------------
        # TOTALS
        # -----------------------------------

        doc.add_paragraph("")

        doc.add_paragraph(
            f"Subtotal: ₹ {subtotal:,.2f}"
        )

        doc.add_paragraph(
            f"GST ({gst_percentage}%): ₹ {gst_amount:,.2f}"
        )

        doc.add_paragraph(
            f"Total Amount: ₹ {total_amount:,.2f}"
        )

        # -----------------------------------
        # PAYMENT DETAILS
        # -----------------------------------

        doc.add_paragraph(
            f"Payment Mode: {payment_mode}"
        )

        doc.add_paragraph(
            f"Remarks: {remarks}"
        )

        # -----------------------------------
        # SIGNATURE
        # -----------------------------------

        doc.add_paragraph("\n")

        doc.add_paragraph(
            "Authorized Signature"
        )

        # -----------------------------------
        # SAVE DOCX
        # -----------------------------------

        buffer = io.BytesIO()

        doc.save(buffer)

        buffer.seek(0)

        st.success(
            "Invoice Generated Successfully"
        )

        st.download_button(
            label="Download Invoice DOCX",
            data=buffer,
            file_name=f"{invoice_number}.docx",
            mime="application/vnd.openxmlformats-officedocument.wordprocessingml.document"
        )

else:

    st.info(
        "Add services to generate invoice."
    )
