# Docker

**Template App Docker.xml** for Zabbix v.4

Auto-discovering docker containers and getting containers status via docker socket.


Requirements
------------

1. Add zabbix-agent user to the docker group.
sudo usermod -G docker -a zabbix

2. Install curl and jq packages.
sudo apt install curl jq

3. Enable remote command in zabbix_agentd.conf.
AllowKey=system.run[*]   # For zabbix_agent version>=5
EnableRemoteCommands=1   #For zabbix_agent version<=4

4. Restart zabbix_agent.


License
-------

BSD

Author Information
------------------

Andrey

