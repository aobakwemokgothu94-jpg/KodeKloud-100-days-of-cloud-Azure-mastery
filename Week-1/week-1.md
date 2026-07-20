📘 Week 1: Azure Fundamentals in Action

# Day 1: Create SSH Key Pair for Azure Virtual Machine

## ✅ Task
Create an SSH key pair with the following requirements:
- Name: `xfusion‑kp`
- Type: `rsa`

## 🛠️ Steps Taken
1. Login to Azure Dashboard  
   ![Step 1](<uploaded image placeholder>)
2. Search for **SSH Keys** and click on it.  
   ![Step 2](<uploaded image placeholder>)
3. Click on **Create**.  
   ![Step 3](<uploaded image placeholder>)
4. Set key name as `xfusion‑kp`, choose **RSA SSH Format**, then click **Review + Create**.  
   ![Step 4](<uploaded image placeholder>)

## 📓 Notes
- RSA is the most common format for SSH keys in Azure.  
- Keys can be reused for VM deployments, ensuring secure access.

## 🎯 XP Earned
+500 XP

Day 2 (2026-06-25):  
Deployed our first Azure Virtual Machine using the Azure Portal.
# Day 2: Create an Azure Virtual Machine

## ✅ Task
The Nautilus DevOps team is migrating part of its infrastructure to Azure. Today’s goal is to create a Virtual Machine (VM) that meets these requirements:
- Use the existing resource group.
- VM name: `xfusion-vm`
- Region: **West US**
- Image: **Ubuntu 22.04 LTS**
- Size: **Standard_B1s**
- Network Security Group (NSG): allow inbound **SSH (port 22)**
- Disk: **30 GB Standard HDD**
- Other configurations: default.

## 🛠️ Steps Taken
1. Go to the **Virtual Machine Dashboard** and click **Create** to start a new VM.  
   ![Step 1](<uploaded image placeholder>)
2. Select the default resource group, VM name, and region.  
   ![Step 2](<uploaded image placeholder>)
3. Choose the **Ubuntu 22.04 LTS** image and **Standard_B1s** size.  
   ![Step 3](<uploaded image placeholder>)
4. Create an **RSA SSH key** and allow inbound SSH traffic on port 22.  
5. Configure the disk: **30 GB Standard HDD**.  
6. Review all settings and click **Create** to deploy the VM.

## 📓 Notes
- Learned how NSGs control inbound traffic.  
- Disk type and size must be explicitly set; defaults may vary.  
- The Azure portal simplifies VM creation with guided steps.

## 🖼️ Screenshot
![Azure VM Creation](<uploaded image placeholder>)

## 🎯 XP Earned
+500 XP

Day 3 (2026-06-26):  
Practiced creating a VM via Azure CLI, reinforcing command-line skills.
# 📘 Week 1: Azure Fundamentals in Action

## Day 3 (2026‑06‑26)  
Created a Virtual Machine using the **Azure CLI** to automate deployment and resource management.

---

# Day 3: Create VM using Azure CLI

## ✅ Task
The Nautilus DevOps team is migrating workloads to Azure. Today’s goal: create a VM using the **Azure CLI** instead of the portal.

### Requirements
- Admin username: `azureuser`
- SSH keys: auto‑generated for secure access
- Storage account: `Standard_LRS`
- Disk size: 30 GB
- VM name: `devops‑vm`
- VM size: `Standard_B2s`
- Ensure the VM is in **running** state after creation.
az vm create \
  --resource-group devops-rg \   # Change based on Step 1 result
  --name devops-vm \
  --image Ubuntu2204 \
  --size Standard_B2s \
  --admin-username azureuser \
  --generate-ssh-keys \
  --storage-sku Standard_LRS \
  --os-disk-size-gb 30
3.<img width="892" height="767" alt="image" src="https://github.com/user-attachments/assets/8fa8de30-30c6-41c0-9794-2bf94fd3d09f" />
 
Day 4 (2026-06-28):  
Built a Virtual Network (VNet) to enable secure communication between resources.
# 📘 Week 1: Azure Fundamentals in Action

