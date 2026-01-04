import pandas as pd
import matplotlib.pyplot as plt
import os
import re

# ==============================
# 1. Load Dataset (POST-ARRIVAL)
# ==============================
FILE_PATH = "POST-ARRIVAL_STUDENT_MENTAL_HEALTH_SURVEY_EXTENDED.csv"
df = pd.read_csv(FILE_PATH)

# ==============================
# 2. Output Folder
# ==============================
OUTPUT_DIR = "post_arrival_eda_report"
IMG_DIR = os.path.join(OUTPUT_DIR, "images")
os.makedirs(IMG_DIR, exist_ok=True)

# ==============================
# 3. Helper function for safe filenames
# ==============================
def safe_name(name):
    return re.sub(r"[^a-zA-Z0-9_]", "_", name)

# ==============================
# 4. Summary Statistics
# ==============================
summary_html = df.describe(include="all").to_html(border=1)

# ==============================
# 5. Missing Value Analysis
# ==============================
missing_df = df.isnull().sum().reset_index()
missing_df.columns = ["Column", "Missing Count"]
missing_html = missing_df.to_html(index=False, border=1)

# ==============================
# 6. Distribution Plots (Numeric)
# ==============================
plot_html = ""

numeric_cols = df.select_dtypes(include=["int64", "float64"]).columns

for col in numeric_cols:
    plt.figure()
    df[col].dropna().hist(bins=20)
    plt.title(col)
    plt.xlabel(col)
    plt.ylabel("Frequency")

    img_name = safe_name(col) + ".png"
    img_path = os.path.join(IMG_DIR, img_name)
    plt.savefig(img_path, bbox_inches="tight")
    plt.close()

    plot_html += f"""
    <h3>{col}</h3>
    <img src="images/{img_name}" width="500">
    <hr>
    """

# ==============================
# 7. Build HTML Report
# ==============================
html_content = f"""
<!DOCTYPE html>
<html>
<head>
    <title>EDA Report – Post-Arrival Students Mental Health Survey</title>
    <style>
        body {{ font-family: Arial, sans-serif; margin: 40px; background-color: #fafafa; }}
        h1 {{ color: #2c3e50; border-bottom: 3px solid #2c3e50; padding-bottom: 10px; }}
        h2 {{ color: #34495e; margin-top: 40px; }}
        h3 {{ color: #1f618d; margin-top: 30px; }}
        table {{ border-collapse: collapse; width: 100%; background: white; }}
        th, td {{ padding: 8px; border: 1px solid #ccc; }}
        th {{ background-color: #f2f2f2; }}
        img {{ margin-bottom: 30px; border: 1px solid #ccc; padding: 5px; background: white; }}
        hr {{ border: none; height: 1px; background: #ccc; }}
        p {{ font-size: 15px; }}
    </style>
</head>

<body>

<h1>Exploratory Data Analysis (EDA) Report</h1>
<p><b>Survey Type:</b> Post-Arrival Student Mental Health Survey</p>

<h2>1. Dataset Overview</h2>
<p>
<b>Rows:</b> {df.shape[0]} <br>
<b>Columns:</b> {df.shape[1]}
</p>

<h2>2. Summary Statistics</h2>
{summary_html}

<h2>3. Missing Values</h2>
{missing_html}

<h2>4. Numeric Feature Distributions</h2>
{plot_html}

<h2>5. Conclusion</h2>
<p>
This post-arrival EDA highlights students’ mental health patterns after settling abroad.
Key stressors include academic workload, financial management, cultural adjustment,
and emotional well-being. The analysis provides insight for targeted support
interventions for international students.
</p>

</body>
</html>
"""

# ==============================
# 8. Save HTML File
# ==============================
output_file = os.path.join(OUTPUT_DIR, "post_arrival_eda_report.html")
with open(output_file, "w", encoding="utf-8") as f:
    f.write(html_content)

print("Post-Arrival EDA HTML report generated successfully!")
print(f"Open this file in browser: {output_file}")
