import datetime

mydb = DAL('sqlite://mydb.sqlite')

mydb.define_table('projects',
    Field('name', 'string'),
    Field('start_date', 'datetime', default = datetime.datetime.now()),
    Field('end_date', 'datetime', writable=False),
    Field('description', 'string', comment='dkljfdskjfdls')
)