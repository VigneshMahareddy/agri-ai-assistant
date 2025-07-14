import streamlit as st
from transformers import AutoTokenizer, AutoModelForCausalLM, pipeline, logging as hf_logging
import torch

# Silence unnecessary warnings
hf_logging.set_verbosity_error()

# App Config
st.set_page_config(page_title="AI Agri Assistant 🌾", page_icon="🌿", layout="centered")

@st.cache_resource
def load_model():
    hf_token = st.secrets["HF_TOKEN"]
    model_id = "TinyLlama/TinyLlama-1.1B-Chat-v1.0"

    tokenizer = AutoTokenizer.from_pretrained(model_id, use_auth_token=hf_token)
    model = AutoModelForCausalLM.from_pretrained(
        model_id,
        use_auth_token=hf_token,
        torch_dtype=torch.float32,
        device_map=None
    )
    model.to("cpu")

    return pipeline("text-generation", model=model, tokenizer=tokenizer, device=-1)

generator = load_model()

# --- UI Layout ---
st.markdown("""
    <h1 style='text-align: center; color: #2E7D32;'>🌾 AI Agri Assistant</h1>
    <p style='text-align: center;'>Ask agriculture-related questions and get instant AI-powered answers! 🧠🌱</p>
    <hr style="border:1px solid #ccc;">
""", unsafe_allow_html=True)

with st.container():
    st.subheader("📝 Enter your question:")
    question = st.text_area("", placeholder="E.g., What is the best fertilizer for tomatoes?", height=100)

    col1, col2, col3 = st.columns([1, 2, 1])
    with col2:
        if st.button("🚀 Generate Answer", use_container_width=True):
            if not question.strip():
                st.warning("⚠️ Please enter a valid question.")
            else:
                with st.spinner("🧠 Thinking..."):
                    result = generator(question, max_new_tokens=100)[0]["generated_text"]
                    answer = result[len(question):].strip()

                st.markdown("### ✅ Answer:")
                st.success(answer)

st.markdown("---")
st.markdown(
    "<p style='text-align: center; font-size: 13px; color: gray;'>Made with ❤️ using Streamlit & TinyLLaMA</p>",
    unsafe_allow_html=True
)
