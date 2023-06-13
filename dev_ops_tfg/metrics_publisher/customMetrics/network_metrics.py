from probeTemplates.NetworkProbe import NetworkProbe


def get_microservice_name():
    import socket

    return socket.gethostname()

def get_pkg_direction(np: NetworkProbe):
    
    def get_my_mac() -> str:
        
        import uuid
        
        return (':'.join(['{:02x}'.format((uuid.getnode() >> ele) & 0xff)
        for ele in range(0,8*6,8)][::-1]))
    
    if not np or not np.eth_header:
        return None

    mac_addr = get_my_mac()
    
    dst_mac = np.eth_header.dst_mac 
    orig_mac = np.eth_header.orig_mac 

    if dst_mac == mac_addr:
        return "in"
    elif orig_mac == mac_addr:
        return "out"
    else:
        return None
    

def get_pkg_size(np: NetworkProbe):
    pass
    
    if not np.ip_header:
        return None
    
    return np.ip_header.t_len_bytes 


def get_protocol(np: NetworkProbe):
    protocols = {
        1 : "ICMP",
        6 : "TCP",
        17: "UDP",
    }
    if not np.ip_header:
        return None

    proto_num = np.ip_header.protocol

    if proto_num not in protocols:
        return None
    
    return protocols[proto_num]

def get_time_to_live(np: NetworkProbe):
    pass

    if not np.ip_header:
        return None
    
    return np.ip_header.ttl

def get_window_size(np: NetworkProbe):
    pass

    if not np.tcp_header:
        return None

    return np.tcp_header.window_size