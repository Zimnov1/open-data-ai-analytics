output "public_ip_address" {
  description = "Публічна IP-адреса віртуальної машини"
  value       = azurerm_public_ip.pip.ip_address
}

output "grafana_url" {
  description = "Посилання на інтерфейс Grafana"
  value       = "http://${azurerm_public_ip.pip.ip_address}:3000"
}

output "prometheus_url" {
  description = "Посилання на інтерфейс Prometheus"
  value       = "http://${azurerm_public_ip.pip.ip_address}:9090"
}