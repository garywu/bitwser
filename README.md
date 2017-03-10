# bitwser
World's first most inefficient browser build with docker, docker compose, selenium and python

Demostrates simplest python to selenium

1. Install docker and docker-compose
2. Build the containers:

  ```sh
  docker-compose build
  ```

3. Run the container

  ```sh
  docker-compose up
  ```

4. Browse to http://localhost:5000
5. Browse to any url by: http://localhost:5000?url=http://google.com
6. For debuging purpose you can use VNC to access the selenium container on localhost port 5900
