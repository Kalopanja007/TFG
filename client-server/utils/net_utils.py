import socket
from utils.macros import *

def create_TCP_socket():
    '''
        Nombre: create_TCP_socket
        Descripción: Devuelve el objeto socket TCP.

        Retorno: 
            - El objeto de tipo socket creado
    '''
    s = socket.socket(socket.AF_INET, TCP_SOCKET)

    s.setblocking(True)

    return s


def create_server_socket(ip, port):
    '''
        Nombre: create_server_socket
        Descripción: Crea un socket servidor listo para escuchar (UDP o TCP).
        Argumentos:
            - ip: string de la ip a la que le asignaremos este socket 
            - port: número del puerto
        Retorno: 
            - El objeto de tipo socket preparado para llamar a accept
    '''
    s = create_TCP_socket()

    s.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)

    s.bind((ip, port))

    s.listen(CONTROL_BACKLOG)

    return s


def create_client_socket(ip, port):
    '''
        Nombre: create_client_socket
        Descripción: Crea un socket de tipo cliente listo para enviar y recibir.
        Argumentos:
            - ip: string de la ip a la que le asignaremos este socket 
            - port: número del puerto
        Retorno: 
            - El objeto de tipo socket preparado para enviar y recibir paquetes
    '''

    s = create_TCP_socket()

    s.settimeout(CLIENT_TIMEOUT)

    s.connect((ip, port))
    s.settimeout(None)

    return s


def recv_msg(conn: socket.socket):
    '''
        Nombre: recv_msg
        Descripción: Recibe información del socket que hemos introducido como argumento.
        Argumentos:
            - conn: socket con el que vamos a recibir BUFFSIZE bytes 
        Retorno: 
            - Los datos recibidos a través del socket
    '''

    datos = ""

    conn.setblocking(True)

    try:
        while True:
            msg = conn.recv(BUFFSIZE).decode()
            if not msg:
                break
            # A partir de ahora si no hay datos que leer finalizamos el bucle

            datos += msg

            conn.setblocking(False)
    except socket.error as e:
        pass

    return datos