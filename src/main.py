"""
Not a real entry point.
Just making sure I can run things.
"""

from functools import reduce
from typing import Dict, List

import dotenv
import pandas as pd

import env
from ynab.client import YnabClient


dotenv.load()

BUDGET_ID = "b973c1de-bf30-4666-bf4a-47f8cf8d6be4"


def unroll_sub_transactions(transaction=Dict) -> List[Dict]:
    """
    A transaction is simply a dictionary.
    However, the subtransactions key contains an array of further transactions.
    This function will "unroll" that. So you pass in a dictionary and get back an array of transactions.
    If there were no sub-transactions, it will simply be a list with one item in it.
    """
    if transaction is None:
        return None

    sub_transactions = transaction.pop("subtransactions", [])

    return [transaction] + sub_transactions


def combine(left: List[Dict], right: List[Dict]) -> List[Dict]:
    """Combine two lists through simple concatenation"""
    return left + right


def main():
    """Hacky main for development."""
    token = env.get("YNAB_TOKEN")
    client = YnabClient(token)
    transactions = client.get_transactions(BUDGET_ID)

    unrolled = reduce(combine, map(unroll_sub_transactions, transactions))

    transactions_frame = pd.DataFrame.from_records(unrolled)
    print(transactions_frame.describe())

    # Unroll subtransactions
    # They have a reference to their parent_id as "transaction_id"
    # So I think if I just pull subtransactions out and append to the list
    # Then we should be in pretty good shape
    print(len(transactions), len(unrolled))


if __name__ == "__main__":
    main()
