
def compute_wallet_score(row):
    # Normalize and compute score out of 1000
    lent_score = min(row['total_lent'] / 10000, 1.0) * 400
    borrow_score = min(row['total_borrowed'] / 10000, 1.0) * 300
    txn_score = min(row['total_txn'] / 100, 1.0) * 200
    net_score = 100 if row['net_value'] > 0 else 0

    total_score = lent_score + borrow_score + txn_score + net_score
    return round(total_score)
