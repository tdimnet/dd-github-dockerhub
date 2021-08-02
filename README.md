# dd-github-dockerhub

## 1. Prerequisites

- Docker
- VsCode
- The DevContainer extension


## 2. Environnement variables and accounts needed

Please have a look at the `.example.env` file. You will find inside different environnement variables you need to have in order to make this project works.

### 2.1. Datadog 
a Datadog account with an API key - this is what will allow you to install the Datadog agent and pull up the data;

### 2.2. Github 
a GitHub account with a token access - this is what will allow you to retrieve the issues and the number of PR.

### 2.3. DockerHub
a DockerHub account - this is what will allow you to communicate with the DockerHub repository API.


## 3. Installation steps

- Clone this Github repository.
- Open VsCode and launch the Docker container with the DevContainer extaension.
- Install the Datadog agent on your container `bash -c "$(curl -L https://s3.amazonaws.com/dd-agent/scripts/install_script.sh)"`


## 4. How it works


## 5. Troubleshooting

- `service datadog-agent status`: it will give you the status of the datadog agent and allows you to see if everything is working as expected
- `tail -f /var/log/datadog/agent.log`: it will prompt you some nice informations about the agent and will help you debug your code.
