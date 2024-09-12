Cienna Gin-Naccarato 
Student ID# 260965061

1. Create a Lightsail instance on AWS as seen in class. 

2. Install apache on your computer. 

3. Connect to the instance by using the command ssh -i [path to private key] ubuntu@X.Y.Z.W where X.Y.Z.W is the public IP address of the EC2 server. 

4. Install Apache on computer if it isn't already. 

5. Make Apache listen on port 8008 by typing 'Listen 8008' in the file that appears following the command: sudo nano /etc/apache2/ports.conf 

6. Modify the defualt virtual host to include port 8008 by changing the virtual host header to <VirtualHost *:8008> in the document given after the following command: sudo nano /etc/apache2/sites-available/000-default.com

7. Create the comp370_hw2.txt file in the web directory with whatever you want to say in it. 

8. Adjust the firewall rules on the Lightsail instance by clicking on the 'Networking' tab found in the instance's management page and adding a new rule with application 'Custom' and port 8008. 

9. Type the following address into a web browser http://X.Y.Z.W:8008/comp370_hw2.txt, where X.Y.Z.W is the server's IP address again and what was written in the file should appear!!
