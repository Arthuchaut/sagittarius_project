# Sagittarius Project

[WIP] A financial management app writed with Django.

## Table of contents
- [Sagittarius Project](#sagittarius-project)
  - [Table of contents](#table-of-contents)
  - [Introduction](#introduction)
  - [Requirements](#requirements)
  - [Setting up](#setting-up)
    - [Environment configuration](#environment-configuration)

## Introduction

This project is intended as a technical demonstration of the use of the Django tool on the generic aspects of a web application.  

The Sagittarius project (temporary name) is a manual financial management application for individuals. The objective is to provide the user with a panel of tools allowing him to supervise his financial movements in order to help him make strategic decisions regarding the management of his assets.  

The application will deliberately not offer a connection with banking APIs: movements will have to be entered manually by the user. This prevents risks related to the security of the user's personal information.

## Requirements

- **Python** >= 3.9
- **Virtualenv** package installed

## Setting up

This section is to describe the project setting up procedure.

### Environment configuration

:newspaper: All the procedures described below are done at the root of the project.  

First, you need to initialize a virtualenv (ensure to have `virtualenv` package installed in your python libs).

```sh
python -m venv venv

# For Windows dist
.\venv\Script\Activate.ps1

# Or Linux dist
source ./venv/script/activate
```

Then, install needed packages.

```sh
pip install -r requirements.txt -r requirements-dev.txt
```

:warning: **For production environment**, you must to install locked packages.

```sh
pip install -r requirements.lock
```

...