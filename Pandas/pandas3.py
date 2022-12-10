import pandas as pd

df = pd.read_csv(r"C:\Users\lenovo\Desktop\survey_results_public.csv")
df2 = df.Employment
print(df2.iloc[-1],df2.iloc[0])