# Navigate to your project folder (replace with your actual folder path)
cd Documents/my_project

# Create a virtual environment named 'venv'
python3 -m venv venv

# Activate the virtual environment
source venv/bin/activate


________________________



# Upgrade pip to the latest version first
pip install --upgrade pip

# Install a specific package (e.g., requests)
pip install requests

# Install a specific version of a package
pip install requests==2.31.0



_____________________



# Deactivate and return to normal terminal
deactivate

# Save your installed packages to a text file
pip freeze > requirements.txt

# Install all packages listed in a requirements file (for future use)
pip install -r requirements.txt
