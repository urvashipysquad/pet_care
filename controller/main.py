#!/usr/bin/python
# -*- coding: utf-8 -*-
from odoo import fields, models, api, _, http, SUPERUSER_ID
from odoo.addons.website_sale.controllers.main import WebsiteSale
from odoo.http import request
from odoo.exceptions import UserError
from werkzeug.exceptions import NotFound


class WebsiteSaleInherited(WebsiteSale):

    @http.route(['''/shop''', '''/shop/page/<int:page>''',
                '''/shop/category/<model("product.public.category"):category>'''
                ,
                '''/shop/category/<model("product.public.category"):category>/page/<int:page>'''
                ], type='http', auth='public', website=True)
    def shop(self,page=0,category=None,search='',ppg=False,**post):
        rtn = super(WebsiteSaleInherited, self).shop(page=0,
                category=None, search='', ppg=False, **post)
        return rtn

    @http.route(['/shop/cart'], type='http', auth='user', website=True,
                sitemap=False)
    def cart(self,access_token=None,revive='',**post):
        rtn = super(WebsiteSaleInherited, self).cart(access_token=None,
                revive='', **post)
        return rtn


class MainAction(http.Controller):

    @http.route('/', website=True, auth='public', type='http')
    def dog_home(self, **kw):
        dog_breed = request.env['dog.breed'].sudo().search([])

        # if product_name:
        #     domain += [('name', 'ilike', product_name)]

        products = request.env['product.template'].sudo().search([])
        instagram = request.env['instagram.post'].sudo().search([])
        img_content = request.env['image.content'].sudo().search([])
        review_comment = request.env['review.comment'].sudo().search([])
        return request.render('pet_care_website.home_page', {
            'dog_breed': dog_breed,
            'products': products,
            'instagram': instagram,
            'img_content': img_content,
            'review_comment': review_comment,
            })

    @http.route('/about', website=True, auth='public', type='http')
    def dog_about(self, **kw):
        img_content = request.env['image.content'].sudo().search([])
        story = request.env['pet.story'].sudo().search([])
        quotes = request.env['pet.quotes'].sudo().search([])
        return request.render('pet_care_website.about_page',
                              {'img_content': img_content,
                              'story': story, 'quotes': quotes})

    @http.route('/why_fresh', website=True, auth='public', type='http')
    def dog_why_fresh(self, **kw):
        img_content = request.env['image.content'].sudo().search([])
        story = request.env['pet.story'].sudo().search([])
        transformation_story = request.env['transform.story'
                ].sudo().search([])
        return request.render('pet_care_website.why_fresh_page',
                              {'img_content': img_content,
                              'story': story,
                              'transformation_story': transformation_story})

    @http.route('/faq', website=True, auth='public', type='http')
    def dog_faq(self, **kw):
        questions = request.env['faq.questions'].sudo().search([])

        return request.render('pet_care_website.faq_page',
                              {'questions': questions})

    @http.route('/reviews', website=True, auth='public', type='http')
    def dog_reviews(self, **kw):
        img_content = request.env['image.content'].sudo().search([])
        instagram = request.env['instagram.post'].sudo().search([])
        transformation_story = request.env['transform.story'
                ].sudo().search([])
        review_comment = request.env['review.comment'].sudo().search([])
        review_users = request.env['review.users'].sudo().search([])

        # review_users = request.env['review.users'].sudo.search([])

        return request.render('pet_care_website.reviews_page', {
            'img_content': img_content,
            'instagram': instagram,
            'transformation_story': transformation_story,
            'review_comment': review_comment,
            'review_users': review_users,
            })

    # @http.route('/food_define', website=True, auth="public", type='http')
    # def food_define(self, **kw):
    #     print(" ************************** food_define")
    #     return request.render('pet_care_website.food_define', {})

    @http.route('/create/pet', website=True, auth='public', type='http')
    def pet_info_create(self, **kw):
        request.env['pet.care'].sudo().create(kw)
        return request.render('pet_care_website.pet_thankyou_page', {})

    @http.route('/articles_page', website=True, auth='public',type='http')
    def articles_custom(self, **kw):
        articles = request.env['articles.post'].sudo().search([])
        img_content = request.env['image.content'].sudo().search([])
        return request.render('pet_care_website.articles_page',
                              {'articles': articles,
                              'img_content': img_content})


class website_add_product(http.Controller):

    @http.route(['/shop/cart/update/product'], type='http',
                auth='public', methods=['GET'], website=True)
    def cart_update_product(self,product_id,add_qty=1,set_qty=0,**kw):
        try:
            add_qty = float(add_qty)
        except ValueError:
            return None
        if add_qty <= 0.0:
            return None
        request.website.sale_get_order(force_create=1)._cart_update(product_id=int(product_id),
                add_qty=add_qty, set_qty=float(set_qty))
        if request.httprequest.headers \
            and request.httprequest.headers.get('Referer'):
            return request.redirect(str(request.httprequest.headers.get('Referer')))
        return request.redirect('''/shop''')


# class PetInfo(http.Controller):
#     @http.route('/pet_webform', website=True, auth="public", type='http')
#     def pet_webform(self, **kw):
#         dog_breed = request.env['dog.breed'].sudo().search([])
#         # pet_weight = request.env['pet.weight'].sudo().search([])
#         print('>>>>>>>>>>>>>>>>> breed', dog_breed)
#         return request.render('pet_care_website.pet_webform', {'dog_breed': dog_breed})
