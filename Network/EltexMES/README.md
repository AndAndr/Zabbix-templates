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

Обнаружение интерфейсов с т.н. context macros, что позволяет определять реакцию Заббикса на падение интерфейсов.

Например:

Вариант1: На устройстве **coreeltex1** все интерфейсы важные, кроме te1/0/2. То есть, все интерфейсы стреляют, кроме te1/0/2.
{$IFCONTROL}=1 (Определен в модуле **Template Module Eltex MES Interfaces SNMPv2** по-умолчанию)

{$IFCONTROL:"te1/0/2"}=0 (Создать макроc на устройстве **coreeltex1**)

Вариант2: На устройстве **accesseltex2** все интерфейсы не важные, кроме te1/0/2. То есть, стреляет только te1/0/2.
{$IFCONTROL}=0 (Переопределить на устройстве **accesseltex2**)

{$IFCONTROL:"te1/0/2"}=1 (Создать макроc на устройстве **accesseltex2**)




Корректно работает со стеком. Тестировалось на MES3324_rev.B, MES5332A_rev.B.


## Howto:
1. Импорт модулей **Template Module Eltex MES Interfaces SNMPv2.xml**, **Template Module Eltex OSPF SNMPv2.xml**.
2. Импорт шаблона **Template Eltex MES SNMPv2 ver.2.xml**.
