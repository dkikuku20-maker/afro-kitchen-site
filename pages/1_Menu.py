import streamlit as st

st.title(" Menu")

st.markdown("Explore our handcrafted platters and small orders.")

st.divider()
st.header("Main Dishes / Platters")

# --- Mandazi & Beignets ---
col1, col2 = st.columns(2)

with col1:
    st.markdown(
        """
        - **MANDAZI MEDIUM PLATTER** — $50  
        - **MANDAZI LARGE PLATTER** — $100  
        - **BEIGNETS MEDIUM PLATTER** — $50  
        - **BEIGNETS LARGE PLATTER** — $100  
        """
    )

with col2:
    st.image(
        "https://raw.githubusercontent.com/YOUR_USERNAME/YOUR_REPO/main/mandazi.jpg",
        caption="Mandazi / Beignets Platter",
        use_column_width=True,
    )

st.divider()
st.header("Small Orders")

c1, c2 = st.columns(2)

with c1:
    st.markdown(
        """
        - **SAMBUSA (4 pieces)** — $10  
        - **CHAPATI** — $10  
        """
    )

with c2:
    st.image(
        "https://raw.githubusercontent.com/YOUR_USERNAME/YOUR_REPO/main/sambusa.jpg",
        caption="Sambusa (4 pcs)",
        use_column_width=True,
    )

st.image(
    "https://raw.githubusercontent.com/YOUR_USERNAME/YOUR_REPO/main/chapati.jpg",
    caption="Chapati",
    use_column_width=True,
)

st.image(
    "https://raw.githubusercontent.com/YOUR_USERNAME/YOUR_REPO/main/waffles.jpg",
    caption="African Waffles",
    use_column_width=True,
)
