# app.py
import streamlit as st
from main import build_proposal
import dotenv

# Load your .env keys
dotenv.load_dotenv()

st.set_page_config(page_title="AI Use-Case Generator", page_icon="🚀")

st.title("🚀 AI Use-Case Generator for Companies & Industries")

# Text input for company/industry
company = st.text_input("Enter Company or Industry:")

if st.button("Generate Proposal"):
    if company:
        with st.spinner("Researching and generating use cases... 🔍"):
            proposal_md = build_proposal(company)
        
        st.success("✅ Proposal Generated Successfully!")
        
        # Display generated proposal
        st.markdown(proposal_md)
        
        # Allow download
        st.download_button(
            label="📥 Download Proposal as .md",
            data=proposal_md,
            file_name=f"{company.lower().replace(' ', '_')}_proposal.md",
            mime="text/markdown"
        )
    else:
        st.warning("⚠️ Please enter a company or industry name.")
