<div align="center">
  <img src="https://www.uvlhub.io/static/img/logos/logo-light.svg" alt="Logo">
</div>


<div align="center">
  <h1>MONTAITO-HUB</h1>
  <h3 style="font-style: italic; font-weight: normal;">
    A fork of the UVLHub project by DiversoLab: montaito-hub is a repository of feature models in UVL format integrated with Zenodo and flamapy following Open Science principles.
  </h3>
  <br><br>
  <a href="">
    <img src="https://github.com/diverso-lab/uvlhub/actions/workflows/tests.yml/badge.svg?branch=main" alt="Pytest Testing Suite">
  </a>
  <a href="">
    <img src="https://github.com/diverso-lab/uvlhub/actions/workflows/commits.yml/badge.svg?branch=main" alt="Commits Syntax Checker">
  </a>
</div>


##  Table of Contents

- [ Overview](#-overview)
- [ Project Structure](#-project-structure)
  - [ Project Index](#-project-index)
- [ Getting Started](#-getting-started)
  - [ Prerequisites](#-prerequisites)
  - [ Installation](#-installation)
  - [ Usage](#-usage)
  - [ Testing](#-testing)
- [ Project Documentation](#-project-documentation)
- [ Acknowledgments](#-acknowledgments)

---

##  Overview

Montaito-hub is a fork of the UVLHub project by DiversoLab, created for the Evolution and Configuration Management (Evolución y Gestión de la configuración - EGC) course in the Software Engineering degree at the University of Seville.

This project serves as a repository for feature models in UVL format, integrated with Zenodo and Flamapy. It includes various modifications made by students of the course, providing hands-on experience in a continuous integration and deployment environment. Students have practiced automating tests and checks using GitHub Actions and collaborating effectively within multiple teams.



---

##  Project Documentation

Montaito-hub is a proyect made by single team: montaito-hub.
You can find all our documentation on the ``/docs`` folder in our common proyect. 

There you may find our commmon working policy checking ``/docs/Acta fundacional.md`` and our specific group documentation in our respective group folder.




---

##  Project Structure

```sh
└── montaito-hub.git/
    ├── .github/
    │   ├── workflows/
    │   └── ...
    ├── CHANGELOG.md
    ├── README.md
    ├── app/
    │   ├── modules/
    │   ├── static/
    │   └── templates/
    ├── core/
    │   ├── ...
    ├── docker/
    │   ├── ...
    ├── docs/
    │   ├── Acta fundacional.md
    │   ├── ...
    │   └── ...
    ├── migrations/
    │   ├── ...
    ├── requirements.txt
    ├── rosemary/
    │   ├── commands/
    │   └── templates/
    ├── scripts/
    │   ├── ...
    └── vagrant/
        ├── ...
```

##  Getting Started

###  Prerequisites

Before getting started with montaito-hub.git, ensure your runtime environment meets the following requirements:

- **Programming Language:** Python
- **Package Manager:** Pip / Pip3


###  Installation

Install montaito-hub.git using one of the following methods:

**Deploy on Docker:**
1. Clone the montaito-hub.git repository:
```sh
❯ git clone https://github.com/Lidiajim/montaito-hub.git
```

2. Navigate to the project directory:
```sh
❯ cd montaito-hub
```

3. Create a local environment:
```sh
❯ python -m venv .evn
❯ cp .env.docker.example .env
❯ source .env/bin/activate
```

4. Install the project dependencies:

**Using `pip`** &nbsp; [<img align="center" src="https://img.shields.io/badge/Pip-3776AB.svg?style={badge_style}&logo=pypi&logoColor=white" />](https://pypi.org/project/pip/)

```sh
❯ pip install -r requirements.txt
❯ deactivate
```

5. Deploy in develop:
```sh
❯ docker compose -f docker/docker-compose.dev.yml up -d 
```

**Deploy locally:**

For more detailed information check https://docs.uvlhub.io/installation/manual_installation.


###  Usage
Run montaito-hub.git using the following command:
**Using `pip`** &nbsp; [<img align="center" src="https://img.shields.io/badge/Pip-3776AB.svg?style={badge_style}&logo=pypi&logoColor=white" />](https://pypi.org/project/pip/)

```sh
❯ python {entrypoint}
```


###  Testing

**Unit tests**
Run the unit test suite using the following command:
```sh
❯ rosemary test
```

If you want to run specific test modules:
```sh
❯ rosemary test <module name>
```

**Frontend tests using Selenium**
Run the unit test suite using the following command:
```sh
❯ rosemary selenium
```

If you want to run specific test modules:
```sh
❯ rosemary selenium <module name>
```

**Load tests using Locust**
Run the unit test suite using the following command:
```sh
❯ rosemary locust
```

If you want to run specific test modules:
```sh
❯ rosemary locust <module name>
```

---


##  Acknowledgments

In this section you can find all the contributors of each team:

- **Óscar Menéndez Márquez** - oscmenmar@alum.us.es
- **Jun Yao** - junyao@alum.us.es
- **Lidia Jiménez Soriano** - lidjimsor@alum.us.es
- **Álvaro Ruiz Gutiérrez** - alvruigut@alum.us.es
- **Carlos Martín de Prado Barragán** - carmarbar9@alum.us.es
- **Francisco Capote García** - fracapgar@alum.us.es
