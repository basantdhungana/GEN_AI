import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

np.random.seed(42)
n = 200
data = {
    "Age": np.random.randint(20, 60, n),
    "Salary": np.random.normal(70000, 15000, n).astype(int),
    "Score": np.random.uniform(60, 95, n),
    "Category": np.random.choice(["A", "B", "C"], n)
}
df_large = pd.DataFrame(data)
df_large.head()



x = np.linspace(0, 10, 100)
plt.figure(figsize=(10, 6))
plt.plot(x, np.sin(x), label="sin(x)", linewidth=4)
plt.plot(x, np.cos(x), label="cos(x)", linestyle="dashed")
plt.title("Trigonometric Functions")
plt.xlabel("X")
plt.ylabel("Value")
plt.legend()
plt.grid(True)
plt.show()