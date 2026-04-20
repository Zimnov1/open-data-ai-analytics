variable "resource_group_name" {
  description = "Назва групи ресурсів"
  default     = "rg-lab-monitoring"
}

variable "location" {
  description = "Регіон Azure"
  default     = "West Europe"
}

variable "vm_size" {
  description = "Розмір віртуальної машини"
  default     = "Standard_B1s" 
}

variable "admin_username" {
  description = "Ім'я користувача"
  default     = "azureuser"
}