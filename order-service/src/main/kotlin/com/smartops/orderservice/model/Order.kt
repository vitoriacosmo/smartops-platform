package com.smartops.order_service.model

import jakarta.persistence.*
import java.math.BigDecimal
import java.time.LocalDateTime

@Entity
@Table(name = "orders")
data class Order(
    @Id
    @GeneratedValue(strategy = GenerationType.UUID)
    val id: String? = null,

    @Column(nullable = false)
    val customerName: String,

    @Column(nullable = false)
    val product: String,

    @Column(nullable = false)
    val quantity: Int,

    @Column(nullable = false)
    val price: BigDecimal,

    @Enumerated(EnumType.STRING)
    val status: OrderStatus = OrderStatus.PENDING,

    val createdAt: LocalDateTime = LocalDateTime.now()
)

enum class OrderStatus {
    PENDING, PROCESSING, COMPLETED, FAILED
}