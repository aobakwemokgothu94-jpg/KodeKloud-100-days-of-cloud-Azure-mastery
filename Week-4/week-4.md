# Week 4: Virtual Machine Configuration & Networking

## 📌 Overview
This week focuses on configuring Azure virtual machines with user data, automating setup via CLI, securing SSH access, managing disk storage, and deploying VMs in both public and private virtual networks.

---

### 🌐 Day 22 (2026-07-24): Configuring Instances with User Data

**Scenario:**  
As a member of the Nautilus DevOps Team, the task was to create a VM with specific configurations and automate Nginx installation using user data.

**Steps Taken:**
1. **VM Creation**
   - Instance Name: `xfusion-vm`
   - Region: East US
   - Image: Ubuntu
   - Size: `Standard_B1s`
   - Disk: Standard HDD
   - Authentication: SSH public key (RSA format)

2. **User Data Script**
   - Enabled *User Data* in the Advanced tab.
   - Added script to install and start Nginx:
     ```bash
     #!/bin/bash
     apt update -y
     apt install -y nginx
     systemctl start nginx
     systemctl enable nginx
     ```

3. **Network Security Group (NSG)**
   - Created inbound port rule for HTTP (port 80).
   - Verified rule in NSG dashboard.

4. **Validation**
   - Retrieved VM public IP and accessed it via browser → Nginx welcome page displayed.
   - SSH into VM using generated key:
     ```bash
     sudo systemctl status nginx
     curl http://<xfusion-vm-ip>
     ```

**Outcome:**  
VM successfully provisioned with automated Nginx installation and accessible via HTTP from the internet.

**Reflection:**  
This exercise reinforced how user data scripts streamline VM setup, ensuring services are installed and running immediately after deployment. It also highlighted the importance of NSG rules for secure and functional access.

**🎯 XP Earned:**  
Day 22 → **500 XP**

---
# Week 4: Virtual Machine Configuration & Networking

## 📌 Overview
This week focuses on configuring Azure virtual machines with user data, automating setup via CLI, securing SSH access, managing disk storage, and deploying VMs in both public and private virtual networks.

---

### 🌐 Day 23 (2026-07-25): Automating User Data Configuration Using the CLI

**Scenario:**  
As a member of the Nautilus DevOps Team, the task was to create a VM using Azure CLI and automate Nginx installation with a cloud-init script.

**Steps Taken:**
1. **Checked Resource Group**
   ```bash
   az group list
#cloud-config
package_upgrade: true
packages:
  - nginx
runcmd:
  - systemctl start nginx
  - systemctl enable nginx

az vm create \
  --resource-group kml_rg_main-06c66b102d8744e8 \
  --name xfusion-vm \
  --image Ubuntu2204 \
  --admin-username azureuser \
  --generate-ssh-keys \
  --custom-data cloud-init.txt \
  --size Standard_B1s \
  --storage-sku Standard_LRS \
  --public-ip-sku Standard
az vm open-port \
  --resource-group kml_rg_main-06c66b102d8744e8 \
  --name xfusion-vm \
  --port 80 \
  --priority 800
curl http://<public-ip>
Outcome:  
VM successfully created using Azure CLI with automated Nginx installation via cloud-init. HTTP traffic allowed through NSG, and service verified as running.

Reflection:  
This exercise highlighted the efficiency of using Azure CLI and cloud-init for automation. It reduced manual steps and ensured consistent VM configuration across deployments.

🎯 XP Earned:  
Day 23 → 500 XP

markdown
# Week 4: Virtual Machine Configuration & Networking

## 📌 Overview
This week focuses on configuring Azure virtual machines with user data, automating setup via CLI, securing SSH access, managing disk storage, and deploying VMs in both public and private virtual networks.

---

### 🌐 Day 24 (2026-07-26): Securing Virtual Machine SSH Access

**Scenario:**  
The Nautilus DevOps team needed to set up a new VM on Azure that could be accessed securely from their landing host (`azure-client`). The goal was to configure password-less SSH access using keys.

**Steps Taken:**
1. **Checked Existing SSH Keys**
   ```bash
   cd ~/.ssh
   ls -a
If no key existed, generated a new one:

bash
ssh-keygen -t rsa
Created Virtual Machine

VM Name: devops-vm

Region: westus

Size: Standard_B1s

Configured with SSH access for azureuser using the generated key.

Configured Password-less SSH Access

Copied id_rsa.pub from azure-client to ~/.ssh/authorized_keys on devops-vm for the azure user account.

Ensured secure, key-based authentication was enabled.

Verified Connectivity

Connected from azure-client:

bash
ssh azureuser@<devops-vm-public-ip>
Checked Nginx service status:

bash
sudo systemctl status nginx
Outcome:  
Secure password-less SSH access was successfully configured between azure-client and devops-vm. The VM could be accessed without a password, improving both security and convenience.

Reflection:  
This exercise reinforced the importance of SSH key-based authentication for secure cloud infrastructure. It eliminated password risks and streamlined DevOps workflows.

🎯 XP Earned:  
Day 24 → 500 XP

### 🌐 Day 25 (2026-07-28): Expanding and Managing Disk Storage

**All-in-One Command Workflow (after resizing OS disk in portal):**

