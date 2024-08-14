# MLKickstart documentation!

## Description

a structured template that showcases the best practices for kickstarting machine learning projects using Cookiecutter Data Science. This project serves as a guide to setting up a reproducible, scalable, and organized ML workflow, ensuring efficiency from data exploration to model deployment.

## Commands

The Makefile contains the central entry points for common tasks related to this project.

### Syncing data to cloud storage

* `make sync_data_up` will use `aws s3 sync` to recursively sync files in `data/` up to `s3://ml-kick-start/data/`.
* `make sync_data_down` will use `aws s3 sync` to recursively sync files from `s3://ml-kick-start/data/` to `data/`.


