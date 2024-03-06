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