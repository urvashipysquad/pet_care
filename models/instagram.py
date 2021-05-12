# -*- coding: utf-8 -*-

from odoo import api, fields, SUPERUSER_ID, http, models, _


class InstagramPost(models.Model):
    _name = "instagram.post"
    _description = "Instagram posts"
    _rec_name = 'name'

    insta_images = fields.Binary("Post Image")
    name = fields.Char('Username')
    description = fields.Text("Description")


class BgImageContent(models.Model):
    _name = "image.content"
    _description = "backgreound image and content"

    page_name = fields.Char("Page Name")
    bg_image = fields.Binary("background Image")
    head_text = fields.Char("Header Text")
    snippet_text1 = fields.Text("Description One")
    snippet_text2 = fields.Text("Description Two")
    button_text = fields.Char("Button Text")
