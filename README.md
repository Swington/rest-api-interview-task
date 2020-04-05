[![Codacy Badge](https://api.codacy.com/project/badge/Grade/a4cd8b7cd0694307b7c929232577e6b2)](https://app.codacy.com/manual/Swington/rest-api-interview-task?utm_source=github.com&utm_medium=referral&utm_content=Swington/rest-api-interview-task&utm_campaign=Badge_Grade_Dashboard)
[![CircleCI](https://circleci.com/gh/Swington/rest-api-interview-task.svg?style=svg)](https://circleci.com/gh/Swington/rest-api-interview-task)

# rest-api-interview-task
Interview task describing creation of REST API

# How to use

1. Run tests
    In order to run tests, run:
    ```bash
    make run-tests
    ```

    This will, firstly, build test image, and then run app tests with pytest.
1. Run local development server
    In order to run local development server, run command:
    ```bash
   docker-compose -f ./docker/docker-compose.yml up --build 
   ```
   Then just nagivate to [http://localhost/swagger](http://localhost/swagger) to view SwaggerUI docs

# CircleCI integration
On every push to any branch, CircleCI build is triggered.
The build executes tests using test docker container.

CircleCI badge for `master` branch build is available to view on top of readme. 
