# KodeKloud 100 Days — Azure mastery (Days 1–50)

A focused, hands‑on 100‑day learning journal documenting Azure labs, VM provisioning, security hardening, and automation. This repo showcases the tasks I built while following KodeKloud-style labs — ideal for a portfolio quick-read.

[![License](https://img.shields.io/github/license/aobakwemokgothu94-jpg/KodeKloud-100-days-of-cloud-Azure-mastery)](LICENSE) <!-- small credibility badge -->

What I can do (TL;DR)
- Provision and secure Azure VMs (SSH hardening, key-based auth, private networking)
- Build and publish VM images and automate VM deployments with az CLI
- Use GitHub Actions to automate simple tracking/updates and validate docs

Quick links
- Highlights (portfolio-ready projects): HIGHLIGHTS.md
- Week-by-week lab notes: Week-1/.. / Week-4/.. (Week-*/week-*.md)

How to preview the site or read locally
- Read the content immediately in the repo (markdown files are self-contained).
- If you want a local site (Jekyll/GitHub Pages):

  ```bash
  # (optional) install Ruby/Bundler/Jekyll, then:
  bundle install
  bundle exec jekyll serve
  # open http://localhost:4000
  ```

Quick commands I use in labs (examples)
```bash
# create SSH key (safe to run locally)
ssh-keygen -t ed25519 -f ~/.ssh/azure_demo_key -N ""
# basic az login (requires browser/credentials)
az login
# quick VM create example (replace values before running)
az vm create --resource-group my-rg --name demo-vm --image UbuntuLTS --size Standard_B1s --admin-username azureuser --ssh-key-value ~/.ssh/azure_demo_key.pub
```

Status
- Days completed: 50 (ongoing)

Want me to: (pick one)
- Convert this repo into a polished Jekyll site with sidebar navigation
- Create three concise portfolio pages (I can auto-generate from weeks)
- Harden the XP-tracker GitHub Action and document how it works

