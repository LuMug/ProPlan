## Web o no?
- Sì perchè è più fedele alla consegna: metti URL e funziona subito
- No perchè è più comodo?, funziona comunque anche da applicativo...

###### TODO: scegliere "modo" per progetto

99% python, SQL,...

## Requisiti
#### Gerarchia a livello di applicazione:
- Admin globale (controllo completo su tutto)
- Utente (accesso, creazione, modifica, eliminazione diversi per ogni progetto)
- ~ Guest?

#### Gerarchia a livello di progetto:
- ospite (lettura del progetto, guardarlo, = accesso speciale a persona eserna)
- capoprogetto (controllo completo sul progetto)
- sotto capo
- membro (modifica limitata su qualche funzione, da definire)
- ~ mandante? (lettura, lasciare note [e notifiche?] -> FIGURA DI RIFERIMENTO PER PROGETTO) DA DEFINIRE

#### Divisione progetti
- Bozza (non necessita gerarchia di persone)
    --> (che si trasforma eventualmente in)
- Finale (ha team di lavoro variabile)

#### Dettagli progetto
- Nome
- Descrizione
- Lista membri con divisioni (VARIABILE)
- Data inizio
- Data fine
###### Dettagli attività
- Nome
- Descrizione
- Durata
- Stati:
    - idea
    - da fare
    - in esecuzione
    - terminato
    - testato approvato
#### Sezioni aggiuntive
- sezione bug (permettere di segnalare un bug)
- sezione amministrativa (permette di gestire utenti, password e progetti esistenti)
#### Interfaccia login
- Colori anche per i daltonici
- registrazione permessa solo a utenti con indirizzo scolastico (@samtrevano.ch e @edu.ti.ch)
- controllo credenziali
#### Database
- database dove salvare tutti i progetti
- alla conclusione di un progetto, le attività non devono essere rimosse (deve essere poissibile riutilizzare le vecchie attività)
