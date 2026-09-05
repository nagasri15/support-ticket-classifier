import streamlit as st
from ticket_classifier import classify_ticket


# ============================================================
# PAGE CONFIGURATION
# ============================================================

st.set_page_config(
    page_title="Support Ticket Classifier",
    page_icon="🎫",
    layout="wide",
    initial_sidebar_state="expanded"
)


# ============================================================
# CUSTOM CSS
# ============================================================

st.markdown("""
<style>
.stApp {
    background-color: #f8f7ff;
}

.main-header {
    text-align: center;
    padding: 25px 0 20px 0;
}

.main-header h1 {
    color: #4c1d95;
    font-size: 42px;
    font-weight: 700;
    margin-bottom: 5px;
}

.main-header p {
    color: #64748b;
    font-size: 17px;
}

.input-title {
    color: #312e81;
    font-size: 20px;
    font-weight: 600;
    margin-bottom: 8px;
}

textarea {
    border: 2px solid #c7d2fe !important;
    border-radius: 12px !important;
}

.stButton > button {
    border-radius: 10px;
    border: none;
    background-color: #6366f1;
    color: white;
    font-weight: 600;
    min-height: 45px;
}

.stButton > button:hover {
    background-color: #4f46e5;
    color: white;
}

.result-box {
    background-color: white;
    border: 1px solid #c7d2fe;
    border-radius: 14px;
    padding: 25px;
    text-align: center;
    margin-top: 10px;
    box-shadow: 0 2px 8px rgba(79, 70, 229, 0.08);
}

.result-title {
    color: #475569;
    font-size: 16px;
    font-weight: 600;
    margin-bottom: 10px;
}

.result-value {
    color: #312e81;
    font-size: 24px;
    font-weight: 700;
}

.footer {
    text-align: center;
    color: #94a3b8;
    font-size: 14px;
    margin-top: 40px;
    padding: 20px;
}
</style>
""", unsafe_allow_html=True)


# ============================================================
# SIDEBAR
# ============================================================

with st.sidebar:

    st.markdown("## 🎫 Ticket Classifier")

    st.markdown("---")

    st.markdown("### 📌 About")

    st.write(
        "This application uses Natural Language Processing "
        "to automatically classify customer support tickets "
        "into different categories."
    )

    st.markdown("### 🤖 Model")

    st.write("**Linear SVM**")

    st.write("Features:")
    st.write("• Word-level TF-IDF")
    st.write("• Character-level TF-IDF")

    st.markdown("### 📂 Categories")

    categories = [
        "Billing",
        "Technical Issue",
        "Account Access",
        "Feature Request",
        "Delivery / Shipping",
        "Refund / Return",
        "General Inquiry",
        "Complaint"
    ]

    for category in categories:
        st.write(f"• {category}")

    st.markdown("---")

    st.markdown("### ⚡ Urgency")

    st.write("**High** – urgent or critical requests")
    st.write("**Medium** – problems or errors")
    st.write("**Low** – general requests or inquiries")


# ============================================================
# MAIN HEADER
# ============================================================

st.markdown(
    '<h1 style="text-align:center;color:#4c1d95;">'
    '🎫 Support Ticket Classifier'
    '</h1>',
    unsafe_allow_html=True
)

st.markdown(
    '<p style="text-align:center;color:#64748b;font-size:17px;">'
    'AI-powered customer support ticket classification'
    '</p>',
    unsafe_allow_html=True
)


# ============================================================
# TICKET INPUT
# ============================================================

st.markdown("### 📝 Enter your support ticket")

if "ticket_text" not in st.session_state:
    st.session_state.ticket_text = ""

ticket_text = st.text_area(
    "Ticket",
    value=st.session_state.ticket_text,
    height=170,
    placeholder=(
        "Example: I was charged twice for my subscription "
        "and would like a refund."
    ),
    label_visibility="collapsed"
)

st.session_state.ticket_text = ticket_text


# ============================================================
# EXAMPLE TICKETS
# ============================================================

st.markdown("### 💡 Try an example")

