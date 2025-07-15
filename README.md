
# 🌾 KrishiAI – Agriculture AI Assistant 🤖👨‍🌾

---

## 🧠 AI Assistant Overview

### **Assistant Name**  
**KrishiAI**

### **Purpose & Target Audience**  
KrishiAI is an open-source AI assistant designed to provide general agricultural knowledge and farming guidance to rural and semi-urban users in India. It is especially useful for:

- Farmers looking for crop care, pest control, or fertilizer guidance  
- Agriculture students seeking summaries of concepts  
- NGOs or agri-tech volunteers assisting with knowledge distribution  

> ⚠️ **Disclaimer**: KrishiAI provides general information and is *not* a substitute for certified agricultural experts or local agronomists.

---

### 🔑 **Key Features**

- Responds to crop-related and farming questions in natural language  
- Covers common topics: pests, fertilizers, irrigation, seasons, etc.  
- Optimized for low-resource devices (TinyLLaMA 1.1B model)  
- Deployable via Streamlit Cloud for quick and easy access  
- Disclaims that responses are general and not region-specific  
- Designed to expand for multilingual support (e.g., Hindi, Telugu)

---

## ✍️ System Prompt Design and Justification

### **System Prompt**
```text
You are a helpful AI assistant named KrishiAI. You provide general information about agriculture, including crop care, fertilizers, pest control, and good farming practices. You do not offer region-specific advice. Always remind users to consult local agricultural officers or experts for detailed guidance. Be friendly, respectful, and easy to understand.
```

---

### ⚙️ Breakdown of Elements

| **Component**               | **Purpose**                                                 |
|-----------------------------|-------------------------------------------------------------|
| **Persona (KrishiAI)**      | Defines identity as a friendly, agri-focused assistant      |
| **General Info Only**       | Avoids giving local or climate-specific advice              |
| **Expert Referral**         | Encourages responsible follow-up with real-world experts    |
| **Tone: Simple & Respectful** | Ensures clarity, simplicity, and user trust                 |
| **Avoid Overpromising**     | Keeps suggestions basic and non-committal                   |

---

### 🛠️ Design Choices

- **Rural-friendly tone**: Simple and supportive responses  
- **No hyperlocal claims**: Due to model’s limitations, avoids false specificity  
- **Low-cost deployment**: Uses Hugging Face + Streamlit stack  
- **Open-source**: Meant for students, NGOs, or AI hackathons

---

## 🧪 User Reviews and Feedback Analysis

### **Methodology**  
Feedback collected from 10 users (farmers, students, volunteers) via direct use and forms.

| **User ID** | **Date** | **Topic Asked**                | **Rating (1–5)** | **Comments**                          |
|------------|----------|--------------------------------|------------------|----------------------------------------|
| U01        | July 6   | Pest on tomato crop            | ⭐⭐⭐⭐             | Useful but wanted chemical names       |
| U02        | July 6   | Drip irrigation basics         | ⭐⭐⭐⭐⭐            | Very well explained                    |
| U03        | July 6   | Fertilizer timing for rice     | ⭐⭐⭐⭐             | Answer was helpful                     |
| U05        | July 7   | Plant disease symptoms         | ⭐⭐⭐              | Was too generic                        |
| U06        | July 7   | Seasonal crop suggestions      | ⭐⭐⭐⭐             | Good info, but could be longer         |
| U07        | July 8   | Rainwater harvesting methods   | ⭐⭐⭐⭐             | Nicely broken down                     |
| U08        | July 8   | Natural pest control tips      | ⭐⭐⭐⭐             | Answer was short but helpful           |
| U09        | July 8   | Organic farming practices      | ⭐⭐⭐⭐⭐            | Loved the clarity                      |
| U10        | July 8   | Soil testing procedure         | ⭐⭐⭐⭐             | Good intro, but missed cost info       |

### **Key Insights**

✅ **Strengths**: Easy-to-understand tone, general accuracy, responsiveness  
❌ **Weaknesses**: Answers can be too generic, lacks regional language support

### **Average Rating**: `4.1 / 5`

---
<img width="2559" height="1345" alt="image" src="https://github.com/user-attachments/assets/f36f1cae-8772-4197-930a-00fff78235d5" />


## 🚀 Future Roadmap

### **Short-Term (1 week)**

- Add top 10 common agri questions and pre-answers  
- Include basic Hindi & Telugu greeting support  
- Improve disclaimer placement and feedback option

### **Mid-Term (2–4 weeks)**

- Add multilingual NLP (Telugu, Hindi, Kannada)  
- Fine-tune model with agriculture domain-specific corpus  
- Reference reliable sources (e.g., ICAR, Krishi Vigyan Kendra)

### **Long-Term (1–2 months)**

- Deploy mobile-optimized web app version  
- Partner with agri NGO or KVK for use case testing  
- Add farmer-friendly visuals/images per question  

---

### **Free and Ethical Use**

- Emphasize that it’s free, open, and safe  
- Make legal disclaimers visible and friendly



## 📌 Conclusion

KrishiAI brings conversational AI to the fields. While it's no substitute for agronomists, it offers a helpful, scalable, and open way to educate and assist farmers, students, and support staff. With responsible deployment and community feedback, KrishiAI can empower better agricultural understanding across India.
