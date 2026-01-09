import shodan
import os
from dotenv import load_dotenv

load_dotenv()
api = shodan.Shodan(os.getenv('SHODAN_API_KEY'))

# try:
#     print(api.info())
# except shodan.APIError as e:
#     print(e)

# try:
#     ip_address = "1.1.1.1"
#     host = api.host(ip_address)
#     print(host.get('org', 'N/A'))
#     print(host.get('os', 'N/A'))

#     for i in host['data']:
#         print(f"Port: {i['port']}, Service: {i.get('product')}")
    
# except shodan.APIError as e:
#     print(e)

# try:    
#     results = api.search('port:22 country:SE')
#     print(f"Total results: {results['total']}")

#     for i in results['matches'][:10]:
#         print(f"IP: {i['ip_str']}, Port: {i['port']} Org: {i.get('org')}")
    
# except shodan.APIError as e:
#     print(e)

try:    
    results = api.search('Apache 2.2.15')
    print(f"Total results: {results['total']}")

    for i in results['matches'][:10]:
        print(f"IP: {i['ip_str']}, Port: {i['port']} Org: {i.get('org')}")
    
except shodan.APIError as e:
    print(e)
