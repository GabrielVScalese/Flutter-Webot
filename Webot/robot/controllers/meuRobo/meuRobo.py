import struct
import socket
import sys
import _thread
import json

from controller import Robot, GPS

timestep = 64

speed = 0
direction = 1

def get_port():
    return 9001

def get_ip():
    hostname = socket.gethostname()
    ip_address = socket.gethostbyname(hostname)
   
    return ip_address

def get_info (request):
    min = request.find('{')
    max = request.find('}')
    
    data = request[min:max + 1]
    
    dict = json.loads(data)
     
    return dict
    
def on_new_client(socket, addr):
    global robot_controler
    global speed
    global direction
        
    while True:
        msg = socket.recv(1024)
        if msg:
            break
        else:
            break
            
    msg1 = msg.decode()
    
    info = get_info(msg1)
    
    if info['msg'].__contains__('l'):
       direction = 1
       
    elif info['msg'].__contains__('r'):
        direction = -1
    
    elif info['msg'].__contains__('u'):
        if speed < 10:
            speed = speed + 1
    
    elif info['msg'].__contains__('d'):
        if speed > 0:
            speed = speed - 1
    else:
        speed = 0
    
    socket.send('Message'.encode())
        
    socket.close()

    return        


def servidor(https, hport):
    sockHttp = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    try:
        sockHttp.bind((https, hport))
    except:
        sockHttp.bind(('', hport))
        
    sockHttp.listen(1)
    
    while True:
        client, addr = sockHttp.accept()
        _thread.start_new_thread(on_new_client, (client,addr))


class MeuRobot:
    def __init__(self, robot):
        
        self.robot = robot
        self.nome  = robot.getName()
        self.motor_esq = self.robot.getDevice("motor roda esquerda")
        self.motor_dir = self.robot.getDevice("motor roda direita")

        self.motor_esq.setPosition(float('+inf'))
        self.motor_dir.setPosition(float('+inf'))

        self.motor_esq.setVelocity(0.0)
        self.motor_dir.setVelocity(0.0)

        self.ir0 = self.robot.getDevice("ir0")
        self.ir0.enable(timestep)

        self.ir1 = self.robot.getDevice("ir1")
        self.ir1.enable(timestep)

        self.gps = self.robot.getDevice("gps")
        self.gps.enable(timestep)

        self.ir3 = self.robot.getDevice("ir3")
        self.ir3.enable(timestep)

       
    def run(self):
        raise NotImplementedError
        

class TI502(MeuRobot):
    def run(self):
        while self.robot.step(timestep) != -1:
            self.motor_esq.setVelocity(speed * direction)
            self.motor_dir.setVelocity(speed * direction)


robot = Robot()

robot_controler = TI502(robot)

_thread.start_new_thread(servidor, (get_ip(),get_port()))

robot_controler.run()         

