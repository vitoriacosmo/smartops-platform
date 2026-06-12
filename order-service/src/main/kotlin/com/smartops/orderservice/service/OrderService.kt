package com.smartops.order_service.service

import com.smartops.order_service.model.Order
import com.smartops.order_service.repository.OrderRepository
import org.slf4j.LoggerFactory
import org.springframework.kafka.core.KafkaTemplate
import org.springframework.stereotype.Service

@Service
class OrderService(
    private val repository: OrderRepository,
    private val kafkaTemplate: KafkaTemplate<String, String>
) {
    private val log = LoggerFactory.getLogger(OrderService::class.java)

    fun createOrder(order: Order): Order {
        val saved = repository.save(order)
        log.info("Order created: id=${saved.id} product=${saved.product}")

        // Publica evento no Kafka
        kafkaTemplate.send("orders.created", saved.id ?: "", saved.toJson())
        log.info("Event sent to Kafka: orders.created id=${saved.id}")

        return saved
    }

    fun listOrders(): List<Order> = repository.findAll()

    fun getOrder(id: String): Order =
        repository.findById(id).orElseThrow { RuntimeException("Order not found: $id") }

    private fun Order.toJson() =
        """{"id":"$id","product":"$product","quantity":$quantity,"price":$price,"status":"$status"}"""
}