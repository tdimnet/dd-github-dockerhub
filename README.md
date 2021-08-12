# dd-github-dockerhub

This repository contains two examples of the custom agent check for the Datadog Agent. You can find the source code of both in the `custom_agent_checks` folder.

- `custom_github` allows you to find pull requests and issues for a specific project.
- `custom_github_projects` allows you to retrieve the cards of a Github project, e.g. **todo**, **in progress** and **done**.

You can find more information about custom agent checks on this [Google Sheet presentation](https://docs.google.com/presentation/d/1GApMTtOXItID_-fZjWWgkpYV7y3bpp6meHAPieqQzg8/edit?usp=sharing)

## 1. Prerequisites

- Docker
- VsCode
- The DevContainer extension


## 2. Accounts and API keys

- Datadog
- Github


## 3. Installation steps

- Clone this Github repository.
- Open VsCode and launch the Docker container with the DevContainer extaension.
- Install the Datadog agent on your container `bash -c "$(curl -L https://s3.amazonaws.com/dd-agent/scripts/install_script.sh)"`


## 4. How it works

Once the Datadog agent has been installed, you can copy the custom agent checks into the `/etc/datadog-agent` directory:

- `cp -R custom_agent_checks/*/*.py /etc/datadog-agent/checks.d/`
- `cp -R custom_agent_checks/*/*.yaml /etc/datadog-agent/conf.d/`

Then you just have to restart the Datadog agent `service datadog-agent restart`.


## 5. Troubleshooting

- `service datadog-agent status`: it will give you the status of the datadog agent and allows you to see if everything is working as expected
- `tail -f /var/log/datadog/agent.log`: it will prompt you some nice informations about the agent and will help you debug your code.
- `datadog-agent check ${checkName}`: here checkName will be `custom_github` and `custom_github_projects`
