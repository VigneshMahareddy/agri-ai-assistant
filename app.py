import streamlit as st
from transformers import AutoModelForCausalLM, AutoTokenizer
import torch
import os

# ✅ Set page config
st.set_page_config(page_title="Agri Assistant", page_icon="🌾")

# ✅ Set device (GPU if available, else CPU)
device = torch.device("cuda" if torch.cuda.is_available() else "cpu")

# ✅ Load model and tokenizer with Hugging Face token
@st.cache_resource
def load_model():
    model_id = "TinyLlama/TinyLlama-1.1B-Chat-v1.0"
    hf_token = os.getenv("HF_TOKEN")  # Load from Streamlit secrets
    tokenizer = AutoTokenizer.from_pretrained(model_id, token=hf_token)
    model = AutoModelForCausalLM.from_pretrained(model_id, token=hf_token, torch_dtype=torch.float32).to(device)
    return tokenizer, model

tokenizer, model = load_model()

# ✅ Streamlit UI
st.title("🌾 Agriculture AI Assistant (TinyLLaMA)")
st.write("Ask me anything about farming, crops, fertilizers, pests, etc.")

# ✅ Input
user_input = st.text_input("👨‍🌾 Enter your question:")

if st.button("Get Answer") and user_input:
    with st.spinner("Generating response..."):
        prompt = f"<|system|>You are an expert agricultural assistant helping Indian farmers.<|user|>{user_input}<|assistant|>"

        inputs = tokenizer(prompt, return_tensors="pt").to(device)

        outputs = model.generate(
            **inputs,
            max_new_tokens=150,
            temperature=0.7,
            top_k=50,
            top_p=0.95,
            pad_token_id=tokenizer.eos_token_id
        )

        full_output = tokenizer.decode(outputs[0], skip_special_tokens=True)
        if "<|assistant|>" in full_output:
            answer = full_output.split("<|assistant|>")[-1].strip()
        else:
            answer = full_output.strip()

        st.success(answer)
