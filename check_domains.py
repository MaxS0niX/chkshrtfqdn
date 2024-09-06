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
    2LDs = [a-z0-9]  # первый сивол
    ccTLDs = ["me", "us", "ru", "de", "fr", "cn"]  # список всех ccTLDs

    for tld in ccTLDs:
		for sld in 2LDs:
			fqdn = f"{sld}.{tld}"
	        if check_domain(fqdn):
	            print(f"Domain exists: {fqdn}")
	        else:
	            print(f"Domain does not exist: {fqdn}")

if __name__ == '__main__':
    main()
