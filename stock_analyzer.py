import pandas as pd
import yfinance as yf
import matplotlib.pyplot as plt
import seaborn as sns
from datetime import datetime, timedelta

# --- Configurações ---
CSV_FILE = "financial_news_sentiment_vader.csv"
STOCKS_TO_ANALYZE = [
    'VALE3.SA',
    'PETR4.SA',
    'ITUB4.SA',
    'BBDC4.SA',
    'ABEV3.SA',
    'B3SA3.SA',
    'WEGE3.SA',
    'BBAS3.SA',
    'ITSA4.SA',
    'SUZB3.SA'
]
DAYS_BACK = 90
SENTIMENT_LAG_DAYS = 1


def analyze_stocks_and_sentiment():

    print("--- Iniciando Análise de Ações e Sentimento (Python) ---")

    # 1. Carregar e Processar Sentimento
    print(f"Carregando dados de sentimento de {CSV_FILE}...")
    try:
        news_df = pd.read_csv(CSV_FILE)
        # Tenta converter 'published' para datetime, tratando erros
        news_df['published_dt'] = pd.to_datetime(
            news_df['published'], errors='coerce')
        # Remove linhas onde a conversão falhou
        news_df.dropna(subset=['published_dt'], inplace=True)
        # Extrai apenas a data
        news_df['date'] = news_df['published_dt'].dt.date
    except FileNotFoundError:
        print(
            f"Erro: Arquivo {CSV_FILE} não encontrado. Execute o main.py primeiro.")
        return
    except Exception as e:
        print(f"Erro ao carregar ou processar o CSV: {e}")
        return

    print("Agregando sentimento por dia...")
    # Agrupa por data e calcula a média do 'sentiment_compound'
    daily_sentiment = news_df.groupby(
        'date')['sentiment_compound'].mean().reset_index()
    daily_sentiment['date'] = pd.to_datetime(
        daily_sentiment['date'])  # Garante que é datetime
    daily_sentiment.set_index('date', inplace=True)
    print(f"Sentimento diário calculado para {len(daily_sentiment)} dias.")

    # 2. Buscar Dados das Ações
    end_date = datetime.now()
    start_date = end_date - timedelta(days=DAYS_BACK)
    print(
        f"Buscando dados de ações para {STOCKS_TO_ANALYZE} de {start_date.strftime('%Y-%m-%d')} a {end_date.strftime('%Y-%m-%d')}...")

    stock_data = yf.download(STOCKS_TO_ANALYZE, start=start_date, end=end_date)

    if stock_data.empty:
        print("Não foi possível buscar dados das ações.")
        return

    # 3. Processar Ações e Unir Dados
    print("Calculando retornos diários e unindo com sentimento...")
    adj_close = stock_data['Close']
    daily_returns = adj_close.pct_change().dropna()

    # Prepara o sentimento com lag
    sentiment_with_lag = daily_sentiment.shift(SENTIMENT_LAG_DAYS)
    sentiment_with_lag.rename(
        columns={'sentiment_compound': 'sentiment_lagged'}, inplace=True)

    # Une os retornos com o sentimento (usando o índice de data)
    analysis_df = daily_returns.join(sentiment_with_lag, how='inner')
    analysis_df.dropna(inplace=True)  # Remove dias sem dados em ambos

    if analysis_df.empty:
        print("Não há dados sobrepostos entre ações e sentimento para o período.")
        return

    print("Dados para análise:")
    print(analysis_df.head())

    # 4. Calcular Correlação
    print("\n--- Correlação ---")
    for stock in STOCKS_TO_ANALYZE:
        if stock in analysis_df.columns:
            correlation = analysis_df[[stock, 'sentiment_lagged']].corr()
            print(f"\nCorrelação para {stock}:")
            print(correlation)

            # 5. Visualizar
            print(f"Gerando gráficos para {stock}...")
            plt.figure(figsize=(12, 6))
            sns.regplot(data=analysis_df, x='sentiment_lagged',
                        y=stock, ci=None, scatter_kws={'alpha': 0.5})
            plt.title(
                f'Sentimento (Lag {SENTIMENT_LAG_DAYS}d) vs. Retorno Diário - {stock}')
            plt.xlabel('Sentimento Composto Médio (Lagged)')
            plt.ylabel('Retorno Diário (%)')
            plt.grid(True)
            plt.tight_layout()
            plt.savefig(f"correlation_{stock}.png")  # Salva o gráfico
            plt.show()  # Mostra o gráfico

    print("\n--- Análise Concluída ---")
    print("Gráficos de correlação foram salvos como .png.")


# Executa a função principal
if __name__ == "__main__":
    analyze_stocks_and_sentiment()
