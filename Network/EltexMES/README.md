# EltexMES

**Template Eltex MES SNMPv2 ver.2.xml** Шаблон для коммутаторов Eltex серии MES для версии Zabbix 4.4.


Работает совместно с модулями:
**Template Module Eltex MES Interfaces SNMPv2.xml**,
**Template Module Eltex OSPF SNMPv2.xml**,
**Template Module Generic SNMPv2**


Реализовано автообнаружение:
1. Вентиляторов.
2. Версий ПО.
3. Датчиков температуры.
4. Соседей OSPF.
5. Интерфейсов медных, оптических, агрегированных.


Корректно работает со стеком. Тестировалось на MES3324_rev.B, MES5332A_rev.B.


## Howto:
1. Импорт модулей **Template Module Eltex MES Interfaces SNMPv2.xml**, **Template Module Eltex OSPF SNMPv2.xml**.
2. Импорт шаблона **Template Eltex MES SNMPv2 ver.2.xml**.
