# 大体流程
# 1. esp32先链接wifi，让其拥有IP地址
# 2. 创建UDP socket
# 3. 接收UDP数据
# 4. 根据UDP数据控制led
import time
import network
import machine


def do_connect():
    """
    此处链接WiFi
    """
    wlan = network.WLAN(network.STA_IF)
    wlan.active(True)
    if not wlan.isconnected():
        print('connecting to network...')
        wlan.connect('Xiaomi_4A2F', 'as1234567890')
        i = 1
        while not wlan.isconnected():
            print("connecting to network...{}".format(i))
            time.sleep(1)
    print('network config:', wlan.ifconfig())


def create_udp_socket():
    import socket

    # 1. 创建udp套接字
    udp_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    # 2. 绑定一个固定端口
    udp_socket.bind(("0.0.0.0", 7788))
    
    return udp_socket
    
    
def main():
    # 1. esp32先链接wifi，让其拥有IP地址
    do_connect()
    
    # 2. 创建UDP socket
    udp_socket = create_udp_socket()
    
    #make a GPIO build control object
    led = machine.Pin(2, machine.Pin.OUT)

    # 3. 接收UDP数据
    while True:
        recv_data, sender_info = udp_socket.recvfrom(1024)
        print("{}发送的数据: {}".format(sender_info, recv_data))
        
        recv_data_str = recv_data.decode("utf-8")
        print("解码后的数据：{}".format(recv_data_str))
        
    # 4. 根据UDP数据控制led
    if recv_data_str == "light on":
        led.value(0)
    elif recv_data_str == "light off":
        led.value(1)


if __name__ == "__main__":
    main()