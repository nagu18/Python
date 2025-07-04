import docker
from docker.errors import DockerException

try:
    client = docker.from_env()
    for container in client.containers.list(all=True):
        print(f"Name: {container.name}, Status: {container.status}")
except DockerException as e:
    print(f"Error connecting to Docker: {e}")