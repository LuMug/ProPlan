# -*- coding: utf-8 -*-
# prova qualcosa come
def index():
    response.flash = T("Hello Everynyan")
    return dict(message=T('Welcome to nyan2nyan!'))

def nyan():
    response.flash = T("Nyan")
    return dict(hello=10, nyan=T('Welcome to nyan2nyan!'))
