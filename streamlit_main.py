# Define each page
dashboard_page = st.Page("pages/alerts.py", title="Alerts", icon="📊")
settings_page = st.Page("pages/settings.py", title="Watchlist Settings", icon="⚙️")

# Create Navigation
pg = st.navigation({
    "Main Operations": [dashboard_page],
    "Configuration": [settings_page]
})

# Sidebar branding (Visible on ALL pages)
st.sidebar.title("🛡️ CyberGuard SOC")
st.sidebar.info("Monitoring Uzbekistan Telegram Segments")

# Run the navigation
pg.run()