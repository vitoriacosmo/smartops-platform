from fastapi import FastAPI
from app.metrics import metrics_store
from app.consumer import start_consumer
import logging

logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s [%(levelname)s] %(name)s - %(message)s"
)

app = FastAPI(title="Analytics Service")

@app.on_event("startup")
def startup():
    start_consumer()

@app.get("/health")
def health():
    return {"status": "ok"}

@app.get("/metrics/summary")
def summary():
    return metrics_store.get_summary()

@app.get("/metrics/products")
def by_product():
    return metrics_store.orders_by_product

@app.get("/metrics/revenue")
def revenue():
    return {"total_revenue": metrics_store.total_revenue}