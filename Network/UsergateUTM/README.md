# UsergateUTM

Тестировался на Usergate D200 SNMPv2.

Для Zabbix версий 4,7.

Часть триггеров уровня инф. закрываются сами через 5 минут (см. макрос {$TRAPPEDTRIGGER_TTL}),
остальные критичные - закрываются вручную, но не ранее значения этого макроса.

## Howto:
1. Настроить snmptrapd в соответствии с Zabbix Manual.
2. Импортировать и прикрепить шаблон к хосту.
3. Настроить устройство на отправку трапов, разрешить SNMP-запросы.
4. Настроить отправку всех событий, кроме событий сработки правил МЭ.
