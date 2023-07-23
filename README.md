# Microservices Monitoring with Grafana

## Instalation and usage

### Previous steps
 * Install <a href="https://docs.docker.com/engine/install/">Docker</a>
 * Clone the repository:
        git clone https://github.com/Kalopanja007/TFG.git
### Build images and execute containers
From the repository directory
 
    cd ./dev_ops_tfg
 * Load environment variables needed by the docker images and their containers:

       . envvars.sh
 * build the images using docker-compose

       docker compose up -d
### Test execution
* Open a broswer to visit grafana container web server page:

  http://localhost:3000

  User: admin
  
  Password: admin

  (Ignore password change suggestion)
* Select dashboard 'Network Monitoring'
* Run the test

  From the repository directory

      cd ./dev_ops_tfg
   
      python demo/docker.py
