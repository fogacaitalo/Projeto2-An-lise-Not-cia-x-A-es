@echo off
title Projeto Noticias e Acoes

echo ===================================================
echo  INICIANDO PROJETO DE ANALISE DE NOTICIAS E ACOES 
echo ===================================================
echo.

echo Navegando para a pasta do projeto...
cd "C:\Users\italofogaca\Desktop\testes\Python\códigos\Projeto2-Análise Noticias x Ações\venv"

echo.
echo Ativando o ambiente virtual (venv)...
call .\venv\Scripts\activate

echo. 
echo ---------------------------------------------------
echo   Executando main.py (Coleta e Sentimento)...
echo ---------------------------------------------------
python main.py

echo.
echo ---------------------------------------------------
echo   Executando stock_analyzer.py (Analise Acoes)...
echo ---------------------------------------------------
python stock_analyzer.py

echo.
echo ===================================================
echo  PROCESSO CONCLUIDO!
echo ===================================================
echo.
echo Pressione qualquer tecla para fechar esta janela...
pause