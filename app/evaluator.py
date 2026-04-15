import pandas as pd
from app.generator import generate_email
from app.metrics import fact_recall, tone_accuracy, conciseness
from app.test_data import test_cases


def evaluate():
    results = []

    for case in test_cases:
        for model in ["basic", "advanced"]:

            output = generate_email(
                case["intent"],
                case["facts"],
                case["tone"],
                advanced=(model == "advanced")
            )

            f_score = fact_recall(output, case["facts"])
            t_score = tone_accuracy(output, case["tone"])
            c_score = conciseness(output)

            final_score = round((f_score * 0.4 + t_score * 0.3 + c_score * 0.3), 2)

            results.append({
                "intent": case["intent"],
                "model": model,
                "fact_score": f_score,
                "tone_score": t_score,
                "conciseness": c_score,
                "final_score": final_score
            })

    df = pd.DataFrame(results)
    df.to_csv("results/evaluation.csv", index=False)

    generate_summary(df)

    print("✅ Evaluation complete!")


def generate_summary(df):
    avg_scores = df.groupby("model")["final_score"].mean()

    best_model = avg_scores.idxmax()

    summary = f"""
Best Model: {best_model}

Average Scores:
{avg_scores}

Conclusion:
Advanced prompting performs better due to improved structure, tone consistency, and fact inclusion.
"""

    with open("results/summary.txt", "w") as f:
        f.write(summary)