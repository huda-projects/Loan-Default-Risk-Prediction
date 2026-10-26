import streamlit as st
import os
import joblib
from huggingface_hub import hf_hub_download

@st.cache_resource
def load_model():
    model_path = hf_hub_download(
        repo_id="halsaud/loan-default-risk-model",
        filename="random_forest_model.joblib",
        token=st.secrets["HF_TOKEN"]
    )
    return joblib.load(model_path)

model = load_model()

st.set_page_config(
    page_title="Loan Default Risk Predictor",
    page_icon="🏦",
    layout="wide"
)

st.markdown("""
<style>
.stApp { background-color: #F5F7FB; }
.header-box {
    background-color: #142C4E;
    padding: 28px;
    border-radius: 12px;
    color: white;
    margin-bottom: 24px;
}
.header-box h1 { color: white; }
.header-box p { color: #D7E4F3; }
</style>
""", unsafe_allow_html=True)

st.markdown("""
<div class="header-box">
    <h1>🏦 Loan Default Risk Predictor</h1>
    <p>Explore loan default risk using machine learning.</p>
</div>
""", unsafe_allow_html=True)

st.subheader("Try a prediction")
st.write("Enter the loan and applicant details below.")

with st.form("loan_form"):
    st.markdown("### Loan details")
    c1, c2, c3 = st.columns(3)

    with c1:
        loan_limit = st.selectbox("Loan limit", ["cf", "ncf"])
        loan_type = st.selectbox("Loan type", ["type1", "type2", "type3"])
        loan_purpose = st.selectbox("Loan purpose", ["p1", "p2", "p3", "p4"])
        loan_amount = st.number_input("Loan amount", min_value=0.0, value=200000.0)
        term = st.number_input("Loan term", min_value=0, value=360)

    with c2:
        approv_in_adv = st.selectbox("Approval in advance", ["nopre", "pre"])
        Credit_Worthiness = st.selectbox("Credit worthiness", ["l1", "l2"])
        property_value = st.number_input("Property value", min_value=0.0, value=250000.0)
        total_units = st.selectbox("Total units", ["1U", "2U", "3U", "4U"])
        occupancy_type = st.selectbox("Occupancy type", ["pr", "ir", "sr"])

    with c3:
        open_credit = st.selectbox("Open credit", ["nopc", "opc"])
        business_or_commercial = st.selectbox("Business or commercial", ["nob/c", "b/c"])
        credit_type = st.selectbox("Credit type", ["CIB", "EXP", "CRIF", "EQUI"])
        Credit_Score = st.number_input("Credit score", min_value=0, max_value=1000, value=700)

    st.markdown("### Applicant details")
    c4, c5, c6 = st.columns(3)

    with c4:
        Gender = st.selectbox("Gender", ["Joint", "Female", "Male", "Sex Not Available"])
        age = st.selectbox("Age group", ["<25", "25-34", "35-44", "45-54", "55-64", "65-74", ">74"])
        income = st.number_input("Income", min_value=0.0, value=50000.0)
        Region = st.selectbox("Region", ["central", "North", "south", "North-East"])

    with c5:
        Neg_ammortization = st.selectbox("Negative amortization", ["not_neg", "neg_amm"])
        interest_only = st.selectbox("Interest only", ["not_int", "int_only"])
        lump_sum_payment = st.selectbox("Lump sum payment", ["not_lpsm", "lpsm"])
        co_applicant_credit_type = st.selectbox("Co-applicant credit type", ["EXP", "CIB"])

    with c6:
        submission_of_application = st.selectbox(
            "Application submission", ["not_inst", "to_inst"]
        )
        LTV = st.number_input("Loan-to-value ratio (LTV)", min_value=0.0, value=80.0)
        dtir1 = st.number_input("Debt-to-income ratio", min_value=0.0, value=35.0)

    submitted = st.form_submit_button("✨ Predict Default Risk")

if submitted:
    st.info("Input form is ready. The trained model will be connected next.")

st.caption("Educational demonstration only — not a lending decision tool.")
