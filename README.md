# AI-Email-Generation

📧 Email Generation Assistant (AI Engineer Assessment)
🚀 Project Overview

This project is an AI-powered Email Generation Assistant that creates professional emails based on user inputs using Large Language Models (LLMs).

The system takes:

Intent (purpose of the email)
Key Facts (important points to include)
Tone (formal, casual, empathetic, etc.)

and generates a well-structured email.

🧠 Key Features
Prompt-based email generation using LLM
Advanced Prompt Engineering (Role-based + structured prompting)
Custom evaluation metrics for performance measurement
Model comparison (Basic vs Advanced prompting)
Automated evaluation with structured output (CSV)
⚙️ Tech Stack
Python 3.x
Groq API (LLM)
Pandas
dotenv
📂 Project Structure
email_generation_assistant/
│
├── generator.py          # Email generation logic (LLM prompts)
├── evaluator.py          # Custom metrics implementation
├── scenarios.py          # Test scenarios + reference emails
├── main.py               # Runs full evaluation
├── results.csv           # Evaluation output
├── .env                  # API key
├── requirements.txt
└── README.md
🧪 Prompt Engineering Strategy
Basic Prompt

A simple instruction-based prompt:

Generates email from intent, facts, and tone
Advanced Prompt (Used for Improvement)
Role-based prompting (acts as professional assistant)
Structured instructions
Enforces:
Fact inclusion
Proper tone
Clear formatting
📊 Custom Evaluation Metrics
1. Fact Recall Score

Measures whether all provided key facts are included in the generated email.

Logic:

score = (facts present in output) / (total facts)
2. Tone Accuracy Score

Checks whether the generated email matches the expected tone.

Logic:

Keyword-based or LLM-based evaluation
Score: 0 to 1
3. Conciseness Score

Measures how clear and concise the email is.

Logic:

Based on word count threshold
Shorter, well-structured emails score higher
Final Score
Final Score = (Fact Score * 0.4) + (Tone Score * 0.3) + (Conciseness * 0.3)
🧾 Test Scenarios

10 different scenarios were created, including:

Follow-up email
Leave request
Project update
Apology email
Client onboarding
Meeting reminder
Feedback request
Invoice reminder
Job application
Thank you email

Each scenario includes:

Input (Intent, Facts, Tone)
Human Reference Email (ideal output)
▶️ How to Run
1. Clone Repository
git clone <your-repo-link>
cd email_generation_assistant
2. Install Dependencies
pip install -r requirements.txt
3. Add API Key

Create .env file:

GROQ_API_KEY=your_api_key_here
4. Run Evaluation
python main.py
📈 Output

The system generates a CSV file:

results.csv

Example:

intent,model,fact_score,tone_score,conciseness,final_score
Follow up after meeting,basic,1.0,1.0,0.7,0.91
Follow up after meeting,advanced,1.0,1.0,1.0,1.0
...
🔍 Model Comparison
Best Model: Advanced Prompting
Average Scores:
Advanced: 0.985
Basic: 0.886
📌 Analysis

The advanced prompting strategy significantly outperforms the basic model.

Key Improvements:
Better fact inclusion
More consistent tone accuracy
Improved structure and clarity
Failure in Basic Model:
Misses some key facts
Less structured output
Lower conciseness in some cases
✅ Conclusion

The advanced prompting strategy is recommended for production use due to:

Higher reliability
Better output quality
Strong performance across all custom metrics
📎 Assumptions
LLM responses are deterministic enough for evaluation
Fact matching is based on keyword presence
Tone evaluation is simplified (can be improved using LLM judge)
📦 Deliverables Included
✔ Source Code
✔ Prompt Templates
✔ Custom Metrics Implementation
✔ Evaluation Script
✔ CSV Output (results)
✔ Model Comparison Analysis
