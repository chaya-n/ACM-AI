import pandas as pd

df = pd.read_csv(r"C:\Users\lenovo\Desktop\survey_results_public.csv")
df2 = df['Employment'].value_counts(normalize=True) * 100
print(df2[0])