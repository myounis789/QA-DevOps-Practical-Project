# QA-DevOps-Practical-Project - Card Generator App
This repository contains my deliverable for the QA devops practical project.

## Contents:
* [Project Brief](##Project-Brief)  
* [Project Planning](#Project-Planning)
* [App Design](#App-Design)
* [CI/CD Pipeline](#CI/CD-Pipeline)  
* [Testing & Results](#Testing-&-Results)
* [Known Issues](#Known-Issues)
* [Future Work](#Future-Work)

## Project Brief:  
The brief for this project was to develop a service-oriented architecture of an application that generates "Objects" upon a set of pre-defined rules. These include:

* Service 1 - This will serve the webpage of the application. It's job is to render Jinja2 templates based on data received from Services #2, #3 and #4, hence it is responsible for communicating with the other services. In my case, it will display a random card on the server.

* Service 2 - This will be the first random object generator. In this case it is my random card symbol generator.

* Service 3 - This will be the second random object generator. In this case it is the random suit generator.

* Service 4 - This will also create an object, hoever this must be based upon the results of services #2 and #3. In terms of this application, this service is responsible for generating an image of the random card based on its symbol and suit values given by services #2 and #3. 

## Project Planning:
During the planning stages of this project, a system architecture was developed to give a visual representation of the number of VM's hosting the application, as well as how they communicate with each other. This is shown below:

![System Architecture](https://github.com/myounis789/QA-DevOps-Practical-Project/blob/main/resources/systemArchitecture.png)

### JIRA board:

In addition to a system architecture, the JIRA console was also utilised to plan out the development process of the project. This helped keep track of project progress via burndown chart reports and sprint backlogs. 

![Sprint 1](https://github.com/myounis789/QA-DevOps-Practical-Project/blob/main/resources/Sprint1.png)

#### Burndown Chart:
Below is the final result of the Sprint Burndown Chart:

![Burndown Chart](https://github.com/myounis789/QA-DevOps-Practical-Project/blob/main/resources/finalburndown.png)

Although it's not perfect, this chart gives us a clear overview of the execution of tasks against time thanks to the story points that were set. JIRA uses these story points to generate a guideline which represents the ideal birn rate. This gives the developer an insight of whether the project development schedule is on track or falling behind.

Furthermore, it is evident that the burndown chart doesn't necessarily start from the first day of the sprint. This is because I had forgotten to add story points to my user-stories and tasks, which were added a day later than the project start date. This is something that I can keep in mind to avoid in the future.
### Risk Assessment:
A risk assessment was carried out as a way of identifying potential project risks. Below are the risks identified before and after development.

### Before:

![Risk Assessment Before](https://github.com/myounis789/QA-DevOps-Practical-Project/blob/main/resources/riskbefore.png)

### After:
![Risk Assessment After](https://github.com/myounis789/QA-DevOps-Practical-Project/blob/main/resources/riskafter.png)

## App Design:

### Version 1:
Version 1 of the card-generator app displays the name of the card along with its image on the webpage as shown below:

![App Version 1](https://github.com/myounis789/QA-DevOps-Practical-Project/blob/main/resources/version1.png)

### Version 2:
Version 2 of the card-generator app displays the symbol and suit of the card along with its image on the webpage as shown below:

![App Version 2](https://github.com/myounis789/QA-DevOps-Practical-Project/blob/main/resources/version2.png)

## CI/CD Pipeline:
A CI-CD pipeline was implemented in this project to allow for the automation of development in to live buildsto automate testing, building, and deploying the application. The diagram below illustrates how this is done:

![CI Pipeline](https://github.com/myounis789/QA-DevOps-Practical-Project/blob/main/resources/cipipeline.jpg)

### Jenkins:

The main tool used here was Jenkins. A pipeline item was created which would locate the Jenkinsfile within the github repo and run it. Below is a screenshot of the application passing each stage of the jenkins application:

![Jenkins](https://github.com/myounis789/QA-DevOps-Practical-Project/blob/main/resources/jenkins.png)

As you can see, the pipeline consists of 3 stages:
* Stage 1 runs the tests.sh script to test each service of the application. Hence, if the test fails the build would also fail. It makes sense doing this first as you wouldn't want to wait for the application to build and deploy before realising it is not functioning as expected.

* Stage 2 builds the images from the docker-compose.yaml file and pushes them to Docker Hub. Environment variables were used to store docker hub credentials in Jenkins as secret keys.

* Stage 3 runs the ansible-playbook.yaml file to configure each vm and setup the swarm for deployment. Finally, the application is deployed and the build is a SUCCESS.

### Docker Hub:

Here is a screenshot of my Docker Hub repo's created upon each successful Jenkins build:

![Jenkins](https://github.com/myounis789/QA-DevOps-Practical-Project/blob/main/resources/docker.png)


These are used by ansible to deploy on the docker stack which manages the docker-swarm.


## Testing & Results:
In order to test the application, pytest was used. This gives i=us the benefit of using unit mock_tests to mock data for http get/post requests. Mocking helps test random generators as it forces the output of the random statement before the test is run. 

These tests were then automated via Jenkins. A tests.sh file was created which cd's into each directory (Service1-Service4) and runs the test file within that directory. The following results were obtained:

### Service 1: FrontEnd

![test1](https://github.com/myounis789/QA-DevOps-Practical-Project/blob/main/resources/service1tests.png)

### Service 2: symbol-generator

![test2](https://github.com/myounis789/QA-DevOps-Practical-Project/blob/main/resources/service2tests.png)

### Service 3: suit-generator

![test3](https://github.com/myounis789/QA-DevOps-Practical-Project/blob/main/resources/service3tests.png)

### Service 4: BackEnd

![test4](https://github.com/myounis789/QA-DevOps-Practical-Project/blob/main/resources/service4tests.png)

## Known issues:
During the development process of my project. I would encounter a 'permission denied' error on multiple occasions when setting up new VM's for my ansible-playbook to play with. Although I have found a temporary fix to work around it, it is a risk of failing again at some point. This is an issue with GCP itself and not a matter in my hands.
## Future Work:
The project was a success other than the exclusion of an SQL database implementation. This is simply due to running out of time as several errors related to those mentioned above ate up a lot of my development time. In the future, an SQL Database can be added to display the last 5 cards on the webpage. 

Another future implementation would be the utilisation of nexus. Nexus is a tool that is helpful for privacy of docker images. The main reason why thus was not implemented in this project is simply due to cost effective measures, as nexus requires a considerably large virtual machine which I do not have credit for on my GCP account. In the future, I can give this a go given that I have sufficient funds.
