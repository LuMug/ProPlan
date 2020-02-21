response.title = settings.title
response.subtitle = settings.subtitle
response.meta.author = '%(author)s <%(author_email)s>' % settings
response.meta.keywords = settings.keywords
response.meta.description = settings.description
response.menu = [
(T('Index'),URL('default','index')==URL(),URL('default','index'),[]),
(T('Utente'),URL('default','utente_manage')==URL(),URL('default','utente_manage'),[]),
(T('Permessi'),URL('default','permessi_manage')==URL(),URL('default','permessi_manage'),[]),
(T('Progetto'),URL('default','progetto_manage')==URL(),URL('default','progetto_manage'),[]),
(T('Attivita'),URL('default','attivita_manage')==URL(),URL('default','attivita_manage'),[]),
]