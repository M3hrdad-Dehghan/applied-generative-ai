#%%
import sys
import os

sys.path.insert(0, os.path.join(os.path.dirname(__file__), "..", "src"))

import streamlit as st
from RAG_Pipeline import PIPELINE

st.set_page_config(
    page_title="RAG Assistant",
    page_icon="💬",
    layout="wide",
    initial_sidebar_state="expanded",
)

st.markdown("""
<style>
    /* Sidebar footer */
    .author-block {
        position: fixed;
        bottom: 1.5rem;
        left: 0;
        width: 18rem;
        padding: 0 1.5rem;
        font-size: 0.75rem;
        color: #555;
    }
    .author-block span {
        color: #6C63FF;
        font-weight: 600;
    }

    /* Chat input */
    .stChatInput textarea {
        background-color: #1A1A1A !important;
    }

    /* Remove top padding */
    .block-container {
        padding-top: 2rem;
    }
</style>
""", unsafe_allow_html=True)


# ── Sidebar ────────────────────────────────────────────────────────────────────
with st.sidebar:
    st.markdown("## 💬 RAG Assistant")
    st.caption("Ask questions about your indexed documents.")
    st.divider()

    # Document status
    doc_count = PIPELINE.vector_store.collection.count()
    if doc_count > 0:
        st.success(f"{doc_count} chunks indexed", icon="✅")
    else:
        st.warning("No documents indexed yet.", icon="⚠️")

    st.markdown("####")

    # Clear chat
    if st.button("🗑️  Clear Conversation", use_container_width=True):
        st.session_state.messages = []
        PIPELINE.reset_conversation()
        st.rerun()

    st.divider()
    st.markdown(
        '<div class="author-block">Built by <span>Mehrdad Mansourdehghan</span></div>',
        unsafe_allow_html=True,
    )


# ── Chat area ──────────────────────────────────────────────────────────────────
st.markdown("### Ask your documents")

if "messages" not in st.session_state:
    st.session_state.messages = []

# Render history
for msg in st.session_state.messages:
    with st.chat_message(msg["role"]):
        st.markdown(msg["content"])

# New input
if prompt := st.chat_input("Type your question here…"):
    st.session_state.messages.append({"role": "user", "content": prompt})
    with st.chat_message("user"):
        st.markdown(prompt)

    with st.chat_message("assistant"):
        with st.spinner("Thinking…"):
            reply = PIPELINE.query(prompt)
        st.markdown(reply)

    st.session_state.messages.append({"role": "assistant", "content": reply})
