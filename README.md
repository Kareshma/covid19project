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
