- quale model usare? Dove definire i database?
- web2py gestisce già login? -> validare domain
- file menu.py


- smart grid personalizzabile
SQLFORM.smartgrid(db.table, param1=...)
- return con dictionary
- 'nome':nome
- db.table.col
- SQLFORM:
- .factory(db.table)
- ".... ()".....
- dict con ":", "**d" è espansione di dictionary = tanti argomenti
- dict con chiavi, lista con indici
- dati.keys()/values()
- pass = niente, utile per scheletro

- leggere DOPO insert

- update: set mio o dati veri?
	- update_record (vero)/update(in memoria)
	- row.update_record() --> commit

- argomento a caso = non visibile

	(a):
		a = request.vars.a if 'a' (se esiste)

- ajax: funzionni senza refresh


app, controller, funzione, arogmenti (vars, args), sottomenu

amministrazione db ->
