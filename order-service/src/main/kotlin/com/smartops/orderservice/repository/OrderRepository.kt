package com.smartops.order_service.repository

import com.smartops.order_service.model.Order
import org.springframework.data.jpa.repository.JpaRepository

interface OrderRepository : JpaRepository<Order, String>