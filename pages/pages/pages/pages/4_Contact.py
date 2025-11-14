import streamlit as st

st.title(" Contact & Socials")

st.markdown("""
**Location:** Edmonton, Alberta  
**Primary contact:** Instagram DM  
""")

st.divider()

st.subheader(" Instagram")

st.markdown(
    """
<a href="https://instagram.com/afrokitchen_flavour" target="_blank">
    <img src="https://img.icons8.com/?size=100&id=118497&format=png&color=000000" width="32" style="vertical-align:middle;margin-right:8px;"/>
    <span style="font-size:1.1rem; vertical-align:middle;">@afrokitchen_flavour</span>
</a>
""",
    unsafe_allow_html=True,
)

st.info("Tap the handle above to open Instagram.")
