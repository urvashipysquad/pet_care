#!/usr/bin/python
# -*- coding: utf-8 -*-

from odoo import api, fields, SUPERUSER_ID, http, models, _


class InstagramPost(models.Model):

    _name = 'instagram.post'
    _description = 'Instagram posts'
    _rec_name = 'name'

    insta_images = fields.Binary('Post Image')
    name = fields.Char('Username')
    description = fields.Text('Description')


class BgImageContent(models.Model):

    _name = 'image.content'
    _description = 'backgreound image and content'

    page_name = fields.Char('Page Name')
    bg_image = fields.Binary('background Image')
    head_text = fields.Char('Header Text')
    snippet_text1 = fields.Text('Description One')
    snippet_text2 = fields.Text('Description Two')
    button_text = fields.Char('Button Text')


class OurStories(models.Model):

    _name = 'pet.story'
    _description = 'Pet Care story'

    name = fields.Char('Name')
    title = fields.Char('Title')
    description = fields.Text('Description')
    description2 = fields.Text('Description')
    image = fields.Binary('Image')


class PetQuotes(models.Model):

    _name = 'pet.quotes'
    _description = 'Pet Care quotes'

    name = fields.Char('Name')
    quote = fields.Char('Quote')
    image = fields.Binary('Image')
    # bg_image = fields.Binary('Background Image')
    admin_name = fields.Char('Admin Name')
    admin_company_position = fields.Char('Admin Company Position')


class TransformStory(models.Model):

    _name = 'transform.story'
    _description = 'transformation story'

    name = fields.Char('Name')
    title1 = fields.Char('Main Title')
    title2 = fields.Char('Second Title')
    description1 = fields.Text('Description')
    description2 = fields.Text('Description')
    image = fields.Binary('Image')
    btn_text = fields.Char('Button Text')


class ReviewComment(models.Model):

    _name = 'review.comment'
    _description = 'Review Comment'

    name = fields.Char('Name')
    comment = fields.Text('Comment')


class ReviewUsers(models.Model):

    _name = 'review.users'
    _description = 'Review Users Comment'

    name = fields.Char('Name')
    image = fields.Binary('Image')
    stars = fields.Float('Review Rating', digits=(1, 5))
    comment = fields.Text('Comment')


class InstagramPost(models.Model):

    _name = 'articles.post'
    _description = 'articles posts'
    _rec_name = 'title'

    article_images = fields.Binary('Post Image')
    title = fields.Char('Username')
    description = fields.Text('Description')
