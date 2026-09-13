# Metodologia di lavoro per la creazione dei diagrammi UML

Questa guida propone un percorso pratico, fase per fase, per andare dai requisiti di un sistema fino ai quattro diagrammi UML più usati: **casi d'uso**, **attività**, **sequenza** e **classi**. L'ordine proposto non è casuale: ogni diagramma si costruisce sfruttando le informazioni emerse dal precedente, in modo simile a come un ciclo RAD procede per iterazioni progressive che raffinano il modello.

## Visione d'insieme del flusso di lavoro

```
1. Diagramma dei Casi d'Uso   →  COSA fa il sistema (requisiti funzionali)
          │
          ▼
2. Diagramma delle Attività    →  COME si svolge un processo/flusso
          │
          ▼
3. Diagramma di Sequenza       →  CHI interagisce con CHI e QUANDO (a runtime)
          │
          ▼
4. Diagramma delle Classi      →  STRUTTURA statica del sistema (dati e comportamento)
```

Si parte dal punto di vista dell'utente (cosa vuole ottenere) e si scende progressivamente verso il dettaglio implementativo (come è strutturato il codice).

---

## Fase 1 — Diagramma dei Casi d'Uso

**Obiettivo**: capire chi usa il sistema e cosa il sistema deve fare, senza entrare nel dettaglio di come.

1. **Raccogli i requisiti**: interviste, documenti di specifica, riunioni con lo stakeholder/cliente.
2. **Identifica gli attori**: chi (persone, ruoli) o cosa (sistemi esterni) interagisce con il sistema. Esempio: `Cliente`, `Amministratore`, `Sistema di Pagamento`.
3. **Identifica i casi d'uso**: le funzionalità che il sistema offre, formulate come verbi all'infinito dal punto di vista dell'utente. Esempio: "Effettuare un ordine", "Gestire il catalogo".
4. **Collega attori e casi d'uso** con linee semplici (chi può fare cosa).
5. **Individua le relazioni tra casi d'uso**, se presenti:
   - `<<include>>` — un caso d'uso ne richiama sempre un altro (es. "Effettuare Ordine" include sempre "Verificare Disponibilità")
   - `<<extend>>` — un comportamento opzionale/estensione (es. "Applicare Sconto" estende "Effettuare Ordine" solo in certe condizioni)
6. **Scrivi una breve descrizione testuale** (scenario) per ogni caso d'uso principale: precondizioni, passi principali, postcondizioni. Questo testo sarà la base della Fase 2.
7. **Valida con lo stakeholder**: rileggi il diagramma insieme a chi conosce il dominio, per verificare che non manchino attori o funzionalità.

**Output di questa fase**: un diagramma con attori, casi d'uso, relazioni, più una descrizione testuale per ciascun caso d'uso rilevante.

---

## Fase 2 — Diagramma delle Attività

**Obiettivo**: dettagliare il flusso logico di uno o più casi d'uso complessi (in particolare quelli con passi condizionali, cicli o attività parallele).

1. **Scegli il caso d'uso da dettagliare** (di solito quelli più complessi o critici individuati in Fase 1).
2. **Identifica il punto di inizio e di fine** del flusso (nodo iniziale ● e nodo finale ⊙).
3. **Elenca le azioni in sequenza**, seguendo la descrizione testuale scritta in Fase 1: ogni passo diventa un rettangolo con angoli arrotondati.
4. **Individua i punti di decisione**: dove il flusso si dirama in base a una condizione, inserisci un rombo (decision node) con le etichette delle condizioni sui rami uscenti (es. `[disponibile]` / `[non disponibile]`).
5. **Individua eventuali attività parallele**: se due o più azioni possono avvenire contemporaneamente, usa le barre di sincronizzazione (fork/join).
6. **Assegna le corsie (swimlane)**, se più attori/componenti partecipano al processo: ogni colonna rappresenta chi è responsabile di quell'azione (utile per capire già in questa fase "chi fa cosa", informazione che servirà in Fase 3).
7. **Rivedi il flusso**: percorrilo mentalmente (o con lo stakeholder) simulando diversi scenari, compresi i casi eccezionali.

**Output di questa fase**: uno o più diagrammi di attività, uno per ogni caso d'uso complesso, con eventuali swimlane che anticipano gli attori coinvolti.

---

## Fase 3 — Diagramma di Sequenza

**Obiettivo**: modellare come gli oggetti/componenti del sistema si scambiano messaggi nel tempo per realizzare un singolo scenario (solitamente il "percorso principale" identificato nelle fasi precedenti).

1. **Scegli lo scenario specifico** da rappresentare (es. "Cliente effettua un ordine con pagamento andato a buon fine" — un solo scenario per diagramma, non tutte le varianti insieme).
2. **Identifica i partecipanti** (lifeline): l'attore che avvia l'interazione e gli oggetti/classi coinvolti. Spesso questi oggetti corrispondono alle **swimlane** individuate in Fase 2, o alle classi che intuisci essere necessarie (che affinerai in Fase 4).
3. **Disponi le lifeline orizzontalmente**, nell'ordine logico di intervento nel processo, con una linea verticale tratteggiata sotto ciascuna (la "vita" nel tempo, che scorre dall'alto verso il basso).
4. **Disegna i messaggi come frecce orizzontali**, nell'ordine cronologico in cui avvengono, dall'alto verso il basso:
   - freccia continua con punta piena = chiamata sincrona di un metodo
   - freccia tratteggiata = messaggio di ritorno (risposta)
   - freccia con punta aperta = messaggio asincrono
