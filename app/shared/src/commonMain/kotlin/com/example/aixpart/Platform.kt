package com.example.aixpart

interface Platform {
    val name: String
}

expect fun getPlatform(): Platform