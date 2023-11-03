# Zabbix-templates/NTP
NTP/TemplateAppNTP.xml for zabbix 4.4 version in general. 
Collecting data from selected source of "ntpq -p" output:

For agent version lt 5.0 you must enable remote command: 
EnableRemoteCommands=1 -> /etc/zabbix/zabbix_agent.conf

For agent version gt 5.0 you must add AllowKey:
AllowKey=system.run[/usr/bin/ntpq*] -> /etc/zabbix/zabbix_agent.conf

Where `/usr/bin/ntpq` is correct `ntpq` location for your distro!

Also check macro {$NTPQ_LOCATION} value.



