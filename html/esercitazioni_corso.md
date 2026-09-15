# Raccolta Esercitazioni Pratiche per Modulo

Questo documento raccoglie la suite completa di esercitazioni guidate e progetti pratici associati a ciascun modulo del corso di Sviluppo Web (HTML, CSS, JavaScript), come delineato nel programma di studio.

---

## Modulo 1: Struttura Web con HTML

### Esercitazione Modulo 1 - Prima Parte: Pagina Statica Personale (Bio / CV)
* **Citazione Modulo:** *Modulo 1 - prima parte: Sintassi, tag, attributi, struttura base, testo (titoli, paragrafi, liste, link, immagini).*
* **Obiettivo:** Creare la prima pagina web statica contenente la propria biografia o curriculum vitae essenziale.
* **Requisiti Pratici:**
  1. Creare un file chiamato `index.html` con la struttura HTML5 completa (`<!DOCTYPE html>`, `html`, `head`, `body`, meta tag charset e viewport).
  2. Inserire un titolo principale `<h1>` con il proprio nome e cognome.
  3. Aggiungere una foto profilo tramite il tag `<img>`, specificando un attributo `alt` descrittivo.
  4. Scrivere due paragrafi `<p>` di introduzione personale e professionale.
  5. Creare una lista non ordinata `<ul>` con le proprie competenze tecniche o hobby.
  6. Inserire una lista ordinata `<ol>` con le ultime esperienze lavorative o di studio.
  7. Inserire link esterni `<a>` verso i propri profili social/professionali (GitHub, LinkedIn) che si aprano in una nuova scheda (`target="_blank"`).
* **Criteri di Verifica:** Il documento deve essere validato senza errori di sintassi e mostrare chiaramente tutti gli elementi richiesti nel browser.

---

### Esercitazione Modulo 1 - Seconda Parte: Form di Contatto / Registrazione Semantico
* **Citazione Modulo:** *Modulo 1 - seconda parte: HTML semantico, tabelle, form ed elementi di input, accessibilità di base e SEO.*
* **Obiettivo:** Realizzare la struttura semantica accessibile di un modulo di contatto e registrazione, senza applicare stili CSS.
* **Requisiti Pratici:**
  1. Strutturare la pagina con tag semantici (`<header>`, `<main>`, `<section>`, `<footer>`).
  2. Inserire un modulo `<form>` con attributi `action="#"` e `method="POST"`.
  3. Aggiungere i seguenti campi di input, garantendo per ciascuno una `<label>` associata tramite attributo `for` ed `id`:
     * Nome e Cognome (`type="text"`, attributo `required`).
     * Email (`type="email"`, attributo `required`).
     * Password (`type="password"`, attributo `required`, `minlength="8"`).
     * Menu a tendina `<select>` per scegliere il motivo del contatto.
     * Area di testo `<textarea>` per il messaggio.
     * Checkbox per l'accettazione della privacy policy.
     * Pulsante di invio `<button type="submit">`.
  4. Creare una sezione separata contenente una tabella `<table>` riassuntiva con orari di disponibilità o contatti utili.
* **Criteri di Verifica:** Il form deve attivare la validazione nativa del browser al tentativo di invio con campi vuoti o email errata.

---

## Modulo 2: Stile e Design con CSS

### Esercitazione Modulo 2 - Prima Parte: Stile e Layout della Pagina Statica (Bio / CV)
* **Citazione Modulo:** *Modulo 2 - prima parte: Sintassi CSS, selettori, collegamento CSS, Box Model, unità di misura, colori, tipografia, spaziature.*
* **Obiettivo:** Estendere la pagina Bio/CV creata nel Modulo 1 applicando uno stile estetico moderno e professionale.
* **Requisiti Pratici:**
  1. Creare la cartella `css/` e il file `style.css`, collegandolo alla pagina `index.html` tramite `<link>`.
  2. Resettare il Box Model con la regola universale `* { box-sizing: border-box; margin: 0; padding: 0; }`.
  3. Impostare un font di testo pulito (es. `font-family: 'Segoe UI', sans-serif;`) sul `body` e scegliere una palette di colori coerente (almeno 3 colori: primario, secondario, sfondo).
  4. Formattare i titoli `<h1>`-`<h3>` utilizzando dimensioni in `rem` e spaziature con `margin-bottom`.
  5. Rendersi l'immagine profilo circolare tramite `border-radius: 50%` e aggiungere un bordo personalizzato.
  6. Applicare padding e margini appropriati alle sezioni della pagina per garantire leggibilità ed respiro visivo.
