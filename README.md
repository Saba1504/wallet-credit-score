# wallet-credit-score
# DeFi Wallet Credit Scoring Using Aave V2 Data

This project analyzes DeFi wallet transactions using Aave V2 protocol data and generates a **credit score between 0 and 1000** for each wallet, based on behavior and usage metrics.

---

## 🔍 Problem Statement

DeFi lacks traditional credit systems. This project attempts to score wallets based on their lending/borrowing behavior, activity levels, and diversity in usage using a behavioral credit scoring model.

---

## 📊 Methodology

1. **Data Ingestion**:
   - JSON file with 100,000 wallet transactions.
   - Each transaction includes action type, amount, asset, price in USD, etc.

2. **Feature Engineering**:
   - For each wallet:
     - Total transactions
     - Unique assets used
     - Total and average USD volume
     - Actions count: deposit, borrow, repay, etc.

3. **Derived Metrics**:
   - Deposit ratio = deposit / total transactions
   - Activity score (weighted metric of usage)
   - Min-Max scaling of activity score → Final Credit Score (0–1000)

4. **Scoring**:
   - Wallets are scored and categorized into 5 buckets:
     - 0–200: Very Low
     - 200–400: Low
     - 400–600: Medium
     - 600–800: High
     - 800–1000: Very High

5. **Visualization**:
   - Credit score distribution
   - Behavioral insights per group

---

## ⚙️ Project Structure

- `src/feature_engineering.py`: Feature extraction and scoring logic
- `src/visualize.py`: Score plotting and behavior summary
- `analysis.md`: Insight into behavior of wallets per score group
- `wallet_credit_scores.csv`: Final output with scores and features

---

## 📦 Requirements

```bash
pip install pandas matplotlib seaborn scikit-learn
