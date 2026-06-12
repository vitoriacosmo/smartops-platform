from collections import defaultdict
from datetime import datetime

class MetricsStore:
    def __init__(self):
        self.total_orders = 0
        self.orders_by_product = defaultdict(int)
        self.total_revenue = 0.0
        self.last_orders = []

    def record_order(self, order: dict):
        self.total_orders += 1
        self.orders_by_product[order.get("product", "unknown")] += 1
        self.total_revenue += float(order.get("price", 0))
        self.last_orders.append({
            "id": order.get("id"),
            "product": order.get("product"),
            "price": order.get("price"),
            "received_at": datetime.now().isoformat()
        })
        # guarda só os últimos 10
        if len(self.last_orders) > 10:
            self.last_orders.pop(0)

    def get_summary(self):
        return {
            "total_orders": self.total_orders,
            "total_revenue": round(self.total_revenue, 2),
            "orders_by_product": dict(self.orders_by_product),
            "last_orders": self.last_orders
        }

metrics_store = MetricsStore()