* **Criteri di Verifica:** Il foglio di stile deve caricarsi correttamente e trasformare la pagina grezza in un layout graficamente ordinato.

---

### Esercitazione Modulo 2 - Seconda Parte: Form Responsive e Layout con Flexbox e Grid
* **Citazione Modulo:** *Modulo 2 - seconda parte: Flexbox, Grid layout, Responsive design (media query, mobile-first), pseudo-elementi e transizioni.*
* **Obiettivo:** Rendere responsive e visivamente accattivante il form di contatto/registrazione utilizzando Flexbox, CSS Grid e Media Queries.
* **Requisiti Pratici:**
  1. Utilizzare **CSS Grid** per la struttura generale della pagina (header, main, sidebar, footer).
  2. Utilizzare **Flexbox** per disporre i campi del form (es. affiancare Nome e Cognome su schermi grandi) e centrare la card del form nello schermo.
  3. Applicare uno stile moderno agli elementi del form (`input`, `select`, `textarea`), inclusi gli stati `:focus` (bordo evidenziato) e `:hover` sui pulsanti.
  4. Aggiungere una transizione fluida (`transition: all 0.3s ease`) sui pulsanti.
  5. Scrivere **Media Queries** in logica *Mobile-First*:
     * Su schermi smartphone (`width < 768px`): layout ad una singola colonna a larghezza piena.
     * Su schermi tablet/desktop (`width >= 768px`): form centrato con larghezza massima (es. `max-width: 600px`), griglia a più colonne.
* **Criteri di Verifica:** Ridimensionando la finestra del browser, la pagina deve adattarsi fluidamente senza generare barre di scorrimento orizzontali indesiderate.

---

## Modulo 3: Comportamento Dinamico con JavaScript

### Esercitazione Modulo 3 - Prima Parte: Mini-Suite di Esercizi Logici in JavaScript
* **Citazione Modulo:** *Modulo 3 - prima parte: Sintassi, variabili (let/const), tipi di dato, operatori, strutture di controllo, funzioni, array e oggetti, metodi (map, filter, forEach).*
* **Obiettivo:** Prendere confidenza con la sintassi core di JavaScript e la manipolazione delle strutture dati.
* **Requisiti Pratici:**
  1. **Esercizio 1 (Calcolatore Voti):** Scrivere una funzione `valutaStudente(punteggio)` che accetta un numero da 0 a 100 e restituisce "Promosso con Lode" (>=90), "Promosso" (>=60) o "Bocciato" (<60).
  2. **Esercizio 2 (Filtraggio Prodotti):** Dato un array di oggetti `prodotti` (ciascuno con `nome`, `prezzo`, `categoria`):
     * Utilizzare `.filter()` per ottenere solo i prodotti con prezzo inferiore a 50€.
     * Utilizzare `.map()` per generare un nuovo array con i nomi dei prodotti in maiuscolo.
  3. **Esercizio 3 (Analisi Array):** Scrivere una funzione che riceve un array di numeri e stampa in console la somma totale ed il valore massimo tramite ciclo o metodi dedicati.
* **Criteri di Verifica:** I risultati degli esercizi devono essere stampati e verificabili nella console dei DevTools.

---

