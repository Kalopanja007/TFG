from utils.net_utils import *
import string
import random

import time

def random_lower_str():
    all_lowercase = [*string.ascii_lowercase]
    
    random.shuffle(all_lowercase)
    random_pos = random.randint(1,len(all_lowercase))
    
    return ''.join(all_lowercase[:random_pos])

def main():

    lower_str = random_lower_str()
    payload = f"{HOSTNAME} {lower_str}"

    with create_client_socket(SERVER_ADDR, SERVER_PORT) as s:
        
        print(f"Sending {lower_str} to server...")
        s.sendall(bytes(payload, FORMAT))

        time.sleep(5)

        upper_str = recv_msg(s)
        print(f"Received {upper_str} from server...")


if __name__ == "__main__":
    main()