import streamlit as st
import pandas as pd


st.set_page_config(page_title="Tax Calculator AI", page_icon="💰", layout="centered")

st.markdown("""
    <style>
        body {
            background-color: #0e1117;
            color: white;
        }
        .title {
            font-size: 40px;
            text-align: center;
            font-weight: bold;
            color: #00FFAA;
        }
        .subtitle {
            text-align: center;
            font-size: 20px;
            color: #CCCCCC;
        }
        .footer {
            text-align: center;
            margin-top: 30px;
            font-size: 14px;
            color: #AAAAAA;
        }
        table {
            border-collapse: collapse;
            width: 100%;
        }
        th {
            background-color: #00FFAA;
            color: black;
        }
    </style>
""", unsafe_allow_html=True)

# Header
st.markdown("<div class='title'> Tax Calculator AI</div>", unsafe_allow_html=True)
st.markdown("<div class='subtitle'>Estimate your total income tax instantly</div>", unsafe_allow_html=True)
st.markdown("---")

# Inputs
d = st.number_input("Enter your **Salary (₹)**", min_value=0.0, step=1000.0)
b = st.number_input("Enter your **Capital Gain Amount (₹)**", min_value=0.0, step=1000.0)
c = st.number_input("Enter your **Other Income (₹)**", min_value=0.0, step=1000.0)

if d > 0 or b > 0 or c > 0:
    a = d - 75000

    # Salary tax calculation
    if a <= 0:
        tax = 0
    elif a < 400000:
        tax = 0
    elif a < 800000:
        tax = 0.05 * a
    elif a < 1200000:
        tax = 0.10 * a
    elif a < 1600000:
        tax = 0.15 * a
    elif a < 2000000:
        tax = 0.20 * a
    elif a < 2400000:
        tax = 0.25 * a
    else:
        tax = 0.30 * a

    # Other income tax
    if c <= 0:
        tax2 = 0
    elif c < 400000:
        tax2 = 0
    elif c < 800000:
        tax2 = 0.05 * c
    elif c < 1200000:
        tax2 = 0.10 * c
    elif c < 1600000:
        tax2 = 0.15 * c
    elif c < 2000000:
        tax2 = 0.20 * c
    elif c < 2400000:
        tax2 = 0.25 * c
    else:
        tax2 = 0.30 * c

    # Capital gain tax
    if b > 100000:
        cap = b - 100000
        cap1 = 0.20 * cap
    else:
        cap1 = 0

    total_tax = tax + cap1 + tax2
    final_amount = (d + b + c) - total_tax

    # Round to 2 decimal places
    data = {
        "Category": [
            "Salary", "Salary Tax",
            "Capital Gain Amount", "Capital Gain Tax",
            "Other Income", "Other Income Tax",
            "Total Tax", "Final Amount After Tax"
        ],
        "Amount (₹)": [round(d, 2), round(tax, 2), round(b, 2), round(cap1, 2),
                       round(c, 2), round(tax2, 2), round(total_tax, 2), round(final_amount, 2)]
    }

    df = pd.DataFrame(data)
    st.success(" Tax calculation completed successfully!")
    st.table(df)

else:
    st.info("Please enter your income details to calculate tax.")

# Footer and disclaimer
st.markdown("---")
st.markdown("""
<div class='footer'>
     <b>Disclaimer:</b> This calculator provides an approximate tax estimation and is not a substitute for professional advice.<br>
    © 2025 All Rights Reserved | Developed by <b>Manush Giridhar</b> 
</div>
""", unsafe_allow_html=True)
