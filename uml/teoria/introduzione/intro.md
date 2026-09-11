# UML - Unified Modeling Language

UML è un linguaggio di modellazione grafica standardizzato, usato principalmente nell'ingegneria del software per progettare, visualizzare e documentare sistemi software (ma anche processi aziendali o strutture organizzative). Non è un linguaggio di programmazione: non si "esegue", serve a rappresentare graficamente idee prima (o durante) la scrittura del codice.

## Storia in breve

UML nasce a metà anni '90 dalla fusione di diversi metodi di modellazione orientati agli oggetti, in particolare quelli di **Grady Booch**, **James Rumbaugh** (OMT) e **Ivar Jacobson** (OOSE) — per questo sono chiamati "i tre amigos". Nel 1997 UML viene adottato come standard dall'**OMG (Object Management Group)**, che ancora oggi lo mantiene.

## A cosa serve

- Comunicare l'architettura di un sistema tra sviluppatori, analisti e stakeholder
- Documentare un sistema esistente
- Progettare prima di implementare (specialmente in contesti object-oriented)
- Fornire un linguaggio comune e non ambiguo, indipendente dal linguaggio di programmazione usato

## Le due grandi categorie di diagrammi

UML definisce 14 tipi di diagrammi, divisi in due famiglie principali:

### Diagrammi strutturali (mostrano la struttura statica del sistema)
- **Diagramma delle classi** — il più usato; mostra classi, attributi, metodi e relazioni (ereditarietà, associazione, aggregazione, composizione)
- Diagramma degli oggetti
- Diagramma dei componenti
- Diagramma di deployment (distribuzione fisica)
- Diagramma dei package
- Diagramma delle strutture composite

### Diagrammi comportamentali (mostrano il comportamento dinamico)
- **Diagramma dei casi d'uso (use case)** — mostra le interazioni tra utenti/attori e il sistema
- **Diagramma di sequenza** — molto usato; mostra lo scambio di messaggi tra oggetti nel tempo
- **Diagramma delle attività** (simile a un flowchart)
- Diagramma di stato (state machine)
- Diagramma di comunicazione
- Diagramma di interazione generale
- Diagramma dei tempi (timing)

## I quattro diagrammi più usati nella pratica

Nella maggior parte dei progetti reali si usano soprattutto questi quattro tipi:

### 1. Diagramma delle classi (Class Diagram)
Rappresenta la struttura statica del sistema: classi, i loro attributi e metodi, e le relazioni tra esse (ereditarietà, associazione, aggregazione, composizione, dipendenza). È il diagramma UML più diffuso perché mappa quasi direttamente sul codice orientato agli oggetti ed è utile sia in fase di progettazione sia di documentazione.

### 2. Diagramma dei casi d'uso (Use Case Diagram)
Descrive le funzionalità del sistema dal punto di vista dell'utente. Mostra gli **attori** (utenti o sistemi esterni) e i **casi d'uso** (le azioni/funzionalità che il sistema offre), insieme alle relazioni tra loro. È molto utile nelle fasi iniziali di analisi dei requisiti, per allineare sviluppatori e stakeholder su cosa deve fare il sistema.

### 3. Diagramma di sequenza (Sequence Diagram)
Mostra come gli oggetti interagiscono tra loro nel tempo, rappresentando lo scambio di messaggi in un ordine cronologico. È particolarmente utile per capire il flusso di uno scenario specifico (es. il processo di login, una transazione) e per progettare la logica di interazione tra componenti.

### 4. Diagramma delle attività (Activity Diagram)
Simile a un diagramma di flusso (flowchart), rappresenta il flusso di controllo o di dati tra diverse attività/azioni, incluse decisioni, cicli ed elaborazioni parallele. È utile per modellare processi di business o la logica di un algoritmo/workflow a un livello più alto rispetto al codice.
