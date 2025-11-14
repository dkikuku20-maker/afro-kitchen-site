import streamlit as st

st.title(" Order & Delivery")

st.write(
    "Place an order request below. We confirm pickup/delivery through Instagram DM."
)

st.divider()

menu_items = [
    "MANDAZI MEDIUM PLATTER — $50",
    "MANDAZI LARGE PLATTER — $100",
    "BEIGNETS MEDIUM PLATTER — $50",
    "BEIGNETS LARGE PLATTER — $100",
    "AFRICAN WAFFLES MEDIUM PLATTER — $80",
    "AFRICAN WAFFLES LARGE PLATTER — $120",
    "SAMBUSA (4 pieces) — $10",
    "CHAPATI — $10",
]

with st.form("order_form"):
    st.subheader("📝 Order Details")

    item = st.selectbox("Choose an item", menu_items)
    quantity = st.number_input("Quantity", min_value=1, max_value=50, value=1, step=1)

    st.subheader("🚚 Pickup or Delivery")
    order_type = st.radio("Order type", ["Pickup", "Delivery"])

    name = st.text_input("Your name")
    contact = st.text_input("Phone number or Instagram handle")
    address = ""
    if order_type == "Delivery":
        address = st.text_area("Delivery address (Edmonton only)")

    notes = st.text_area("Extra notes (optional)", "")

    submitted = st.form_submit_button("Submit order request")

if submitted:
    st.success("Order received! Please DM us on Instagram @afrokitchen_flavour to confirm.")
    st.write("### Order Summary")
    st.write(f"**Item:** {item}")
    st.write(f"**Quantity:** {quantity}")
    st.write(f"**Type:** {order_type}")
    st.write(f"**Name:** {name}")
    st.write(f"**Contact:** {contact}")
    if order_type == "Delivery":
        st.write(f"**Address:** {address}")
    if notes:
        st.write(f"**Notes:** {notes}")
