# web-blocker
Basic website blocker for MacOS.
Desired websites are copied from blocked_sites.json to /etc/hosts, redirecting requrests to localhosts. The default state for /etc/hosts is restored when the script is terminated with a ctrl+c KeyboardInterupt.
