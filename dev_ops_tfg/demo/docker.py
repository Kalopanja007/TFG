from random import choice, randint
from os import system
from time import sleep

SERVICES = ["IMG_GEN", "ASCII_ART", "GRAY_SCALE"]

MICROSERVICES = ["Frontend", "TextDescriptor", "APICaller", "Showdata", "ImgUploader", "ASCIIArt", "GrayScale", "VideoSrv", "FFmpeg"]

EXEC_CMD = "docker exec"
STOP_CMD = "docker container stop"

def container_is_up(container: str) -> bool:
    ret = False
    CMD = f"{EXEC_CMD} {container} hostname > /dev/null 2>&1"
    
    if system(f"{CMD}") == 0:
        ret = True
    return ret

def is_running():
    import subprocess
    DOCKER_CMD = "docker ps -q"
    ret = subprocess.check_output(f"{DOCKER_CMD}", shell=True, universal_newlines=True)
    
    return False if ret == '' else True

def test():
    cont = random_container()
    print(cont, container_is_up(cont))

def random_container() -> str:
    while True:
        candidate = choice(MICROSERVICES)
        if container_is_up(candidate):
            return candidate

def choose_two_containers() -> tuple[str, str]:    
    while True:
        cont_1 = random_container()
        cont_2 = random_container()

        if cont_1 != cont_2: 
            return cont_1, cont_2
    

def stop():
    pass
    container = random_container()
    
    print(f"Stopping {container}...")
    system(f"{STOP_CMD} {container}")
    print(f"Stopped {container} !!!")

def ping():
    pass
    cont_1, cont_2 = choose_two_containers() 
    
    seconds = randint(2,8)

    ping_cmd = f"bash -c 'ping {cont_2} & sleep {seconds} && kill -9 $(pgrep -f ping)'"

    print(f"Ping command between {cont_1} and {cont_2} ({seconds}s)")
    print()
    system(f"{EXEC_CMD} {cont_1} {ping_cmd}")
    print()
    print(f"End ping")


def ffmpeg():
    while True:
        container = random_container()
        
        if container != "VideoSrv":
            break
    
    ffmpeg_cmd = f"{container} ./receivevideo.sh"

    print(f"FFmpeg from {container}")
    system(f"{EXEC_CMD} {ffmpeg_cmd} > /dev/null 2>&1")


def main():

    seconds = randint(2,8)

    if is_running():
        # stop()
        ping()

        sleep(seconds)
        print(f"Waiting {seconds} seconds")
        
        ffmpeg()
        # test()
    
    else:
        print("Microservices are not running :(")

if __name__ == "__main__":
    pass
    main()