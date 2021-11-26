from odoo import models, fields
    
    
class Author(models.Model):
	_name ='author'
	_description = 'Author'

	name = fields.Char()
	address = fields.Text()
	# book_id = fields.Many2one('books')

class BookCategory(models.Model):
	_name = 'books.category'
	_description = 'Book Category'

	name = fields.Char()

class BookDepartment(models.Model):
	_name = 'books.department'
	_description = 'Book Department'

	name = fields.Char()

class BookPublisher(models.Model):
	_name = 'books.publisher'
	_description = 'Book Publisher'

	name = fields.Char()

class EstatePropertyLibrary(models.Model):
     _name = 'books.library'
     _description = 'Library data'
     _sql_constraints = [('isbn_unique', 'unique(isbn)', 'Duplicate isbn not allowed')]


     name = fields.Char(string="Book Name", default="Book", required=True)
     price = fields.Float()
     # author_ids = fields.One2many('author', 'book_id')
     author_ids = fields.Many2many('author')
     isbn = fields.Integer()
     category_id = fields.Many2one('books.category')
     department_id = fields.Many2one('books.department')
     barcode = fields.Char()
     publisher_id = fields.Many2one('books.publisher')
     edition = fields.Char() # Many 2 one 
     date = fields.Date()

     

