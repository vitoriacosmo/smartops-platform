import os
from groq import Groq
from dotenv import load_dotenv

load_dotenv()

client = Groq(api_key=os.getenv("GROQ_API_KEY"))

def generate_insight(metrics: dict) -> str:
    prompt = f"""
    Você é um analista de negócios. Analise as métricas abaixo e gere um insight
    curto e útil em português, com no máximo 3 frases.

    Métricas:
    - Total de pedidos: {metrics.get('total_orders')}
    - Receita total: R${metrics.get('total_revenue')}
    - Pedidos por produto: {metrics.get('orders_by_product')}

    Gere uma análise objetiva com recomendação.
    """

    response = client.chat.completions.create(
        model="llama-3.1-8b-instant",
        messages=[{"role": "user", "content": prompt}],
        max_tokens=200
    )

    return response.choices[0].message.content