# LegistAIBack

Backend server for the LegistAI application.

## 📋 Prerequisites

- Python 3.12.6
- pip (Python package manager)
- Git

## 🚀 Getting Started

### Clone the Repository

```bash
git clone https://github.com/yourusername/LegistAIBack.git
cd LegistAIBack
```

### Environment Setup

#### Using virtualenv

```bash
# Create virtual environment
python -m venv env

# Activate virtual environment
# On Windows
./env/Scripts/activate

# On macOS/Linux
source env/bin/activate
```



### Installation

```bash
# Install required packages
pip install -r requirements.txt
```

### Configuration

Create a `.env` file in the root directory with the following variables:

```
# Database Configuration
SECRET_KEY=
JWT_SECRET_KEY=
DB_USERNAME=
DB_PASSWORD=
DB_HOST=
DB_DATABASE=
DB_DRIVER=ODBC Driver 18 for SQL Server
DB_ENCRYPT=no
DB_TRUST_CERT=no
DB_TIMEOUT=30

```

## 🏃‍♂️ Running the Application

```bash
# Start the Flask server
python run.py
```

The server will be available at `http://localhost:5000` by default.



## 📁 Project Structure

```
LegistAIBack/
├── app/
│   ├── __init__.py
│   ├── config.py
│   ├── database.py
│   ├── routes.py
│   └── models.py
├── .env
├── .gitignore
├── requirements.txt
└── run.py
```

