# FC HBA

Шаблон для мониторинга (через Zabbix агента) FC HBA (в том числе fc_host_statistics) Linux для Zabbix 4 и Zabbix 7.

Тестировалось на qla2xxx.


## Howto:

Zabbix 7: Присоединить шаблон к хосту.

Zabbix 4: Необходимо переопределение на хосте макроса {$FC.LOWEST.HOSTNUM} для указания минимального порядкового

номера /sys/class/fc_host/host*, если отсчёт идёт не с единицы.
