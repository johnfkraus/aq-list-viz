# un-sanc-viz

Deployment notes for Digital Ocean, 2024.

https://www.linkedin.com/pulse/deploying-nodejs-app-digitalocean-server-hayk-simonyan/

ubuntu-s-1vcpu-512mb-10gb-nyc1-01


204.48.22.234

curl -sL https://deb.nodesource.com/setup_18.x | sudo -E bash -

sudo apt install nodejs

https://stackoverflow.com/questions/14772508/npm-failed-to-install-time-with-make-not-found-error
sudo apt-get install build-essential

pm2 start index.js


pm2 startup


ufw status


Inside the location block:

proxy_pass http://localhost:3000; 

https://www.namecheap.com/cart/checkout/orderconfirmation/?id=145096683

registered domain name on namecheap.com

al-qaida-sanctions.com

ns1.digitalocean.com
ns2.digitalocean.com
ns3.digitalocean.com


sudo add-apt-repository ppa:certbot/certbot


sudo add-apt-repository ppa:certbot/certbot
PPA publishes dbgsym, you may need to include 'main/debug' component
Repository: 'Types: deb
URIs: https://ppa.launchpadcontent.net/certbot/certbot/ubuntu/
Suites: noble
Components: main
'
Description:
The PPA has been DEPRECATED.

To get up to date instructions on how to get certbot for your systems, please see https://certbot.eff.org/docs/install.html.
More info: https://launchpad.net/~certbot/+archive/ubuntu/certbot
Adding repository.
Press [ENTER] to continue or Ctrl-c to cancel.



To get up to date instructions on how to get certbot for your systems, please see https://certbot.eff.org/docs/install.html.
More info: https://launchpad.net/~certbot/+archive/ubuntu/certbot
Adding repository.
Press [ENTER] to continue or Ctrl-c to cancel.
Hit:1 http://security.ubuntu.com/ubuntu noble-security InRelease
Hit:2 http://mirrors.digitalocean.com/ubuntu noble InRelease
Get:3 http://mirrors.digitalocean.com/ubuntu noble-updates InRelease [126 kB]
Hit:4 https://deb.nodesource.com/node_18.x nodistro InRelease
Hit:5 https://repos-droplet.digitalocean.com/apt/droplet-agent main InRelease
Hit:6 http://mirrors.digitalocean.com/ubuntu noble-backports InRelease
Ign:7 https://ppa.launchpadcontent.net/certbot/certbot/ubuntu noble InRelease
Get:8 http://mirrors.digitalocean.com/ubuntu noble-updates/main amd64 Packages [96.9 kB]
Err:9 https://ppa.launchpadcontent.net/certbot/certbot/ubuntu noble Release
404  Not Found [IP: 185.125.190.80 443]
Get:10 http://mirrors.digitalocean.com/ubuntu noble-updates/universe amd64 Packages [44.9 kB]
Reading package lists... Done
E: The repository 'https://ppa.launchpadcontent.net/certbot/certbot/ubuntu noble Release' does not have a Release file.
N: Updating from such a repository can't be done securely, and is therefore disabled by default.
N: See apt-secure(8) manpage for repository creation and user configuration details.
root@al-qaida-sanctions:/etc/nginx/sites-available#



sudo certbot --nginx -d yourdomain.com -d www.yourdomain.com
Saving debug log to /var/log/letsencrypt/letsencrypt.log
Enter email address (used for urgent renewal and security notices)
(Enter 'c' to cancel): johnkraus3@gmail.com

- - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -
Please read the Terms of Service at
https://letsencrypt.org/documents/LE-SA-v1.4-April-3-2024.pdf. You must agree in
order to register with the ACME server. Do you agree?
- - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -
(Y)es/(N)o: Y

- - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -
Would you be willing, once your first certificate is successfully issued, to
share your email address with the Electronic Frontier Foundation, a founding
partner of the Let's Encrypt project and the non-profit organization that
develops Certbot? We'd like to send you email about our work encrypting the web,
EFF news, campaigns, and ways to support digital freedom.
- - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -
(Y)es/(N)o: Y
Account registered.
Requesting a certificate for yourdomain.com and www.yourdomain.com

Certbot failed to authenticate some domains (authenticator: nginx). The Certificate Authority reported these problems:
Domain: www.yourdomain.com
Type:   unauthorized
Detail: 192.124.249.6: Invalid response from https://www.yourdomain.com/: "<meta name=\"robots\" content=\"noindex, nofollow\">\n<!DOCTYPE html>\r\n<html lang=\"en-us\">      \r\n<head>\r\n\t<meta charset=\"utf-8\" /><m"

Domain: yourdomain.com
Type:   unauthorized
Detail: 192.124.249.6: Invalid response from https://www.yourdomain.com/.well-known/acme-challenge/FkQafyvcV84IZR4WmD2odVFXfdlY19kTjVU_KPmy540: 502

Hint: The Certificate Authority failed to verify the temporary nginx configuration changes made by Certbot. Ensure the listed domains point to this nginx server and that it is accessible from the internet.

Some challenges have failed.
Ask for help or search for solutions at https://community.letsencrypt.org. See the logfile /var/log/letsencrypt/letsencrypt.log or re-run Certbot with -v for more details.
root@al-qaida-sanctions:/etc/nginx/sites-available#


sudo certbot --nginx -d al-qaida-sanctions.com -d www.al-qaida-sanctions.com


Some challenges have failed.
Ask for help or search for solutions at https://community.letsencrypt.org. See the logfile /var/log/letsencrypt/letsencrypt.log or re-run Certbot with -v for more details.
root@al-qaida-sanctions:/etc/nginx/sites-available# sudo certbot --nginx -d al-qaida-sanctions.com -d www.al-qaida-sanctions.com
Saving debug log to /var/log/letsencrypt/letsencrypt.log
Requesting a certificate for al-qaida-sanctions.com and www.al-qaida-sanctions.com

Successfully received certificate.
Certificate is saved at: /etc/letsencrypt/live/al-qaida-sanctions.com/fullchain.pem
Key is saved at:         /etc/letsencrypt/live/al-qaida-sanctions.com/privkey.pem
This certificate expires on 2024-08-30.
These files will be updated when the certificate renews.
Certbot has set up a scheduled task to automatically renew this certificate in the background.

Deploying certificate
Successfully deployed certificate for al-qaida-sanctions.com to /etc/nginx/sites-enabled/default
Successfully deployed certificate for www.al-qaida-sanctions.com to /etc/nginx/sites-enabled/default
Congratulations! You have successfully enabled HTTPS on https://al-qaida-sanctions.com and https://www.al-qaida-sanctions.com

- - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -
If you like Certbot, please consider supporting our work by:
* Donating to ISRG / Let's Encrypt:   https://letsencrypt.org/donate
* Donating to EFF:                    https://eff.org/donate-le
- - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -
root@al-qaida-sanctions:/etc/nginx/sites-available#


