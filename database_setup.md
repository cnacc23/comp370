Cienna Gin-Naccarato
Student ID# 260965061

1. Install MariaDB using the command sudo apt install mariadb-server. 

2. Set a root password on MariaDB if needed, following the command sudo mysql_secure_installation. 

3. Run MariaDB on Ubuntu using the command sudo systemctl start mariadb. 

4. Log into MariaDB and create the data base using the sql command CREATE DATABASE comp370_test. 

5. Create the user and password with the command CREATE USER 'comp370'@'%' IDENTIFIED BY '$ungl@ss3s'. The % means that the user can connect from any IP address. 

6. Connect to the database using the command mysql -u comp370 -p -h [server IP address] -P 6002 (6002 the port). 
