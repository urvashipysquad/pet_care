from odoo import fields,models,api,_


class PetCare(models.Model):
    _name = "pet.care"
    _description = "Pet Care"

    pet_type = fields.Selection([('dog', 'Dog'), ('cat', 'Cat')],
                                 help="Help to choose real products to pets")
    gender = fields.Selection([('dog_male', 'DogMale'), ('dog_female', 'DogFemale'), ('cat_male', 'CatMale'), ('cat_female', 'CatFemale')],
                                 help="choose right gender for dogs and cats t  o get good product")

    pet_name = fields.Char("Food Name", required=True)
    pet_mail = fields.Char("Email")
    breed = fields.Many2one('dog.breed')
    pet_size = fields.Selection([('small', 'Small'), ('medium', 'Medium'), ('large', 'Large')], 'Pet Size')
    pet_birthday = fields.Date(string="pet birthdate")
    pet_weight = fields.Integer(string="pet weight")
    pet_weight_condition = fields.Selection([('skinny', 'Skinny'), ('just_right', 'Just Right'), ('chubby', 'Chubby')], 'Pet Size')
    pet_activity_level = fields.Selection([('couch_potato', 'couch potato'), ('somewhat_active', 'somewhat active'), ('active', 'active'), ('very_active', 'very active'), ('energy ball', 'energy ball')])
    treats = fields.Selection([('no_treats', 'No treats'), ('some_treats', 'Some treats'), ('lots_of_treats', 'Lots of treats')])
    neutered = fields.Selection([('yes', 'Yes'), ('no', 'No')])


class Breed(models.Model):
    _name = "breed"
    _description = "Mixed Dogs Breed"


class DogBreed(Breed):
    _name = "dog.breed"
    _description = "Mixed Dogs Breed"

    name = fields.Char("Dog Breed")
    description = fields.Text("Information")


class CatBreed(Breed):
    _name = "cat.breed"
    _description = "Mixed Cats Breed"

    name = fields.Char("Cats Breed")
    description = fields.Text("Information")