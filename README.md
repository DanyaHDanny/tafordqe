# Test Automation for DQE

[Data dev README.md file](data_dev/dev.env)
 
## Containers 

**docker-compose.yml** creates containers for MySQL, PostgreSQL, and Jenkins, all connected to the same network.

Compose using terminal in folder with docker-compsoe.yml file.
```
podman-compose up -d
```

If podman-compose is not installed: 
```
pip install podman-compose
```

Check that the containers are running and connected to the same network:
```
podman ps
podman network inspect tafordqenetwork
```

## Access Jenkins

Open your browser and navigate to: http://localhost:8080

### Retrieve Initial Admin Password

From a file: 
```
jenkins_home\secrets\initialAdminPassword
```

From logs: 
```
podman logs jenkins | grep "Please use the following password"
```

### First initialization
1) Login using password from previous step to start initializing and click on “Install suggested plugins”. 
2) Wait until all plugins are installed. 
3) Create first admin user (remember credentials).

## Access MySQL TBD
MySQL can be accessed:
* from local machine, port 3306; TBD instruction
* at mysql:3306 from other containers in the network.

## Access PostgreSQL TBD

PostgreSQL can be accessed:
* from local machine, port 5434; TBD Instruction
* at postgres:5432 from other containers in the network.