col1, col2, col3, col4 = st.columns(4)

with col1:
    if st.button("💳 Billing", use_container_width=True):
        st.session_state.ticket_text = (
            "I was charged twice for my subscription."
        )
        st.rerun()

with col2:
    if st.button("🔧 Technical", use_container_width=True):
        st.session_state.ticket_text = (
            "The application keeps crashing when I try to open it."
        )
        st.rerun()

with col3:
    if st.button("🔐 Account", use_container_width=True):
        st.session_state.ticket_text = (
            "I forgot my password and cannot log in."
        )
        st.rerun()

with col4:
    if st.button("📦 Delivery", use_container_width=True):
        st.session_state.ticket_text = (
            "My package has not arrived yet."
        )
        st.rerun()


# ============================================================
# CLASSIFY
# ============================================================

st.write("")

if st.button("🔍 Classify Ticket", use_container_width=True):

    ticket_text = st.session_state.ticket_text

    if not ticket_text.strip():

        st.warning(
            "Please enter a support ticket before classifying."
        )

    else:

        result = classify_ticket(ticket_text)

        category = result["category"]
        urgency = result["urgency"]

        st.markdown("### 📊 Classification Result")

        result_col1, result_col2 = st.columns(2)

        with result_col1:

            st.markdown(
                '<div class="result-box">'
                '<div class="result-title">🏷️ Ticket Category</div>'
                f'<div class="result-value">{category}</div>'
                '</div>',
                unsafe_allow_html=True
            )

        with result_col2:

            st.markdown(
                '<div class="result-box">'
                '<div class="result-title">⚡ Urgency</div>'
                f'<div class="result-value">{urgency}</div>'
                '</div>',
                unsafe_allow_html=True
            )


# ============================================================
# PROJECT HIGHLIGHTS
# ============================================================

# ============================================================
# PROJECT HIGHLIGHTS
# ============================================================
# ============================================================
# PROJECT HIGHLIGHTS
# ============================================================

st.markdown("---")

st.markdown("### ✨ Project Highlights")

highlight1, highlight2, highlight3 = st.columns(3)

with highlight1:
    st.markdown(
        """
        <div style="
            background-color: #c4b5fd;
            padding: 24px;
            border-radius: 14px;
            min-height: 155px;
        ">
            <h3 style="
                color: #000000;
                margin-top: 0;
                margin-bottom: 12px;
            ">
                🤖 AI Classification
            </h3>
            <p style="
                color: #000000;
                font-size: 15px;
                line-height: 1.5;
            ">
                Automatically categorizes customer support
                tickets into 8 different categories.
            </p>
        </div>
        """,
        unsafe_allow_html=True
    )


with highlight2:
    st.markdown(
        """
        <div style="
            background-color: #93c5fd;
            padding: 24px;
            border-radius: 14px;
            min-height: 155px;
        ">
            <h3 style="
                color: #000000;
                margin-top: 0;
                margin-bottom: 12px;
            ">
                ⚡ Urgency Detection
            </h3>
            <p style="
                color: #000000;
                font-size: 15px;
                line-height: 1.5;
            ">
                Identifies whether a ticket requires
                Low, Medium, or High priority attention.
            </p>
        </div>
        """,
        unsafe_allow_html=True
    )


with highlight3:
    st.markdown(
        """
        <div style="
            background-color: #86efac;
            padding: 24px;
            border-radius: 14px;
            min-height: 155px;
        ">
            <h3 style="
                color: #000000;
                margin-top: 0;
                margin-bottom: 12px;
            ">
                🎯 NLP Powered
            </h3>
            <p style="
                color: #000000;
                font-size: 15px;
                line-height: 1.5;
            ">
                Uses Word and Character TF-IDF features
                with a Linear SVM machine learning model.
            </p>
        </div>
        """,
        unsafe_allow_html=True
    )


# ============================================================
# FOOTER
# ============================================================

st.markdown("---")

st.caption(
    "Support Ticket Category Classifier • "
    "Built with Python, Scikit-learn & Streamlit"
)