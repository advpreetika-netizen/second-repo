import streamlit as st
from pathlib import Path

st.set_page_config(
    page_title="Pheran Valley | Kashmiri Pherans",
    page_icon="🧣",
    layout="wide",
    initial_sidebar_state="expanded",
)

APP_DIR = Path(__file__).parent
ASSETS_DIR = APP_DIR / "assets"

KASHMIR_BG_GRADIENT = """
<style>
body {
  background: radial-gradient(circle at top, #1b233b 0, #050610 55%, #020109 100%) !important;
}
section.main > div {
  padding-top: 1rem;
}
.pv-title {
  font-family: system-ui, -apple-system, BlinkMacSystemFont, "Segoe UI", sans-serif;
  letter-spacing: 0.08em;
  text-transform: uppercase;
  font-size: 0.8rem;
  color: #fbd38d;
}
.pv-hosted {
  font-size: 0.75rem;
  color: #a3a6c0;
}
.block-container {
  padding-top: 1.5rem;
  padding-bottom: 2rem;
}
.pv-card {
  border-radius: 1.1rem;
  border: 1px solid rgba(255,255,255,0.12);
  background: radial-gradient(circle at top left, rgba(224,167,90,0.12), rgba(5,7,24,0.98));
  box-shadow: 0 24px 60px rgba(0,0,0,0.55);
  padding: 1.1rem 1.2rem;
}
.pv-kashmir-tag {
  display: inline-flex;
  align-items: center;
  gap: 0.3rem;
  padding: 0.2rem 0.7rem;
  border-radius: 999px;
  font-size: 0.7rem;
  border: 1px solid rgba(251,211,141,0.45);
  background: rgba(251,211,141,0.09);
  color: #fbd38d;
}
.pv-muted {
  color: #a3a6c0;
  font-size: 0.85rem;
}
.pv-price {
  font-weight: 600;
  font-size: 1rem;
}
</style>
"""

st.markdown(KASHMIR_BG_GRADIENT, unsafe_allow_html=True)

header_col1, header_col2 = st.columns([3, 1], gap="small")
with header_col1:
    st.markdown('<div class="pv-title">PHERAN VALLEY</div>', unsafe_allow_html=True)
    st.markdown(
        "### Warmth from Kashmir, woven for you  \n"
        '<span class="pv-hosted">Handcrafted pherans · Hosted by <strong>Preetika Thakur</strong></span>',
        unsafe_allow_html=True,
    )
with header_col2:
    st.markdown(
        '<div style="text-align:right;margin-top:0.45rem">'
        '<span class="pv-kashmir-tag">❄️ Srinagar · Dal Lake · Zabarwan</span>'
        "</div>",
        unsafe_allow_html=True,
    )

st.write("")

tab_home, tab_catalog, tab_order, tab_about = st.tabs(
    ["🏔️ Home", "🧣 Pheran Gallery", "📦 Order Request", "ℹ️ About & Contact"]
)

with tab_home:
    left, right = st.columns([1.3, 1], gap="large")
    with left:
        st.markdown(
            '<div class="pv-card">',
            unsafe_allow_html=True,
        )
        st.markdown(
            "#### Handpicked Pherans from the Valleys of Kashmir  \n"
            '<span class="pv-muted">'
            "Each pheran is curated from local artisans around Srinagar – from the narrow lanes of old city "
            "to the houseboats of Dal Lake. Choose from classic wool, modern pashmina-style, and richly embroidered "
            "heritage pieces."
            "</span>",
            unsafe_allow_html=True,
        )
        st.write("")
        st.markdown(
            "- ✅ Authentic Kashmiri craftsmanship  \n"
            "- ✅ Warm, comfortable winter wear  \n"
            "- ✅ Personal assistance over call / WhatsApp before dispatch",
        )
        st.write("")
        st.info(
            "This is a demo ordering portal. Once you submit an order request, "
            "the seller can contact you to confirm payment and delivery details."
        )
        st.markdown("</div>", unsafe_allow_html=True)

    with right:
        st.markdown('<div class="pv-card">', unsafe_allow_html=True)
        st.markdown("##### Kashmir Moodboard")
        mood1, mood2 = st.columns(2)
        for idx, col in enumerate((mood1, mood2), start=1):
            with col:
                img_path = ASSETS_DIR / f"sample-pheran-{idx}.jpg"
                if img_path.exists():
                    st.image(str(img_path), use_column_width=True, caption=f"Curated Pheran Look {idx}")
                else:
                    st.image(
                        "https://images.pexels.com/photos/1322001/pexels-photo-1322001.jpeg?auto=compress&cs=tinysrgb&w=800",
                        use_column_width=True,
                        caption=f"Kashmir inspiration {idx}",
                    )
        st.caption("Photo inspirations for colors, textures, and embroidery. Actual products may vary.")
        st.markdown("</div>", unsafe_allow_html=True)


PRODUCTS = [
    {
        "name": "Classic Kashmiri Wool Pheran",
        "desc": "Traditional pheran with fine Sozni-style motifs along the neck and sleeves.",
        "price": 3200,
        "asset": "sample-pheran-1.jpg",
    },
    {
        "name": "Modern Pashmina-Blend Pheran",
        "desc": "Lightweight, soft drape with contemporary cut and subtle embroidery.",
        "price": 4500,
        "asset": "sample-pheran-2.jpg",
    },
    {
        "name": "Heritage Hand-Embroidered Pheran",
        "desc": "Statement pheran with dense hand embroidery, perfect for winter weddings.",
        "price": 5200,
        "asset": "sample-pheran-3.jpg",
    },
]

