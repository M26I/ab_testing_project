# 🧪 A/B Testing: Conversion Rate Analysis

This is a basic A/B testing project written in Python. It compares the conversion rates between two groups — **control** and **treatment** — and checks whether the difference is statistically significant using a t-test.

---

## 📁 Project Structure

ab_testing_project/
├── analyze.py 
├── data/
│ └── ab_data.csv
├── output/
│ ├── conversion_chart.png # Bar chart of conversion rates
│ └── report.md # Markdown report of the results
├── .gitignore
└── requirements.txt


---

## 📊 What This Project Does

- Loads a dataset with user conversion data  
- Calculates conversion rates for control and treatment groups  
- Performs a **t-test** to check if the difference is statistically significant  
- Saves:
  - A bar chart comparing the two groups
  - A Markdown summary report in the `output/` folder

---

## 🧪 Sample Output

Conversion Rates:

Control: 12.04%

Treatment: 11.89%

T-statistic: 1.2369
P-value: 0.2161

Conclusion: ❌ Not statistically significant — the difference may be due to chance.

> Since the p-value is above 0.05, we conclude there is no strong evidence that one version outperforms the other.

---

## 🛠️ Technologies Used

- Python 3
- pandas
- seaborn
- matplotlib
- scipy

---

## 📬 How to Run This Project

```bash
# (Optional) Set up virtual environment
python -m venv venv
venv\Scripts\activate      # On Windows
# or
source venv/bin/activate   # On macOS/Linux

# Install dependencies
pip install -r requirements.txt

# Run analysis
python analyze.py

## 📎 Dataset
The dataset used is from Kaggle, and contains simulated data for an A/B test.

Columns include:

user_id

group (control or treatment)

converted (0 or 1)

## 📈 Output Files
After running analyze.py, you’ll find:

output/conversion_chart.png: A bar chart showing conversion rates

output/report.md: A Markdown report summarizing the results

## 📌 Notes
This is a small and simple project, perfect for learning A/B testing fundamentals.
It doesn’t use Flask or machine learning — just clean, understandable Python code and basic statistics.


