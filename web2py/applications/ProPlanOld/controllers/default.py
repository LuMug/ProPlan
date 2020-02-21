# -*- coding: utf-8 -*-
### required - do no delete
import sqlite3

def user(): return dict(form=auth())
def download(): return response.download(request,db)
def call(): return service()
### end requires
def index():
    return dict()

def create_connection():
	conn = None
	try:
		conn = sqlite3.connect(test.db)
	except Error as e:
		print(e)
	return conn

def utente_manage():

    form = SQLFORM.factory(
        Field('username', requires=IS_NOT_EMPTY),
        Field('email', requires=IS_NOT_EMPTY),
        Field('password', 'password', requires=IS_NOT_EMPTY)
    )
    return dict(form=form)

def view_utenti():
	with open(file) as readfile:
		inventory = json.load(readfile)
	return dict(inventory=inventory)

def permessi_manage():
    form = SQLFORM.smartgrid(db.t_permessi,onupdate=auth.archive)
    return locals()

def progetto_manage():
    form = SQLFORM.smartgrid(db.t_progetto,onupdate=auth.archive)
    return locals()

def attivita_manage():
    form = SQLFORM.smartgrid(db.t_attivita,onupdate=auth.archive)
    return locals()
