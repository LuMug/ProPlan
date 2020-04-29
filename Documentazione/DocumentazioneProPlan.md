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
**Nome: ProPlan**
- Allievi: Kushtrim Rushi, Filippo Zinetti, Jure Grgic, Jonathan Müller
- Docente responsabile al controllo del lavoro: Luca Muggiasca
- Data inizio del progetto: 17 Gennaio 2020
- Data fine del progetto: 15 Maggio 2020
- Luogo di lavoro: Scuola arti e mestieri di Trevano, Canobbio
- Sezione scolastica: 3° anno d'informatica
- Materia: modulo 306 (Realizzare un progetto IT)

### Abstract
Migliaia sono i progetti che ogni giorno vengono avviati. Hanno diverse dimensioni, diversi scopi e finscono in diversi modi, ma quello che hanno in comune è una delle fasi cruciali, che deve essere svolta all'inizio indipendentemente da tutto: la progettazione.
Questa comprende una scomposizione del lavoro in fasi più piccole e più gestibili da singole persone o team, che devono poi collaborare al meglio per raggiungere un obbiettivo comune. Questo non dovrebbe essere un problema, poichè esistono molte soluzioni per gestire team di persone... quello che manca a questi è **semplicità** e **immediatezza** nel loro utilizzo.
È per questo che abbiamo sviluppato ProPlan, uno strumento che permette di creare e gestire piccoli progetti in modo immediato e senza quindi perdersi in impostazioni e funzionalità superflue.
La piattaforma è sviluppata in python, linguaggio sempre più popolare grazie alla sua semplicità, che rispecchia quindi perfettamente gli ideali del progetto.

<!--
E’ una breve e accurata rappresentazione dei contenuti di un documento,
senza notazioni critiche o valutazioni. Lo scopo di un abstract efficace
dovrebbe essere quello di far conoscere all’utente il contenuto di base
di un documento e metterlo nella condizione di decidere se risponde ai
suoi interessi e se è opportuno il ricorso al documento originale.

Può contenere alcuni o tutti gli elementi seguenti:

-   **Background/Situazione iniziale**

-   **Descrizione del problema e motivazione**: Che problema ho cercato
    di risolvere? Questa sezione dovrebbe includere l'importanza del
    vostro lavoro, la difficoltà dell'area e l'effetto che potrebbe
    avere se portato a termine con successo.

-   **Approccio/Metodi**: Come ho ottenuto dei progressi? Come ho
    risolto il problema (tecniche…)? Quale è stata l’entità del mio
    lavoro? Che fattori importanti controllo, ignoro o misuro?

-   **Risultati**: Quale è la risposta? Quali sono i risultati? Quanto è
    più veloce, più sicuro, più economico o in qualche altro aspetto
    migliore di altri prodotti/soluzioni?

Esempio di abstract:

> *As the size and complexity of today’s most modern computer chips
> increase, new techniques must be developed to effectively design and
> create Very Large Scale Integration chips quickly. For this project, a
> new type of hardware compiler is created. This hardware compiler will
> read a C++ program, and physically design a suitable microprocessor
> intended for running that specific program. With this new and powerful
> compiler, it is possible to design anything from a small adder, to a
> microprocessor with millions of transistors. Designing new computer
> chips, such as the Pentium 4, can require dozens of engineers and
> months of time. With the help of this compiler, a single person could
> design such a large-scale microprocessor in just weeks.*
-->

### Scopo
Il progetto ci è stato assegnato dalla scuola ed è quindi un progetto didattico, ma potrà poi risultare utile anche a coloro che necessiteranno di gestire un progetto di gruppo nei prossimi anni.
L'obbettivo è quello di creare uno strumento simile ad alcuni già esistenti, ma con funzionalità meno dispersive in modo da risultare più semplice per gli utilizzatori. Le soluzioni attuali presentano infatti diversi elementi superflui per il target di ProPlan, di cui anche gli sviluppatori hanno fanno parte, ed è quindi sull'analisi dei bisogni e degli elementi di disturbo che la piattaforma è sviluppata.
L'applicativo sarà reso disponibile tramite pagina web, quindi raggiungibile da ovunque tramite l'apposito dominio.

