# ProPlan | Diario di lavoro
##### Kushtrim Rushi & Jure Grgic & Jonathan Mueller & Filippo Zinetti
### Trevano, 2020-03-06

## Lavori svolti

| Orario        | Lavoro svolto |
|---------------|---------------|
| 08:20 - 09:50 | Pensate alcune FAQ da includere nel sito, terminato il codice del database |
| 08:20 - 09:00 | Trovato il modo di inserire immagini all'interno del sito |
| 08:20 - 16:30 | Debug degli errori generati da pythonanywhere |
| 15:30 - 16:00 | Completato il diario |

##  Problemi riscontrati e soluzioni adottate

#### Spiegazione 1
"Web2py quando trova un errore blocca completamente il sito, per capire questo errore ci abbiamo impiegato ora, aperto una volta il sito in locale sono usciti gli errori riscontrati, l'errore che non faceva funzionare tutto il programma è la versione sbagliata del pickle."


#### Spiegazione 2:
- Il caricamento delle immagini non funzionava. Abbiamo provato con il progetto di ProPlan web2py online, un progetto offline (entrambi con versione di python 3.7) e un progetto offline con versione 2.7, e solo in quest'ultimo il caricamento è andato a buon fine, quindi pensiamo che la causa del problema sia python 3.7 non completamente reso compatibile con web2py.
- La piattaforma pythonanywhere, oltre ad essere lenta nei caricamenti rallentando i ritmi di lavoro, ha avuto degli insoliti blocchi totali la cui ricerca degli errori ci ha fatto perdere quasi l'intera giornata: al salvataggio di un file, il sito cominciava a non più rispondere, per poi eseguire lunghi caricamenti che terminavano con la visualizzazione errata degli elementi del sito per la gestione del progetto e quindi l'impossiblità di potervi interagire in alcun modo.
    - Dopo alcune discussioni sulla fattiblità del progetto, abbiamo trovato il modo di far ripartire, seppur con grande dispendio di tempo, la piattaforma dopo questi errori: essendo causati da file per la definizione di database con piccoli errori, abbiamo scoperto come il rimuovere questi file (accedendovi da pythonanywhere, poichè web2py rimaneva inaccesibile) aiutasse a riacquisire il controllo sul progetto.
    - In seguito, ho svolto altre prove fuori orario che hanno consistito nella clonazione del progetto in un altro account creato apposta di pythonanywhere per lavorare senza la paura di perdere completamente il lavoro svolto. Ho notato come il clone gestisse in modo appropriato gli errori creando i ticket per il debug e fermandosi prima di intaccare il sistema. Ho concluso che la causa di tutti i problemi erano, molto probabilmente i file di routing che avrebbero dovuto rendere ProPlan l'unica applicazione accessibile (escludendo totalmente examples, admin, welcome ed altre eventuali): alcune configurazioni in questi file, a quanto pare, impedivano il caricamento dei ticket e permettevano così al codice di continuare creando errori in altri file, che poi impedivano il caricamento di tutto il sistema
    - Un altra spiegazione è però quella di un errore di pythonanywhere: i ticket sono tornati a generarsi in seguito all'eliminazione dei file di routing e lo spegnimento+riaccensione del sito sempre dall'host, quindi la soluzione è stata una di queste due azioni.
- (La testardaggine, la riluttanza nel continuare a lavorare di alcuni membri, l'indecisione, la voglia di ricominciare da zero il progetto alla cieca e le brevi ma frequenti pause di distrazione per parlare di altri argomenti o fare commenti su altre questioni...)


##  Punto della situazione rispetto alla pianificazione
È stata una giornata poco produtiva ma siamo più o meno come pianificato.
Abbiamo risolto tanti piccoli problemi prendendoci il tempo necessario finchè possibile, ma il morale del team scende drasticamente ad ogni giornata

## Programma di massima per la prossima giornata di lavoro
Poichè i bug di oggi sono già stati risolti grazie ad alcune ore aggiuntive di lavoro, l'obbiettivo è ottenere risultati pratici (logica e schermate presentabili). E, magari, non abbattersi di fronte alle difficoltà...
