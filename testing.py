import pandas as pd

df = pd.DataFrame(
    {
        "Name": ["Alice", "Bob", "Charlie"],
        "Age": [25, 30, 35],
        "City": ["New York", "Paris", "London"],
    }
)
df.loc[df["Name"] == "Zoe"]

print(df)
