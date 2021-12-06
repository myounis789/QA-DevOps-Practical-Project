# QA-DevOps-Practical-Project - Card Generator App
This repository contains my deliverable for the QA devops practical project.

## Contents:
* [Project Brief](##Project-Brief)  
* [Project Planning](#Project-Planning)
* [App Design](#App-Design)
* [CI/CD Pipeline](#CI/CD-Pipeline)  
* [Testing & Results](#Testing-&-Results)
* [The App](#The-App)
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

![System Architecture](https://github.com/myounis789/QA-DevOps-Practical-Project/blob/dev/resources/systemArchitecture.png)

### JIRA board:

In addition to a system architecture, the JIRA console was also utilised to plan out the development process of the project. This helped keep track of project progress via burndown chart reports and sprint backlogs. 

![Sprint 1](https://github.com/myounis789/QA-DevOps-Practical-Project/blob/dev/resources/Sprint1.png)

#### Burndown Chart:
Below is the final result of the Sprint Burndown Chart:

![Burndown Chart](https://github.com/myounis789/QA-DevOps-Practical-Project/blob/dev/resources/finalburndown.png)

Although it's not perfect, this chart gives us a clear overview of the execution of tasks against time thanks to the story points that were set. JIRA uses these story points to generate a guideline which represents the ideal birn rate. This gives the developer an insight of whether the project development schedule is on track or falling behind.

Furthermore, it is evident that the burndown chart doesn't necessarily start from the first day of the sprint. This is because I had forgotten to add story points to my user-stories and tasks, which were added a day later than the project start date. This is something that I can keep in mind to avoid in the future.
### Risk Assessment:
A risk assessment was carried out as a way of identifying potential project risks. Below are the risks identified before and after development.

### Before:

![Risk Assessment Before](https://github.com/myounis789/QA-DevOps-Practical-Project/blob/dev/resources/riskbefore.png)

### After:
![Risk Assessment After](https://github.com/myounis789/QA-DevOps-Practical-Project/blob/dev/resources/riskafter.png)

## App Design:

### Version 1:
Version 1 of the card-generator app displays the name of the card along with its image on the webpage as shown below:

![App Version 1](https://github.com/myounis789/QA-DevOps-Practical-Project/blob/dev/resources/version1.png)

### Version 2:
Version 2 of the card-generator app displays the symbol and suit of the card along with its image on the webpage as shown below:

![App Version 2](https://github.com/myounis789/QA-DevOps-Practical-Project/blob/dev/resources/version2.png)

## CI/CD Pipeline:

## Testing & Results: