# utils/ssl_utils.py
import ssl
import socket
from urllib.parse import urlparse

def check_ssl_certificate(url):
    """
    Checks if the SSL certificate of the provided URL is valid.
    Returns True if the SSL certificate is valid, False otherwise.
    """
    try:
        parsed_url = urlparse(url)
        host = parsed_url.netloc

        # Establish an SSL connection to the host
        context = ssl.create_default_context()
        conn = context.wrap_socket(socket.socket(socket.AF_INET), server_hostname=host)
        conn.connect((host, 443))

        # Check if SSL handshake is successful
        cert = conn.getpeercert()
        conn.close()

        return True if cert else False
    except Exception as e:
        return False
