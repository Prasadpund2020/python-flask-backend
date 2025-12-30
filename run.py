# run.py

from app import create_app

app = create_app()

if __name__ == "__main__":
    """
    THIS LINE IS CRITICAL
    ---------------------
    Without app.run(), server will NOT start

    मराठीत:
    ----------
    ह्या ओळीशिवाय Flask server चालू होत नाही
    """
    app.run(debug=True)
