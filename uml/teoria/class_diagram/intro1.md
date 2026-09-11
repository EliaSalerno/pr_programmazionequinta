# Introduzione al Diagramma delle Classi (UML)

## 1. Cos'è il Diagramma delle Classi?
Il **Diagramma delle Classi** (*Class Diagram*) è il diagramma strutturale più diffuso e utilizzato del linguaggio UML (Unified Modeling Language). La sua funzione principale è rappresentare la struttura statica di un sistema software, descrivendo le **classi**, i loro **attributi**, le **operazioni** (metodi) e le **relazioni** che intercorrono tra le differenti entità.

A differenza dei diagrammi comportamentali, il diagramma delle classi si concentra su ciò che compone il sistema anziché sul suo comportamento dinamico nel tempo. Poiché si mappa quasi direttamente sui linguaggi di programmazione orientati agli oggetti (OOP), risulta essenziale sia nella fase di analisi e progettazione sia nella fase di documentazione del codice.

---

## 2. Notazione della Classe
Graficamente, una classe è rappresentata da un singolo rettangolo suddiviso verticalmente in **tre scomparti**:

1. **Nome della Classe** (scomparto superiore):
   - Posizionato in alto, scritto in **grassetto** e con l'iniziale maiuscola.
   - Per le **classi astratte**, il nome viene convenzionalmente scritto in *corsivo*.
2. **Attributi** (scomparto centrale):
   - Elenca le proprietà e i dati memorizzati dall'oggetto.
   - Ogni attributo esprime le caratteristiche dell'entità ed è solitamente associato a un fattore di visibilità che ne definisce il livello di accesso.
3. **Operazioni / Metodi** (scomparto inferiore):
   - Elenca i processi e le funzionalità che la classe è in grado di eseguire.

---

## 3. Relazioni tra Classi
I collegamenti tra le classi permettono di definire l'architettura complessiva del sistema. Le principali relazioni modellate sono:

* **Generalizzazione (Ereditarietà)**: Collega una sottoclasse a una superclasse, permettendo alla sottoclasse di ereditare attributi e metodi.
* **Associazione**: Rappresenta una relazione statica tra due entità (ad esempio, la relazione tra uno studente e la scuola). Include il fattore di **molteplicità**, che specifica quante istanze partecipano al legame.
* **Aggregazione**: Un tipo di associazione che esprime una relazione "tutto-parte" debole, in cui le parti possono continuare a esistere indipendentemente dalla classe contenitore.
* **Composizione**: Una variante forte dell'aggregazione in cui la parte è strettamente dipendente dal tutto; se la classe principale cessa di esistere, anche le sue componenti smettono di esistere.
* **Dipendenza**: Indica che una classe fa uso di un'altra, pertanto una modifica nella classe da cui si dipende può comportare modifiche nella classe dipendente.

---

## 4. Ambiti di Utilizzo ed Esempi
Il diagramma delle classi trova applicazione in molteplici contesti di modellazione e ingegnerizzazione del software, quali:

- **Sistemi Bancari e ATM**: Modellazione di conti, utenti, carte e transazioni.
- **Gestione di Biblioteche ed Ospedali**: Organizzazione di libri, prestiti, pazienti, trattamenti e personale.
- **E-commerce e Sistemi Aerei**: Rappresentazione di carrelli, ordini, spedizioni, passeggeri e prenotazioni.

Inoltre, costituisce la base fondamentale sia per il **forward engineering** (trasformazione del modello in codice eseguibile) sia per il **reverse engineering** (ricostruzione del modello concettuale a partire da codice esistente).
