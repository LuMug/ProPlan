### we prepend t_ to tablenames and f_ to fieldnames for disambiguity


########################################
db.define_table('t_progetto',
    Field('f_nome', type='string',
          label=T('Nome')),
    Field('f_descrizione', type='text',
          label=T('Descrizione')),
    Field('f_data_inizio', type='date',
          label=T('Data Inizio')),
    Field('f_data_fine', type='date',
          label=T('Data Fine')),
    format='%(f_nome)s',
    migrate=settings.migrate)

db.define_table('t_progetto_archive',db.t_progetto,Field('current_record','reference t_progetto',readable=False,writable=False))

########################################
db.define_table('t_utente',
    Field('f_username', type='string',
          label=T('Username')),
    Field('f_email', type='string',
          label=T('Email')),
    Field('f_password', type='password',
          label=T('Password')),
    format='%(f_username)s',
    migrate=settings.migrate)

db.define_table('t_utente_archive',db.t_utente,Field('current_record','reference t_utente',readable=False,writable=False))

########################################
db.define_table('t_attivita',
    Field('f_id_progetto', type='string',
          label=T('Id Progetto')),
    Field('f_id_utente', type='string',
          label=T('Id Utente')),
    Field('f_descrizione', type='string',
          label=T('Descrizione')),
    Field('f_data_inizio', type='string',
          label=T('Data Inizio')),
    Field('f_data_fine', type='string',
          label=T('Data Fine')),
    format='%(f_id_progetto)s',
    migrate=settings.migrate)

db.define_table('t_attivita_archive',db.t_attivita,Field('current_record','reference t_attivita',readable=False,writable=False))

########################################
db.define_table('t_permessi',
    Field('f_id_utente', type='string',
          label=T('Id Utente')),
    Field('f_id_progetto', type='string',
          label=T('Id Progetto')),
    Field('f_permesso', type='string',
          label=T('Permesso')),
    format='%(f_id_utente)s',
    migrate=settings.migrate)

db.define_table('t_permessi_archive',db.t_permessi,Field('current_record','reference t_permessi',readable=False,writable=False))
