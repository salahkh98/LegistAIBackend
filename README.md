# Navigate to the LegistAIBack folder
cd LegistAIBack

# Set up the virtual environment (using venv or conda)
python -m venv env  # For virtualenv
source venv/bin/activate  # On Linux/macOS
./env/Scripts/activate  # On Windows

# Install dependencies
pip install -r requirements.txt

# Set environment variables (create .env file with your database and secret keys)
# Run the Flask app
python run.py