5. **Aggiungi i riquadri di attivazione** (piccoli rettangoli sulla lifeline) per indicare quando un oggetto è "attivo" nell'elaborare una richiesta.
6. **Gestisci le condizioni**, se presenti, con i frame `alt` (alternative) o `opt` (opzionale) attorno ai messaggi coinvolti.
7. **Verifica la coerenza con il diagramma delle attività**: ogni azione/decisione della Fase 2 dovrebbe trovare corrispondenza in uno o più messaggi scambiati qui.

**Output di questa fase**: uno o più diagrammi di sequenza, uno per scenario significativo, con i nomi (provvisori) delle classi/oggetti coinvolti — che diventeranno la base della Fase 4.

---

## Fase 4 — Diagramma delle Classi

**Obiettivo**: definire la struttura statica del sistema — le classi, i loro attributi, metodi e le relazioni tra esse — sintetizzando quanto emerso nelle fasi precedenti.

1. **Estrai i candidati classe** dai sostantivi ricorrenti nei casi d'uso, nelle attività e nei diagrammi di sequenza (es. `Cliente`, `Ordine`, `Prodotto`, `Pagamento`).
2. **Estrai i candidati metodo** dai verbi/messaggi visti nel diagramma di sequenza: ogni messaggio scambiato tra due lifeline diventa, tipicamente, un metodo della classe ricevente (es. il messaggio `verificaDisponibilità()` diventa un metodo di `Prodotto` o `Magazzino`).
3. **Definisci gli attributi** di ogni classe: quali dati deve mantenere per svolgere il proprio ruolo (es. `Ordine` ha `Data`, `Totale`, `Stato`).
4. **Stabilisci le relazioni tra le classi**, scegliendo il tipo corretto in base alla semantica:
   - **Associazione**: due classi collaborano stabilmente (es. `Cliente` — `Ordine`)
   - **Aggregazione** (◇): relazione tutto-parte debole, la parte sopravvive al tutto (es. `Squadra` ◇ `Giocatore`)
   - **Composizione** (◆): relazione tutto-parte forte, la parte muore con il tutto (es. `Ordine` ◆ `RigaOrdine`)
   - **Generalizzazione** (△ continua): ereditarietà tra classi (es. `ClienteVIP` eredita da `Cliente`)
   - **Realizzazione** (△ tratteggiata): una classe implementa un'interfaccia/contratto
   - **Dipendenza** (tratteggiata semplice): uso occasionale, non un attributo permanente
5. **Assegna le molteplicità** alle associazioni (es. `1`, `0..1`, `1..*`, `*`), verificando la coerenza con le cardinalità già emerse nei requisiti.
6. **Definisci la visibilità** di attributi e metodi (`+` public, `-` private, `#` protected), in base a chi deve poter accedere a cosa.
7. **Rivedi il diagramma verificando la tracciabilità**: ogni caso d'uso della Fase 1 dovrebbe poter essere "spiegato" da un insieme di classi e metodi presenti qui.

**Output di questa fase**: il diagramma delle classi completo, pronto per essere tradotto in codice (es. C#) o in schema di database.

---

## Suggerimenti generali sul metodo di lavoro

- **Procedi in modo iterativo, non lineare**: come nel RAD, è normale tornare indietro — ad esempio, mentre disegni il diagramma delle classi potresti scoprire che un caso d'uso della Fase 1 era incompleto. Aggiorna i diagrammi precedenti quando serve.
- **Un diagramma alla volta, uno scenario alla volta**: soprattutto per sequenza e attività, non cercare di rappresentare tutti i casi possibili in un unico diagramma — meglio più diagrammi semplici che uno complesso e illeggibile.
- **Mantieni coerenza terminologica** tra tutti i diagrammi: se un'entità si chiama `Ordine` nel caso d'uso, deve chiamarsi `Ordine` anche nella classe, non `Order` o `OrdineCliente` in un altro diagramma.
- **Valida con gli stakeholder ad ogni fase**, non solo alla fine: un errore nei casi d'uso, se scoperto solo al diagramma delle classi, costa molto di più da correggere.
- **In un contesto Agile**, non serve produrre tutti i diagrammi per l'intero sistema prima di iniziare a programmare: si può applicare questo stesso percorso fase-per-fase a una singola user story o a un singolo incremento, mantenendo i diagrammi leggeri e aggiornandoli solo quando aggiungono reale valore di comunicazione.

## Tabella riassuntiva rapida

| Fase | Diagramma | Domanda a cui risponde | Input principale | Output principale |
|---|---|---|---|---|
| 1 | Casi d'uso | Cosa deve fare il sistema? | Requisiti, interviste | Attori, casi d'uso, scenari testuali |
| 2 | Attività | Come si svolge il processo? | Scenari testuali della Fase 1 | Flusso con decisioni, swimlane |
| 3 | Sequenza | Chi scambia cosa, e quando? | Swimlane/attori della Fase 2 | Oggetti, messaggi, metodi provvisori |
| 4 | Classi | Come è strutturato il sistema? | Oggetti e metodi della Fase 3 | Classi, attributi, metodi, relazioni |
