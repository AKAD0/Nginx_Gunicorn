```
— Deploy Nginx-Gunicorn-Flask on Raspberry Pi 5 —

1) Raspberry Pi 5 setup
2) Network setup
3) Setup web-server
4) Setup Flask web-app

— Raspberry Pi 5 setup
https://www.youtube.com/watch?v=d1y1ZIIX-XQ&pp=0gcJCb8Ag7Wk3p_U
//the OS is different!
1. Create image & boot //enable SSH during imaging
2. Ping the Raspberry
3. SSH into Raspberry //<user>@<address> ; password is user's password
4. Set static IP
+. Add Static Lease within router DHCP for the Raspberry

— Network setup
1. Buy static IP from an Internet provider (e.g. rostelekom)
2. Buy domain from a Registrar (e.g. nic.ru)
3. Delegate DNS handling to a DNS provider's (e.g. cloudflare) nameservers
4. Set the domain DNS Record at the DNS provider        //Proxied. domain-IP pair.
5. Set the SSH subdomain DNS Record at the DNS provider //No proxy "DNS Only". ssh.domain-IP pair.
6. Setup Port forwarding within firewall settings of router
   b. ssh (:22)
      External port: 22
      Internal IP address: <IP of Raspberry>
      Internal port: 22
   a. http (:80)
      External port: 80
      Internal IP address: <IP of Raspberry>
      Internal port: 80
   b. https (:443)
      External port: 443
      Internal IP address: <IP of Raspberry>
      Internal port: 443

— Setup web-server
//Below is a result of combined solutions from the following links:
https://www.youtube.com/watch?v=KWIIPKbdxD0
https://chatgpt.com/share/67f1a234-9c88-8007-91fa-cf2ebc755215
1. Make sure firewall is off
   sudo ufw status
2. Create Flask-app placeholder
   a. Setting up:
      mkdir flask_app
      cd flask_app
      python3 -m venv venv
      source venv/bin/activate
      pip install flask
   b. Create 'app.py':
      "/app.py"             //needs to be configured
   //test: flask run
3. Setup Gunicorn
   a. Install:
      pip install gunicorn
   b. Create 'wsgi.py':
      "/wsgi.py"            //needs to be configured
   //test: gunicorn --workers 3 --bind 192.168.1.208:8000 wsgi:app
   //"--bind 192.168.1.208:8000" is gunicorn-nginx interface
4. Setup Nginx
   a. Install:
      deactivate
      sudo apt update
      sudo apt install nginx
   b. Create '/etc/nginx/sites-available/flask_app.conf':
      "/flask_app.conf"   //needs to be configured
   c. Deploy conf:
      sudo ln -s /etc/nginx/sites-available/flask_app.conf /etc/nginx/sites-enabled/
   d. Test nginx:
      sudo nginx -t      
5. Launch procedure:
   source venv/bin/activate
   sudo systemctl restart nginx
   gunicorn --workers 3 --bind 192.168.1.208:8000 wsgi:app

— Setup a Flask web-app
https://youtu.be/3vfum74ggHE?si=z_8Hrt5hKy9jSHr4
<follow the tutorial>
