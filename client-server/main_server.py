from utils.net_utils import *
from sys import exit

def main():
    
    with create_server_socket(SERVER_ADDR, SERVER_PORT) as s:

        n_connections = 0

        while True:

            print("\n\nWaiting for connections...")

            try:
                conn_socket, address = s.accept()
                n_connections += 1

                with conn_socket:
                    datos = recv_msg(conn_socket)

                    hostname, in_word = datos.split()

                    print(f"{n_connections}.-[{hostname}]: {in_word}")
                    
                    out_word = in_word.upper()

                    print(f"Sending {in_word} --> {out_word} to [{hostname}]")

                    conn_socket.sendall(bytes(out_word, FORMAT))
            
            except KeyboardInterrupt:
                print("\nProgram interrupted, Bye ;)")
                exit()



if __name__ == "__main__":
    pass
    main()

    