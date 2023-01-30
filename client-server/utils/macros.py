from socket import SOCK_STREAM, gethostname

LOCALHOST = "localhost"
PORT = 2100

# SERVER
SERVER_PORT = PORT
SERVER_ADDR = "10.12.215.168"

# OTHERS
FORMAT   = "utf-8"
BUFFSIZE = 1024


K_HOSTNAME = "hostname" 
K_WORD     = "word"

HOSTNAME = gethostname()

############################

CLIENT_TIMEOUT  = 10
CONTROL_BACKLOG = 50
TCP_SOCKET      = SOCK_STREAM