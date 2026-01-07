import pandas as pd 
import os
from datetime import datetime
def generate_report(prompt: str, reponses: dict):
    os.makedirs("data/comparison_reports", exist_ok=True)
    rows = []
    for model, output in reponses.items():
        rows.append({
            "Model": model,
            "Prompt": prompt,
            "Response": output,
            "Timestamp": datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        })
    df = pd.DataFrame(rows)
    df.to_csv(f"data/comparison_reports/report.csv", index=False)
    return "data/comparison_reports/report.csv"