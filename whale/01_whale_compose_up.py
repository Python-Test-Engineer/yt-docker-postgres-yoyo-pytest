from python_on_whales import DockerClient

docker = DockerClient(compose_files=["../docker-compose.yml"])

docker.compose.build()
docker.compose.up(detach=True)

# docker.compose.down()
