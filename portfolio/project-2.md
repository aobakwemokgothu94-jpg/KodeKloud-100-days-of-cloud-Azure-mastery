# Project 2 — Networking, VM images & automation

Short summary

Configured Azure networking (public/private IPs, NSGs), created VM images and used automation scripts to standardize VM provisioning. The work demonstrates reproducible VM builds and network-aware deployment.

Tech & skills

- Azure CLI: `az network`, `az vm`, `az image`
- NSG (Network Security Group) configuration
- VM image creation & reuse
- Small automation scripts (bash)

Key commands (examples)

```bash
# create a virtual network and subnet
az network vnet create --resource-group lab-rg --name lab-vnet --address-prefix 10.1.0.0/16 --subnet-name lab-subnet --subnet-prefix 10.1.1.0/24

# create network security group and rule
az network nsg create --resource-group lab-rg --name lab-nsg
az network nsg rule create --resource-group lab-rg --nsg-name lab-nsg --name AllowSSH --priority 1000 --protocol Tcp --destination-port-range 22 --access Allow

# create a VM with NIC attached to the subnet and NSG
az vm create --resource-group lab-rg --name net-vm --image UbuntuLTS --vnet-name lab-vnet --subnet lab-subnet --nsg lab-nsg --admin-username azureuser --ssh-key-value ~/.ssh/azure_demo_key.pub

# capture a VM to an image (prepare VM, deallocate, generalize if needed)
az vm deallocate --resource-group lab-rg --name build-vm
az vm generalize --resource-group lab-rg --name build-vm
az image create --resource-group lab-rg --name my-custom-image --source build-vm
```

How to reproduce (quick)

1. Create lab resource group and VNet as above.
2. Provision a VM, prepare it (install packages/config), then deallocate + generalize and create an image.
3. Use that image to create consistent VMs across environments.

Full writeup

- See `../Week-2/week-2.md` for the full lab with screenshots and extra automation notes.

Outcome & evidence

- Demonstrates networking fundamentals in Azure, ability to craft golden images for reproducible deployments, and automation that saves time when provisioning multiple VMs.
