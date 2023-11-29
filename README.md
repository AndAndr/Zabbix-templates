# Zabbix-templates
Templates for Zabbix

## Applications
**Docker**
Auto-discovering docker containers and getting containers status via docker socket.

**ETCD**
For Zabbix 4.4. All Linux and Windows versions.

**NTP**
Collecting data from **"selected source"** of `ntpq -p` output:

```     remote           refid      st t when poll reach   delay   offset  jitter
==============================================================================
*ntp-1.dom.nm    172.17.70.17     2 u  668 1024  377   10.201   +0.319   0.643
+ntp-2.dom.nm    172.17.70.17     2 u  867 1024  377    6.932   +1.012   3.857
```

## Modules
**TemplateModuleEltexESRBGP4.xml** Eltex ESR BGP state


## Network
**UsergateUTM** Шаблон для Usergate UTM SNMP poll and traps.

**EltexMES** Шаблон+модули для коммутаторов Eltex серии MES.


## Other_hardware
**DeltaSTS** for zabbix 4.4 version. Delta Static Transfer Switch - **Delta STS32A** Tested on STS30002SR10035 v.01.12.15j.

**ELEMY_ATS-1203** Мониторинг по SNMP для версий Zabbix 4.4 и выше. Тестировалось на прошивке h2_b2_m1.1.8.

**EatonPowerware9390** Мониторинг по SNMP для версий Zabbix 4.4 и выше.

**LGe_webos** SNMP monitoring for 24/7 LG commercial display.

**APC_ATS** For Zabbix 4.4 version. Tested on APC AP7721.


## Server_hardware
**YADRO_Vegman_V4-4.xml** for zabbix 4-6 version. Monitoring YADRO Vegman servers via SNMP.




