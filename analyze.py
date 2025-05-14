import pandas as pd
from scipy import stats
import matplotlib.pyplot as plt
import seaborn as sns
import os

# Load dataset
df = pd.read_csv('data/ab_data.csv')

# Calculate conversion rates
rates = df.groupby('group')['converted'].mean()

# Extract group data
control = df[df['group'] == 'control']['converted']
treatment = df[df['group'] == 'treatment']['converted']

# T-test
t_stat, p_val = stats.ttest_ind(control, treatment)

# Print Results
print("\n📊 Conversion Rates:")
print(rates)

print(f"\n🧪 T-statistic: {t_stat:.4f}")
print(f"📉 P-value: {p_val:.4f}")

if p_val < 0.05:
    conclusion = "✅ Result: Statistically Significant — there's a real difference."
else:
    conclusion = "❌ Result: Not Statistically Significant — could be random."

print(conclusion)

# Save plot
plt.figure(figsize=(6, 4))
sns.barplot(x=rates.index, y=rates.values)
plt.title("Conversion Rates (Control vs Treatment)")
plt.ylabel("Conversion Rate")
plt.ylim(0, 0.15)

# Make sure 'output' folder exists
os.makedirs('output', exist_ok=True)
plot_path = 'output/conversion_chart.png'
plt.savefig(plot_path)
plt.close()

# Generate Markdown Report
report = f"""
# A/B Testing Report

**Conversion Rates:**
- Control: {rates['control']:.4f}
- Treatment: {rates['treatment']:.4f}

**T-Test:**
- T-statistic: {t_stat:.4f}
- P-value: {p_val:.4f}

**Conclusion:**  
{conclusion}

![Chart](conversion_chart.png)
"""

with open('output/report.md', 'w', encoding='utf-8') as f:
    f.write(report)


print("\n📄 Report saved to: output/report.md")
print(f"🖼️  Chart saved to: {plot_path}")
