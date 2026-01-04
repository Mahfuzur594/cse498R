import pandas as pd
from ydata_profiling import ProfileReport
import os

# ==============================
# 1. Create output folder
# ==============================
OUTPUT_DIR = "ydata_eda_reports"
os.makedirs(OUTPUT_DIR, exist_ok=True)

# ==============================
# 2. PRE-DEPARTURE EDA
# ==============================
pre_file = "PRE_DEPARTURE_STUDENTS_MENTAL_HEALTH_SURVEY_EXTENDED.csv"
df_pre = pd.read_csv(pre_file)

pre_profile = ProfileReport(
    df_pre,
    title="EDA Report – Pre-Departure Students Mental Health Survey",
    explorative=True,
    minimal=False
)

pre_output = os.path.join(OUTPUT_DIR, "pre_departure_eda.html")
pre_profile.to_file(pre_output)

print("✅ Pre-Departure EDA generated:", pre_output)

# ==============================
# 3. POST-ARRIVAL EDA
# ==============================
post_file = "POST-ARRIVAL_STUDENT_MENTAL_HEALTH_SURVEY_EXTENDED.csv"
df_post = pd.read_csv(post_file)

post_profile = ProfileReport(
    df_post,
    title="EDA Report – Post-Arrival Students Mental Health Survey",
    explorative=True,
    minimal=False
)

post_output = os.path.join(OUTPUT_DIR, "post_arrival_eda.html")
post_profile.to_file(post_output)

print("✅ Post-Arrival EDA generated:", post_output)
