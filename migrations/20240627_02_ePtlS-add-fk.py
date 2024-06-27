"""
Add FK
"""

from yoyo import step

__depends__ = {"20240627_01_nOYE1-add-tables"}


steps = [
    step(
        """

alter table product_tags add constraint fk_products_product_tags 
    foreign key (product_id)
    references products (id) ;
alter table product_tags add constraint fk_tags_product_tags 
    foreign key (tag_id)
    references tags (id) ;
alter table product_categories add constraint fk_category_products_categories 
    foreign key (category_id)
    references categories (id) ;
alter table sales_orders add constraint fk_user_sales_order 
    foreign key (user_id)
    references users (id) ;
alter table order_products add constraint fk_sales_orders_order_products 
    foreign key (order_id)
    references sales_orders (id) ;
alter table cc_transactions add constraint fk_sales_order_cc_transaction 
    foreign key (order_id)
    references sales_orders (id) ;
alter table product_categories add constraint fk_product_product_category 
    foreign key (product_id)
    references products (id) ;
alter table categories add constraint fk_category_parent_category 
    foreign key (parent_id)
    references categories (id) ;

        """,
        # ROLLBACK
        """
            
    -- get_constraints_drop 

    alter table product_tags drop constraint fk_products_product_tags ;
    alter table product_tags drop constraint fk_tags_product_tags ;
    alter table product_categories drop constraint fk_category_products_categories ;
    alter table sales_orders drop constraint fk_user_sales_order ;
   
    alter table order_products drop constraint fk_sales_orders_order_products ;
    alter table cc_transactions drop constraint fk_sales_order_cc_transaction ;
    alter table product_categories drop constraint fk_product_product_category ;
    alter table categories drop constraint fk_category_parent_category ;

        """,
    )
]
