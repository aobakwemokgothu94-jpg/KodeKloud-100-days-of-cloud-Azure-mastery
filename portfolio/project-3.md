# Project 3 — Storage, deployment & CI validations

Short summary

Configured Azure storage and deployment pipelines; validated VM provisioning using scripted checks and lightweight CI (GitHub Actions) to ensure docs and small automation scripts render/build correctly.

Tech & skills

- Azure Storage and container use
- Jekyll/GitHub Pages basics (site preview)
- GitHub Actions for doc/workflow validations (see `.github/workflows`)
- Small Bash/az scripts to validate VM state and connectivity

Key commands / snippets

```bash
# preview site locally (Jekyll)
bundle install
bundle exec jekyll serve

# basic storage account container create
az storage account create --name mystorageacct --resource-group lab-rg --location eastus --sku Standard_LRS
az storage container create --account-name mystorageacct --name site-assets

# run a quick remote check (example)
az vm run-command invoke --resource-group lab-rg --name demo-vm --command-id RunShellScript --scripts "hostname && uptime"
```

How to reproduce (quick)

1. Follow the `Week-3/week-3.md` and `Week-4/week-4.md` notes to create the storage account and deploy simple resources.
2. Use `bundle exec jekyll serve` to preview the repo content locally if you want a static site view.
3. Review `.github/workflows/update-xp.yml` to see how actions automate updates (workflow file lives at `.github/workflows/update-xp.yml`).

Full writeup

- See `../Week-3/week-3.md` and `../Week-4/week-4.md` for the full labs, screenshots, and CI snippets.

Outcome & evidence

- Shows end-to-end lab workflow: document, provision, validate, and automate. Useful for portfolio reviewers who want to see both manual steps and automated checks.
