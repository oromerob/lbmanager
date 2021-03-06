import paramiko
import os
import socket, struct
from libs.debinterface.interfaces import interfaces

class ConfManager():
    def __init__(self, host, user, passwd, port):
        self.host=host
        self.user=user
        self.passwd=passwd
        self.port=port
        self.connected=False
        self.error_msg=None
        self.ssh=None
        self.ftp=None
        self.connect()
        self.stdin=None
        self.stdout=None
        self.stderr=None

    def connect(self):
        ssh = paramiko.SSHClient()
        ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
        try:
            ssh.connect(self.host, username=self.user, password=self.passwd, port=self.port, timeout=5)
            self.ssh=ssh
            self.connected=True
        except Exception, e:
            self.connected=False
            self.error_msg=e

    def copy(self,src,dst):
        ftp=self.ssh.open_sftp()
        ftp.put(src,dst)
        self.ftp=ftp

    def command(self,command):
        self.stdin, self.stdout, self.stderr = self.ssh.exec_command(command)

    def close(self):
        self.ssh.close()

    def IPToNum(self,ip):
        packedIP = socket.inet_aton(ip)
        return struct.unpack("!L", packedIP)[0]

    def NumToIP(self,num):
        return socket.inet_ntoa(struct.pack('!L', num))
        
    def checkAndAddIP(self,ips):
        self.command('ip addr show |grep "inet "|grep -v "scope host lo"')
        exists = []
        for line in self.stdout.readlines():
            lines = line.strip().split(' ')
            if lines[1][:-3] not in ips:
                self.command('ip addr del %s dev lo' % lines[1])
            else:
                exists.append(lines[1][:-3])

        for ip in ips:
            if ip not in exists:
                command = 'ip addr add %s/32 dev lo label lo:%s' % (ip, self.IPToNum(ip))
                self.command( command )

    def checkAndConfigIP(self,ips):
        sftp=self.ssh.open_sftp()
        adapters = interfaces(sftp)
        new_adapters = []
        for adapter in adapters.adapters:
            if adapter.export()['name'] == 'lo':
                up = []
                down = []
                for ip in ips:
                    upline = 'ip addr add %s/32 dev $IFACE label $IFACE:%s' % ( ip, self.IPToNum(ip) )
                    up.append(upline)
                    downline = 'ip addr del %s/32 dev $IFACE' % ip
                    down.append(downline)

                adapter.setDown(down)
                adapter.setUp(up)

            new_adapters.append(adapter)

        adapters.adapters = new_adapters
        adapters.writeInterfaces()

class FilesManager():
    @staticmethod
    def DirExists(path):
        if not os.path.exists(path): os.makedirs(path)

    @staticmethod
    def WriteFile(dst,content):
        hl=open(dst, 'w')
        hl.write(content)
        hl.close()
