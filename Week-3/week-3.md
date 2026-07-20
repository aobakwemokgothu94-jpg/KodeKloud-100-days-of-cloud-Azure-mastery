📘 Week 3: Azure Storage & Deployment Essentials

Day 15 (2026‑07‑15): Create Network Security Group (NSG)  
✅ Task  
Create and configure an NSG to control inbound and outbound traffic for Azure resources.

🛠️ Steps Taken

Signed in to Azure Portal.

Navigated to Network Security Groups.

Created a new NSG and associated it with the target subnet.

Configured inbound/outbound rules for HTTP, HTTPS, and SSH traffic.

📓 Notes  
NSGs act as firewalls at the subnet or NIC level.
They provide granular traffic control, improving security posture.
<img width="852" height="1234" alt="image" src="https://github.com/user-attachments/assets/d6321f1b-cff7-44bc-9076-8c986fc1d8cb" /><img width="808" height="1247" alt="image" src="https://github.com/user-attachments/assets/b530aba3-a510-4b98-b07a-9874884773ad" />

Day 16 (2026‑07‑16): Create a Private Azure Blob Storage Container  
✅ Task  
Create a new storage account named xfusionst20524 and a private Blob container named xfusion-blob-5813 within the storage account.

🛠️ Steps Taken

Navigated to Storage Accounts in the Azure Portal.

Clicked + Create to set up a new storage account.

Entered the name xfusionst20524, selected region and performance options, then clicked Review + Create.

After deployment, opened the resource and went to Storage Browser.

Selected Blob Containers and clicked + Add Container.

Named the container xfusion-blob-5813 and set access level to Private (no anonymous access).

Verified container creation under the storage account.

📓 Notes

Private Blob containers ensure only authenticated requests can access stored data.

This setup is ideal for sensitive workloads during migration.

Consolidating storage within Azure improves manageability and security posture.

🎯 XP Earned  
Strengthened skills in secure storage configuration and data migration readiness.
<img width="852" height="1288" alt="image" src="https://github.com/user-attachments/assets/b1f9fbad-a499-4bfa-ae77-54672b9c0245" /><img width="852" height="1288" alt="image" src="https://github.com/user-attachments/assets/8701a614-d455-4e28-8db1-ff5266ba7acf" /><img width="870" height="1281" alt="image" src="https://github.com/user-attachments/assets/93c873f9-060a-4667-b314-6d8ec276736e" />


📘 Week 3: Azure Storage & Deployment Essentials

Day 17 (2026‑07‑17): Create a Public Azure Blob Storage Container  
✅ Task  
Create a new storage account named xfusionst12898 and a public Blob container named xfusion‑blob‑26174 within the storage account. Ensure anonymous read access for containers and blobs is enabled.

🛠️ Steps Taken

Went to Storage center and clicked + Create.

Entered the storage account name xfusionst12898, selected region and performance options, then clicked Review + Create.

After deployment, opened the resource and navigated to Storage Browser.

From the navigation pane, selected Settings → Configuration, enabled Anonymous Access, and saved changes.

Under Blob Containers, clicked + Add Container.

Entered the container name xfusion‑blob‑26174 and set access level to Blob (anonymous read access).

Verified creation and previewed the container under the storage account.

🖼️ Screenshot  
(Your attached image shows the Azure Portal interface where the storage account creation begins — the “Storage center | Blob Storage” page with the + Create button visible, confirming the correct setup process.)

📓 Notes

Public Blob containers allow anonymous read access, ideal for hosting static content such as images or documents.

Always confirm that anonymous access is enabled only for non‑sensitive data.

Testing blob URLs ensures accessibility and validates configuration.

🎯 XP 500 Earned  
Enhanced proficiency in public data hosting, access control, and Azure storage configuration.

📘 Week 3: Azure Storage & Deployment Essentials

Day 18 (2026‑07‑18): Copy Data to an Azure Blob Storage Container  
✅ Task  
Copy the file /tmp/xfusion.txt into the existing Blob container xfusion‑blob‑24050 under the storage account xfusionst17600 in the East US region.

🛠️ Steps Taken

Navigated to All Resources in the Azure Portal.

Located and opened the storage account xfusionst17600.

From the navigation pane, selected Storage Browser → Blob Containers.

Under Blob Containers, selected the existing container xfusion‑blob‑24050.

Clicked Upload, selected the file /tmp/xfusion.txt, and confirmed the upload.

Verified that the file appeared in the container after completion.

🖼️ Screenshot  
(The image shows the Azure Portal’s Storage Browser interface for the storage account xfusionst17600. The left‑hand panel lists navigation items such as Favorites, Recently viewed, and Blob containers. The main section displays the container xfusion‑blob‑24050 with toolbar options like Add container, Upload, Refresh, and Delete. The “Upload blob” window confirms that one file — xfusion.txt — was selected and successfully uploaded. The final preview shows the blob listed with details: Access tier = Hot (Inferred), Blob type = Block blob, Size = 32 B.)

