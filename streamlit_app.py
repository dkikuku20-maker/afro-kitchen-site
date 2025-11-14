import streamlit as st

# -----------------------------------------
# Afro Kitchen Website (HOME PAGE)
# -----------------------------------------

st.set_page_config(
    page_title="Afro Kitchen Flavours",
    page_icon="",
    layout="wide",
)

# --- SMALL CSS BRANDING ---
st.markdown(
    """
    <style>
    .big-title {
        font-size: 3rem;
        font-weight: 800;
        letter-spacing: 0.08em;
    }
    .tagline {
        font-size: 1.1rem;
        color: #5a4634;
    }
    </style>
    """,
    unsafe_allow_html=True,
)

# --- HERO SECTION ---
col1, col2 = st.columns([3, 2])

with col1:
    st.markdown('<div class="big-title">AFRO KITCHEN FLAVOURS</div>', unsafe_allow_html=True)
    st.markdown(
        '<p class="tagline">Bold African flavours. Fresh. Local. Authentic.</p>',
        unsafe_allow_html=True,
    )
    st.write(
        "Experience the rich, vibrant flavours of Africa through our handcrafted "
        "platters, small bites, and traditional delicacies."
    )
    st.markdown("** Edmonton, Alberta · Online ordering via Instagram @afrokitchen_flavour**")

with col2:
    # Temporary placeholder image — replace this later with your real banner image
    st.image(
        "https://via.placeholder.com/600x400.png?text=Afro+Kitchen+Flavours",
        caption="Handcrafted African-inspired platters",
        use_column_width=True,
    )

st.divider()

# --- HIGHLIGHTS ---
st.subheader("Why People Love Afro Kitchen")

c1, c2, c3 = st.columns(3)

with c1:
    st.markdown("###  Homemade Taste")
    st.write("Recipes inspired by East & West African classics with a modern twist.")

with c2:
    st.markdown("###  Platters & Small Orders")
    st.write("From Mandazi platters to Sambusa, perfect for events or cozy nights in.")

with c3:
    st.markdown("###  Delivery-Friendly")
    st.write("Message us on Instagram to arrange pick-up or local delivery options.")

st.divider()

st.markdown("###  Use the left sidebar to browse the Menu, place an Order, learn About us, or Contact us.")
