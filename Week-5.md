# Week 5: Advanced Cloud Services & Networking

📌 Overview  
This week focuses on container registries, databases, web app deployment, container synchronization, VM load balancing, internet connectivity, and VNet peering.

---

## 🌐 Day 29 (2026-08-01): Working with Azure Container Registry (ACR)
**Scenario:** The Nautilus DevOps team needed to store and manage container images securely in Azure.  
**Steps Taken:**  
# Week 5: Advanced Cloud Services & Networking

📌 Overview  
This week focuses on container registries, databases, web app deployment, container synchronization, VM load balancing, internet connectivity, and VNet peering.

---

## 🌐 Day 29 (2026-08-01): Working with Azure Container Registry (ACR)
**Scenario:** The Nautilus DevOps team needed to store and manage container images securely in Azure.  
**Steps Taken:**  
```bash
az group create --name acr-rg --location eastus
az acr create --resource-group acr-rg --name xfusionacr --sku Basic
az acr login --name xfusionacr
docker tag nginx xfusionacr.azurecr.io/nginx:v1
docker push xfusionacr.azurecr.io/nginx:v1


Outcome: Image successfully pushed to ACR and available for deployments.
Reflection: ACR centralizes image management and integrates seamlessly with Azure services.

🎯 XP Earned: 500 XP

🌐 Day 30 (2026-08-02): Create Azure SQL Database
Scenario: Provision a managed SQL database for application data.
Steps Taken:
az sql server create --name xfusion-sqlsrv --resource-group acr-rg \
 --location eastus --admin-user azureuser --admin-password MyP@ssword123

az sql db create --resource-group acr-rg --server xfusion-sqlsrv \
 --name xfusiondb --service-objective S0


Outcome: SQL database created and ready for connections.
Reflection: Azure SQL Database reduces overhead by handling backups, patching, and scaling automatically.

🎯 XP Earned: 500 XP

🌐 Day 31 (2026-08-03): Deploying and Managing a Web Application
Scenario: Deploy a sample web app to Azure App Service.
Steps Taken:
az webapp up --resource-group acr-rg --name xfusion-webapp --runtime "PYTHON:3.9"


Outcome: Web app deployed and accessible via public URL.
Reflection: App Service simplifies deployment and scaling without managing servers.

🎯 XP Earned: 500 XP

🌐 Day 32 (2026-08-04): Synchronizing Containers Using the CLI
Scenario: Ensure container images are synchronized between local Docker and ACR.
Steps Taken:
docker pull nginx:latest
docker tag nginx:latest xfusionacr.azurecr.io/nginx:latest
docker push xfusionacr.azurecr.io/nginx:latest
az acr repository list --name xfusionacr --output table


Outcome: Containers synchronized successfully with ACR.
Reflection: CLI automation ensures consistency across environments.

🎯 XP Earned: 500 XP

🌐 Day 33 (2026-08-05): Integrating Virtual Machines with Application Load Balancer
Scenario: Distribute traffic across multiple VMs using Azure Load Balancer.
Steps Taken:
az network lb create --resource-group acr-rg --name xfusion-lb --sku Basic \
 --frontend-ip-name LoadBalancerFrontEnd --backend-pool-name xfusion-backend

az network lb rule create --resource-group acr-rg --lb-name xfusion-lb \
 --name xfusion-http-rule --protocol Tcp --frontend-port 80 --backend-port 80 \
 --frontend-ip-name LoadBalancerFrontEnd --backend-pool-name xfusion-backend


Outcome: Load Balancer evenly distributed traffic across VMs.
Reflection: Improves availability and resilience of applications.

🎯 XP Earned: 500 XP

🌐 Day 34 (2026-08-06): Enabling Internet Connectivity for Virtual Machines
Scenario: The Nautilus DevOps team needed to enable outbound internet access for VMs to download updates and connect to external services.

Steps Taken:

Associated a public IP address with the VM’s network interface.

Updated the Network Security Group (NSG) to allow outbound traffic on ports 80 (HTTP) and 443 (HTTPS).

Verified connectivity using ping and curl commands from inside the VM.

Outcome: The VM successfully accessed external internet resources, confirming outbound connectivity.
Reflection: Internet connectivity is essential for patching, updates, and integrating with external APIs. Proper NSG rules ensure secure access without exposing unnecessary ports.

🎯 XP Earned: 800 XP

🌐 Day 35 (2026-08-07): Configuring Virtual Network Peering
Scenario: Connect two VNets for secure communication.
Steps Taken:
az network vnet peering create --name vnet1-to-vnet2 --resource-group acr-rg \
 --vnet-name vnet1 --remote-vnet vnet2 --allow-vnet-access



🎯 XP Earned: 500 XP

Week 5 Summary
Total XP Earned: 3,800 XP
Cumulative XP: 20,300 XP
