from pd_comm_server import ServerHandle
from pymavlink import mavutil

import time


# UNIT TEST
if __name__ == "__main__":
    sitl_platform_udp = 'udpin:localhost:14551'
    sh = ServerHandle(sitl_platform_udp)
    

    msg_cnt = 0
    
    prev_delta = None
    avg_delta = None 
    
    
    print("Running...\n")
    while 1:
        fetch_begin = time.time()
        
        sh.get_telemetry()


        msg_cnt += 1
        fetch_end = time.time()


        # Display test params
        current_delta = fetch_end - fetch_begin
        if prev_delta is not None:
            avg_delta = (current_delta + prev_delta)/2.0

        else:
            prev_delta = current_delta

        # 
        if msg_cnt % 100 == 0:
            pass

        
