import pandas as pd
import time
import fireducks.pandas as fdpd  # FireDucks-compatible pandas interface
from fireducks.core import get_fireducks_options

# Enable benchmark mode to get accurate timings
get_fireducks_options().set_benchmark_mode(True)
# Create a large sample dataset (50 million rows)
N = 50000000  # Increase size for more noticeable performance difference
data = {
    'Product': ['A', 'B', 'C'] * (N // 3) + ['A', 'B', 'C'][:(N % 3)],  # Ensure equal length for the 'Product' column
    'Sales': range(1, N + 1)  # Sales goes from 1 to N
}
df = pd.DataFrame(data)
# More complex transformations and grouping for FireDucks
start_time = time.time()

# Create a FireDucks DataFrame from the pandas DataFrame
fd_df = fdpd.DataFrame(df)

# More complex transformations (filtering, transformations, joins, etc.)
fd_result = (
    fd_df[fd_df["Sales"] > 500000]  # More stringent filter
    .assign(Discount=lambda x: x["Sales"] * 0.25)  # Apply a more complex transformation
    .groupby("Product")["Discount"]  # Grouping and applying more transformations
    .sum()  # Aggregation sum instead of mean
)

# Force evaluation (FireDucks is lazy, so we force evaluation)
try:
    fd_result._evaluate()
except AttributeError:
    pass

fireducks_time = time.time() - start_time
print(f"\n🔥 FireDucks complex operations time: {fireducks_time:.6f} seconds")

# 🐼 Pandas Benchmark (similar complexity)
start_time = time.time()

pandas_result = (
    df[df["Sales"] > 500000]  # Similar filter in Pandas
    .assign(Discount=lambda x: x["Sales"] * 0.25)  # Similar transformation in Pandas
    .groupby("Product")["Discount"]  # Same groupby
    .sum()  # Same aggregation
)
