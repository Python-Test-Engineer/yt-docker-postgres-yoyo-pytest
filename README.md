# Database migrations with YoYo

*view in preview for images, otherwise view images in images folder.*

Based on: https://www.youtube.com/watch?v=2ldy3HcW_w8 with a variety of adaptations for my Windows set up.

https://ollycope.com/software/yoyo/latest/#

https://github.com/medwig/yoyo-migration-tutorial

Set up of Docker with Postgress, PgAdmin and Adminer with Python CRUD.

Combines PgAdmin and Adminer for DB viewing.

Don't forget `docker compose up -d` or `docker compose up`.


## Set up Docker-Postgres-PgAdmin-Adminer
[My YouTube Video](https://youtu.be/mipRKPHwlBkI)

https://youtu.be/mipRKPHwlBk

I use a named volume here but video has bind mount volume - used in `docker-compose-bound-mount.yml`

NOTE
```
conn = psycopg2.connect(
    database="postgres",
    user="postgres",
    password="postgres",
    host="host.docker.internal", !!! localhost etc don't seem to work...
)
```

### PgAdmin

<img src="./images/register-server-1.png"  width="500" >

<img src="./images/register-server-2.png"  width="500" >


<!-- ![PAGE](./images/register-server-1.png ) -->


- http://localhost:5050/
- admin@email.com
- admin

register-server

page-1 use any name
page-2:
      - POSTGRES_DB=postgres # optional
      - POSTGRES_USER=postgres
      - POSTGRES_PASSWORD=postgres

run docker-compose up in terminal ->

 ✔ Network postgres_default       Created                                                                                 
 ✔ Container postgres-pg-admin-1  Created                                                                                 
 ✔ Container postgres-postgres-1  Created                                                                                 
 ✔ Container postgres-adminer-1   Created     

### Adminer

admininer login on port http://localhost:8080

<img src="./images/adminer-login.png"  width="500" >

### YoYo

When I installed on Windows it complained of 'no pkg_resources'.

This was fixed with installing setuptools, (in requirements.txt).

## Using existing unapplied migrations I ran `yoyo list` I got:

![Initial](./images/yoyo-initial.png 'YoYo')

## After `yoyo apply`:

![First Apply](./images/yoyo-list-after-apply.png 'YoYo')

## After two `yoyo rollback`:

![Two Rollbacks](./images/yoyo-list-after-two-rollbacks.png 'YoYo')

## PgAdmin looks like:

![PgAdmin](./images/yoyo-pgadmin.png 'YoYo')