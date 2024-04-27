import sys
import subprocess
import os

def fetch():
    os.chdir(docker_compose_dir)
    command_line = f"docker compose run --rm tester fetch"
    subprocess.run(command_line.split(" "))
    os.chdir(original_dir)
    return

def run(command):
    # Path to the directory containing docker-compose.yml
    if(command == "fetch"):
        fetch()

original_dir = os.getcwd()
docker_compose_dir = os.path.join(os.path.dirname(__file__))

if __name__ == '__main__':
    # Default command if no argument is provided
    command = "fetch"
    # Check if an argument is provided and use it as the command
    if len(sys.argv) > 1:
        command = sys.argv[1]
    run(command)
