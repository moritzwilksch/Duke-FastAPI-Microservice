[![Continuous Integration](https://github.com/moritzwilksch/Duke-FastAPI-Microservice/actions/workflows/main.yml/badge.svg)](https://github.com/moritzwilksch/Duke-FastAPI-Microservice/actions/workflows/main.yml)  

# Duke-FastAPI-Microservice
Whats for lunch? This microservice knows and returns a randomly chosen, currently open restaurant on Duke's campus.

## Architecture
![](architecture_diag.svg)  

## CI/CD
- Makefile for environment setup
- pytest for unit testing
- Test runs through Github Actions for CI
- Continuous Delivery to GCP AppEngine to deploy changes on build