## Day 4 (2026‑06‑27)  
Created a Virtual Network (VNet) in Azure to establish a secure, isolated environment for resources.

---

# Day 4: Create a Virtual Network (VNet) in Azure

## ✅ Task
Create a Virtual Network (VNet) named `nautilus‑vnet` in the **East US** region with any IPv4 CIDR block.

---

## 🛠️ Steps Taken
1. Go to **Virtual Network Dashboard**, enter VNet name and choose region.  
   ![Step 1](<uploaded image placeholder>)
2. As there are no further requirements, click **Review + Create** to deploy the VNet.  
   ![Step 2](<uploaded image placeholder>)
3. Confirm deployment completion and verify that the VNet resource is active.

---

## 📓 Notes
- VNets provide logical isolation for Azure resources.  
- CIDR blocks define IP address ranges for subnets.  
- This setup prepares the environment for future subnet and NSG configurations.

## 🖼️ Screenshot
![Deployment Overview](<uploaded image placeholder>)

## 🎯 XP Earned
+500 XP

Day 5 (2026-06-29):  
Configured a Virtual Network with IPv4 addressing, learning about IP ranges and allocation.
# 📘 Week 1: Azure Fundamentals in Action

## Day 5 (2026‑06‑28)  
Configured a Virtual Network (VNet) with a custom IPv4 address space in Azure.

---

# Day 5: Create a Virtual Network (IPv4) in Azure

## ✅ Task
Create a Virtual Network (VNet) named `nautilus‑vnet` in the **East US** region with the IPv4 CIDR block `192.168.0.0/24`.

---

## 🛠️ Steps Taken
1. In the Azure portal, search for and select **Virtual networks**.  
2. On the **Virtual networks** page, click **+ Create**.  
3. On the **Basics** tab, enter or select:  
   - **Subscription:** Azure Free Labs  
   - **Resource group:** `kml_rg‑main‑2c8d27913d34fe7`  
   - **Virtual network name:** `nautilus‑vnet`  
   - **Region:** (US) East US  
   ![Step 1](<uploaded image placeholder>)
4. Click **Next** to proceed to the **Security** tab.  
5. Click **Next** again to reach the **IP Addresses** tab and delete all existing address spaces.  
   ![Step 2](<uploaded image placeholder>)
6. In **Add IPv4 Address space**, enter `192.168.0.0/24` to meet the challenge requirement.  
   ![Step 3](<uploaded image placeholder>)
7. Review the configuration and click **Review + Create** to deploy the VNet.

---

## 📓 Notes
- Learned how to define custom IPv4 CIDR blocks in Azure.  
- Removing default address spaces ensures precise network segmentation.  
- This configuration prepares the environment for subnet and Bastion host setup.

## 🖼️ Screenshot
![IPv4 Configuration](<uploaded image placeholder>)

## 🎯 XP Earned
+500 XP
Day 6 (2026-07-02):  
Added a Subnet inside the VNet to segment network traffic logically.
# 📘 Week 1: Azure Fundamentals in Action

## Day 6 (2026‑06‑29)  
Created a subnet within an Azure Virtual Network to define address segmentation and improve resource isolation.

---

# Day 6: Create a Subnet in Azure Virtual Network

## ✅ Task
Create a Virtual Network (VNet) named `datacenter‑vnet` and one subnet named `datacenter‑subnet` within the VNet in the **East US** region.  
Ensure the IPv4 address range is `10.0.0.0/16`.

---

## 🛠️ Steps Taken
1. Under the **Basic** tab, create a **Virtual Network** using the existing resource group `datacenter‑vnet` in **East US**.  
   ![Step 1](<uploaded image placeholder>)
2. Click **Next**, go to the **IP Address** tab, and edit the default subnet:  
   - Subnet name: `datacenter‑subnet`  
   - IPv4 address range: `10.0.0.0/16`  
   - Starting address: `10.0.0.0`  
   - Size: `/24 (256 addresses)`  
   ![Step 2](<uploaded image placeholder>)
3. Save the subnet configuration and verify that the subnet name and address space are correct (`10.0.0.0/16`).

