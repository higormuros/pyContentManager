import requests
from dotenv import load_dotenv
import os

load_dotenv()

class GoogleAIStudioClient:
    def __init__(self):
        """
        Inicializa o cliente carregando a chave de API do arquivo .env.
        """
        self.api_key = os.getenv("GOOGLE_API_KEY")
        if not self.api_key:
            raise ValueError("A chave de API do Google AI Studio não foi encontrada no arquivo .env.")
        self.base_url = "https://generativelanguage.googleapis.com/v1beta"

    def enviar_texto(self, model_name, prompt):
        """
        Envia um texto (prompt) para o modelo especificado e retorna a resposta como JSON.

        Args:
            model_name (str): O nome do modelo do Google AI Studio a ser utilizado (ex: "gemini-pro").
            prompt (str): O texto a ser enviado para o modelo.

        Returns:
            dict: Um dicionário Python representando a resposta JSON da API.
                  Retorna None em caso de erro na requisição.
        """
        url = f"{self.base_url}/models/{model_name}:generateContent?key={self.api_key}"
        headers = {
            "Content-Type": "application/json",
        }
        data = {
            "contents": [
                {
                    "parts": [{"text": prompt}]
                }
            ],
        }

        try:
            response = requests.post(url, headers=headers, json=data)
            response.raise_for_status()
            return response.json()
        except requests.exceptions.RequestException as e:
            print(f"Erro ao enviar a requisição: {e}")
            return None
