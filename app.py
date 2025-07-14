import streamlit as st
from transformers import AutoModelForCausalLM, AutoTokenizer
import torch

# ✅ Set page config first
st.set_page_config(page_title="Agri Assistant", page_icon="🌾")

# ✅ Set device manually (CPU or GPU)
device = torch.device("cuda" if torch.cuda.is_available() else "cpu")

# ✅ Load model and tokenizer
@st.cache_resource
def load_model():
    model_id = "TinyLlama/TinyLlama-1.1B-Chat-v1.0"
    tokenizer = AutoTokenizer.from_pretrained(model_id)
    model = AutoModelForCausalLM.from_pretrained(model_id, torch_dtype=torch.float32).to(device)
    return tokenizer, model

tokenizer, model = load_model()

# ✅ Streamlit UI
st.title("🌾 Agriculture AI Assistant (TinyLLaMA)")
st.write("Ask me anything about farming, crops, fertilizers, pests, etc.")

# ✅ User input
user_input = st.text_input("👨‍🌾 Enter your question:")

if st.button("Get Answer") and user_input:
    with st.spinner("Generating response..."):
        # ✅ Build prompt
        prompt = f"<|system|>You are an expert agricultural assistant helping Indian farmers.<|user|>{user_input}<|assistant|>"

        # ✅ Tokenize and move to same device as model
        inputs = tokenizer(prompt, return_tensors="pt").to(device)

        # ✅ Generate response
        outputs = model.generate(
            **inputs,
            max_new_tokens=150,
            temperature=0.7,
            top_k=50,
            top_p=0.95,
            pad_token_id=tokenizer.eos_token_id
        )

        # ✅ Decode response
        full_output = tokenizer.decode(outputs[0], skip_special_tokens=True)
        if "<|assistant|>" in full_output:
            answer = full_output.split("<|assistant|>")[-1].strip()
        else:
            answer = full_output.strip()

        # ✅ Display result
        st.success(answer)