---

## 📓 Notes
- Learned how to define subnets within a VNet to segment resources logically.  
- Subnets enable better traffic control and security management.  
- CIDR notation helps allocate IP ranges efficiently.

## 🖼️ Screenshot
![Subnet Configuration](<uploaded image placeholder>)

## 🎯 XP Earned
+500 XP

Day 7 (2026-07-04):  
Created a Public IP Address for our VM, enabling external access.
# 📘 Week 1: Azure Fundamentals in Action

## Day 7 (2026‑06‑30)  
Created a Public IP Address for the Azure Virtual Machine to enable external connectivity.

---

# Day 7: Create a Public IP Address for Azure VM

## ✅ Task
Allocate a **Public IP Address** named `datacenter‑pip` for the VM in the **East US** region.

---

## 🛠️ Steps Taken
1. In the Azure portal, search for and select **Public IP addresses**.  
   ![Step 1](<uploaded image placeholder>)
2. On the **Public IP addresses** page, click **Create**.  
   ![Step 2](<uploaded image placeholder>)
3. On the **Basics** tab of the **Create public IP address** screen, enter required values:  
   - **Subscription:** Azure Free Labs  
   - **Resource group:** `kml_rg_main‑dfc2f0ac2d579482a`  
   - **Region:** (US) East US  
   - **Name:** `datacenter‑pip`  
   ![Step 3](<uploaded image placeholder>)
4. Review the configuration and click **Review + Create** to deploy the Public IP Address.

---

## 📓 Notes
- Public IP addresses allow inbound and outbound communication between Azure resources and the internet.  
- Each VM can be associated with a unique Public IP for external access.  
- This completes the networking foundation for the VM created earlier.

## 🖼️ Screenshot
![Public IP Creation](<uploaded image placeholder>)

## 🎯 XP Earned
+500 XP
# 
# 📘 Week 1: Azure Fundamentals in Action

## 🗓️ Overview
This week focused on mastering Azure’s foundational services — from secure VM access to networking and automation. Each daily task earned **500 XP**, totaling **3 500 XP** for the week.

---

## 🧩 Daily Logs
| Day | Date | Task | XP Earned |
|-----|------|------|-----------|
| 1 | 2026‑06‑24 | Create SSH Key Pair for Azure VM | 500 XP |
| 2 | 2026‑06‑25 | Create Azure Virtual Machine via Portal | 500 XP |
| 3 | 2026‑06‑26 | Create VM using Azure CLI | 500 XP |
| 4 | 2026‑06‑27 | Create Virtual Network (VNet) in Azure | 500 XP |
| 5 | 2026‑06‑28 | Configure VNet with IPv4 Addressing | 500 XP |
| 6 | 2026‑07‑02 | Add Subnet to VNet | 500 XP |
| 7 | 2026‑07‑04 | Create Public IP Address for VM | 500 XP |

**Total XP for Week 1:** 3 500 XP  
**Cumulative XP:** 3 500 XP

---

## ✨ Reflection
This week gave hands‑on exposure to Azure’s core building blocks:
- **Compute:** Creating and managing VMs via Portal and CLI.  
- **Networking:** Building VNets, subnets, and public IPs.  
- **Security:** Using SSH keys and NSGs for secure access.  

It set the stage for deeper exploration in the coming weeks. You’ve now mastered the basics of Azure compute and networking — the foundation for everything that follows.

---

## 🔗 Quick Access
- [Day 1 – Create SSH Key Pair](Day‑1.md)
- [Day 2 – Create Azure Virtual Machine](Day‑2.md)
- [Day 3 – Create VM using Azure CLI](Day‑3.md)
- [Day 4 – Create Virtual Network (VNet)](Day‑4.md)
- [Day 5 – Configure VNet with IPv4 Addressing](Day‑5.md)
- [Day 6 – Add Subnet to VNet](Day‑6.md)
- [Day 7 – Create Public IP Address for VM](Day‑7.md)

---

## 🎯 XP Tracker
Weekly_XP = 3500
Cumulative_XP = 3500
