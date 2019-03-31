from pexpect import pxssh
import pexpect
import sys

#s = pxssh.pxssh()
cisco_ssh = pxssh.pxssh(options={"StrictHostKeyChecking":"no","KexAlgorithms":"+diffie-hellman-group1-sha1"})
#s = pexpect.spawn("sshpass", ["-p",'', "ssh", "-l", "admin", "-oStrictHostKeyChecking=no", "-oKexAlgorithms=+diffie-hellman-group1-sha1", sys.argv[1]])
#cisco_ssh._spawn("sshpass",["-oKexAlgorithms=+diffie-hellman-group1-sha1"])
#cisco_ssh.SSH_OPTS=["-oKexAlgorithms=+diffie-hellman-group1-sha1","-oStrictHostKeyChecking=no"]
#cisco_ssh.SSH_OPTS="'-o'KexAlgorithms=+diffie-hellman-group1-sha1"
print(cisco_ssh.options)
cisco_ssh.login('192.168.20.253', 'noacs', 'rec0v3ry', port=22, auto_prompt_reset=False,)
