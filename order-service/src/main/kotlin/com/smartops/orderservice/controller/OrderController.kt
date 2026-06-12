package com.smartops.order_service.controller

import com.smartops.order_service.model.Order
import com.smartops.order_service.service.OrderService
import org.springframework.http.HttpStatus
import org.springframework.web.bind.annotation.*

@RestController
@RequestMapping("/orders")
class OrderController(private val service: OrderService) {

    @PostMapping
    @ResponseStatus(HttpStatus.CREATED)
    fun create(@RequestBody order: Order): Order =
        service.createOrder(order)

    @GetMapping
    fun list(): List<Order> = service.listOrders()

    @GetMapping("/{id}")
    fun get(@PathVariable id: String): Order = service.getOrder(id)
}