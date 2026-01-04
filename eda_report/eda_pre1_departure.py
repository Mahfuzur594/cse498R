import pandas as pd

# ==============================
# Load Dataset
# ==============================
df = pd.read_csv("PRE_DEPARTURE_STUDENTS_MENTAL_HEALTH_SURVEY_EXTENDED.csv")

# ==============================
# Basic EDA Calculations
# ==============================
rows, cols = df.shape
missing_values = df.isnull().sum()
missing_percent = (missing_values / rows) * 100
summary = df.describe(include="all").transpose()

# ==============================
# Convert tables to HTML
# ==============================
summary_html = summary.to_html(classes="table", border=0)
missing_html = pd.DataFrame({
    "Missing Count": missing_values,
    "Missing %": missing_percent.round(2)
}).to_html(classes="table", border=0)

# ==============================
# HTML + CSS (INLINE)
# ==============================
html_content = f"""
<!DOCTYPE html>
<html lang="en">
<head>
<meta charset="UTF-8">
<title>EDA Report – Student Mental Health Survey</title>

<style>
body {{
    font-family: Arial, sans-serif;
    background: #f4f6f9;
    margin: 0;
    padding: 0;
}}

header {{
    background: #1e3c72;
    color: white;
    padding: 25px;
    text-align: center;
}}

section {{
    background: white;
    margin: 25px;
    padding: 25px;
    border-radius: 8px;
    box-shadow: 0 0 10px rgba(0,0,0,0.1);
}}

h2 {{
    border-bottom: 2px solid #1e3c72;
    padding-bottom: 5px;
}}

.table {{
    width: 100%;
    border-collapse: collapse;
    margin-top: 15px;
}}

.table th, .table td {{
    border: 1px solid #ccc;
    padding: 8px;
    text-align: left;
}}

.table th {{
    background: #1e3c72;
    color: white;
}}

.table tr:nth-child(even) {{
    background: #f2f2f2;
}}

footer {{
    background: #ddd;
    text-align: center;
    padding: 15px;
    font-size: 14px;
}}

.highlight {{
    font-weight: bold;
    color: #1e3c72;
}}
</style>
</head>

<body>

<header>
    <h1>Exploratory Data Analysis (EDA)</h1>
    <p>Pre-Departure Students Mental Health Survey</p>
</header>

<section>
    <h2>1. Dataset Overview</h2>
    <p>
        <span class="highlight">Total Rows:</span> {rows}<br>
        <span class="highlight">Total Columns:</span> {cols}
    </p>
    <p>
        This dataset contains survey responses related to students' mental health
        before departure. The purpose of this EDA is to understand the structure,
        quality, and distribution of the data.
    </p>
</section>

<section>
    <h2>2. Missing Values Analysis</h2>
    <p>
        This table shows the number and percentage of missing values in each column.
        Columns with high missing percentages may require imputation or removal.
    </p>
    {missing_html}
</section>

<section>
    <h2>3. Statistical Summary</h2>
    <p>
        The statistical summary provides information such as count, mean, standard
        deviation, minimum, and maximum values for numerical features, and frequency
        details for categorical features.
    </p>
    {summary_html}
</section>

<section>
    <h2>4. Key Observations</h2>
    <ul>
        <li>Presence of missing values indicates the need for data cleaning.</li>
        <li>Some features may have limited variance or repeated values.</li>
        <li>Numerical features show varying distributions which may require normalization.</li>
        <li>Categorical features dominate the dataset, reflecting survey-based data.</li>
    </ul>
</section>

<section>
    <h2>5. Conclusion</h2>
    <p>
        This Exploratory Data Analysis helps in understanding the overall quality and
        characteristics of the mental health survey dataset. The insights gained from
        this analysis will guide preprocessing, feature selection, and model building
        in further stages.
    </p>
</section>

<footer>
    <p>EDA Report generated using Python, HTML & CSS</p>
</footer>

</body>
</html>
"""

# ==============================
# Save HTML File
# ==============================
with open("mental_health_eda.html", "w", encoding="utf-8") as f:
    f.write(html_content)

print("✅ EDA HTML report generated: mental_health_eda.html")


