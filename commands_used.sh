#  Building Docker Images Commands
docker build .
docker-compose build

# Build Docker Image with dev dependencies
docker build .
docker-compose build
# After setting up flake8 for linting support
docker-compose run --rm app sh -c "flake8"
docker-compose run --rm app sh -c "which flake8"


# Creates a django project named app
docker-compose run --rm app sh -c "django-admin startproject app ."

# Start docker container via docker compose yml file
docker-compose up

# Used TDD approach, created Test Cases, and ran following command to test the code
docker-compose run --rm app sh -c "python manage.py test"