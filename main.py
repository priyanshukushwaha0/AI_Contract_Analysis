import argparse
import pandas as pd

from data_loader import load_contracts
from preprocessing import normalize
from llm_pipeline import analyze_contract

parser = argparse.ArgumentParser()

parser.add_argument("--input", required=True)
parser.add_argument("--limit", type=int, default=50)

args = parser.parse_args()

contracts = load_contracts(args.input, args.limit)

rows = []

for contract in contracts:

    text = normalize(contract["text"])

    result = analyze_contract(text)

    rows.append({
        "contract_id": contract["contract_id"],
        "summary": result["summary"],
        "termination_clause": result["termination_clause"],
        "confidentiality_clause": result["confidentiality_clause"],
        "liability_clause": result["liability_clause"]
    })

df = pd.DataFrame(rows)


df.to_json(
    "output/contracts.json",
    orient="records",
    indent=4
)

print("Done")
