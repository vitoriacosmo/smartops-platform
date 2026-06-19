package com.smartops.notification_service.service

import org.slf4j.LoggerFactory
import org.springframework.stereotype.Service

@Service
class NotificationService {
    private val log = LoggerFactory.getLogger(NotificationService::class.java)

    fun notifyOrderCreated(orderJson: String) {
        // Em produção isso enviaria um email/Slack/SMS de verdade.
        // Aqui simulamos a notificação registrando o evento.
        log.info("📩 Notification sent! New order processed: $orderJson")
    }
}