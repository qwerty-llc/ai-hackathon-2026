import streamlit as st
from supabase import create_client
from os import environ


# 1. Connect to your Database
url = environ.get("SUPABASE_URL")
key = environ.get("SUPABASE_KEY")

supabase = create_client(url, key)

st.set_page_config(page_title="CyberGuard SOC", layout="wide")

# 2. Header & Branding
st.title("🛡️ CyberGuard: Uzbekistan OSINT Command Center")
st.markdown("Real-time AI Monitoring for Public Safety")


# 3. Fetch Data from Supabase
def fetch_data():
    response = (
        supabase.table("alert_test")
        .select("*")
        .order("created_at", desc=True)
        .execute()
    )
    return response.data


data = fetch_data()

# 4. Top Level Metrics (The "Wow" Stats)
col1, col2, col3 = st.columns(3)
with col1:
    st.metric("Total Messages Analyzed", len(data))
with col2:
    high_risk = len([x for x in data if x["risk_score"] >= 8])
    st.metric("High Risk Threats", high_risk, delta_color="inverse")
with col3:
    st.metric("System Status", "Active / Monitoring", delta="Live")

# 5. The Threat Table
st.subheader("🚨 Live Intelligence Feed")
st.dataframe(data, use_container_width=True)

# 6. Sidebar for Admin Control
with st.sidebar:
    st.header("Admin Controls")
    if st.button("Refresh Data"):
        st.rerun()
    st.write("Monitoring: Telegram (Active)")
    st.write("AI Model: Gemini 1.5 Flash")
