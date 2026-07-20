📘 Week 2: Azure Networking Deep Dive
  
# 📘 Week 2: Azure Networking & Automation

## Day 8 (2026‑07‑05)  
Attached a managed disk to an existing Azure Virtual Machine to expand storage capacity.

# Day 8: Attach Managed Disk to Azure Virtual Machine

## ✅ Task
An existing VM named `nautilus‑vm` and a managed disk named `nautilus‑disk` already exist in the **East US** region.  
Attach the disk `nautilus‑disk` to the VM `nautilus‑vm` as a data disk.  
Ensure the disk is properly attached and the VM initialization is complete before submission.

---

## 🛠️ Steps Taken
1. Sign in to the **Azure portal**.  
2. Search for and select **Virtual machines**.  
3. Choose the VM named `nautilus‑vm` from the list.  
   ![Step 1](<uploaded image placeholder>)
4. On the VM pane, under **Settings**, select **Disks**.  
   ![Step 2](<uploaded image placeholder>)
5. Under **Data disk**, choose **Attach existing disk** and select the existing disk `nautilus‑disk`.  
   ![Step 3](<uploaded image placeholder>)
6. Confirm the disk attachment and save changes.

---

## 📓 Notes
- Managed disks simplify storage management and improve reliability.  
- Attaching existing disks allows flexible scaling without recreating VMs.  
- Always verify disk encryption and performance tiers (LRS, ZRS, etc.) before deployment.

## 🖼️ Screenshot
![Disk Attachment Overview](<uploaded image placeholder>)

## 🎯 XP Earned
+500 XP

# 📘 Week 2: Azure Networking & Automation

## Day 9 (2026‑07‑06)  
Attached a Network Interface Card (NIC) to an existing Azure Virtual Machine to enable additional network connectivity.

# Day 9: Attach Network Interface Card (NIC) to Azure Virtual Machine

## ✅ Task
An existing VM named `nautilus‑vm` and a network interface named `nautilus‑nic` already exist in the **West US** region.  
Attach the network interface `nautilus‑nic` to the VM `nautilus‑vm`.  
Ensure the NIC’s status is **attached** before submitting the task.

---

## 🛠️ Steps Taken
1. Go to the **Azure portal** and search for **Virtual machines**.  
2. Select the VM named `nautilus‑vm`.  
3. On the **Overview** page, click **Stop**, confirm with **Yes**, and wait until the VM status changes to **Stopped (deallocated)**.  
   ![Step 1](<uploaded image placeholder>)
4. Navigate to **Networking → Attach network interface**.  
   - Choose **Attach existing network interface**.  
   - Select the NIC `nautilus‑nic`.  
   - Click **OK** to confirm.  
   ![Step 2](<uploaded image placeholder>)
5. Return to **Overview → Start** to restart the VM and verify that the NIC is attached successfully.

---

## 📓 Notes
- Attaching NICs allows VMs to communicate across multiple networks.  
- VM sizes determine how many NICs can be attached — always verify compatibility.  
- The NIC must be in the same region and resource group as the VM.

## 🖼️ Screenshot
![NIC Attachment Overview](<uploaded image placeholder>)

## 🎯 XP Earned
+500 XP

Day 10 (2026-07-07):  
Explored Azure DNS Zones and custom domain setup.
# 📘 Week 2: Azure Networking & Automation

## Day 10 (2026‑07‑07)  
Attached a Public IP Address to an existing Azure Virtual Machine to enable external connectivity.

---

# Day 10: Attach Public IP to Azure Virtual Machine

## ✅ Task
An existing VM named `nautilus‑vm‑pip` and a Public IP Address named `nautilus‑pip` already exist in the **West US** region.  
Attach the public IP `nautilus‑pip` to the network interface of the VM `nautilus‑vm‑pip`.  
Ensure the VM is properly assigned the public IP before submission.

---

## 🛠️ Steps Taken
1. Sign in to the **Azure portal**.  
2. Search for and select the VM `nautilus‑vm‑pip`.  
3. Under **Settings → Networking**, select the network interface to which the public IP will be added.  
   ![Step 1](<uploaded image placeholder>)
4. From the **Network interface** window, under **Settings**, select **IP configurations**.  
   - Enable **IP forwarding**.  
   - Select an IP configuration from the list.  
   ![Step 2](<uploaded image placeholder>)
5. In the **Edit IP configuration** window, select **Associate public IP address**, then choose **Public IP address** from the drop‑down list.  
6. Click **Apply** to save changes.  
7. Search for **Public IP Addresses** and verify that `nautilus‑pip` is attached successfully.

---

