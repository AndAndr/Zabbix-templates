# Zabbix-templates/Applications/NTP
TemplateAppNTP.xml for zabbix 4.4 version in general.
Collecting data from selected source of "ntpq -p" output:


```     remote           refid      st t when poll reach   delay   offset  jitter
==============================================================================
*ntp-1.dom.nm    172.17.70.17     2 u  668 1024  377   10.201   +0.319   0.643
+ntp-2.dom.nm    172.17.70.17     2 u  867 1024  377    6.932   +1.012   3.857
```

For agent version lt 5.0 you must enable remote command: 
EnableRemoteCommands=1 -> /etc/zabbix/zabbix_agent.conf

For agent version gt 5.0 you must add AllowKey:
AllowKey=system.run[/usr/bin/ntpq*] -> /etc/zabbix/zabbix_agent.conf

Where `/usr/bin/ntpq` is correct `ntpq` location for your distro!

Also check macro {$NTPQ_LOCATION} value.



