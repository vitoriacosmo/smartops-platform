# SmartOps Platform

![Order Service CI](https://github.com/vitoriacosmo/smartops-platform/actions/workflows/order-service-ci.yml/badge.svg)
![Notification Service CI](https://github.com/vitoriacosmo/smartops-platform/actions/workflows/notification-service-ci.yml/badge.svg)
![Python Services CI](https://github.com/vitoriacosmo/smartops-platform/actions/workflows/python-services-ci.yml/badge.svg)

Plataforma de monitoramento inteligente de pedidos com microsserviços e IA Generativa.

## 🏗️ Arquitetura

```
[Cliente] → order-service (Kotlin) → PostgreSQL
                    |
                  Kafka
                    |
        ┌───────────┴───────────┐
analytics-service        notification-service
   (Python)                  (Kotlin)
        |
ai-insights-service
  (Python + IA)
```

## 🧩 Serviços

| Serviço | Linguagem | Função | Porta |
|---|---|---|---|
| order-service | Kotlin + Spring Boot | API REST de pedidos | 8080 |
| analytics-service | Python + FastAPI | Cálculo de métricas | 8081 |
| ai-insights-service | Python

## 📡 Endpoints principais

- `POST /orders` (8080) — cria um pedido
- `GET /orders` (8080) — lista pedidos
- `GET /metrics/summary` (8081) — métricas agregadas
- `GET /insights` (8082) — análise gerada por IA

## ⚙️ CI/CD

Cada serviço possui pipeline próprio no GitHub Actions, validando build a cada push.

## 📌 Roadmap

- [x] Microsserviços com comunicação via Kafka
- [x] Integração com IA Generativa
- [x] Pipelines de CI/CD
- [ ] Observabilidade com Grafana
- [ ] Deploy em nuvem (Railway)