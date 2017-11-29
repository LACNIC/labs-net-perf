# NET-PERF

## ATENCIÓN

**Este set de scripts fue desarrollado durante un corto período de tiempo en el año 2010. Luego de ese momento han recibido poca o ninguna atención.**
**Los mismos pueden contener bugs o tener problemas para correr en versiones más recientes de python**

## Metricas y mediciones de red

El concepto original incluía generar una especie de framework para la obtención periódica de métricas, pero la única que se desarrolló de forma más o menos completa fue la de "Resolución de DNS en IPv6".

## Metrica de resolucion de DNS x IPv6

### Requisitos previos:

- Paquete cliente MySQL: "sudo apt-get install default-libmysqlclient-dev"
- Python 2.x
   - Modulos:
      - dnspython
      - mysqlclient
- base de datos MySQL
- importar en la base el dump o la estructura vacía
- editar DbAccess.py y adecuar los parámetros de acceso a la base de datos

### Ejecucion:

```
./src/net-perf.py --test=v6-dns-resol --target=perform
```

### Obtener reporte:

Para obtener el reporte hay que consultar directamente a la base de datos. Hay un esqueleto de como hacerlo con el propio script pero no está completo.

```
use `net-perf`
SELECT A.`target-handle`, domain, status from targets AS A, `test-results` AS B WHERE A.`target-handle`=B.`target-handle` AND B.`test-datetime` LIKE "2017-%" and A.`target-handle` LIKE "%-tld%" GROUP BY domain ORDER BY status;
```
