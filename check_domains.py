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
    # Перебор символов от 'a' до 'z' и от '0' до '9'
    characters = [chr(char) for char in range(ord('a'), ord('z') + 1)]
    digits = [chr(digit) for digit in range(ord('0'), ord('9') + 1)]
    
    # Объединяем два списка
    SLDs = characters + digits
    #SLDs = [a-z0-9]  # Доменное имя второго уровня из единственного символа
    ccTLDs = ["me", "us", "ru", "de", "fr", "cn", "ac", "ad", "ae", "af", "ag", "ai"]  # список всех ccTLDs

    for tld in ccTLDs:
      for sld in SLDs:
        fqdn = f"{sld}.{tld}"
        if check_domain(fqdn):
          print(f"Domain exists: {fqdn}")

if __name__ == '__main__':
    main()
