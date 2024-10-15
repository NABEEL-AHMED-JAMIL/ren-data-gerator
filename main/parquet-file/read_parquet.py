import pandas as pd

# process use to read the data from parquest file
df = pd.read_parquet('example.parquet')
# after reading the file write into console
print(df)