with tab_catalog:
    st.markdown('<div class="pv-card">', unsafe_allow_html=True)
    st.subheader("Featured Pherans")
    st.markdown(
        '<p class="pv-muted">Browse a small curated set of pherans inspired by the colors of Kashmir. '
        "The seller can update these designs in code or by changing the images.</p>",
        unsafe_allow_html=True,
    )
    st.write("")

    cols = st.columns(3)
    for product, col in zip(PRODUCTS, cols):
        with col:
            img_path = ASSETS_DIR / product["asset"]
            if img_path.exists():
                st.image(str(img_path), use_column_width=True)
            else:
                st.image(
                    "https://images.pexels.com/photos/1322000/pexels-photo-1322000.jpeg?auto=compress&cs=tinysrgb&w=800",
                    use_column_width=True,
                )
            st.markdown(f"**{product['name']}**")
            st.markdown(f'<span class="pv-price">₹{product["price"]}</span>', unsafe_allow_html=True)
            st.caption(product["desc"])
            st.write("")

    st.markdown("</div>", unsafe_allow_html=True)


with tab_order:
    st.markdown('<div class="pv-card">', unsafe_allow_html=True)
    st.subheader("Place an Order Request")
    st.markdown(
        '<p class="pv-muted">'
        "Fill in your details below. This demo app will show you a summary of your order instead of processing "
        "real payment. In a real deployment, this could send an email or connect to WhatsApp."
        "</p>",
        unsafe_allow_html=True,
    )
    st.write("")

    with st.form("order_form"):
        col_a, col_b = st.columns(2)
        with col_a:
            product_names = [p["name"] for p in PRODUCTS]
            product_choice = st.selectbox("Select Pheran", ["Choose from catalog"] + product_names)
            size = st.selectbox("Size", ["S", "M", "L", "XL", "Custom measurements"])
            quantity = st.number_input("Quantity", min_value=1, max_value=10, value=1, step=1)
            preferences = st.text_area(
                "Color / Embroidery Preference",
                placeholder="E.g. deep maroon with gold embroidery, minimal motifs",
                height=80,
            )

        with col_b:
            customer_name = st.text_input("Full Name")
            phone = st.text_input("Phone / WhatsApp Number")
            email = st.text_input("Email (optional)")
            address = st.text_area(
                "Full Address",
                placeholder="House / Street, Area, City, State, Pincode",
                height=80,
            )

        st.write("")
        payment_method = st.radio(
            "Preferred Payment Method (to be arranged after confirmation)",
            ["Cash on Delivery (COD)", "UPI (GPay / PhonePe / Paytm)", "Card (secure link)"],
        )
        notes = st.text_area("Additional Notes", placeholder="Any delivery instructions, occasion, gift wrap etc.")

        submitted = st.form_submit_button("Submit Order Request")

        if submitted:
            missing = []
            if product_choice == "Choose from catalog":
                missing.append("Pheran selection")
            if not customer_name:
                missing.append("Full Name")
            if not phone:
                missing.append("Phone / WhatsApp")
            if not address:
                missing.append("Address")

            if missing:
                st.error("Please fill: " + ", ".join(missing))
            else:
                st.success("Order request captured (demo). See summary below.")
                st.write("---")
                st.markdown("#### Order Summary")
                st.markdown(f"- **Pheran**: {product_choice}")
                st.markdown(f"- **Size**: {size} · **Qty**: {quantity}")
                st.markdown(f"- **Preferences**: {preferences or '—'}")
                st.markdown(f"- **Name**: {customer_name}")
                st.markdown(f"- **Phone**: {phone}")
                st.markdown(f"- **Email**: {email or '—'}")
                st.markdown(f"- **Address**: {address}")
                st.markdown(f"- **Payment**: {payment_method}")
                st.markdown(f"- **Notes**: {notes or '—'}")

                st.info(
                    "In a production deployment, this data could be emailed to the seller or sent via a WhatsApp API. "
                    "For now, you can copy this summary and share it manually."
                )

    st.markdown("</div>", unsafe_allow_html=True)


with tab_about:
    st.markdown('<div class="pv-card">', unsafe_allow_html=True)
    st.subheader("About Pheran Valley")
    st.markdown(
        '<p class="pv-muted">'
        "Pheran Valley is a boutique idea that connects you to the warmth and culture of Kashmir through its iconic "
        "pherans. Each piece is chosen with care, keeping in mind comfort, embroidery finesse, and how it makes you feel "
        "on a snowy morning or a misty hill station evening."
        "</p>",
        unsafe_allow_html=True,
    )
    st.write("")
    col_info, col_contact = st.columns(2)
    with col_info:
        st.markdown("##### Why People Love Pherans")
        st.markdown(
            "- Long, cozy silhouette perfect for winter\n"
            "- Beautiful neck and sleeve work inspired by old Srinagar lanes\n"
            "- Can be styled casually or for weddings and festivals\n"
            "- A reminder of the valleys, chinars, and houseboats of Kashmir",
        )
    with col_contact:
        st.markdown("##### Contact (example)")
        st.markdown(
            "- **WhatsApp / Phone**: `+91-XXXXXXXXXX`\n"
            "- **Email**: `hello@pheranvalley.com`\n"
            "- **Instagram**: `@pheranvalley`",
        )
        st.info(
            "Replace these contact details with your real ones before sharing this app with customers."
        )

    st.markdown("</div>", unsafe_allow_html=True)


