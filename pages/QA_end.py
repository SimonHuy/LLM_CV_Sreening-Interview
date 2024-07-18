import streamlit as st
from fpdf import FPDF

st.title("Your answer are saved")
st.subheader("Our team will contact you shortly")
st.subheader("Have a nice day!")


def txt_to_pdf(txt_file, pdf_file):
    # Create instance of FPDF class
    pdf = FPDF()

    # Add a page
    pdf.add_page()

    # Set font
    pdf.set_font("Arial", size=12)

    # Read text file
    with open(txt_file, 'r') as file:
        lines = file.readlines()

    # Add text to PDF
    for line in lines:
        pdf.cell(200, 10, txt=line, ln=True, align='L')

    # Save the PDF with name .pdf
    pdf.output(pdf_file)

# Define path of the files
txt_file = 'report.txt'
pdf_file = 'report.pdf'

# Exit button
if st.button("Exit"):
    txt_to_pdf(txt_file, pdf_file)
    st.stop()