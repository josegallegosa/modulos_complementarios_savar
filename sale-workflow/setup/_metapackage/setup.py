import setuptools

with open('VERSION.txt', 'r') as f:
    version = f.read().strip()

setuptools.setup(
    name="odoo14-addons-oca-sale-workflow",
    description="Meta package for oca-sale-workflow Odoo addons",
    version=version,
    install_requires=[
        'odoo14-addon-portal_sale_personal_data_only',
        'odoo14-addon-pricelist_cache',
        'odoo14-addon-pricelist_cache_rest',
        'odoo14-addon-product_supplierinfo_for_customer_sale',
        'odoo14-addon-sale_advance_payment',
        'odoo14-addon-sale_automatic_workflow',
        'odoo14-addon-sale_automatic_workflow_delivery_state',
        'odoo14-addon-sale_automatic_workflow_payment_mode',
        'odoo14-addon-sale_by_packaging',
        'odoo14-addon-sale_cancel_confirm',
        'odoo14-addon-sale_commercial_partner',
        'odoo14-addon-sale_commitment_date_mandatory',
        'odoo14-addon-sale_delivery_state',
        'odoo14-addon-sale_discount_display_amount',
        'odoo14-addon-sale_exception',
        'odoo14-addon-sale_force_invoiced',
        'odoo14-addon-sale_invoice_blocking',
        'odoo14-addon-sale_invoice_plan',
        'odoo14-addon-sale_isolated_quotation',
        'odoo14-addon-sale_last_price_info',
        'odoo14-addon-sale_mail_autosubscribe',
        'odoo14-addon-sale_mrp_bom',
        'odoo14-addon-sale_order_archive',
        'odoo14-addon-sale_order_carrier_auto_assign',
        'odoo14-addon-sale_order_disable_user_autosubscribe',
        'odoo14-addon-sale_order_general_discount',
        'odoo14-addon-sale_order_line_date',
        'odoo14-addon-sale_order_line_description',
        'odoo14-addon-sale_order_line_menu',
        'odoo14-addon-sale_order_line_note',
        'odoo14-addon-sale_order_line_packaging_qty',
        'odoo14-addon-sale_order_line_price_history',
        'odoo14-addon-sale_order_lot_generator',
        'odoo14-addon-sale_order_lot_selection',
        'odoo14-addon-sale_order_note_template',
        'odoo14-addon-sale_order_qty_change_no_recompute',
        'odoo14-addon-sale_order_report_without_price',
        'odoo14-addon-sale_order_revision',
        'odoo14-addon-sale_order_type',
        'odoo14-addon-sale_partner_incoterm',
        'odoo14-addon-sale_partner_version',
        'odoo14-addon-sale_pricelist_from_commitment_date',
        'odoo14-addon-sale_product_brand_exception',
        'odoo14-addon-sale_product_category_menu',
        'odoo14-addon-sale_product_multi_add',
        'odoo14-addon-sale_product_rating_verified',
        'odoo14-addon-sale_product_seasonality',
        'odoo14-addon-sale_product_set',
        'odoo14-addon-sale_product_set_packaging_qty',
        'odoo14-addon-sale_product_set_sale_by_packaging',
        'odoo14-addon-sale_quotation_number',
        'odoo14-addon-sale_shipping_info_helper',
        'odoo14-addon-sale_start_end_dates',
        'odoo14-addon-sale_stock_picking_blocking',
        'odoo14-addon-sale_tier_validation',
        'odoo14-addon-sale_transaction_form_link',
        'odoo14-addon-sale_validity',
        'odoo14-addon-sale_wishlist',
        'odoo14-addon-sales_team_security',
        'odoo14-addon-sales_team_security_crm',
        'odoo14-addon-sales_team_security_sale',
    ],
    classifiers=[
        'Programming Language :: Python',
        'Framework :: Odoo',
        'Framework :: Odoo :: 14.0',
    ]
)