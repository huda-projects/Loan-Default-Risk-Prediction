```python
import streamlit as st

st.set_page_config(
    page_title="Loan Default Risk Predictor",
    page_icon="🏦",
    layout="wide"
)

# Page styling
st.markdown("""
<style>
.stApp {
    background-color: #F5F7FB;
}
.header-box {
    background-color: #142C4E;
    padding: 28px;
    border-radius: 12px;
    color: white;
    margin-bottom: 24px;
}
.header-box h1 {
    color: white;
}
.header-box p {
    color: #D7E4F3;
}
</style>
""", unsafe_allow_html=True)

# Header
st.markdown("""
<div class="header-box">
    <h1>🏦 Loan Default Risk Predictor</h1>
    <p>Explore loan default risk using machine learning.</p>
</div>
""", unsafe_allow_html=True)

st.subheader("Try a prediction")
st.write("Enter the loan and applicant details below.")

# Input form
with st.form("loan_form"):
    st.markdown("### Loan details")
    col1, col2, col3 = st.columns(3)

    with col1:
        loan_amount = st.number_input("Loan amount", min_value=0.0, value=200000.0)
        term = st.number_input("Loan term", min_value=0, value=360)
        property_value = st.number_input("Property value", min_value=0.0, value=250000.0)
        total_units = st.selectbox("Total units", [1, 2, 3, 4])

    with col2:
        loan_limit = st.selectbox("Loan limit", ["cf", "ncf"])
        loan_type = st.selectbox("Loan type", ["type1", "type2", "type3"])
        loan_purpose = st.selectbox("Loan purpose", ["p1", "p2", "p3", "p4"])
        occupancy_type = st.selectbox("Occupancy type", ["pr", "sr", "ir"])

    with col3:
        approv_in_adv = st.selectbox("Approval in advance", ["pre", "nopre"])
        Credit_Worthiness = st.selectbox("Credit worthiness", ["l1", "l2"])
        credit_type = st.selectbox("Credit type", ["CIB", "CRIF", "EQUI", "EXP"])
        Credit_Score = st.number_input("Credit score", min_value=0, max_value=1000, value=700)

    st.markdown("### Applicant details")
    col4, col5, col6 = st.columns(3)

    with col4:
        Gender = st.selectbox("Gender", ["Male", "Female", "Joint", "Sex Not Available"])
        age = st.selectbox("Age group", ["25-34", "35-44", "45-54", "55-64", "65-74", "75-84", "55-64"])
        income = st.number_input("Annual income", min_value=0.0, value=50000.0)
        co_applicant_credit_type = st.selectbox(
            "Co-applicant credit type", ["CIB", "EXP"]
        )

    with col5:
        LTV = st.number_input("Loan-to-value ratio (LTV)", min_value=0.0, value=80.0)
        dtir1 = st.number_input("Debt-to-income ratio", min_value=0.0, value=35.0)
        Region = st.selectbox("Region", ["North", "South", "Central", "North-East"])

    with col6:
        open_credit = st.selectbox("Open credit", ["open_credit", "nopc"])
        business_or_commercial = st.selectbox(
            "Business or commercial", ["business", "nob/c"]
        )
        Neg_ammortization = st.selectbox("Negative amortization", ["not_neg", "neg_amm"])
        interest_only = st.selectbox("Interest only", ["not_int", "int_only"])

    st.markdown("### Additional loan settings")
    col7, col8, col9 = st.columns(3)

    with col7:
        lump_sum_payment = st.selectbox("Lump sum payment", ["not_lpsm", "lpsm"])
        submission_of_application = st.selectbox(
            "Application submission", ["to_inst", "not_inst"]
        )

    with col8:
        Credit_Worthiness = st.selectbox(
            "Credit worthiness (confirm)", ["l1", "l2"]
        )
        Neg_ammortization = st.selectbox(
            "Negative amortization (confirm)", ["not_neg", "neg_amm"]
        )

    with col9:
        interest_only = st.selectbox(
            "Interest only (confirm)", ["not_int", "int_only"]
        )
        loan_limit = st.selectbox("Loan limit (confirm)", ["cf", "ncf"])

    submitted = st.form_submit_button("✨ Predict Default Risk")

if submitted:
    st.info("Your inputs are captured. The trained model will be connected in the next step.")

st.caption(
    "Educational demonstration only. Predictions should not be used as the sole basis for lending decisions."
)
```
