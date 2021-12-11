import pandas as pd

DATA_PATH = './sample.xlsx'
df = pd.read_excel(DATA_PATH)

print(df[df['A'].apply(lambda x: isinstance(x, int) or isinstance(x, float)) == False])

