# -*- coding: utf-8 -*-
##############################################################################
#
#    OpenERP, Open Source Management Solution
#    Copyright (C) 2016-Today Geminate Consultancy Services (<http://geminatecs.com>).
#
#    This program is free software: you can redistribute it and/or modify
#    it under the terms of the GNU Affero General Public License as
#    published by the Free Software Foundation, either version 3 of the
#    License, or (at your option) any later version.
#
#    This program is distributed in the hope that it will be useful,
#    but WITHOUT ANY WARRANTY; without even the implied warranty of
#    MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#    GNU Affero General Public License for more details.
#
#    You should have received a copy of the GNU Affero General Public License
#    along with this program.  If not, see <http://www.gnu.org/licenses/>.
#
##############################################################################
{
    'name': 'QuangVinh Geminate Ecommerce Theme',
    'description': 'Theme Gashion Vega is a Modern, Clean & Sectioned Odoo eCommerce Theme.The theme is a very user-friendly and is suitable for your eCommerce website.It is the most powerful, easy to use theme.Many customized snippets allows to feature higher consumer experience.it is suitable for eCommerce sites of all types of industries like Furniture, Fashion, Electronics, Beauty, Health & Fitness, Jewellery, Food, Sports,etc.Being fully Responsive, it looks equally stunning on all kinds of screens and devices.Contains New arrival and Deal of the week,Product Silder,Most Popular,Trending Product. This theme is fully customized the eCommerce website, shop view, product view, contact us page, about us page, magnify product photos,cart, Compress, Whishlist...etc.',
    'summary': 'Theme Gashion Vega is a Modern, Clean & Sectioned Odoo eCommerce Theme.The theme is a very user-friendly and is suitable for your eCommerce website.It is the most powerful, easy to use theme.Many customized snippets allows to feature higher consumer experience.it is suitable for eCommerce sites of all types of industries like Furniture, Fashion, Electronics, Beauty, Health & Fitness, Jewellery, Food, Sports,etc.',
    'category': 'Theme/eCommerce',
    'version': '16.0.0.1',
    'license': 'Other proprietary',
    'author': 'Geminate Consultancy Services',
    'company': 'Geminate Consultancy Services',
    'maintainer': 'Geminate Consultancy Services',
    'website': "http://www.geminatecs.com",
    'depends': ['website_sale_wishlist', 'website_sale',
                'website_sale_comparison'],
    'data': [

        'views/header.xml',
        'views/footer.xml',
        'views/res_company.xml',
        'views/home.xml',
        'views/contact_us.xml',
        'views/about.xml',
        'views/product_template.xml',
        'views/address_contact.xml',
        'views/templates.xml',
        'views/test_index.xml',
        'views/website_template.xml',
        
        'views/website_template_views.xml',
        'views/website_template_views2.xml',

        'views/header/header2.xml',
        'views/header/header3.xml',
        'views/header/header4.xml',
        'views/header/header5.xml',
        'views/header/header6.xml',
        
        
        'views/snippets/home.xml',
        'views/snippets/image_blocks.xml',
        'views/snippets/about_us_block.xml',
        'views/snippets/auto_count_block.xml',
        'views/snippets/big_pic.xml',
        'views/snippets/card_silder.xml',
        'views/snippets/client_block.xml',
        'views/snippets/hot_deals.xml',
        'views/snippets/product_silder.xml',
        'views/snippets/progressbar.xml',
        'views/snippets/right_side_image_and_left_side_4_box.xml',
        'views/snippets/right_text_image.xml',
        'views/snippets/team_member.xml',
        'views/snippets/testimonial.xml',
       
        'views/snippets/main_silder.xml',
        #Buttons
        'views/snippets/animated_btns/btn_hover_1.xml',
        'views/snippets/animated_btns/btn_hover_2.xml',
        'views/snippets/animated_btns/btn_hover_3.xml',
        'views/snippets/animated_btns/btn_hover_4.xml',
        'views/snippets/animated_btns/btn_hover_5.xml',
        'views/snippets/animated_btns/btn_hover_6.xml',
        'views/snippets/animated_btns/btn_hover_7.xml',
        'views/snippets/animated_btns/btn_hover_8.xml',
        'views/snippets/animated_btns/btn_hover_9.xml',
        'views/snippets/animated_btns/btn_hover_10.xml',
        'views/snippets/animated_btns/btn_hover_11.xml',
        'views/snippets/animated_btns/btn_hover_12.xml',
        'views/snippets/animated_btns/btn_hover_13.xml',
        'views/snippets/animated_btns/btn_hover_14.xml',
        'views/snippets/animated_btns/btn_hover_15.xml',
        'views/snippets/animated_btns/btn_hover_16.xml',
        #fancy boxes
        'views/snippets/fancy_box/fancy_box_1.xml',
        'views/snippets/fancy_box/fancy_box_3.xml',
        'views/snippets/fancy_box/fancy_box_4.xml',
        'views/snippets/fancy_box/fancy_box_5.xml',
        'views/snippets/fancy_box/fancy_box_6.xml',
        'views/snippets/fancy_box/fancy_box_7.xml',
        #titles
        'views/snippets/tittle_snippet/left_2_border_tittle_1.xml',
        'views/snippets/tittle_snippet/tittle_2.xml',
        'views/snippets/tittle_snippet/tittle_3.xml',
        'views/snippets/tittle_snippet/tittle_4.xml',
        'views/snippets/tittle_snippet/tittle_5.xml',
        'views/snippets/tittle_snippet/tittle_6.xml',
        
        'views/snippets/big_hero_banner/hero_banner_1.xml',
        'views/snippets/big_hero_banner/hero_banner_2.xml',
        'views/snippets/big_hero_banner/hero_banner_3.xml',
        # banners
        'views/snippets/banner/banner2.xml',
        'views/snippets/banner/banner3.xml',
        'views/snippets/banner/banner4.xml',
        'views/snippets/banner/banner5.xml',
        'views/snippets/banner/banner6.xml',
        'views/snippets/banner/banner7.xml',
        'views/snippets/banner/banner8.xml',

        # footer
        'views/footer/footer_1.xml',
        'views/footer/footer_2.xml',
        'views/footer/footer_3.xml',
        'views/footer/footer_4.xml',
        'views/footer/footer_5.xml',
        'views/footer/footer_6.xml',
        'views/footer/footer_7.xml',
        'views/footer/footer_8.xml',
    ],
    'assets': {
        'web.assets_frontend': [
            "/geminate_ecommerce_theme/static/src/css/style.scss",
            "/geminate_ecommerce_theme/static/src/css/style.css",
            "/geminate_ecommerce_theme/static/src/css/header.css",
            "/geminate_ecommerce_theme/static/src/css/header/header2.css",    
            "/geminate_ecommerce_theme/static/src/css/header/header3.css",    
            "/geminate_ecommerce_theme/static/src/css/header/header4.css",    
            "/geminate_ecommerce_theme/static/src/css/header/header5.css",    
            "/geminate_ecommerce_theme/static/src/css/header/header6.css",    
            "/geminate_ecommerce_theme/static/src/css/footer.css",
            "/geminate_ecommerce_theme/static/src/css/home.css",
            "/geminate_ecommerce_theme/static/src/css/about_us.css",
            "/geminate_ecommerce_theme/static/src/css/address_contact.css",
            "/geminate_ecommerce_theme/static/src/css/popup_cart.css",
            "/geminate_ecommerce_theme/static/src/css/shop_inner_page.css",

            # banners
            "geminate_ecommerce_theme/static/src/css/banner/banner2.css",
            "geminate_ecommerce_theme/static/src/css/banner/banner3.css",
            "geminate_ecommerce_theme/static/src/css/banner/banner4.css",
            "geminate_ecommerce_theme/static/src/css/banner/banner5.css",
            "geminate_ecommerce_theme/static/src/css/banner/banner6.css",
            "geminate_ecommerce_theme/static/src/css/banner/banner7.css",
            "geminate_ecommerce_theme/static/src/css/banner/banner8.css",

            "/geminate_ecommerce_theme/static/src/css/snippets/index1.css",
            "/geminate_ecommerce_theme/static/src/css/snippets/all_css_tittle.css",    
            "/geminate_ecommerce_theme/static/src/css/snippets/all_css_hero_banner.css",    
            "/geminate_ecommerce_theme/static/src/css/snippets/all_css_fancy_box.css",    
            "/geminate_ecommerce_theme/static/src/css/snippets/all_css_btn.css",    
            "/geminate_ecommerce_theme/static/src/css/snippets/header_silder_1.css",  
            "/geminate_ecommerce_theme/static/src/css/snippets/animation_aos.css",    
            "/geminate_ecommerce_theme/static/src/css/snippets/animate.min.css",
            "/geminate_ecommerce_theme/static/src/js/ssnippets/ilder_header_2.js",    
            "/geminate_ecommerce_theme/static/src/css/snippets/header_silder_2.css",  
            "/geminate_ecommerce_theme/static/src/css/snippets/header_silder_4.css", 

            "/geminate_ecommerce_theme/static/src/css/snippets/about_us_block.css",
            "/geminate_ecommerce_theme/static/src/css/snippets/auto_count_block.css",
            "/geminate_ecommerce_theme/static/src/css/snippets/big_pic.css",
            "/geminate_ecommerce_theme/static/src/css/snippets/card_silder.css",
            "/geminate_ecommerce_theme/static/src/css/snippets/client_block.css",
            "/geminate_ecommerce_theme/static/src/css/snippets/image_block.css",
            "/geminate_ecommerce_theme/static/src/css/snippets/progressbar.css",
            "/geminate_ecommerce_theme/static/src/css/snippets/right_side_image-left_txt.css",
            "/geminate_ecommerce_theme/static/src/css/snippets/right_text_image.css",
            "/geminate_ecommerce_theme/static/src/css/snippets/sale_and_hot_deals.css",
            "/geminate_ecommerce_theme/static/src/css/snippets/services_1.css",
            "/geminate_ecommerce_theme/static/src/css/snippets/team_member.css",
            "/geminate_ecommerce_theme/static/src/css/snippets/testimonial.css",
            "/geminate_ecommerce_theme/static/src/css/snippets/unpkg_lib.css",

            '/geminate_ecommerce_theme/static/src/js/auto_count_block.js',
            '/geminate_ecommerce_theme/static/src/js/contact_location.js',
            '/geminate_ecommerce_theme/static/src/js/jquery.counterup.min.js',
            '/geminate_ecommerce_theme/static/src/js/jquery.waypoints.min.js',
            '/geminate_ecommerce_theme/static/src/js/progressbar.js',
            '/geminate_ecommerce_theme/static/src/js/progressbar_1.js',
            '/geminate_ecommerce_theme/static/src/js/slick.js',
            '/geminate_ecommerce_theme/static/src/js/unpkg_lib.js',
            '/geminate_ecommerce_theme/static/src/js/unpkg.js',
            '/geminate_ecommerce_theme/static/src/js/ityped.min.js',
            '/geminate_ecommerce_theme/static/src/js/ityped.js',

            '/geminate_ecommerce_theme/static/src/xml/review_static_view.xml',
            


            # footer
            "/geminate_ecommerce_theme/static/src/css/footer/footer_1.css",
            "/geminate_ecommerce_theme/static/src/css/footer/footer_2.css",
            "/geminate_ecommerce_theme/static/src/css/footer/footer_3.css",
            "/geminate_ecommerce_theme/static/src/css/footer/footer_4.css",
            "/geminate_ecommerce_theme/static/src/css/footer/footer_5.css",
            "/geminate_ecommerce_theme/static/src/css/footer/footer_6.css",
            "/geminate_ecommerce_theme/static/src/css/footer/footer_7.css",
            "/geminate_ecommerce_theme/static/src/css/footer/footer_8.css",

            "/geminate_ecommerce_theme/static/src/css/swiper-bundle.min.css",
            '/geminate_ecommerce_theme/static/src/js/swiper-bundle.min.js',
            '/geminate_ecommerce_theme/static/src/js/silder.js',

            "/geminate_ecommerce_theme/static/src/css/product_silder.css",
        ],
    },
    'images': [
        'static/description/banner.png',
    ],
    # 'installable': True,
    # 'application': False,
    # 'auto_install': False,
}
