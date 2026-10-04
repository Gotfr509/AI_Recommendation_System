import numpy as np
import pandas as pd

np.random.seed(42)
n = 100
df = pd.DataFrame({
    'feature1': np.random.uniform(0, 10, n).round(2),
    'feature2': np.random.uniform(0, 10, n).round(2),
    'feature3': np.random.uniform(0, 10, n).round(2),
})
df['label'] = np.where(df['feature1'] + df['feature2'] > 10, 'Producto_A', 'Producto_B')
df.to_csv('products.csv', index=False)
print('products.csv creado')