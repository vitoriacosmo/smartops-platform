package com.smartops.notification_service.consumer

import com.smartops.notification_service.service.NotificationService
import org.apache.kafka.clients.consumer.ConsumerRecord
import org.slf4j.LoggerFactory
import org.springframework.kafka.annotation.KafkaListener
import org.springframework.stereotype.Component

@Component
class OrderEventConsumer(
    private val notificationService: NotificationService
) {
    private val log = LoggerFactory.getLogger(OrderEventConsumer::class.java)

    @KafkaListener(topics = ["orders.created"], groupId = "notification-group")
    fun listen(record: ConsumerRecord<String, String>) {
        log.info("Event received from Kafka: key=${record.key()}")
        notificationService.notifyOrderCreated(record.value())
    }
}