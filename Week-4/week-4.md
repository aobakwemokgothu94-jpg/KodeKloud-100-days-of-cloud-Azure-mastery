

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

**Points Allocated:**  
- VM Creation: **10 XP**  
- User Data Script: **15 XP**  
- NSG Configuration: **10 XP**  
- Validation & Testing: **5 XP**  

**Total XP Earned: 40**
---
