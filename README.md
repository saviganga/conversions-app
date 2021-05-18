[![saviganga](https://circleci.com/gh/saviganga/conversions-app.svg?style=svg)](https://circleci.com/gh/saviganga/conversions-app)

In this repository, we set up a simple application Coninuous Integration Pipeline using CircleCI. 
There will be subsequent updates to implement Continuous Development to achieve the full CI/CD pipeline functionalities .

The application is a simple django app that makes conversions from different related units e.g temperature, distance, weight etc

Unit tests to confirm the proper working of different functions in the code base 

The app is then packaged using a docker container to allow for easy set up without dependency issues

a circleci build is set up to implement automatic tests and build of the codebase

USAGE

1. Clone the repository in a virtual environment

2. Install docker (if you have docker, skip this step)

3. in your terminal, run the command "docker compose up"
- this builds a container of the project with all its dependencies in your local computer


UP NEXT

1. Continuous Integration Pipeline setup using CircleCI (done)

2. Extend pipeline to realize full CI/CD functionalities






