import streamlit as st
import pandas as pd

d = st.number_input("ENTER YOUR SALARY")
b = st.number_input("ENTER YOUR CAPITAL GAIN AMOUNT")
c = st.number_input("OTHERS")

if d > 0 or b > 0 or c > 0:  # only calculate if something entered
    a = d - 75000
    if a > 0 and a < 400000:
        tax = 0
    elif a > 400000 and a < 800000:
        tax = 0.05 * a
    elif a > 800000 and a < 1200000:
        tax = 0.10 * a
    elif a > 1200000 and a < 1600000:
        tax = 0.15 * a
    elif a > 1600000 and a < 2000000:
        tax = 0.20 * a
    elif a > 2000000 and a < 2400000:
        tax = 0.25 * a
    else:
        tax = 0.30 * a if a > 0 else 0

    # OTHERS tax
    if c > 0 and c < 400000:
        tax2 = 0
    elif c > 400000 and c < 800000:
        tax2 = 0.05 * c
    elif c > 800000 and c < 1200000:
        tax2 = 0.10 * c
    elif c > 1200000 and c < 1600000:
        tax2 = 0.15 * c
    elif c > 1600000 and c < 2000000:
        tax2 = 0.20 * c
    elif c > 2000000 and c < 2400000:
        tax2 = 0.25 * c
    else:
        tax2 = 0.30 * c if c > 0 else 0

    # CAPITAL GAIN
    if b > 100000:
        cap = b - 100000
        cap1 = 0.20 * cap
    else:
        cap1 = 0

    total_tax = tax + cap1 + tax2
    final_amount = (d + b + c) - total_tax

    data = {
        "Category": [
            "SALARY", "SALARY TAX",
            "CAPITAL GAIN AMOUNT", "CAPITAL GAIN TAX",
            "OTHERS", "OTHERS TAX",
            "TOTAL TAX", "FINAL AMOUNT AFTER TAX"
        ],
        "Amount (₹)": [d, tax, b, cap1, c, tax2, total_tax, final_amount]
    }

    df = pd.DataFrame(data)
    st.table(df)
else:
    st.info("ℹ️ Please enter your income details to calculate tax.")
