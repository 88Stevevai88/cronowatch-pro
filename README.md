
# 🌀 CronoWatch Pro

**CronoWatch Pro** è una Web App real-time in Streamlit per monitorare il wallet Cronos e visualizzare tutte le transazioni WCRO ricevute dai token venduti (LION, BARA, AGENTFUN).

---

## 🚀 Funzionalità

- ✅ Monitoraggio automatico WCRO in entrata
- 🧠 Rilevamento del token venduto da transazioni (con parsing `input`)
- 📊 Grafici interattivi con Plotly
- 📆 Storico mensile e media giornaliera
- 🎯 Tracker per token più usati
- 💬 Integrazione con Telegram (opzionale)
- 🔐 API Key nascoste tramite `secrets.toml`
- 🌐 Pubblicabile su [Streamlit Cloud](https://streamlit.io/cloud)

---

## 🧰 Requisiti

- Python 3.10+
- Account su [Streamlit Cloud](https://streamlit.io/cloud)
- API Key da:
  - [CronoScan](https://cronoscan.com/apis)
  - [CoinMarketCap](https://coinmarketcap.com/api)

---

## ⚙️ Setup (locale)

```bash
git clone https://github.com/tuo-username/cronowatch-pro.git
cd cronowatch-pro
pip install -r requirements.txt
streamlit run app.py
```

---

## 🔐 Configurazione API (Streamlit Cloud)

Crea un file `.streamlit/secrets.toml` con:

```toml
API_KEY = "la-tua-chiave-cronoscan"
CMC_API_KEY = "la-tua-chiave-coinmarketcap"
```

---

## 📁 Struttura del Progetto

```
cronowatch-pro/
├── app.py                     # Web App principale
├── requirements.txt           # Librerie necessarie
└── .streamlit/
    └── secrets.toml           # File con le API Key
```

---

## 📸 Screenshot

*(Aggiungi qui screenshot se vuoi)*

---

## 📬 Contatti

Creato da **Piero Pasquariello**  
🦾 Powered by Python, Streamlit & Crypto Tools  
📧 pieropasquariello@icloud.com

---

## 📄 Licenza

MIT License
