# NET-PERF
## Metricas y mediciones de red

## Metrica de resolucion de DNS x IPv6

Ejecucion:
./src/net-perf.py --test=v6-dns-resol --target=perform

Obtener reporte:
```
SELECT A.`target-handle`, domain, status from targets AS A, `test-results` AS B WHERE A.`target-handle`=B.`target-handle` AND B.`test-datetime` LIKE "2017-%" and A.`target-handle` LIKE "%-tld%" GROUP BY domain ORDER BY status;
ERROR 1046 (3D000): No database selected
```
