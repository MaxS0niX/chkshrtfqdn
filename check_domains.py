# by AI
# check_domains.py
import socket

def check_domain(domain):
    try:
        socket.gethostbyname(domain)
        return True
    except socket.gaierror:
        return False

def main():
    base_domain = "[0-9,a-z]"  # замените на ваш базовый домен (например, "example")
    ccTLDs = ["me", "us", "ru", "de", "fr", "cn"]  # список всех ccTLDs

    for tld in ccTLDs:
        fqdn = f"{base_domain}.{tld}"
        if check_domain(fqdn):
            print(f"Domain exists: {fqdn}")
        else:
            print(f"Domain does not exist: {fqdn}")

if __name__ == '__main__':
    main()
