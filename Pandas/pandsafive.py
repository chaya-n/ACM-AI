import pandas as pd

df = pd.read_csv(r"C:\Users\lenovo\Desktop\survey_results_public.csv")
df2 = df[df['name'].str.contains('DevType')]
print(df2['question'])