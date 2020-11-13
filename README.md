# Covid19 project - Big Data and Architecture CISC 525
Prediction of Covid 19 cases in the US


# Setup
Boot an Amazon Linux Instance and ssh into your instance
```
## install docker
sudo yum update -y
sudo yum install -y docker

## start docker
sudo service docker start

## confirm docker is working
sudo usermod -a -G docker ec2-user

## also confirm that storage driver is set to overlay2
## this ensures that the memory is 
docker info | grep 'overlay2'

## run docker deploy script
bash docker-deploy-hdp265.sh

## run the startup script
bash start_sandbox.sh

## configure to start at boot
echo "bash /root/start_sandbox.sh" >> /etc/rc.local

## Print the URL for accessing the Sandbox
echo -e "##\nAccess the Sandbox at:\nhttp://$(curl -sS4 icanhazip.com):8080\n##"
```

3. Access the Sandbox at the hosts public IP.

# Add MongoDB Service
Reference: https://github.com/nikunjness/mongo-ambari
```
cd /var/lib/ambari-server/resources/stacks/HDP/2.3/services
git clone https://github.com/nikunjness/mongo-ambari.git

service ambari-server restart
```
On bottom left -> Actions -> Add service -> check MongoDB -> Next -> Next -> Next -> Deploy


# Run the scripts
https://gist.github.com/dshamanthreddy/cb1160230d28279f84f85d848c79f76b

# Connect to Zeppelin Notebook (use Covid19.json)

# How to install Python 3.8
https://www.liquidweb.com/kb/how-to-install-python-3-on-centos-7/