📓 Notes

Uploading files to Blob Storage is a key step in data migration and cloud storage management.

The Azure Portal provides a simple interface for manual uploads, while Azure CLI or PowerShell can automate bulk operations.

Always verify file integrity and accessibility after upload to ensure successful migration.

🎯 XP 500 Earned  
Strengthened skills in data migration, storage operations, and hands‑on Blob management.

📘 Week 3: Azure Storage & Deployment Essentials

Day 19 (2026‑07‑19): Convert Public Azure Blob Container to Private  
✅ Task  
Two Blob containers — nautilus‑container‑18181 (public) and nautilus‑priv‑29130 (private) — exist in the East US region under the storage account nautilusst10815. Convert nautilus‑container‑18181 from public to private while leaving nautilus‑priv‑29130 unchanged.

🛠️ Steps Taken

Navigated to Storage center in the Azure Portal and located the storage account nautilusst10815.

Opened the storage account and selected Storage Browser from the navigation pane.

Under Blob Containers, identified nautilus‑container‑18181 (currently public).

Clicked on the container name to open its settings.

Changed the Access Level from Blob (anonymous read access) to Private (no anonymous access).

Saved the configuration changes.

Verified that nautilus‑priv‑29130 remained private and unchanged.

🖼️ Screenshot  
(The screenshot would show the Azure Portal’s Storage Browser interface for the storage account nautilusst10815, highlighting the two containers — one public and one private — and the configuration panel where the access level for nautilus‑container‑18181 is updated to Private.)

📓 Notes

Changing a container’s access level to Private ensures that only authenticated users can access its contents.

This operation reinforces secure data management practices in Azure Storage.

Always verify access permissions after modification to confirm that public access has been disabled.

🎯 XP 500 Earned  
Enhanced understanding of access control, data security, and Azure Blob configuration management.
📘 Week 3: Azure Storage & Deployment Essentials

Day 20 (2026‑07‑20): Backup and Delete Azure Storage Blob Container  
✅ Task  
A private Blob container named xfusion‑blob‑27304 already exists in the East US region under the storage account xfusionst23814.
Copy the contents of xfusion‑blob‑27304 to the /opt directory on the Azure‑client host, then delete the Blob container from the storage account.

🛠️ Steps Taken

Navigated to Storage center and located the storage account xfusionst23814.

Verified the existence of the Blob container xfusion‑blob‑27304.

Used Azure CLI to back up the container contents to /opt on the landing host:

bash
sudo az storage blob download-batch \
   --destination /opt \
   --source xfusion-blob-27304 \
   --account-name xfusionst23814 \
   --auth-mode login
Confirmed that all blobs were successfully copied to /opt.

Deleted the Blob container from the storage account using:

bash
az storage container delete \
   --name xfusion-blob-27304 \
   --account-name xfusionst23814 \
   --auth-mode login
🖼️ Screenshot  
(The image shows a GitHub documentation page titled “Day 20: Backup and Delete Azure Storage Blob Container.” It includes Azure CLI commands for downloading blobs from the container to /opt and deleting the container afterward. The layout clearly demonstrates the step‑by‑step process for performing these operations.)

📓 Notes

Backing up Blob data before deletion ensures data recovery and continuity.

The az storage blob download-batch command simplifies bulk transfers.

Always verify successful backup before executing deletion commands.

This workflow reinforces data protection and storage lifecycle management best practices.

🎯 XP 500 Earned  
Advanced proficiency in Azure CLI automation, data backup, and resource cleanup.

🌟 Weekly Reflection — Week 3: Azure Storage & Deployment Essentials
This week was all about mastering Azure Storage and reinforcing security best practices. I progressed from creating containers to managing access levels, migrating data, and handling lifecycle operations.

🔑 Key Learnings
Security & Access Control

Differentiated between private and public Blob containers.

Practiced converting containers from public to private to enforce secure access.

Data Migration & Management

Uploaded files manually via the Azure Portal.

Automated bulk transfers using Azure CLI for efficiency.

Lifecycle Operations

Backed up Blob data before deletion to ensure continuity.

Practiced safe cleanup of resources to maintain a lean environment.

Networking & Protection

Configured Network Security Groups (NSGs) to control inbound/outbound traffic.

🎯 XP Earned
Day 15 → 500 XP

Day 16 → 500 XP

Day 17 → 500 XP

Day 18 → 500 XP

Day 19 → 500 XP

Day 20 → 500 XP

Total Week 3 XP: 3000  
Cumulative XP: 10,000

🚀 Reflection
Week 3 solidified my confidence in Azure Storage fundamentals. I can now:

Securely configure containers for different workloads.

Manage data migration both manually and via automation.

Enforce access control and lifecycle management with precision.

This week felt like a turning point — moving from basic resource creation to real DevOps practices that balance accessibility, security, and automation.
