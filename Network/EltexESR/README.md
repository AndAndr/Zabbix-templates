# EltexESR

Шаблоны и модули для маршрутизаторов Eltex серии ESR для версий Zabbix 4,6,7.
Мониторинг по SNMPv2 маршрутизаторов Eltex ESR. Тестировалось на ESR1000, ESR1500.

## Реализовано автообнаружение:
1. Интерфейсов.
2. ЦПУ.
3. BGP4 пиров.
4. Соседей OSPFv2.

## Дополнительно реализован мониторинг:
1. Температуры.
2. Блоков питания.
3. Памяти.
4. Вентиляторов.
5. Состояния пиров BGP4.
6. Состояния соседей OSPFv2.

## Howto:
1. Импорт модулей, шаблона **Generic SNMP**.
2. Импорт **Template Eltex ESR SNMPv2**.
3. При желании, модули и шаблон п.1 можно отсоединить от шаблона п.2.


