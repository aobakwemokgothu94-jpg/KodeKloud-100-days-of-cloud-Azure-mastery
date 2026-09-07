# Project 1 — VM provisioning & SSH hardening

Short summary

Provisioned Linux VMs in Azure, enabled key-based SSH, hardened basic SSH settings, and documented the whole flow so a reviewer can reproduce the VM creation and secure access.

Tech & skills

- Azure CLI (az)
- SSH key management (ed25519)
- Ubuntu LTS images
- Basic security hardening (disable password auth, change SSH port, configure UFW)

Key commands (examples)

```bash
# create an SSH key (local)
ssh-keygen -t ed25519 -f ~/.ssh/azure_demo_key -N ""

# login to Azure
az login

# create resource group (one-time)
az group create --name lab-rg --location eastus

# create VM using SSH key (replace names)
az vm create \
  --resource-group lab-rg \
  --name demo-vm \
  --image UbuntuLTS \
  --admin-username azureuser \
  --ssh-key-value ~/.ssh/azure_demo_key.pub \
  --size Standard_B1s

# disable password auth after login (on the VM)
sudo sed -i 's/^#\?PasswordAuthentication yes/PasswordAuthentication no/' /etc/ssh/sshd_config
sudo systemctl restart sshd
```

How to reproduce (quick)

1. Follow the commands above (ensure you replace resource names and region).
2. Verify you can SSH using the private key: `ssh -i ~/.ssh/azure_demo_key azureuser@<public-ip>`.
3. Take screenshots of successful SSH login and `sshd_config` showing PasswordAuthentication=no.

Full writeup

- See the detailed notes: `../Week-1/week-1.md` (step-by-step lab, screenshots)

Outcome & evidence

- Reproducible VM creation and secure SSH login recorded in Week-1; this shows practical Azure VM provisioning and baseline OS hardening skills.
