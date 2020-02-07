1. [Introduzione](#introduzione)

  - [Informazioni sul progetto](#informazioni-sul-progetto)

  - [Abstract](#abstract)

  - [Scopo](#scopo)

1. [Analisi](#analisi)

  - [Analisi del dominio](#analisi-del-dominio)
  
  - [Analisi dei mezzi](#analisi-dei-mezzi)

  - [Analisi e specifica dei requisiti](#analisi-e-specifica-dei-requisiti)

  - [Use case](#use-case)

  - [Pianificazione](#pianificazione)

1. [Progettazione](#progettazione)

  - [Design dell’architettura del sistema](#design-dell’architettura-del-sistema)

  - [Design dei dati e database](#design-dei-dati-e-database)

1. [Implementazione](#implementazione)

1. [Test](#test)

  - [Protocollo di test](#protocollo-di-test)

  - [Risultati test](#risultati-test)

  - [Mancanze/limitazioni conosciute](#mancanze/limitazioni-conosciute)

1. [Consuntivo](#consuntivo)

1. [Conclusioni](#conclusioni)

  - [Sviluppi futuri](#sviluppi-futuri)

  - [Considerazioni personali](#considerazioni-personali)

1. [Sitografia](#sitografia)

1. [Allegati](#allegati)


## Introduzione

### Informazioni sul progetto

  #### Il nome del progetto è ProPlan, è fatto come progetto si 2° semestre presso l'arti e mestieri di Trevano.

    Allievi: Kushtrim Rushi, Filippo Zinetti, Jure Grgic, Jonathan Mueller

	Docente responsabile al controllo del lavoro: Luca Muggiasca

	Data inizio del progetto: 17 Gennaio 2020

	Data fine del progetto: 15 Maggio 2020

	Luogo di lavoro: Scuola arti e mestieri di Trevano

	Sezione scolastica: 3° anno d'informatica

	Materia dove viene svolto il lavoro: modulo 306

### Abstract

  Oggi giorno ci sono migliaia di progetti che vengono creati.
  
  Al termine di ogni progetto oppure quando si hanno più progetti 
  su cui lavorare, non si sa dove metterli e magari vengono messi in un 
  disco, che in seguito verranno lasciati nel dimenticatoio. 
  
  Per questo motivo, abbiamo creato ProPlan, un sito web che 
  permette di creare progetti e di poterli gestire in seguito. 
  
  Tutti i vostri progetti possono essere racchiusi in un unico posto. 
  Esistono svariati siti web simili a questo, che permettono la gestione 
  dei progetti, però il sito web che il nostro team di sviluppo ha creato, 
  è più pratico e semplice da capire.


### Scopo

Il progetto ci è stato assegnato dalla scuola, il che lo rende un progetto didattico.

ProPlan ha lo scopo di gestire i progetti.

Non vi è nessuna restrizione sul tipo di progetto che si può creare. 

Alla creazione di un progetto si possono creare le attività del progetto e si possono definire i permessi di altri utenti, nominando magari un cocapo progetto oppure un semplice membro del progetto.

Si possono creare anche delle bozze di progetti, ovvero non dei veri e propri progetti, ma delle idee per il progetto vero e proprio.

## Analisi

### Analisi del dominio

	- Inizialmente si presentaerà una schermata di autenticazione utente
	- ProPlan verrà usufruito nell'ambiente scolastico (SAMT), andando a sostituire altri programmi (es: trello)
	- Il ruolo di utente, verrà assegnato agli allievi e docenti della SAMT (scuola arti e mestieri di Trevano)
	- Gli utenti hanno bisogno di gestire i loro progetti
	- Chi utilizzerà codesto applicativo, dovrà saper utilizzare un computer
	- Dovrà essere a conoscenza delle basi di gestione dei progetti
	- Non sono presenti convenzioni o standard nel dominio

### Analisi e specifica dei requisiti

  |**ID**            |Req-1                                                                          |
  |------------------|-------------------------------------------------------------------------------|
  |**Nome**          | Deve essere presente un admin globale                                         |
  |**Priorità**      |                                                                               |
  |**Versione**      |                                                                               |
  |**Note**          |                                                                               |

  req-1: Deve essere presente un admin globale
  req-2: L'admin globale deve aver il controllo assoluto del sito web
  req-3: Ci possono essere degli ospiti per un progetto
  req-4: Gli ospiti hanno un permesso di sola lettura in un determinato progetto
  req-5: Ogni progetto avrà un capoprogetto
  req-6: È possibile nominare un cocapo del progetto
  req-7: Possono essere nominati dei membri del progetto
  req-8: Ogni membro ha la possibilità di lavorare sul progetto, con qualche piccola restrizione.
  req-9: Si deve avere la possibilità di poter creare un bozza di progetto. (Nota: non è un progetto effettivo, ma sarà solo una prova dove poter scrivere le idee iniziali di un progetto)
  req-10: Il sito web deve essere realizzato con HTML, CSS, JS e Python
  req-11: Dovranno essere specificati dei dettagli del progetto, ovvero, nome del progetto, attività,
  lista dei membri, l'inizio e la fine del progetto, descrizione del progetto.
  req-12: È necessario che vengano specificati nome, descrizione e durata di un attività
  req-

  |**ID**|**Nome**        |**Priorità**|**Vers**|**Note**|
  |------|----------------|------------|--------|--------|
  |Req-01|Il programma è fatto come applicativo o sito web|1|1.0|...|
  |Req-02|Gerarchia dell'applicazione (admin, utente)|1|1.0|...|
  |Req-03|Ci devono essere più tipi di utente (capoprogetto, ospite, …)|1|1.0|...|
  |Req-04|Un progetto può essre una bozza o un progetto finale|1|1.0|...|
  |Req-05|Dettagli progetti (nome, descrizione, lista membri, inizio e fine)|1|1.0|...|
  |Req-06|Dettagi attività (nome, descrizione, durata)|1|1.0|...|
  |Req-07|Stati attività (idea, da fare, in esecuzione, terminato, testato, approvato)|1|1.0|...|
  |Req-08|Sezione bug|2|1.0|...|
  |Req-09|Sezione amministratori|1|1.0|...|
  |Req-10|Interfaccia di login|1|1.0|...|
  |Req-11|Colori adatti anche per i daltonici|2|1.0|...|
  |Req-12|Controllo indirizzo email|1|1.0|consentito solo per @samtrevano.ch — @edu.ti.ch|
  |Req-13|Database per il salvataggio dei progetti|1|1.0|...|
  |Req-14|Il database permette di riaprire i vecchi progetti|1|1.0|...|
  |Req-15|Creazione sito web con tutorial programma|2|1.0|...|
  |Req-16|Download dell'applicativo tramite sito web|2|1.0|...|


**Spiegazione elementi tabella dei requisiti:**

**ID**: identificativo univoco del requisito

**Nome**: breve descrizione del requisito

**Priorità**: indica l’importanza di un requisito nell’insieme del
progetto, definita assieme al committente. Ad esempio poter disporre di
report con colonne di colori diversi ha priorità minore rispetto al
fatto di avere un database con gli elementi al suo interno. Solitamente
si definiscono al massimo di 2-3 livelli di priorità.

**Versione**: indica la versione del requisito. Ogni modifica del
requisito avrà una versione aggiornata.

Sulla documentazione apparirà solamente l’ultima versione, mentre le
vecchie dovranno essere inserite nei diari.

**Note**: eventuali osservazioni importanti o riferimenti ad altri
requisiti.


### Use case


### Pianificazione

Gantt preventivo:

![Gant preventivo](../Pianificazione/ProPlan_GanttPreventivo.PNG)

### Analisi dei mezzi

Elencare e *descrivere* i mezzi disponibili per la realizzazione del
progetto. Ricordarsi di sempre descrivere nel dettaglio le versioni e il
modello di riferimento.

SDK, librerie, tools utilizzati per la realizzazione del progetto e
eventuali dipendenze.

Su quale piattaforma dovrà essere eseguito il prodotto? Che hardware
particolare è coinvolto nel progetto? Che particolarità e limitazioni
presenta? Che hw sarà disponibile durante lo sviluppo?

## Progettazione

Questo capitolo descrive esaustivamente come deve essere realizzato il
prodotto fin nei suoi dettagli. Una buona progettazione permette
all’esecutore di evitare fraintendimenti e imprecisioni
nell’implementazione del prodotto.

### Design dell’architettura del sistema

Descrive:

-   La struttura del programma/sistema lo schema di rete...

-   Gli oggetti/moduli/componenti che lo compongono.

-   I flussi di informazione in ingresso ed in uscita e le
    relative elaborazioni. Può utilizzare *diagrammi di flusso dei
    dati* (DFD).

-   Eventuale sitemap

### Design dei dati e database

Descrizione delle strutture di dati utilizzate dal programma in base
agli attributi e le relazioni degli oggetti in uso.

### Schema E-R, schema logico e descrizione.

Se il diagramma E-R viene modificato, sulla doc dovrà apparire l’ultima
versione, mentre le vecchie saranno sui diari.

### Design delle interfacce

Descrizione delle interfacce interne ed esterne del sistema e
dell’interfaccia utente. La progettazione delle interfacce è basata
sulle informazioni ricavate durante la fase di analisi e realizzata
tramite mockups.

### Design procedurale

Descrive i concetti dettagliati dell’architettura/sviluppo utilizzando
ad esempio:

-   Diagrammi di flusso e Nassi.

-   Tabelle.

-   Classi e metodi.

-   Tabelle di routing

-   Diritti di accesso a condivisioni …

Questi documenti permetteranno di rappresentare i dettagli procedurali
per la realizzazione del prodotto.

## Implementazione

In questo capitolo dovrà essere mostrato come è stato realizzato il
lavoro. Questa parte può differenziarsi dalla progettazione in quanto il
risultato ottenuto non per forza può essere come era stato progettato.

Sulla base di queste informazioni il lavoro svolto dovrà essere
riproducibile.

In questa parte è richiesto l’inserimento di codice sorgente/print
screen di maschere solamente per quei passaggi particolarmente
significativi e/o critici.

Inoltre dovranno essere descritte eventuali varianti di soluzione o
scelte di prodotti con motivazione delle scelte.

Non deve apparire nessuna forma di guida d’uso di librerie o di
componenti utilizzati. Eventualmente questa va allegata.

Per eventuali dettagli si possono inserire riferimenti ai diari.

## Test

### Protocollo di test

Definire in modo accurato tutti i test che devono essere realizzati per
garantire l’adempimento delle richieste formulate nei requisiti. I test
fungono da garanzia di qualità del prodotto. Ogni test deve essere
ripetibile alle stesse condizioni.


|Test Case      | TC-001                               |
|---------------|--------------------------------------|
|**Nome**       |Import a card, but not shown with the GUI |
|**Riferimento**|REQ-012                               |
|**Descrizione**|Import a card with KIC, KID and KIK keys with no obfuscation, but not shown with the GUI |
|**Prerequisiti**|Store on local PC: Profile\_1.2.001.xml (appendix n\_n) and Cards\_1.2.001.txt (appendix n\_n) |
|**Procedura**     | - Go to “Cards manager” menu, in main page click “Import Profiles” link, Select the “1.2.001.xml” file, Import the Profile - Go to “Cards manager” menu, in main page click “Import Cards” link, Select the “1.2.001.txt” file, Delete the cards, Select the “1.2.001.txt” file, Import the cards |
|**Risultati attesi** |Keys visible in the DB (OtaCardKey) but not visible in the GUI (Card details) |


### Risultati test

Tabella riassuntiva in cui si inseriscono i test riusciti e non del
prodotto finale. Se un test non riesce e viene corretto l’errore, questo
dovrà risultare nel documento finale come riuscito (la procedura della
correzione apparirà nel diario), altrimenti dovrà essere descritto
l’errore con eventuali ipotesi di correzione.

### Mancanze/limitazioni conosciute

Descrizione con motivazione di eventuali elementi mancanti o non
completamente implementati, al di fuori dei test case. Non devono essere
riportati gli errori e i problemi riscontrati e poi risolti durante il
progetto.

## Consuntivo

Gantt consuntivo:

![Gantt consuntivo](./img/ganttconsuntivo.png)

## Conclusioni

Quali sono le implicazioni della mia soluzione? Che impatto avrà?
Cambierà il mondo? È un successo importante? È solo un’aggiunta
marginale o è semplicemente servita per scoprire che questo percorso è
stato una perdita di tempo? I risultati ottenuti sono generali,
facilmente generalizzabili o sono specifici di un caso particolare? ecc

### Sviluppi futuri
  Migliorie o estensioni che possono essere sviluppate sul prodotto.

### Considerazioni personali
  Cosa ho imparato in questo progetto? ecc

## Bibliografia

### Bibliografia per articoli di riviste
1.  Cognome e nome (o iniziali) dell’autore o degli autori, o nome
    dell’organizzazione,

2.  Titolo dell’articolo (tra virgolette),

3.  Titolo della rivista (in italico),

4.  Anno e numero

5.  Pagina iniziale dell’articolo,

### Bibliografia per libri


1.  Cognome e nome (o iniziali) dell’autore o degli autori, o nome
    dell’organizzazione,

2.  Titolo del libro (in italico),

3.  ev. Numero di edizione,

4.  Nome dell’editore,

5.  Anno di pubblicazione,

6.  ISBN.

### Sitografia

1.  URL del sito (se troppo lungo solo dominio, evt completo nel
    diario),

2.  Eventuale titolo della pagina (in italico),

3.  Data di consultazione (GG-MM-AAAA).

**Esempio:**

-   http://standards.ieee.org/guides/style/section7.html, *IEEE
    Standards Style Manual*, 07-06-2008.

## Allegati

Elenco degli allegati, esempio:

-   Diari di lavoro

-   Codici sorgente/documentazione macchine virtuali

-   Istruzioni di installazione del prodotto (con credenziali
    di accesso) e/o di eventuali prodotti terzi

-   Documentazione di prodotti di terzi

-   Eventuali guide utente / Manuali di utilizzo

-   Mandato e/o Qdc

-   Prodotto

-   …
