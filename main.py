import pandas as pd
import os
import news_fetcher
import sentiment_analyzer

# --- Configurações ---
RSS_URL = "https://br.investing.com/rss/news_25.rss"
OUTPUT_CSV = "financial_news_sentiment_vader.csv"


def main():

    print("--- Iniciando processo de coleta e análise de notícias ---")

    news_data = news_fetcher.fetch_news(RSS_URL)

    if not news_data:
        print("Nenhuma notícia encontrada. Encerrando.")
        return

    new_sentiment_df = sentiment_analyzer.analyze_sentiment(news_data)

    print(f"Gerenciando o arquivo de saída: {OUTPUT_CSV}...")
    if os.path.exists(OUTPUT_CSV):
        print("Arquivo CSV existente encontrado. Carregando...")
        try:
            existing_df = pd.read_csv(OUTPUT_CSV)
            print(f"{len(existing_df)} notícias existentes carregadas.")
            # Combina dataframes e remove duplicatas baseadas no link
            combined_df = pd.concat([existing_df, new_sentiment_df]).drop_duplicates(
                subset=['link'], keep='last')
            print(
                f"{len(combined_df) - len(existing_df)} novas notícias adicionadas.")
        except pd.errors.EmptyDataError:
            print("Arquivo CSV existente está vazio. Usando apenas os novos dados.")
            combined_df = new_sentiment_df
        except Exception as e:
            print(
                f"Erro ao ler CSV existente: {e}. Usando apenas os novos dados.")
            combined_df = new_sentiment_df
    else:
        print("Arquivo CSV não encontrado. Criando um novo.")
        combined_df = new_sentiment_df

    try:
        combined_df.to_csv(OUTPUT_CSV, index=False, encoding='utf-8-sig')
        print(
            f"Dados salvos com sucesso em {OUTPUT_CSV}. Total de {len(combined_df)} notícias.")
    except Exception as e:
        print(f"Erro ao salvar o arquivo CSV: {e}")

    print("\nÚltimas notícias processadas:")
    print(new_sentiment_df.head())


if __name__ == "__main__":
    main()
