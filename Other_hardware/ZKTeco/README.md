# Биометрический считыватель ZKTeco

Контроль состояния считывателей с использованием библиотек zklib (UDP4370) и агента Zabbix. Тестировалось на **MA300**.
Шаблон `Template_ZKTeco.xml` создан для четырёх считывателей. Количество считывателей легко модифицируется в большую или
меньшую стороны.

## Howto:

0. С условного сервера **srv1** необходимо обеспечить доступ к порту UDP4370 считывателей
1. Скопировать `template_zkteco.conf` в каталог `/etc/zabbix/zabbix_agentd.conf.d/` сервера **srv1**
2. Включить опцию и увеличить таймаут `Timeout=4` в файле `/etc/zabbix/zabbix_agentd.conf`сервера **srv1**
3. Каталог `zklib` положить в `/var/lib/zabbix/zklib/` сервера **srv1**
4. Скопировать `zktstatus.py` в `/var/lib/zabbix/zklib/` сервера **srv1**
5. Рестарт агента Заббикса на сервере **srv1**
6. Импорт шаблона `Template_ZKTeco.xml` и привязка его к **srv1**
7. Корректировка значений макросов `{$FPSCANER1}, {$FPSCANER2}, {$FPSCANER3}, {$FPSCANER4}` в шаблоне `Template_ZKTeco.xml` 
   или создание их на **srv1**. Значения = IP считывателей.