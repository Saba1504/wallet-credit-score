# wallet-credit-score
# 🧠 DeFi Wallet Credit Scoring using Aave V2 Data

This project analyzes 100,000+ user wallet transactions on Aave V2 and computes a **credit score from 0 to 1000** for each wallet. The goal is to evaluate user behavior and creditworthiness based on DeFi activity.

---

## 📊 Problem Statement

DeFi protocols lack traditional credit scores. We aim to assign a wallet-based score using past transaction behaviors such as deposits, borrowings, repayments, and frequency of interaction.

---

## 🧱 Architecture

1. **Input**: A JSON file containing 100,000+ transactions with fields like:
   - `userWallet`, `network`, `protocol`, `action`, `actionData`, `timestamp`

2. **Processing Steps**:
   - Extract data from the ZIP file
   - Parse the JSON
   - Group transactions by `userWallet`
   - Compute features per wallet:
     - Total deposits
     - Total borrowings
     - Number of interactions
     - Average transaction size
     - Asset diversity
   - Normalize features and compute final score

3. **Output**:
   - A DataFrame containing wallet address and their credit score
   - Score distribution analysis and visualization

---

## ⚙️ Technologies Used

- Python
- Pandas
- NumPy
- Matplotlib / Seaborn
- Jupyter Notebook

---

## 🚀 How to Run

1. Clone the repo
```bash
git clone https://github.com/your-username/wallet-credit-score.git
cd wallet-credit-score
