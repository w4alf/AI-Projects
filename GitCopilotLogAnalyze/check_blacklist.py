# This script will need to be modified since blacklist checker uses basic authentication and uses the username to pass the api key
#

import requests

API_KEY = 'place_ur_own_API_Key_Here'

# List of IP addresses to check
ip_addresses = [
    '45.57.120.190',
    '35.212.56.18',
    '97.88.136.1',
    '45.57.40.1',
    '142.93.60.243',
    '141.98.11.88',
    '154.213.200.14',
    '205.210.31.229',
    '17.248.203.64',
    '52.123.128.14'
]

def check_blacklist(ip):
    url = f'https://api.blacklistchecker/check/{ip}'
    response = requests.get(url, auth=(API_KEY, ''))
    if response.status_code == 200:
        return response.json()
    else:
        return None

def main():
    results = {}
    for ip in ip_addresses:
        result = check_blacklist(ip)
        if result:
            results[ip] = result
        else:
            results[ip] = 'Error or not found'

    # Print results
    for ip, status in results.items():
        print(f'IP: {ip}, Status: {status}')

if __name__ == '__main__':
    main()
