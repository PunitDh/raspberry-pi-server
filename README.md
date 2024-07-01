# Flask App in Virtual Environment

This README provides a quick guide on how to run a Flask application inside a Python virtual environment using `venv`.

## Prerequisites

- Python 3 (with `pip` installed)
- `venv` module (usually comes with Python 3.3 and above)

## Setup

1. **Clone the Repository:**
   
   If your Flask app is in a Git repository, clone it:

   ```bash
   git clone git@github.com:PunitDharmadhikariLexicon/innovation-lab-team-1-pi-server.git
   cd innovation-lab-team-1-pi-server
   ```

   Otherwise, navigate to your project directory:

   ```bash
   cd innovation-lab-team-1-pi-server
   ```

2. **Create a Virtual Environment:**

   ```bash
   python3 -m venv venv
   ```

   This will create a virtual environment named `venv` in your project directory.

3. **Activate the Virtual Environment:**

   - **On macOS and Linux:**

     ```bash
     source venv/bin/activate
     ```

   - **On Windows:**

     ```bash
     .\venv\Scripts\activate
     ```

   Once activated, your terminal prompt should show the name of your virtual environment.

4. **Install Dependencies:**

   If you have a `requirements.txt` file:

   ```bash
   pip install -r requirements.txt
   ```

   Otherwise, install Flask:

   ```bash
   pip install Flask
   ```

## Running the Flask App

1. **Set Flask Environment Variables:**

   ```bash
   export FLASK_APP=app.py
   export FLASK_ENV=development
   ```

2. **Run the App:**

   ```bash
   flask run
   ```

   Otherwise:

   ```bash
   python3 app.py
   ```

   Your Flask app should now be running on `http://127.0.0.1:5000/` or the provided port if different.

## Deactivate Virtual Environment

When done, deactivate the virtual environment:

```bash
deactivate
```

## Notes

- Always activate the virtual environment when working on the project.
- Ensure dependencies are kept up to date in `requirements.txt` for consistency across environments.
- To update the `requirements.txt` file, run the following command:

```bash
pip freeze > requirements.txt
```