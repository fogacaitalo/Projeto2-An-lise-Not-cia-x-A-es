# Análise de Sentimento de Notícias Financeiras e Correlação com Ações Brasileiras 📈🇧🇷

## Visão Geral

Este projeto Python automatiza a coleta de notícias financeiras (via RSS), analisa seu sentimento (VADER) e investiga a correlação com o desempenho de ações da B3 (`yfinance`), gerando gráficos e permitindo execução automatizada.

## ⚠️ Status Atual (27/05/2025)

Os dados de exemplo refletem apenas **um dia** de coleta. Portanto, a execução inicial **não gerará gráficos** devido à falta de histórico. É **essencial executar o projeto diariamente** para acumular dados e obter resultados.

---

## Funcionalidades Principais ✨

* Coleta automática de notícias via RSS (Investing.com).
* Análise de sentimento com `vaderSentiment`.
* Armazenamento incremental de notícias em CSV, evitando duplicatas.
* Download de dados históricos de ações da B3 (`yfinance`).
* Cálculo de correlação entre sentimento e retornos diários.
* Geração de gráficos de dispersão/regressão.
* Script `.bat` para execução simplificada no Windows.
* Preparado para automação via Agendador de Tarefas.

---

## Tecnologias Utilizadas 🛠️

* **Linguagem:** Python 3.x
* **Bibliotecas:** `pandas`, `yfinance`, `vaderSentiment`, `feedparser`, `matplotlib`, `seaborn`.
* **Automação:** Windows Batch (`.bat`).

---
## Estrutura do Projeto 📁
```
/Projeto_Noticias_Acoes/
|
├── venv/                   # Ambiente virtual
├── news_fetcher.py         # Busca notícias
├── sentiment_analyzer.py   # Analisa sentimento
├── main.py                 # Orquestra coleta/salvamento
├── stock_analyzer.py       # Orquestra busca/análise de ações
├── Executar_Projeto.bat    # Script de execução
└── *.csv / *.png           # Arquivos de dados e gráficos (gerados)
```
---


## Como Usar 🚀

1.  **Execução:**
    * **Via `.bat`:** Dê um duplo clique em `Executar_Projeto.bat`.
    * **Via Terminal (com `venv` ativo):** `python main.py` e depois `python stock_analyzer.py`.
2.  **Acumulação de Dados:** **Execute o script diariamente.** A análise de correlação e os gráficos só funcionarão após vários dias de coleta.
3.  **Automação:** Use o Agendador de Tarefas do Windows para executar `Executar_Projeto.bat` todos os dias.

---

## Limitações e Observações ⚠️

* `vaderSentiment` é otimizado para inglês; a precisão em português pode variar.
* A coleta depende da disponibilidade e formato do feed RSS.
* Dados do `yfinance` podem ter imprecisões ocasionais.
* Correlação não implica causalidade.
* A análise requer um volume razoável de dados acumulados.

---
