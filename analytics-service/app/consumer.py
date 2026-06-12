import json
import threading
from kafka import KafkaConsumer
from app.metrics import metrics_store
import logging

logger = logging.getLogger(__name__)

def start_consumer():
    def consume():
        try:
            consumer = KafkaConsumer(
                "orders.created",
                bootstrap_servers="localhost:9092",
                group_id="analytics-group",
                value_deserializer=lambda m: json.loads(m.decode("utf-8")),
                auto_offset_reset="earliest"
            )
            logger.info("Kafka consumer started")
            for message in consumer:
                order = message.value
                logger.info(f"Order received: {order}")
                metrics_store.record_order(order)
        except Exception as e:
            logger.error(f"Kafka consumer error: {e}")

    thread = threading.Thread(target=consume, daemon=True)
    thread.start()