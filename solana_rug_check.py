import requests

def rug_check(mint: str):
    url = f"https://api.rugcheck.xyz/v1/tokens/{mint}/report"
    data = requests.get(url).json()
    print(f"{data['name']} ({data['symbol']})\n"
          f"Риск: {data['riskScore']}/100\n"
          f"Минт заморожен: {'Нет ❌' if data['isMintRenounced'] else 'Да ✅'}\n"
          f"LP сожжён: {'Да ✅' if data['isLpBurned'] else 'Нет ❌'}\n"
          f"Топ-10 держат: {data['top10HoldersPercent']:.1f}%\n"
          f"Сниперы: {data['sniperBoughtPercent']:.1f}%\n"
          f"https://rugcheck.xyz/tokens/{mint}")

if __name__ == "__main__":
    addr = input("Solana mint: ").strip()
    rug_check(addr)
