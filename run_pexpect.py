import pexpect
import sys
from pathlib import Path

username = sys.argv[1]
path = Path(sys.argv[2])
child = pexpect.spawn(f'su - {username}')
child.expect('Password:')
child.sendline(path.open().read().strip())
child.expect('\$')
child.sendline('sudo su')
child.sendline(path.open().read().strip())
child.sendline('sed -i "s/X11Forwarding yes/#X11Forwarding yes/" /etc/ssh/sshd_config')
child.sendline('cp /etc/ssh/sshd_config /tmp/sshd_config')
child.sendline('chmod a+rwx /tmp/sshd_config')
child.sendline('systemctl restart sshd')
child.sendeof()
child.sendeof()
print(child.read())