```bash
# Verify disks
lsblk

# Format the new data disk (assuming it's /dev/sdc)
sudo mkfs -t ext4 /dev/sdc

# Create mount point
sudo mkdir -p /mnt/devops-disk

# Mount the disk
sudo mount /dev/sdc /mnt/devops-disk

# Make mount persistent
UUID=$(sudo blkid -s UUID -o value /dev/sdc)
echo "UUID=$UUID   /mnt/devops-disk   ext4   defaults,nofail   1   2" | sudo tee -a /etc/fstab

# Verify mount
df -h /mnt/devops-disk

# Change ownership so azureuser can write without sudo
sudo chown azureuser:azureuser /mnt/devops-disk

# Final checks
lsblk
df -h
🎯 XP Earned:  
Day 25 → 500 XP


### 🌐 Day 26 (2026-07-29): Deploying Virtual Machines in a Public Virtual Network

**Scenario:**  
The Nautilus DevOps team needs to deploy a new VM in a public virtual network. The goal is to configure it with default settings and review the configuration after deployment.

**All-in-One Command Workflow:**

1. **Create the Virtual Network (if not already existing)**  
   ```bash
   az network vnet create \
     --resource-group your-rg-name \
     --name your-vnet-name \
     --address-prefix 10.0.0.0/16
az network vnet subnet create \
  --resource-group your-rg-name \
  --vnet-name your-vnet-name \
  --name your-subnet-name \
  --address-prefix 10.0.1.0/24
az vm create \
  --resource-group your-rg-name \
  --name devops-vm \
  --image Ubuntu2204 \
  --admin-username azureuser \
  --generate-ssh-keys \
  --size Standard_B1s \
  --vnet-name your-vnet-name \
  --subnet your-subnet-name
az vm show --resource-group your-rg-name --name devops-vm
Finalize and Validate  
Leave other settings as default. After reviewing, select Review + Create in the portal to finalize the deployment.

Outcome:  
VM deployed successfully in a public virtual network with default settings.

Reflection:  
This exercise reinforced the process of deploying VMs into a public virtual network, emphasizing the importance of network configuration and VM review before creation.

🎯 XP Earned:  
Day 26 → 500 XP

# Week 4: Virtual Machine Configuration & Networking

## 📌 Overview
This week focuses on configuring Azure virtual machines with user data, automating setup via CLI, securing SSH access, managing disk storage, and deploying VMs in both public and private virtual networks.

---

### 🌐 Day 27 (2026-07-30): Deploying Virtual Machines in a Private Virtual Network

**Scenario:**  
The Nautilus DevOps team needed to set up a private Virtual Network (VNet) and subnet to ensure resources remain isolated from external networks. The goal was to create a VM accessible only via SSH within the VNet, secured by a Network Security Group (NSG) allowing internal traffic only.

**All-in-One Command Workflow:**

```bash
# Create a private virtual network and subnet
az network vnet create \
  --resource-group your-rg-name \
  --name xfusion-priv-vnet \
  --address-prefix 10.1.0.0/16 \
  --subnet-name xfusion-priv-subnet \
  --subnet-prefix 10.1.1.0/24 \
  --location eastus

# Create a Network Security Group (NSG)
az network nsg create \
  --resource-group your-rg-name \
  --name xfusion-priv-nsg \
  --location eastus

# Add rule to allow SSH only from within the VNet CIDR block
az network nsg rule create \
  --resource-group your-rg-name \
  --nsg-name xfusion-priv-nsg \
  --name AllowInternalSSH \
  --protocol Tcp \
  --direction Inbound \
  --priority 100 \
  --source-address-prefixes 10.1.0.0/16 \
  --source-port-ranges '*' \
  --destination-port-ranges 22 \
  --access Allow

# Create the VM under the private VNet
az vm create \
  --resource-group your-rg-name \
  --name xfusion-priv-vm \
  --image Ubuntu2204 \
  --admin-username azureuser \
  --generate-ssh-keys \
  --size Standard_B1s \
  --vnet-name xfusion-priv-vnet \
  --subnet xfusion-priv-subnet \
  --nsg xfusion-priv-nsg \
  --location eastus

# Verify VM network configuration
az vm show --resource-group your-rg-name --name xfusion-priv-vm --query "networkProfile"
Outcome:  
A private VNet (xfusion-priv-vnet) and subnet (xfusion-priv-subnet) were successfully created in East US. The VM (xfusion-priv-vm) was deployed within this network, secured by an NSG (xfusion-priv-nsg) allowing SSH access only from within the VNet CIDR block.

Reflection:  
This exercise demonstrated how private VNets enhance isolation and security in cloud environments. Restricting SSH access to internal traffic ensures controlled communication and protects resources from external exposure.

🎯 XP Earned:  
Day 27 → 500 XP

### 🌐 Day 28 (2026-07-31): Week 4 Summary and Review

**Summary:**  
This week focused on advanced Azure VM configuration and networking. You successfully:
- Automated VM provisioning using user data and cloud-init scripts.  
- Secured SSH access with key-based authentication.  
- Expanded and managed disk storage, including persistent mounts.  
- Deployed VMs in both public and private virtual networks with proper NSG rules.  

**Key Learnings:**  
- Automation through CLI and scripts ensures consistency and scalability.  
- SSH key management is critical for secure DevOps operations.  
- Disk management and mounting workflows improve data organization and performance.  
- Network isolation via private VNets enhances security and internal communication.  

**Total XP Earned This Week:**  
- Day 22 → 500 XP  
- Day 23 → 500 XP  
- Day 24 → 500 XP  
- Day 25 → 500 XP  
- Day 26 → 500 XP  
- Day 27 → 500 XP  
- **Total Week 4 XP: 3,000 XP**

**Cumulative XP:**  
**16,500 XP**

--- 

