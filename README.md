# QA-DevOps-Practical-Project - Card Generator App
This repository contains my deliverable for the QA devops practical project.

## Contents:
* [Project Brief](#Project-Brief)  
* [Project Planning](#Project-Planning)
* [App Design](#App-Design)
* [CI/CD Pipeline](#CI/CD-Pipeline)  
* [Testing Services](#Testing)
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
