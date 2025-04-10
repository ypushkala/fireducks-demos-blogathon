import fireducks as fd
import pandas as pd
import time
data = {'Product': ['A', 'B', 'C'] * 333333 + ['A'],
        'Sales': range(1, 1000001)}
df = pd.DataFrame(data)
start_time = time.time()
fd_grouped = fd.DataFrame(df).groupby('Product')['Sales'].sum()
fireducks_time = time.time() - start_time
print(f"FireDucks time: {fireducks_time:.6f} seconds")
start_time = time.time()
pandas_grouped = df.groupby('Product')['Sales'].sum()
pandas_time = time.time() - start_time
print(f"Pandas time: {pandas_time:.6f} seconds")
