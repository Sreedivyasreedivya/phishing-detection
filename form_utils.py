# utils/form_utils.py
import requests
from bs4 import BeautifulSoup

def check_for_suspicious_forms(url):
    """
    Checks if the given URL contains suspicious forms (e.g., login forms).
    """
    try:
        response = requests.get(url)
        soup = BeautifulSoup(response.text, "html.parser")

        forms = soup.find_all("form")
        for form in forms:
            # Check for suspicious form input names like password, email, username, etc.
            if any(input_tag.get("name", "").lower() in ["password", "email", "username", "bank", "account"] for input_tag in form.find_all("input")):
                return True
    except Exception as e:
        print(f"Error checking for suspicious forms: {e}")

    return False
