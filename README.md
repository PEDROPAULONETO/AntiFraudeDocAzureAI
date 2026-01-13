# AntiFraude Azure AI 🛡️

Sistema de detecção de fraudes em cartões de crédito utilizando Azure AI e Streamlit.

## 📋 Sobre o Projeto

Este projeto é uma aplicação web desenvolvida em Python que permite o upload de imagens de cartões de crédito para análise. O sistema armazena as imagens no Azure Blob Storage e realiza a validação de dados para identificar possíveis fraudes.

## 🚀 Tecnologias Utilizadas

*   [Python](https://www.python.org/)
*   [Streamlit](https://streamlit.io/) - Interface Web
*   [Azure Blob Storage](https://azure.microsoft.com/en-us/services/storage/blobs/) - Armazenamento de Imagens
*   [Azure AI Document Intelligence](https://azure.microsoft.com/en-us/services/ai-services/document-intelligence/) - Processamento de Documentos

## ⚙️ Configuração e Instalação

### Pré-requisitos

*   Python 3.9 ou superior
*   Conta no Microsoft Azure
*   Storage Account e Container criados no Azure

## ▶️ Como Executar

Para iniciar a aplicação, execute o comando abaixo a partir da raiz do projeto:

```bash
streamlit run src/app.py
```

## 📂 Estrutura do Projeto

*   `src/app.py`: Arquivo principal da aplicação.
*   `src/services/blob_service.py`: Lógica de upload para o Azure Blob Storage.
*   `src/utils/Config.py`: Configurações da página e variáveis de ambiente.
*   `src/requirements.txt`: Lista de dependências do projeto.
