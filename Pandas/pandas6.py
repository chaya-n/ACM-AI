import pandas as pd

df = pd.read_csv(r"C:\Users\lenovo\Desktop\survey_results_public.csv")
filtered_data = df[df["Country"]=='United Kingdom of Great Britain and Northern Ireland']
filter2 = df[df["Country"]=='United States of America']
print(filtered_data,filter2, end = '\n')