from odoo import fields,models,api,_,http
from odoo.addons.website_sale.controllers.main import WebsiteSale
from odoo.http import request
from odoo.exceptions import UserError
from werkzeug.exceptions import NotFound


class WebsiteSaleInherited(WebsiteSale):

    @http.route([
        '''/shop''',
        '''/shop/page/<int:page>''',
        '''/shop/category/<model("product.public.category"):category>''',
        '''/shop/category/<model("product.public.category"):category>/page/<int:page>'''
    ], type='http', auth="user", website=True)
    def shop(self, page=0, category=None, search='', ppg=False, **post):
        print('>>>>>>>>>>>>>>>>>>>>> working  controllser')
        rtn = super(WebsiteSaleInherited, self).shop(page=0, category=None, search='', ppg=False, **post)
        return rtn


class MainAction(http.Controller):

    @http.route('/', website=True, auth="public", type='http')
    def dog_home(self, **kw):
        print(" ************************** main")
        return request.render('pet_care_website.home_page', {})

    @http.route('/about', website=True, auth="public", type='http')
    def dog_about(self, **kw):
        print(" ************************** ")
        return request.render('pet_care_website.about_page', {})

    @http.route('/why_fresh', website=True, auth="public", type='http')
    def dog_why_fresh(self, **kw):
        print(" ************************** why_fresh")
        return request.render('pet_care_website.why_fresh_page', {})

    @http.route('/faq', website=True, auth="public", type='http')
    def dog_faq(self, **kw):
        print(" ************************** faq")
        return request.render('pet_care_website.faq_page', {})

    @http.route('/reviews', website=True, auth="public", type='http')
    def dog_reviews(self, **kw):
        print(" ************************** reviews_page")
        return request.render('pet_care_website.reviews_page', {})


class PetInfo(http.Controller):
    @http.route('/pet_webform_work', website=True, auth="public", type='http')
    def pet_webform(self, **kw):
        dog_breed = request.env['dog.breed'].sudo().search([])
        # pet_weight = request.env['pet.weight'].sudo().search([])
        print('>>>>>>>>>>>>>>>>> breed', dog_breed)

        return request.render('pet_care_website.pet_webform_work', {'dog_breed': dog_breed})

    @http.route('/pet_care_form', website=True, auth='public', type='http')
    def pet_care_form(self,*kw):
        return request.render('pet_care_website.pet_care_form',{})

    @http.route('/create/pet', website=True, auth="public", type='http')
    def pet_info_create(self, **kw):
        print('>>>>>>>>>>>>>>>>>>>>>> pet_thankyou_page ', kw)
        request.env['pet.care'].sudo().create(kw)
        return request.render('pet_care_website.pet_thankyou_page', {})