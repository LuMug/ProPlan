# ProPlan | Diario di lavoro
##### Kushtrim Rushi & Jure Grgic & Jonathan Mueller & Filippo Zinetti
### Trevano, 2020-03-27

## Lavori svolti

| Orario        | Lavoro svolto |
|---------------|---------------|
| 08:20 - 11:35 | Fatto il pop-up per creare un nuovo progetto |
| 10:05 - 11:30 | Migliorati i routing |
| 13:15 - 14:15 | Fatto il pop-up per modificare le informazioni principali di un progetto |
| 08:20 - 16:30 | Lavorato sul sign-in e sign-up |
| 10:05 - 11:35 | Fatto in modo che un utente che non è loggato non possa accedere ad altre pagine se non il log-in, in caso l'utente cerca di accedere ad una pagina che non è il log-in viene indirizzato ad esso |
| 15:30 - 16:00 | Completato il diario |


##  Problemi riscontrati e soluzioni adottate

Il redirezionamento veniva fatto sul percorso sbagliato perché non utilizzavamo il percorso di default ma ne abbiamo creato uno nostro, e per risolverlo abbiamo messo un redirezionamento nel percorso di default che reindirizzava nel percorso desiderato.

Un altro problema era dove gestire il controllo delle mail (il file), per risolvere il problema abbiamo dovuto spostare il metodo da user.py (controllers) a db.py (models), così che comunica direttamente con il database.

Gli strumenti offerti da web2py, seppur comodi, spesso richiedono molto studio, prove ed errori per essere compresi (per esempio SQLFORM.smartgrid, SQLFORM.factory, \@auth.requires_login())


##  Punto della situazione rispetto alla pianificazione

Siamo un po' indietro; abbiamo pochi risultati pratici.

## Programma di massima per la prossima giornata di lavoro

Sistemare il log-in e il sign-up, poi iniziare le pagine della creazione di progetti. In generale, ottenere risultati pratici
