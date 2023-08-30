# VinoVault

**Description:** VinoVault is a Django project designed to help you track your wine inventory at home.

## Table of Contents

- [Installation](#installation)
  - [Local Setup](#local-setup)
  - [Docker Setup](#docker-setup)
- [Usage](#usage)
- [Credits](#credits)

## Installation

### Local Setup

1. Make sure you have Python 3.10 installed.
2. Set up a virtual environment (recommended):

  ```bash
  python -m venv venv
  source venv/bin/activate   # On Windows: venv\Scripts\activate
  ```
3. Install project dependencies:

  ```bash
  pip install -r requirements.txt
  ```

4. Run the Django development server:

  ```bash
  python manage.py runserver
  ```

### Docker Setup
1. Install Docker on your system.

2. Pull the Docker image from Docker Hub:

```bash
docker pull thenod555/vinovault
```

3. Run the Docker container:

```bash
docker run -p 8000:8000 thenod555/vinovault
```

## Usage
VinoVault aims to simplify wine inventory management. Keep track of your wine collection to ensure you never run out.

Visit the documentation in the docs folder for detailed information. Sphinx docs are available to guide you.

## Credits
Project by Naude Opperman
GitHub: [Naude555](https://github.com/Naude555)
