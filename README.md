# NET-PERF

## ATENCIÓN

**Este set de scripts fueron escritos en un corto período durante el año 2010. Luego de ese momento han recibido poca o ninguna atención.**
**Los mismos pueden contener bugs o tener problemas para correr en versiones más recientes de python**

## Metricas y mediciones de red

## Metrica de resolucion de DNS x IPv6

Requisitos previos:
- Python 2.x
- base de datos MySQL
- importar en la base el dump o la estructura vacía
- editar DbAccess.py y adecuar los parámetros de acceso a la base de datos

Ejecucion:
./src/net-perf.py --test=v6-dns-resol --target=perform

Obtener reporte:
```
use `net-perf`
SELECT A.`target-handle`, domain, status from targets AS A, `test-results` AS B WHERE A.`target-handle`=B.`target-handle` AND B.`test-datetime` LIKE "2017-%" and A.`target-handle` LIKE "%-tld%" GROUP BY domain ORDER BY status;
```
