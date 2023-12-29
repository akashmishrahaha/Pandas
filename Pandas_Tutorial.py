import pandas as pd

import numpy as np

df = pd.DataFrame(
    np.arange(20).reshape(5, 4),
    index=["Row1", "Row2", "Row3", "Row4", "Row5"],
    columns=["Col1", "Col2", "Col3", "Col4"],
)

print(df)

print("\n")


# Operations on Pandas

# saving file

# indexing

print(df["Col1"])
print("\n")
# using loc and iloc

print(df.loc["Row1"])
print(df.iloc[0:3, 1:4])

# Converting dataframes into matrix

mat = df.iloc[0:3, 1:3].values
print(mat)
