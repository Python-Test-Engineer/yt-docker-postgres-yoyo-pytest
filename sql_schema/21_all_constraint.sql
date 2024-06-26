SELECT con.conname "constraint",
       concat(nsp.nspname, '.', rel.relname) "table",
       (SELECT array_agg(att.attname)
               FROM pg_attribute att
                    INNER JOIN unnest(con.conkey) unnest(conkey)
                               ON unnest.conkey = att.attnum
               WHERE att.attrelid = con.conrelid) "columns"
       FROM pg_constraint con
            INNER JOIN pg_class rel
                       ON rel.oid = con.conrelid
            INNER JOIN pg_namespace nsp
                       ON nsp.oid = rel.relnamespace;