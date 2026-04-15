# 📧 Email Generation Assistant (AI Engineer Assessment)

## 🚀 Overview
This project is an AI-powered Email Generation Assistant that generates professional emails using LLMs based on:
- **Intent** (purpose)
- **Key Facts** (important points)
- **Tone** (formal, casual, etc.)

---

## 🧠 Features
- LLM-based email generation
- Advanced Prompt Engineering (role-based + structured prompts)
- Custom evaluation metrics
- Model comparison (Basic vs Advanced prompting)
- CSV-based evaluation output

---

## ⚙️ Tech Stack
Python, Groq API, Pandas, dotenv

---

## 📂 Structure
email_generation_assistant/
├── generator.py
├── evaluator.py
├── scenarios.py
├── main.py
├── results.csv
├── .env
├── requirements.txt
└── README.md


---

## 🧪 Prompting Strategy
- **Basic Prompt**: Simple instruction-based generation  
- **Advanced Prompt**: Role-based + structured instructions for better:
  - Fact inclusion
  - Tone consistency
  - Formatting

---

## 📊 Evaluation Metrics
1. **Fact Recall Score**  
   = Facts included / Total facts  

2. **Tone Accuracy Score**  
   = Tone match (0–1)  

3. **Conciseness Score**  
   = Based on clarity and length  

**Final Score:**  
`0.4 * Fact + 0.3 * Tone + 0.3 * Conciseness`

---

## 🧾 Test Scenarios
10 scenarios including:
- Follow-up
- Leave request
- Project update
- Apology
- Client onboarding
- Meeting reminder
- Feedback request
- Invoice reminder
- Job application
- Thank you email

---

## ▶️ How to Run

### 1. Install dependencies
pip install -r requirements.txt


### 2. Add API Key (.env)
GROQ_API_KEY=your_api_key


### 3. Run
python main.py


## 📈 Output
Generated file:

results.csv

Example:
intent,model,fact_score,tone_score,conciseness,final_score
Follow up,basic,1.0,1.0,0.7,0.91
Follow up,advanced,1.0,1.0,1.0,1.0


---

## 🔍 Model Comparison
**Best Model:** Advanced Prompting  

**Average Scores:**
- Advanced: 0.985  
- Basic: 0.886  

---

## 📌 Analysis
- Advanced prompting performs better in:
  - Fact inclusion
  - Tone accuracy
  - Structure and clarity  
- Basic model sometimes misses facts and produces less structured output  

---

## ✅ Conclusion
Advanced prompting is recommended for production due to higher reliability and better output quality.

---

## 📎 Assumptions
- Fact matching uses keyword presence  
- Tone evaluation is simplified  

---

## 📦 Deliverables
- Source code  
- Prompt templates  
- Evaluation script  
- CSV results  
- Model comparison

