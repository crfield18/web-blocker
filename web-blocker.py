import signal, time, os
from json import load

script_path = os.path.abspath(os.path.dirname(__file__))

BLOCKED_SITES = load(open(f'{script_path}/blocked_sites.json', 'r'))
blocked_sites = BLOCKED_SITES['websites']

redirect = '127.0.0.1'

def block_websites():
    print('web-blocker.py running!')
    with open('/etc/hosts', 'r+') as HOSTFILE:
        hosts_content = HOSTFILE.read()
        for site in blocked_sites:
            if site not in hosts_content:
                HOSTFILE.write(f'{redirect} {site}\n')

def revert():
    HOSTS_DEFAULT = open(f'{script_path}/hosts_DEFAULT', 'r+')
    with open('/etc/hosts', 'r+') as HOSTFILE:
        HOSTFILE.truncate(0)
        for line in HOSTS_DEFAULT:
            HOSTFILE.write(line)

def handler(signum, frame):
    print('\nweb-blocker.py switched off!')
    revert()
    exit(1)

def main():
    revert()
    signal.signal(signal.SIGINT, handler)
    block_websites()
    while True:
        time.sleep(60)

if __name__ == '__main__':
    main()

