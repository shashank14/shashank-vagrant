# -*- mode: ruby -*-
# vi: set ft=ruby :

# All Vagrant configuration is done below. The "2" in Vagrant.configure
# configures the configuration version (we support older styles for
# backwards compatibility). Please don't change it unless you know what
# you're doing.
Vagrant.configure("2") do |config|
  # The most common configuration options are documented and commented below.
  # For a complete reference, please see the online documentation at
  # https://docs.vagrantup.com.

  # Every Vagrant development environment requires a box. You can search for
  # boxes at https://atlas.hashicorp.com/search.
  config.vm.box = "ubuntu/xenial64"

  config.vm.network "forwarded_port", host_ip: "127.0.0.1", guest: 9090, host: 9090
  #config.vm.network "forwarded_port", host_ip: "127.0.0.1", guest: 4200, host: 4200

  config.vm.provision "shell", inline: <<-SHELL
    # Update and upgrade the server packages.
    sudo apt-get update
    sudo apt-get -y upgrade
    # Set Ubuntu Language $ sudo apt-get install python3.6

    sudo locale-gen en_GB.UTF-8
    # Install Python, SQLite and pip
    sudo apt-get install -y python3-dev sqlite python-pip

    sudo apt-get install python3-dev mysql-server libmysqlclient-dev

    # Upgrade pip to the latest version.
    sudo pip install --upgrade pip
    # Install and configure python virtualenvwrapper.
    sudo pip install virtualenvwrapper
    if ! grep -q VIRTUALENV_ALREADY_ADDED /home/vagrant/.bashrc; then
        echo "# VIRTUALENV_ALREADY_ADDED" >> /home/vagrant/.bashrc
        echo "WORKON_HOME=~/.virtualenvs" >> /home/vagrant/.bashrc
        echo "PROJECT_HOME=/vagrant" >> /home/vagrant/.bashrc
        echo "source /usr/local/bin/virtualenvwrapper.sh" >> /home/vagrant/.bashrc
    fi
  SHELL

end


#deployement
## sudo apt-get update
## sudo apt-get install python3.6
# sudo apt-get install apache2 apache2-mpm-prefork apache2-utils libexpat1
# sudo apt-get install python-pip
# sudo apt-get install apache2-utils libexpat1
# sudo apt-get install apache2-utils
# sudo apt-get install libexpat1
# sudo apt-get install libapache2-mod-wsgi
# sudo apt-get install mysql-server mysql-client
#sudo apt-get install libmysqlclient-dev
#sudo apt-get install python-dev
# sudo apt-get install mysql-server mysql-client
# sudo pip install mysqlclient


# root@ip-172-31-44-17:/var/www# sudo chown -R ubuntu .
# root@ip-172-31-44-17:/var/www# sudo chmod -R g+w .

# WSGIScriptAlias / /var/www/Project/Project/wsgi.py
# WSGIPythonPath /var/www/Project
#
# <Directory /var/www/Project/Project>
# <Files wsgi.py>
# Require all granted
# </Files>
# </Directory>



##s3
#djshashank
#id= AKIAIR2V474MFG5HWPEQ
#key= 653Vzr2y1y0wfv4SI0xwL+KlYMwSABxzhGvMoHWO
