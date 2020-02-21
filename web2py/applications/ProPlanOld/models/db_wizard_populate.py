from gluon.contrib.populate import populate
if db(db.auth_user).isempty():
     populate(db.t_progetto,10)
     populate(db.t_utente,10)
     populate(db.t_attivita,10)
     populate(db.t_permessi,10)
