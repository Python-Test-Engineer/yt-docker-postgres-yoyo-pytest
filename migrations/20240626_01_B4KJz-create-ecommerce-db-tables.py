"""
Create ecommerce db tables
"""

from yoyo import step

__depends__ = {}

steps = [
    step(
        """
create table users (
   id          serial                   not null     ,
   email       varchar(255)             not null     ,
   first_name  varchar(255)             not null     ,
   last_name   varchar(255)             not null     ,
   active      bool                      default true,
   inserted_at timestamp with time zone not null     ,
   updated_at  timestamp with time zone not null     ,
   constraint pk_users primary key (id)
)   ;

create table categories (
   id          serial                   not null,
   name        varchar(255)             not null,
   parent_id   integer                          ,
   inserted_at timestamp with time zone not null,
   updated_at  timestamp with time zone not null,
   constraint pk_categories primary key (id)
)   ;
create table products (
   id                serial                   not null      ,
   sku               varchar(255)             not null      ,
   name              varchar(255)             not null      ,
   description       text                                   ,
   product_status_id integer                  not null      ,
   regular_price     numeric                   default 0    ,
   discount_price    numeric                   default 0    ,
   quantity          integer                   default 0    ,
   taxable           bool                      default false,
   inserted_at       timestamp with time zone not null      ,
   updated_at        timestamp with time zone not null      ,
   constraint pk_products primary key (id)
)   ;
create table tags (
   id          serial                   not null,
   name        varchar(255)             not null,
   inserted_at timestamp with time zone not null,
   updated_at  timestamp with time zone not null,
   constraint pk_tags primary key (id)
)   ;
create table sales_orders (
   id          serial                   not null,
   order_date  date                     not null,
   total       numeric                  not null,
   coupon_id   integer                          ,
   session_id  varchar(255)             not null,
   user_id     integer                  not null,
   inserted_at timestamp with time zone not null,
   updated_at  timestamp with time zone not null,
   constraint pk_sales_orders primary key (id)
)   ;

create table product_tags (
   product_id  integer                  not null,
   tag_id      integer                  not null,
   inserted_at timestamp with time zone not null,
   updated_at  timestamp with time zone not null,
   constraint pk_product_tags primary key (product_id,tag_id)
)   ;
create table cc_transactions (
   id                 serial                   not null,
   code               varchar(255)                     ,
   order_id           integer                  not null,
   transdate          timestamp with time zone         ,
   processor          varchar(255)             not null,
   processor_trans_id varchar(255)             not null,
   amount             numeric                  not null,
   cc_num             varchar(255)                     ,
   cc_type            varchar(255)                     ,
   response           text                             ,
   inserted_at        timestamp with time zone not null,
   updated_at         timestamp with time zone not null,
   constraint pk_cc_transactions primary key (id)
)   ;
create table product_categories (
   category_id integer                  not null,
   product_id  integer                  not null,
   inserted_at timestamp with time zone not null,
   updated_at  timestamp with time zone not null,
   constraint pk_product_categories primary key (category_id,product_id)
)   ;
create table order_products (
   id          serial                   not null,
   order_id    integer                          ,
   sku         varchar(255)             not null,
   name        varchar(255)             not null,
   description text                             ,
   price       numeric                  not null,
   quantity    integer                  not null,
   subtotal    numeric                  not null,
   inserted_at timestamp with time zone not null,
   updated_at  timestamp with time zone not null,
   constraint pk_order_products primary key (id)
)   ;

        """,
        "",
    )
]
