# Chrony

Автообнаружение и мониторинг источников времени, заданных для синхронизации, через вызов `/usr/bin/chronyc`

Для Zabbix версии 7.0

## Howto:

1. Добавить в файл /etc/sudoers:
`zabbix ALL = NOPASSWD: /usr/bin/chronyc -nc ntpdata*`
, где zabbix - пользователь, от имени которого работает агент.
2. Добавить в файл /etc/zabbix/zabbix_agent.conf:

`AllowKey=system.run[/usr/bin/sudo /usr/bin/chronyc -nc ntpdata*]`

`AllowKey=system.run[/usr/bin/chronyc -nc sources*]`


3. Прикрепить шаблон к хосту, где выполнены п.1,2
4. При необходимости, скорректировать значения макросов.


