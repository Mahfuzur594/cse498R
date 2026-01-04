import pandas as pd
import matplotlib.pyplot as plt
import os
import re

# ==============================
# 1. Load Dataset
# ==============================
FILE_PATH = "PRE_DEPARTURE_STUDENTS_MENTAL_HEALTH_SURVEY_EXTENDED.csv"
df = pd.read_csv(FILE_PATH)

# ==============================
# 2. Output Folder
# ==============================
OUTPUT_DIR = "eda_report"
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
    plt.savefig(img_path)
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
    <title>EDA Report – Pre-Departure Students Mental Health Survey</title>
    <style>
        body {{ font-family: Arial; margin: 40px; }}
        h1 {{ color: #2c3e50; }}
        h2 {{ color: #34495e; }}
        table {{ border-collapse: collapse; width: 100%; }}
        th, td {{ padding: 8px; text-align: left; }}
        th {{ background-color: #f2f2f2; }}
        img {{ margin-bottom: 30px; }}
    </style>
</head>

<body>

<h1>Exploratory Data Analysis (EDA) Report</h1>

<h2>1. Dataset Overview</h2>
<p><b>Rows:</b> {df.shape[0]} <br>
<b>Columns:</b> {df.shape[1]}</p>

<h2>2. Summary Statistics</h2>
{summary_html}

<h2>3. Missing Values</h2>
{missing_html}

<h2>4. Numeric Feature Distributions</h2>
{plot_html}

</body>
</html>
"""

# ==============================
# 8. Save HTML File
# ==============================
output_file = os.path.join(OUTPUT_DIR, "eda_report.html")
with open(output_file, "w", encoding="utf-8") as f:
    f.write(html_content)

print("EDA HTML report generated successfully!")
print(f"Open this file in browser: {output_file}")

