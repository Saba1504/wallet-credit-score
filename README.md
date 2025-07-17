# wallet-credit-score
# 🧠 Wallet Credit Scoring using Aave V2 Transaction Data

## 📁 Dataset
The dataset contains ~100,000 user wallet transactions from Aave V2.  
Each entry in the JSON file includes:
- `userWallet`: the wallet address
- `network`: network used
- `protocol`: protocol used (Aave V2)
- `action`: deposit, borrow, repay, withdraw, etc.
- `actionData`: includes:
  - `amount`
  - `assetSymbol`
  - `assetPriceUSD`
- `timestamp`: Unix timestamp

---

## ⚙️ Method & Architecture

### 1. **Loading & Preprocessing**
- Extracted the JSON from the ZIP file.
- Grouped transactions by wallet.
- Cleaned and converted relevant data (e.g., timestamp to datetime).
- Filtered essential fields for scoring.

### 2. **Feature Engineering**
Extracted these features per wallet:
- Total number of transactions
- Total amount deposited / borrowed / repaid / withdrawn
- Average USD value per transaction
- Diversity of assets used
- First & last transaction date

### 3. **Scoring Logic**
Each wallet received a score from **0 to 1000**, based on:
- Volume and frequency of positive behaviors (e.g., repaying loans, consistent deposits)
- Penalty for risky behavior (e.g., large withdrawals with no repayments)

Final score formula (simplified):


---

## 🧪 Output

After scoring:
- Each wallet was saved in a CSV file: `wallet_scores.csv`
- Score distribution histogram was generated.
- Analysis done on high vs. low scoring wallets.

---

## 📊 Score Distribution
See `analysis.md` for graphs and insights.

---

## ▶️ How to Run
1. Upload the `user-wallet-transactions.json.zip` file.
2. Run the notebook or Python script.
3. Output CSV and graphs will be generated.

---

## 🧰 Requirements
- Python 3.8+
- `pandas`
- `matplotlib`
- `numpy`
- `json`
- `zipfile`
- `datetime`

---

## 👨‍💻 Author
Saba Khan  
Project for Wallet Behavior Scoring using Aave V2 Data.