## 📓 Notes
- Public IP addresses enable inbound and outbound communication between Azure resources and the internet.  
- Each VM can be associated with a unique Public IP for external access.  
- Always confirm IP forwarding and configuration status after association.

## 🖼️ Screenshot
![Public IP Association Overview](<uploaded image placeholder>)

## 🎯 XP Earned
+500 XP

Week 2: Azure Networking & Automation

Day 11: Change Azure Virtual Machine Size Using SSH
✅ Task
An existing VM named xfusion‑vm is running in the West US region with size Standard_B1s.
Resize the VM to Standard_B2s using SSH/CLI and ensure it remains in the running state after the change.

🛠️ Steps Taken (SSH/CLI)
bash
ssh azureuser@<public-ip-of-xfusion-vm> "az vm resize --resource-group <your-resource-group> --name xfusion-vm --size Standard_B2s && az vm get-instance-view --resource-group <your-resource-group> --name xfusion-vm --query \"instanceView.statuses[?code=='PowerState/running']\""
Replace <public-ip-of-xfusion-vm> with the VM’s public IP.

Replace <your-resource-group> with the actual resource group name.

azureuser is the VM’s admin username.

This one‑liner connects via SSH, resizes the VM, and immediately checks that it’s running.

📓 Notes
VM sizes define CPU, memory, and performance capacity.

Standard_B1s → 1 vCPU, 1 GiB RAM (entry‑level).

Standard_B2s → 2 vCPUs, 4 GiB RAM (better performance for workloads).

Resizing may restart the VM briefly; always confirm its status afterward.

Using SSH + Azure CLI allows automation without portal clicks.
<img width="899" height="1288" alt="image" src="https://github.com/user-attachments/assets/9fa7e1f6-0100-45cd-a2e4-6851ddf7ccd4" />
🎯 XP Earned
+500 XP

Day 12 (2026-07-09):  
Configured VPN Gateway for hybrid connectivity.
📘 Week 2: Azure Networking & Automation
Day 12 (2026‑07‑09)
Added and managed tags for an Azure Virtual Machine to improve resource organization.

Day 12: Add and Manage Tags for Azure Virtual Machines
✅ Task
Add the tag Environment=dev to the virtual machine named datacenter‑vm.
Confirm that the tag is applied successfully.

🛠️ Steps Taken (Azure Portal)
Sign in to the Azure portal.

Navigate to Virtual machines and select the VM named datacenter‑vm.

In the navigation pane, select Tags.

Enter the tag key Environment and value dev.

Click Apply to save the tag.

Verify that the tag appears under the VM’s Tags section.

🛠️ Steps Taken (SSH/CLI)
bash
ssh azureuser@<public-ip-of-datacenter-vm> "az vm update --resource-group <your-resource-group> --name datacenter-vm --set tags.Environment=dev && az vm show --resource-group <your-resource-group> --name datacenter-vm --query tags"
Replace <public-ip-of-datacenter-vm> with the VM’s public IP.

Replace <your-resource-group> with the actual resource group name.

This one‑liner connects via SSH, applies the tag, and immediately queries the VM to confirm the tag is present.

📓 Notes
Tags help organize resources by environment, department, or cost center.

They are key‑value pairs applied to Azure resources.

Tags can be used for automation, billing, and policy enforcement.

Example: Environment=dev, Owner=AOBAKWE, Project=CloudLab.

🖼️ Screenshot
(<img width="903" height="1288" alt="image" src="https://github.com/user-attachments/assets/449bd383-22dd-4467-9093-92bc947e9bc7" />
)

🎯 XP Earned
+500 XP
Day 13 (2026-07-10):  
Set up Application Gateway with WAF for web apps.
📘 Week 2: Azure Networking & Automation
Day 13 (2026‑07‑10)
Configured secure SSH access for an Azure Virtual Machine by adding the root user’s public key.

Day 13: SSH into an Azure Virtual Machine
✅ Task
The VM named nautilus‑vm is running in the West US region.
The default SSH user is azureuser.
Add the root user’s SSH public key from the Azure client host (/root/.ssh/id_rsa.pub) to the authorized_keys file of the root user on nautilus‑vm.
Verify password‑less SSH access as root.

🛠️ Steps Taken (SSH/CLI)
On the Azure client host, display the root public key:

bash
sudo cat /root/.ssh/id_rsa.pub
Copy the public key to the VM:

bash
ssh azureuser@<nautilus-vm-ip> "sudo mkdir -p /root/.ssh && sudo sh -c 'cat >> /root/.ssh/authorized_keys'" < /root/.ssh/id_rsa.pub
Set proper permissions on the VM:

bash
ssh azureuser@<nautilus-vm-ip> "sudo chmod 700 /root/.ssh && sudo chmod 600 /root/.ssh/authorized_keys && sudo chown -R root:root /root/.ssh"
Verify root login without password:

