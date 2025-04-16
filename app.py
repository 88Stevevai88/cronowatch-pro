
import streamlit as st
import requests
import pandas as pd
import plotly.express as px
from datetime import datetime

WALLET = "0x65957920DA8F24592F54800039B31443Bb4CDE80".lower()
API_KEY = st.secrets["API_KEY"]
CMC_API_KEY = st.secrets["CMC_API_KEY"]
START_DATE = datetime(2025, 3, 29)

token_names = {
    "0x9d8c68f185a04314ddc8b8216732455e8dbb7e45": "LION",
    "0xf24409d155965ca87c45ad5bc084ad8ad3be4f39": "BARA",
    "0x96733708c4157218b6e6889eb9e16b1df7873061": "AGENTFUN"
}

def get_internal_transactions():
    url = f"https://api.cronoscan.com/api?module=account&action=txlistinternal&address={WALLET}&startblock=0&endblock=99999999&sort=asc&apikey={API_KEY}"
    return requests.get(url).json().get("result", [])

def get_transaction_input(tx_hash):
    url = f"https://api.cronoscan.com/api?module=proxy&action=eth_getTransactionByHash&txhash={tx_hash}&apikey={API_KEY}"
    result = requests.get(url).json()
    return result.get("result", {}).get("input", "")

def detect_token_from_input(input_data):
    for address, name in token_names.items():
        cleaned = address.lower().replace("0x", "").rjust(64, "0")
        if cleaned in input_data.lower():
            return name
    return "Non rilevato"

def get_wcro_price():
    url = "https://pro-api.coinmarketcap.com/v1/cryptocurrency/quotes/latest"
    params = {"symbol": "CRO", "convert": "EUR"}
    headers = {"X-CMC_PRO_API_KEY": CMC_API_KEY}
    try:
        response = requests.get(url, params=params, headers=headers)
        return float(response.json()["data"]["CRO"]["quote"]["EUR"]["price"])
    except:
        return 0.0

def main():
    st.set_page_config("CronoWatch Pro", layout="wide")
    st.title("CronoWatch Pro")
    st.caption("Monitoraggio WCRO + Analisi Token")

    data = get_internal_transactions()
    wcro_price = get_wcro_price()

    swap_data = []
    for tx in data:
        time_stamp = datetime.fromtimestamp(int(tx["timeStamp"]))
        if time_stamp < START_DATE or tx.get("isError") != "0":
            continue
        if tx.get("to", "").lower() == WALLET and float(tx.get("value", 0)) > 0:
            value = int(tx["value"]) / 1e18
            eur = value * wcro_price
            input_data = get_transaction_input(tx["hash"])
            token = detect_token_from_input(input_data)
            swap_data.append({
                "Data": time_stamp,
                "Token": token,
                "Da": tx.get("from"),
                "Valore WCRO": value,
                "Valore EUR": eur,
                "Link": f"https://cronoscan.com/tx/{tx['hash']}"
            })

    df = pd.DataFrame(swap_data)
    if df.empty:
        st.error("Nessuna transazione trovata.")
        return

    df["Data"] = pd.to_datetime(df["Data"])
    df["Giorno"] = df["Data"].dt.date
    df["Mese"] = df["Data"].dt.strftime("%Y-%m")
    df["Anno"] = df["Data"].dt.year

    st.metric("Totale WCRO", f"{df['Valore WCRO'].sum():.2f}")
    st.metric("Totale EUR", f"€ {df['Valore EUR'].sum():.2f}")
    st.dataframe(df.tail(10))

if __name__ == "__main__":
    main()