### Esercitazione Modulo 3 - Seconda Parte: Form Interattivo con Validazione JS Dinamica
* **Citazione Modulo:** *Modulo 3 - seconda parte: Selezione elementi DOM, modifica contenuto/stile via JS, event listener, validazione form lato client con feedback visivo.*
* **Obiettivo:** Collegare JavaScript al form HTML/CSS creato precedentemente per effettuare una validazione in tempo reale prima dell'invio.
* **Requisiti Pratici:**
  1. Selezionare il form e i campi tramite `document.querySelector`.
  2. Intercettare l'evento `submit` del form e bloccare il comportamento nativo tramite `event.preventDefault()`.
  3. Verificare i seguenti requisiti tramite codice JS:
     * Campo Nome: non vuoto e lungo almeno 3 caratteri.
     * Campo Email: rispetta la struttura di un'email valida.
     * Campo Password: lunghezza minima 8 caratteri.
  4. **Feedback Visivo Dinamico:**
     * Se un campo è errato, aggiungere la classe CSS `.input-error` (bordo rosso) e mostrare un messaggio di errore sotto l'input.
     * Se il campo è valido, aggiungere la classe CSS `.input-success` (bordo verde).
  5. Se tutti i campi sono validi, mostrare un messaggio di successo dinamico all'utente e resettare il form con `form.reset()`.
* **Criteri di Verifica:** Il form deve mostrare e rimuovere dinamicamente gli errori visivi in risposta alle azioni dell'utente.

---

### Esercitazione Modulo 3 - Terza Parte: Integrazione Fetch API e Rendering Dati Esterni
* **Citazione Modulo:** *Modulo 3 - terza parte: Template literals, destructuring, spread/rest, fetch() e JSON, try/catch, connessione al backend.*
* **Obiettivo:** Effettuare una chiamata HTTP asincrona ad un'API pubblica e mostrare i dati ricevuti dinamica all'interno del DOM.
* **Requisiti Pratici:**
  1. Creare una funzione asincrona `caricaUtenti()` che utilizza `fetch()` verso l'API pubblica `https://jsonplaceholder.typicode.com/users`.
  2. Gestire eventuali errori di rete o di risposta HTTP utilizzando il blocco `try...catch`.
  3. Mostrare uno stato di caricamento ("Caricamento dati in corso...") nell'interfaccia durante l'attesa della risposta.
  4. Una volta ricevuti i dati JSON, ciclare sull'array di utenti e generare per ciascuno una scheda HTML utilizzando i **Template Literals** e il **Destructuring**.
  5. Inserire le schede generate all'interno di un contenitore griglia nel DOM.
* **Criteri di Verifica:** All'apertura della pagina (o al click su un pulsante "Ricarica"), le schede utente devono essere popolate dinamicamente con i dati provenienti dall'API remota.

---

## Progetto Finale Integrato

### Esercitazione Finale: Sviluppo Mini-Dashboard o Web App Completa
* **Citazione Modulo:** *Progetto finale integrato (1 settimana): Consolidamento HTML semantico + CSS responsive + JS con validazione e fetch.*
* **Obiettivo:** Realizzare un'applicazione web completa (es. Mini-Dashboard Meteo, Gestore Task/To-Do List con persistenza/API, o Catalogo Prodotti Interattivo).
* **Traccia di Lavoro Consigliata (Catalogo Prodotti Interattivo):**
  1. **Struttura (HTML):**
     * Header con logo e barra di ricerca.
     * Main diviso in due sezioni: Sidebar dei filtri e Griglia prodotti.
     * Footer con info e contatti.
  2. **Stile (CSS):**
     * Layout responsive Mobile-First con CSS Grid e Flexbox.
     * Card prodotto curate con effetti `:hover` e transizioni.
  3. **Interattività (JS):**
     * Chiamata `fetch()` all'API `https://fakestoreapi.com/products` per scaricare il catalogo.
     * Barra di ricerca in tempo reale (evento `input`) per filtrare i prodotti per titolo.
     * Filtro per categoria tramite menu a tendina o bottoni.
     * Gestione del carrello (aggiunta/rimozione prodotti e calcolo del totale).
* **Checklist di Consegna e Valutazione:**
  * [ ] Codice HTML privo di errori di validazione W3C e semanticamente corretto.
  * [ ] Layout perfettamente fruibile sia su Mobile che su Desktop.
  * [ ] Nessun errore visibile nella console JavaScript.
  * [ ] Presentazione orale del progetto con spiegazione delle scelte architetturali.
