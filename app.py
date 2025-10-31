import streamlit as st
import pandas as pd



st.set_page_config(page_title="Tax Calculator AI", page_icon="💰", layout="centered")

st.markdown("""
    <style>
        /* Background Gradient */
        [data-testid="stAppViewContainer"] {
            background: linear-gradient(135deg, #0f2027, #203a43, #2c5364);
            color: white;
        }

        /* Title Style */
        .title {
            font-size: 45px;
            text-align: center;
            font-weight: 900;
            color: #00ffc3;
            text-shadow: 0px 0px 15px #00ffc3;
            letter-spacing: 1px;
        }

        /* Subtitle */
        .subtitle {
            text-align: center;
            font-size: 18px;
            color: #d3d3d3;
        }

        /* Table Style */
        table {
            width: 100%;
            border-collapse: collapse;
            border-radius: 12px;
            overflow: hidden;
            box-shadow: 0 0 20px rgba(0,255,200,0.25);
            margin-top: 20px;
        }

        thead th {
            background-color: #00ffc3;
            color: #000;
            text-align: center;
            padding: 12px;
            font-size: 18px;
            font-weight: 800;
            text-transform: uppercase;
            letter-spacing: 0.5px;
            border-bottom: 3px solid #00bfa5;
        }

        tbody tr {
            background-color: rgba(255, 255, 255, 0.05);
            border-bottom: 1px solid rgba(255,255,255,0.1);
        }

        tbody tr:hover {
            background-color: rgba(0, 255, 200, 0.15);
            transition: 0.3s;
        }

        td {
            text-align: center;
            padding: 12px;
            font-size: 16px;
            color: #f1f1f1;
        }

        /* Footer */
        .footer {
            text-align: center;
            margin-top: 40px;
            font-size: 14px;
            color: #aaaaaa;
        }
    </style>
""", unsafe_allow_html=True)


st.markdown("<div class='title'> Tax Calculator AI</div>", unsafe_allow_html=True)
st.markdown("<div class='subtitle'>Instantly calculate your estimated tax & net income</div>", unsafe_allow_html=True)
st.markdown("---")


d = st.number_input("Enter your **Salary (₹)**", min_value=0.0, step=1000.0)
b = st.number_input("Enter your **Capital Gain Amount (₹)**", min_value=0.0, step=1000.0)
c = st.number_input("Enter your **Other Income (₹)**", min_value=0.0, step=1000.0)

if d > 0 or b > 0 or c > 0:
    a = d - 75000

 
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

    data = {
        "Category": [
            "Salary", "Salary Tax",
            "Capital Gain Amount", "Capital Gain Tax",
            "Other Income", "Other Income Tax",
            "Total Tax", "Final Amount After Tax"
        ],
        "Amount (₹)": [f"{d:,.2f}", f"{tax:,.2f}", f"{b:,.2f}", f"{cap1:,.2f}",
                       f"{c:,.2f}", f"{tax2:,.2f}", f"{total_tax:,.2f}", f"{final_amount:,.2f}"]
    }

    df = pd.DataFrame(data)

    st.success(" Tax calculation completed successfully!")

    # Display Styled Table
    st.markdown(df.to_html(index=False, escape=False), unsafe_allow_html=True)

else:
    st.info(" Please enter your income details to calculate tax.")

# Footer
st.markdown("---")
st.markdown("""
<div class='footer'>
    <b>Disclaimer:</b> This tool provides approximate tax estimations and is not official financial advice.<br>
    © 2025 | Designed & Developed by <b>Manush Giridhar</b> 
</div>
""", unsafe_allow_html=True)
