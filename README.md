# dd-github-dockerhub

## Prerequisites

- Docker
- VsCode
- The DevContainer extension

In addition to these technical prerequisites, you will also need:

- a Datadog account with an API key - this is what will allow you to install the Datadog agent and pull up the data;
- a GitHub account with a token access - this is what will allow you to retrieve the issues and the number of PR.
- a DockerHub account - this is what will allow you to communicate with the DockerHub repository API.

## Installation steps

- Clone this Github repository.
- Open VsCode and launch the Docker container with the DevContainer extaension.
- Install the Datadog agent on your container `bash -c "$(curl -L https://s3.amazonaws.com/dd-agent/scripts/install_script.sh)"`


## Troubleshooting

- `service datadog-agent status`: it will give you the status of the datadog agent and allows you to see if everything is working as expected
- `tail -f /var/log/datadog/agent.log`: it will prompt you some nice informations about the agent and will help you debug your code.
