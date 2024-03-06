#!/usr/bin/env bash
# setting up the web servers to deploy the web static

sudo apt-get update
sudo apt-get install -y nginx
mkdir -p /data/web_static/releases/test
mkdir -p /data/web_static/shared
echo "<html>
  <head>
  </head>
  <body>
    Holberton School
  </body>
</html>" > /data/web_static/releases/test/index.html
ln -sf /data/web_static/releases/test /data/web_static/current
chown -R ubuntu:ubuntu /data/
serve="\n\tlocation \/hbnb_static {\n\t\talias \/data\/web_static\/current;\n\t}"
sudo sed -i "s/^\tserver_name .*;$/&\n$serve/" /etc/nginx/sites-available/default
sudo service nginx restart