bash
ssh root@<nautilus-vm-ip>
📓 Notes
SSH keys enable secure, password‑less authentication.

The authorized_keys file must have strict permissions (600) and the .ssh directory must be 700.

Always ensure firewall/security group rules allow inbound SSH (port 22).

Root login may require enabling in /etc/ssh/sshd_config (PermitRootLogin yes).

🖼️ Screenshot
(<img width="852" height="1208" alt="image" src="https://github.com/user-attachments/assets/c5e5041d-31f4-4b56-be53-8930603221cc" />
)

🎯 XP Earned
+500 XP
Day 14 (2026-07-11):  
Reviewed and tested networking configurations.
📘 Week 2: Azure Networking & Automation
Day 14 (2026‑07‑11)
Created and attached a managed disk to an Azure Virtual Machine.

Day 14: Create and Attach Managed Disks in Azure
✅ Task
Create a managed disk with the following requirements:

Disk name: datacenter‑disk

Disk type: Standard_LRS

Disk size: 2 GiB

Attach the disk to the target VM.

🛠️ Steps Taken (Azure Portal)
Sign in to the Azure portal.

Navigate to Disks under Storage.

Click Create.

Under the Basics tab:

Select the appropriate Resource group.

Enter disk name: datacenter‑disk.

Choose Region (same as VM).

Set Size to 2 GiB.

Select Standard_LRS (Standard HDD).

Click Review + Create → Create.

After creation, go to the target VM (datacenter‑vm).

In the VM menu, select Disks → Attach existing disk.

Choose datacenter‑disk and attach it.

Verify the disk is listed under the VM’s Disks section.

🛠️ Steps Taken (SSH/CLI)
bash
# Create the managed disk
az disk create --resource-group <your-resource-group> --name datacenter-disk --size-gb 2 --sku Standard_LRS

# Attach the disk to the VM
az vm disk attach --resource-group <your-resource-group> --vm-name datacenter-vm --name datacenter-disk
Replace <your-resource-group> with the actual resource group name.

--sku Standard_LRS specifies Standard HDD.

--size-gb 2 sets the disk size to 2 GiB.

📓 Notes
Managed disks simplify storage management in Azure.

Standard_LRS = locally redundant storage, cost‑effective for dev/test workloads.

Always ensure the disk region matches the VM region.

After attaching, the disk must be partitioned and formatted inside the VM OS before use.

🖼️ Screenshot
<img width="816" height="1288" alt="image" src="https://github.com/user-attachments/assets/effe1fcf-5428-40bd-bdd9-4f1105e6d13f" />
()

🎯 XP Earned
+500 XP
🎯 Experience Points Earned: 500  
✨ Weekly Reflection:  
This week strengthened our networking skills — from NSGs and load balancers to secure access with Bastion and hybrid connectivity with VPN Gateway.
📘 Week 2: Azure Networking & Automation — Summary
🗓️ Days 8–14 Overview
This week focused on strengthening Azure VM management skills, automation with CLI/SSH, and resource organization. Each day built on practical DevOps tasks that mirror real‑world cloud operations.

📌 Day 8
Task: Create a VM in Azure.

Provisioned xfusion‑vm in West US.

Verified successful deployment.

Learned basics of VM creation via portal.

📌 Day 9
Task: Attach a network interface to VM.

Added NIC to xfusion‑vm.

Configured networking for connectivity.

Reinforced understanding of VM networking.

📌 Day 10
Task: Configure VM networking rules.

Set inbound/outbound rules.

Allowed SSH/HTTP traffic.

Practiced security group management.

📌 Day 11
Task: Resize VM.

Changed xfusion‑vm size from Standard_B1s → Standard_B2s.

Verified VM remained in running state.

Learned both portal and SSH resize methods.

📌 Day 12
Task: Add tags to VM.

Applied tag Environment=dev to datacenter‑vm.

Practiced resource organization with tags.

Used both portal and CLI for tagging.

📌 Day 13
Task: Configure SSH access.

Copied root public key from client host to nautilus‑vm.

Updated /root/.ssh/authorized_keys.

Set permissions and verified password‑less SSH login as root.

📌 Day 14
Task: Create and attach managed disk.

Created datacenter‑disk (2 GiB, Standard_LRS).

Attached disk to datacenter‑vm.

Learned disk provisioning and attachment via portal + CLI.

🎯 Key Learnings
VM lifecycle management (create, resize, attach resources).

Secure access with SSH keys.

Resource organization using tags.

Storage management with managed disks.

Balanced use of Azure Portal and CLI/SSH for automation.

🏆 XP Earned
+3500 XP (500 XP per day × 7 days)

