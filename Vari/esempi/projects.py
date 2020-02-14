def index():
    g = SQLFORM.smartgrid(mydb.projects, 
    user_signature=False,
    fields = [mydb.projects.name]
    )

    return {'grid':g}

def manuale():
    dato = ['a', 'b']


    log = []
    mydb.projects.end_date.writable=True    #override della definizione nel model
    f = SQLFORM.factory(mydb.projects)

    if f.process().accepted:
        response.flash = 'input rilevato'
        log.append('request.vars {}'.format( request.vars) )
        log.append('f.vars {}'.format(f.vars))

        nome = f.vars.name
        desc = f.vars.description

        dati = {'nome':'coso'}
        dati['name'] = nome
        dati['description'] = desc


        log.append('nome {nome}, desc {desc}'.format(desc=desc, nome=nome))
        log.append('nome {name}, desc {description}'.format( **dati ))

        keys = sorted( dati.keys() )
        for k in keys:
            pass
        for k in dati.keys():
            v = dati[k]
            pass
        for v in dati.values():
            pass
        for k, v in dati.items():
            pass

        mydb.projects.insert(name = nome, description = desc)
        mydb.projects.insert( **dati )

    elif f.errors:
        response.flash = 'errori'


    rows = mydb(mydb.projects.id > 0).select(mydb.projects.name, mydb.projects.description)

    names = []
    if rows:
        for row in rows:
            nome = row.name.upper()
            names.append(nome)
    
    return {'dsfds':dato, 'rows':rows, 'names':names, 'f':f, 'log':log}

def not_visible_from_url(a):
    pass

def it_is_visible_from_url():
    a = request.vars.a if 'a' in request.vars else None # /app/projects/it_is_visible_from_url?a=213423
    b = request.args[0] if len(request.args) > 0 else None # /app/projects/it_is_visible_from_url?213423
    pass