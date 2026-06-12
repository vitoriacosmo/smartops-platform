from fastapi import FastAPI, HTTPException
import httpx
from app.insights import generate_insight
import logging

logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s [%(levelname)s] %(name)s - %(message)s"
)

logger = logging.getLogger(__name__)

app = FastAPI(title="AI Insights Service")

@app.get("/health")
def health():
    return {"status": "ok"}

@app.get("/insights")
async def get_insights():
    try:
        # Busca métricas do analytics-service via REST
        async with httpx.AsyncClient() as client:
            response = await client.get("http://localhost:8081/metrics/summary")
            metrics = response.json()

        logger.info(f"Metrics fetched: {metrics}")

        # Gera insight com IA
        insight = generate_insight(metrics)
        logger.info(f"Insight generated: {insight}")

        return {
            "metrics": metrics,
            "insight": insight
        }
    except Exception as e:
        logger.error(f"Error generating insight: {e}")
        raise HTTPException(status_code=500, detail=str(e))