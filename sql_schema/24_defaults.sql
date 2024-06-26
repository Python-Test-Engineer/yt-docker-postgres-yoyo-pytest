select col.table_schema,
       col.table_name,
       col.column_name,
       col.column_default
from information_schema.columns col
where col.column_default is not null
      and col.table_schema not in('information_schema', 'pg_catalog')
order by col.column_name;