# Voting Application – DevOps Project Report

## 1. Introduction
The Voting Application is a web-based application developed to demonstrate core DevOps concepts through a real, working software system. The project focuses on building a simple application and implementing industry-standard DevOps practices such as containerization, version control, and continuous integration.


## 2. Project Objectives
The main objectives of this project are:
-   To remind and apply DevOps concepts using a simple web application
-   To containerize an application using Docker
-   To implement Continuous Integration (CI) using GitHub Actions
-   To manage source code using Git and GitHub
-   To gain hands-on experience with an end-to-end DevOps workflow


## 3. Scope of the Project
The scope of this project includes:
- Developing a basic voting web application
- Running the application locally and inside Docker containers
- Automating build processes using CI pipelines
- Hosting and managing the project using GitHub


## 4. System Architecture
The architecture of the Voting Application follows a simple flow:

User Browser > Flask Web Application > Docker Container > Local Host  
CI Pipeline > GitHub Actions > Docker Build Automation

The application logic runs inside a Docker container, ensuring consistency across different environments.


## 5. Technology Stack
The technologies used in this project are:

- **Programming Language:**----- Python
- **Web Framework:**----- Flask
- **Frontend:**----- HTML
- **Containerization:**----- Docker
- **Version Control:**----- Git
- **Repository Hosting:**----- GitHub
- **CI/CD Tool:**----- GitHub Actions


## 6. Project Implementation

### 6.1 Application Development
The voting application allows users to:
- Vote for Candidate A or Candidate B
- View real-time voting results on the web page


### 6.2 Containerization with Docker
The application is containerized using Docker to ensure consistent execution across environments.

Key Docker features used:
-    Dockerfile for image creation
-    Port mapping to expose the application
-    Lightweight Python base image


### 6.3 Version Control with Git
Git is used to:
- Track source code changes
- Maintain commit history
- Enable collaboration and rollback if required



### 6.4 Continuous Integration using GitHub Actions
A CI pipeline is implemented using GitHub Actions.

Pipeline features:
- Automatically triggered on every code push
- Checks out repository code
- Builds Docker image to validate application integrity


## 7. Testing and Validation
The application is tested by:
- Running locally using Python
- Running inside a Docker container
- Verifying successful CI pipeline execution on GitHub Actions



## 8. Results
The project achieved the following outcomes:
-     Successfully developed a working voting application
-     Successfully containerized the application using Docker
-     Implemented an automated CI pipeline
-     Verified application functionality through browser and Docker execution


## 09. Conclusion
This project successfully demonstrates the fundamentals of DevOps through a practical application. By combining application development, containerization, version control, and continuous integration, the project provides strong foundational experience for entry-level DevOps and cloud roles.

BY:
Mokshith S