<!--
Lo scopo del progetto (scopi didattici/scopi operativi). Dovrebbe
descrivere il mandato, ma non vanno ricopiate le informazioni del
quaderno dei compiti (che va invece allegato).
-->
## Analisi
### Analisi del dominio
ProPlan è progettato per l'uso nell'ambiente scolastico della SAMT, andando a sostituire altri programmi (es: trello, eventualmente Microsoft Project e Project Libre). Il software dovrà risiedere da qualche parte nella rete della scuola o quantomeno accessibile da questa, e dovrà quindi far fronte al proxy che blocca parte delle comunicazioni. Lo sviluppo avverrà su una piattaforma apposita di hosting online [pyhtonanywhere](https://www.pythonanywhere.com/).
Gli utilizzatori saranno allievi ed eventualmente docenti mandanti della SAMT (scuola arti e mestieri di Trevano), che necessitano rispettivamente di imparare e di valutare la gestione dei progetti.
La conoscenza richiesta, oltre al saper utilizzare un computer per interagire con la pagina vera e propria, è quella di una base delle modalità di gestione di un progetto per poter amministrare l'incarico e un minimo di propensione nel lavoro in team.

<!--
Questo capitolo dovrebbe descrivere il contesto in cui il prodotto verrà
utilizzato, da questa analisi dovrebbero scaturire le risposte a quesiti
quali ad esempio:
-   Background/Situazione iniziale
-   Quale è e come è organizzato il contesto in cui il prodotto dovrà
    funzionare?
-   Come viene risolto attualmente il problema? Esiste già un prodotto
    simile?
-   Chi sono gli utenti? Che bisogni hanno? Come e dove lavorano?
-   Che competenze/conoscenze/cultura posseggono gli utenti in relazione
    con il problema?
-   Esistono convenzioni/standard applicati nel dominio?
-   Che conoscenze teoriche bisogna avere/acquisire per poter operare
    efficacemente nel dominio?
    -->
### Analisi e specifica dei requisiti

<!--
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
-->

|**ID**|**Nome**        |**Priorità**|**Vers**|**Note**|
|------|----------------|------------|--------|--------|
|Req-01|Realizzare un sito web per la gesitone dei progetti|1|1.0|...|
|Req-02|Il sito web è programmato in python|1|1.0|...|
|Req-03|Ci deve essere una schermata di signup e una di login|1|1.0|...|
|Req-04|Ci deve essere una schermata di password recovery|3|1.0|...|
|Req-05|Ci sono due tipi di utente a livello del login (admin, utente)|1|1.0|...|
|Req-06|Ci deve essere una schermata principale con la lista dei progetti|2|1.0|...|
|Req-07|Si può creare un progetto|1|1.0|...|
|Req-08|Un progetto deve avere dei dettagli (nome, descrizione, lista membri, inizio e fine)|1|1.0|...|
|Req-09|Un progetto può essere una bozza o un progetto finale|1|1.0|...|
|Req-10|Una bozza si può convertire in un progetto finale|2|1.0|...|
|Req-11|Un progetto può essere pubblico o privato (non visibile da non-membri)|1|1.0|...|
|Req-12|Gli utenti hanno ruoli diversi a livello di progetto (capoprogetto, ospite, …)|1|1.0|...|
|Req-13|Nel progetto si possono creare delle attività|1|1.0|...|
|Req-14|Si possono modificare le informazioni di un progetto|2|1.0|...|
|Req-15|Una attività deve avere dei dettagli (nome, descrizione, durata)|1|1.0|...|
|Req-16|Un'attività può essere in determinate sezioni (idea, da fare, in esecuzione, terminato, testato, approvato)|1|1.0|...|
|Req-17|Si possono creare nuove sezioni|1|1.0|...|
|Req-18|Ci deve essere una sezione dove si può reportare i bug|2|1.0|...|
|Req-19|Vanno controllati gli indirizzi email per registrarsi|2|1.0|consentito solo per @samtrevano.ch — @edu.ti.ch|
|Req-20|Ci deve essere un database per il salvataggio dei progetti|1|1.0|...|
|Req-21|Si possono utilizzare le attività di un progetto concluso come nuove attività|4|1.0|!!!|

<!--
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
-->

### Use case

### Pianificazione
Gantt preventivo:
![Gant preventivo](../Pianificazione/ProPlan_GanttPreventivo.PNG)
Il lavoro durerà 5 mesi, da gennaio a maggio. Abbiamo pianificato un mese di studio (fino a inizio febbraio), due settimane di design, circa 3 mesi di implementazione e infine due settimane di test e rifinimenti vari. Inoltre, per un mese dall'inizio del progetto dovremo inoltre dedicare parte del tempo ad imparare gli strumenti da utilizzare.

### Analisi dei mezzi

#### Linguaggio
L'applicativo si basa su python, un linguaggio di alto livello disponibile su ogni piattaforma e che si distingue per la sua sintassi severa rispetto all'indentazione, a favore di una scrittura spesso più breve.

#### Framework
Per lo sviluppo è stato utilizzato Web2py, un framework leggero e pensato per creare piccole applicazioni web. Inoltre, integra SQLite, le librerie necessarie per interagirci ed eventualmente la possiblità di espandere il database (passando, per esempio, ad Oracle o mySQL) senza problemi grazie all'alto livello di astrazione.

#### Hosting
L'ambiente di sviluppo sarà la piattaforma di hosting pythonanywhere, quindi l'hardware è rappresentato da computer portatili che integreranno il server grazie a web2py e dei client simulati tramite browser.
La piattaforma di funzionamento è vincolata non a sistemi operativi specifici, quanto più ai browser che andranno a visitare le pagine del sito, i quali dovranno essere abbastanza recenti ed aggiornati da supportare le funzioni del software.

#### Altre librerie

##### Highcharts - Libreria javascript
Per realzzare i diagrammi di gantt abbiamo utilizzato la libreria messa a disposizione da [Highcharts](https://www.highcharts.com/): questa libreria permette la creazione di diversi tipi di grafici convertendoli da codice JSON.

<!--
Elencare e *descrivere* i mezzi disponibili per la realizzazione del
progetto. Ricordarsi di sempre descrivere nel dettaglio le versioni e il
modello di riferimento.
SDK, librerie, tools utilizzati per la realizzazione del progetto e
eventuali dipendenze.
Su quale piattaforma dovrà essere eseguito il prodotto? Che hardware
particolare è coinvolto nel progetto? Che particolarità e limitazioni
presenta? Che hw sarà disponibile durante lo sviluppo?
-->

## Progettazione
<!--
Questo capitolo descrive esaustivamente come deve essere realizzato il
prodotto fin nei suoi dettagli. Una buona progettazione permette
all’esecutore di evitare fraintendimenti e imprecisioni
nell’implementazione del prodotto.
-->

### Design dell’architettura del sistema
![Schema use cases](../Progettazione/ProPlan_useCases.svg)
La base della nostra progettazione è questo diagramma, che rappresenta in stile use case le interazioni possibili e gli indirizzamenti conseguenti dell'applicazione. Non è propriamente uno schema dei casi d'uso, poichè ne abbiamo definito regole riconosciute solo all'interno del team di lavoro e visibili nella legenda allegata al diagramma.

Il suo scopo è rappresentare in forma schematica le schermate e pulsanti disponibili, ma senza scendere nei dettagli della parte visiva.

#### Struttura delle cartelle
Per avere in chiaro dove lavorare e per trovare un accordo sulla struttura dei link, abbiamo definito la [struttura delle cartelle](../Progettazione/strutturaCartelle.md) che avrebbero dovuto essere usate per il sito.

Alla creazione di un progetto si possono creare le attività del progetto e si possono definire i permessi di altri utenti, nominando magari un cocapo progetto oppure un semplice membro del progetto.
Si possono creare anche delle bozze di progetti, ovvero non dei veri e propri progetti, ma delle idee per il progetto vero e proprio.

<!--
Descrive:
- La struttura del programma/sistema lo schema di rete...
- Gli oggetti/moduli/componenti che lo compongono.
- I flussi di informazione in ingresso ed in uscita e le
relative elaborazioni. Può utilizzare *diagrammi di flusso dei
dati* (DFD).
- Eventuale sitemap
-->

### Design dei dati e database
<!--Descrizione delle strutture di dati utilizzate dal programma in base
agli attributi e le relazioni degli oggetti in uso.-->

### Schema E-R, schema logico e descrizione.

![Schema E/R](../Progettazione/diagrammaERProPlan.svg)

<!--
Se il diagramma E-R viene modificato, sulla doc dovrà apparire l’ultima
versione, mentre le vecchie saranno sui diari.
-->

### Design delle interfacce

#### Progetti iniziali
Abbiamo cominciato disegnando alcune schermate in modo da renderci conto di quali elementi avremmo avuto bisogno. Non sono state scelte di comune accordo, quindi risultano diverse dal risultato finale.
![Popup creazione progetto](../Progettazione/popup_creazione_progetto.png)
![Progetti personali](../Progettazione/schermata_progetti_personali.png)
![Home](../Progettazione/schermata_home.png)

In seguito abbiamo anche provato a disegnare delle schermate con programmi appositi, ma non eravamo in chiaro sugli strumenti che avremmo avuto a disposizione per crearle, quindi anche queste si differenziano dal design definitivo.
![Login](../Progettazione/Schermata_Login.png)
![Sing in](../Progettazione/Schermata_Registrazione.png)
<!--Descrizione delle interfacce interne ed esterne del sistema e
dell’interfaccia utente. La progettazione delle interfacce è basata
sulle informazioni ricavate durante la fase di analisi e realizzata
tramite mockups.-->

### Design procedurale
![Diagramma UML](../Progettazione/UMLDiagramm.svg)
Il diagramma UML spiega in modo più dettagliato la logica descrivendo i nomi dei metodi e il loro livello nella struttura MVC (model, view, contorller)

<!--
Descrive i concetti dettagliati dell’architettura/sviluppo utilizzando
ad esempio:
-   Diagrammi di flusso e Nassi.
-   Tabelle.
-   Classi e metodi.
-   Tabelle di routing
-   Diritti di accesso a condivisioni …
Questi documenti permetteranno di rappresentare i dettagli procedurali
per la realizzazione del prodotto.-->

## Implementazione

<!--
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
-->

## Test

### Protocollo di test

|*Test Case*|*TC-01*|
|-----------|-------|
|Nome|Sito web|
|Riferimento|Req-01|
|Descrizione|Deve esistere un sito web funzionante che permette di gestire i progetti|
|Prerequisiti|…|
|Procedura|Andare su internet e cercare il sito web, una volta trovato entrarci e vedere se funziona il tutto |
|Risultati attesi|Bisogna vedersi un sito funzionante|

|*Test Case*|*TC-02*|
|-----------|-------|
|Nome|Signup, Login|
|Riferimento|Req-03|
|Descrizione|Il sito deve permettere ad un utente di registrarsi o loggarsi all'interno del sito, per entrare nel sito serve email e password|
|Prerequisiti|…|
|Procedura|Una volta entrati nel sito questo ti reindizerrà nella pagina di signup, e si posso inserire i vari dati poi ci sarà una conferma per email, in caso che si ha già un account c'è un riferimento al login dove si posso inserire i dati per loggarsi|
|Risultati attesi|Alla fine di tutto si dovra essere alla pagine principale del sito "/home/index"|

|*Test Case*|*TC-03*|
|-----------|-------|
|Nome|Password recovery|
|Riferimento|Req-04|
|Descrizione|Deve essere possibile poter cambiare password in caso che si sia dimenticata o in caso che untento voglia di sua spontanea volontà di cambiare password|
|Prerequisiti|…|
|Procedura|In caso si sia dimenticato nella pagina di login c'è un link che porta alla pagina di password recovery, una volta arrivati qui basta inserire la propria mail e arrivare nella mail box della persona una mail con un codice, inserire il codice nel sito e poi si potrà cambiare password, invece se una persona vuole cambiare la propria mail in alto a destra ci sono le informazione dell'utente, c'è un bottone che permette di andare nella nella password recovery e eseguire lo stesso passaggio di prima|
|Risultati attesi|Al loggin deve essere possibile loggarsi con la password cambiata e non con la vecchia password|

|*Test Case*|*TC-04*|
|-----------|-------|
|Nome|Lista progetti|
|Riferimento|Req-06|
|Descrizione|Ci deve essere una pagina nel sito in cui c'è la lista dei propri progetti|
|Prerequisiti|…|
|Procedura|Dopo il login nella pagina principale del sito c'è una categoria "Personali", bisogna cliccarci sopra e comparirà un drop down, nel drop down c'è un link alla lista di progetti|
|Risultati attesi|Una volta finito si deve essere nella pagina dove ci sono tutti i progetti che una persona ha fatto, quelli che sta facendo e quelli che deve fare, la pagina è "/projectlist/index"|

|*Test Case*|*TC-05*|
|-----------|-------|
|Nome|Creazione progetto|
|Riferimento|Req-07|
|Descrizione|Si può creare un nuovo progetto, così poi ci si puoi lavorare|
|Prerequisiti|…|
|Procedura|Nella pagina di "/projectlist/index" c'è il bottone "Crea progetto" dove una volta inserito i dati neccesari con il pulsante "Crea" si crea il nuovo progetto|
|Risultati attesi|Una volta fatto "Crea" nella lista dei progetti dovrebbe apparire il nuovo progetto con i dati che si sono definiti alla creazione|

|*Test Case*|*TC-06*|
|-----------|-------|
|Nome|Evuluzione di una bozza|
|Riferimento|Req-10|
|Descrizione|Dato che un progetto può essere una bozza (il progetto che è una bozza può solo butare giù delle idee) o un progetto finale (nel progetto finale è possibile inserire più dati: data_inizio, data_fine, team, …), una volta che si è scelto una bozza si può fare un upgrade del progetto e renderlo finale così da definire un team e le date di inizio e fine.|
|Prerequisiti|…|
|Procedura|All'interno della pagina del singolo progetto (in caso questo sia una bozza) c'è un bottone "Upgrade", per far diventare una bozza in finale bisogna cliccare il bottone|
|Risultati attesi|Il risultato deve essere un progetto finale dove è possibile inserire data inizio, fine e inserire il team di lavoro|

|*Test Case*|*TC-07*|
|-----------|-------|
|Nome|Progetto publicco o privato|
|Riferimento|Req-11|
|Descrizione|Un progetto può essere pubblico (visibile a tutte le persone) o privato (visibile alle persone che fan parte del team di progetto), e si deve poter scegliere se il progetto sia uno o l'altro|
|Prerequisiti|…|
|Procedura|Alla creazione di un progetto si può definire se il progetto è pubblico o privato (in caso che questo solo se il progetto è finale). Invece in caso che è una bozza all'upgrade del progetto si può definire se il progetto diventerà pubblico o finale|
|Risultati attesi||

|*Test Case*|*TC-08*|
|-----------|-------|
|Nome|Creazione attività|
|Riferimento|Req-13|
|Descrizione|In un progetto si può creare un attività che un persona del team dovrà svolgere per il compimento del progetto|
|Prerequisiti|…|
|Procedura|Nella pagina di progetto sotto a ogni sezoine c'è un bottone "Crea attività" dove una volta cliccato è possibile definire una attività che verà collocata nella sezione in cui si è cliccato il bottone|
|Risultati attesi|Una volta creato l'attività si dovrebbe vedre la stessa attività nella sezione selezionata|

|*Test Case*|*TC-09*|
|-----------|-------|
|Nome|Creazione di sezione|
|Riferimento|Req-17|
|Descrizione|Ci sono le sezione di default (per chi vuole), ma in caso che serve aggiungere più sezioni un utente può farlo, così da poter mettere le attività di propria creazione|
|Prerequisiti|…|
|Procedura|Nella pagina di progetto dopo le sezione c'è un bottone che permette di creare una nuova sezione definità da nome|
|Risultati attesi|Una volta inserita una nuova sezione dovrebbe vedersi aparrire questa nella pagine di progetto e si potrebbe aggiungere un'attività in questa sezione|

|*Test Case*|*TC-10*|
|-----------|-------|
|Nome|Spostamento attività|
|Riferimento|Req-16|
|Descrizione|Si può fare in modo di spostare una attività da una sezione ad un'altra|
|Prerequisiti|…|
|Procedura|Nella pagina di rpogetto si vedono tutte le attività basta cliccare l'attivatà e usciranno tutte le sue informazioni e basterà cambiare il riferimento della sezione|
|Risultati attesi|Si dovrà vedere l'attività nella nuova sezione e non in quella vecchia (da dove si è spostato)|

|*Test Case*|*TC-11*|
|-----------|-------|
|Nome|Email corretti|
|Riferimento|Req-19|
|Descrizione|Dato che il progetto è scolastico, è possibile collegarsi solo con account della scuola ovvero per gli allievi "@samtrevano.ch" mentre per i professori "@edu.ti.ch"|
|Prerequisiti|…|
|Procedura|Nel signup quando si inserisce un nuvo utento viene effettuato il controllo della mail in caso la mail non è ne di un alievo e neanche di professore allora non viene inserito nel database, mentre se la mail è valida questa viene inserito nel database|
|Risultati attesi|In caso la mail non è valida esce un errore, invece in caso che la mail è valida esce la scritta "Success"|

<!--
|Test Case      | TC-00                               |
|---------------|--------------------------------------|
|**Nome**       | |
|**Riferimento**|REQ-00                               |
|**Descrizione**| |
|**Prerequisiti**| |
|**Procedura**     |  |
|**Risultati attesi** | |

|Test Case      | TC-00                               |
|---------------|--------------------------------------|
|**Nome**       | |
|**Riferimento**|REQ-00                               |
|**Descrizione**| |
|**Prerequisiti**| |
|**Procedura**     |  |
|**Risultati attesi** | |
-->

<!--
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
-->

### Risultati test

<!--
Tabella riassuntiva in cui si inseriscono i test riusciti e non del
prodotto finale. Se un test non riesce e viene corretto l’errore, questo
dovrà risultare nel documento finale come riuscito (la procedura della
correzione apparirà nel diario), altrimenti dovrà essere descritto
l’errore con eventuali ipotesi di correzione.
-->
### Mancanze/limitazioni conosciute

<!--
Descrizione con motivazione di eventuali elementi mancanti o non
completamente implementati, al di fuori dei test case. Non devono essere
riportati gli errori e i problemi riscontrati e poi risolti durante il
progetto.
-->
## Consuntivo
Gantt consuntivo:
![Gantt consuntivo](../Pianificazione/ganttconsuntivo.png)

## Conclusioni

<!--
Quali sono le implicazioni della mia soluzione? Che impatto avrà?
Cambierà il mondo? È un successo importante? È solo un’aggiunta
marginale o è semplicemente servita per scoprire che questo percorso è
stato una perdita di tempo? I risultati ottenuti sono generali,
facilmente generalizzabili o sono specifici di un caso particolare? ecc
-->
### Sviluppi futuri

<!--Migliorie o estensioni che possono essere sviluppate sul prodotto.
-->
### Considerazioni personali

<!--
  Cosa ho imparato in questo progetto? ecc
-->
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
