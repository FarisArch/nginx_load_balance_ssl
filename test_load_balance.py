import requests
from urllib3.exceptions import InsecureRequestWarning
import time

# Disable insecure warnings for self-signed certs (just for lab)
requests.packages.urllib3.disable_warnings(InsecureRequestWarning)

URL = "https://localhost"  # your load balancer URL
NUM_REQUESTS = 10

def check_backend():
    try:
        resp = requests.get(URL, verify=False, timeout=3)
        content = resp.text.lower()

        if "backup" in content:
            return "apache_backup"
        else:
            return "apache"
    except Exception as e:
        return f"error: {e}"

if __name__ == "__main__":
    for i in range(NUM_REQUESTS):
        backend = check_backend()
        print(f"Request {i+1}: Served by {backend}")
        time.sleep(1)  # small delay between requests
