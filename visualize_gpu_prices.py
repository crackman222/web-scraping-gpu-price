
import pandas as pd
import matplotlib.pyplot as plt
import os

# Path to margin analysis CSV (update if needed)
csv_file = os.path.join('data', 'gpu_price_margin_analysis.csv')
df = pd.read_csv(csv_file)

# Bar graph for margin vs 2022
df_2022 = df[df['Margin vs 2022 (%)'].notnull() & (df['Margin vs 2022 (%)'] != '')]
plt.figure(figsize=(14, 7))
plt.bar(df_2022['Model'], df_2022['Margin vs 2022 (%)'].astype(float), color='skyblue')
plt.xticks(rotation=90)
plt.ylabel('Margin vs 2022 (%)')
plt.title('GPU Price Margin vs 2022')
plt.tight_layout()
plt.savefig('gpu_margin_vs_2022.png')
plt.show()

# Bar graph for margin vs 2024
df_2024 = df[df['Margin vs 2024 (%)'].notnull() & (df['Margin vs 2024 (%)'] != '')]
plt.figure(figsize=(14, 7))
plt.bar(df_2024['Model'], df_2024['Margin vs 2024 (%)'].astype(float), color='orange')
plt.xticks(rotation=90)
plt.ylabel('Margin vs 2024 (%)')
plt.title('GPU Price Margin vs 2024')
plt.tight_layout()
plt.savefig('gpu_margin_vs_2024.png')
plt.show()
