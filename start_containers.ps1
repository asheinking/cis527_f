# Stop all running containers
docker ps -q | ForEach-Object { docker stop $_ }

# Remove all stopped containers
docker ps -a -q | ForEach-Object { docker rm $_ }

docker build -t test:latest .
docker run -p 5000:5000 -it test:latest
