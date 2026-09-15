# Documentazione Didattica Completa: Sviluppo Web (HTML, CSS, JavaScript)

Questa documentazione costituisce il manuale di riferimento e la guida teorico-pratica per il corso di Sviluppo Web Frontend. Il percorso è strutturato in tre macro-aree fondamentali: **Struttura (HTML)**, **Stile (CSS)** e **Comportamento (JavaScript)**, culminando in un **Progetto Finale Integrato**.

---

## Modulo 0: Strumenti e Fondamenti del Web

### 1.1 Strumenti di Sviluppo
Per sviluppare applicazioni web moderne in modo efficiente è necessario configurare un ambiente di lavoro professionale:
* **Visual Studio Code (VS Code):** L'editor di codice sorgente di riferimento nel settore. Offre evidenziazione della sintassi, completamento automatico (IntelliSense) ed un ricco ecosistema di estensioni.
* **Estensione Live Server:** Consente di avviare un server di sviluppo locale con funzionalità di *Hot Reload*. Ad ogni salvataggio dei file (`.html`, `.css`, `.js`), il browser aggiorna automaticamente la pagina in tempo reale.
* **DevTools del Browser:** Gli strumenti per sviluppatori integrati nei browser (Chrome, Firefox, Edge, Safari). Accessibili tramite la scorciatoia `F12` o tasto destro -> *Ispeziona*, permettono di:
  * Ispezionare la struttura DOM e modificare gli stili CSS in tempo reale.
  * Monitorare le richieste di rete (Network tab).
  * Analizzare gli errori e stampare log di debug nella Console JavaScript.

### 1.2 Struttura di un Progetto Web e Convenzioni di Naming
La pulizia e la coerenza nell'organizzazione delle cartelle sono essenziali per la manutenibilità del progetto:
* **Root di progetto (cartella principale):**
  * `index.html` (File di ingresso principale del sito web).
  * `css/` -> contiene `style.css` (o file CSS suddivisi per modulo).
  * `js/` -> contiene `main.js` o `script.js`.
  * `assets/` o `img/` -> contiene immagini, icone, font e file multimediali.
* **Convenzioni di Naming:**
  * Utilizzare solo caratteri minuscoli, privi di spazi e caratteri speciali/accentati.
  * Separare le parole tramite trattino medio (`kebab-case`), es. `chi-siamo.html`, `main-banner.png`.

### 1.3 Come funziona il Browser: Richiesta, Rendering e DOM
1. **Richiesta HTTP/HTTPS:** Il client (browser) invia una richiesta ad un server web digitando un URL o cliccando su un link.
2. **Parsing HTML & Costruzione del DOM:** Il browser riceve il codice HTML sorgente, lo analizza riga per riga e costruisce la struttura ad albero in memoria chiamata **DOM (Document Object Model)**.
3. **Parsing CSS & CSSOM:** Contemporaneamente, il browser analizza i fogli di stile e crea il CSSOM (CSS Object Model).
4. **Render Tree & Layout:** Il DOM e il CSSOM vengono combinati per calcolare la geometria, le dimensioni e le posizioni degli elementi sullo schermo.
5. **Paint & Compositing:** Gli elementi vengono disegnati sullo schermo a livello di pixel.

---

## Modulo 1: Struttura Web con HTML

### Parte 1: Fondamenti di HTML

#### Sintassi, Tag, Attributi ed Elementi Vuoti
HTML (*HyperText Markup Language*) è un linguaggio di marcatura basato su **tag**:
* **Tag di apertura e chiusura:** `<tagname>Contenuto</tagname>`
* **Attributi:** Forniscono informazioni aggiuntive all'elemento e si inseriscono nel tag di apertura. Sintassi: `nome="valore"`. Es: `<a href="https://example.com">Link</a>`.
* **Elementi Vuoti (Self-Closing):** Tag che non racchiudono testo e non richiedono tag di chiusura, come `<img>`, `<input>`, `<br>`, `<meta>`.

#### Struttura Base di un Documento HTML5
```html
<!DOCTYPE html>
<html lang="it">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Titolo della Pagina</title>
</head>
<body>
    <h1>Benvenuti nel Corso di Web Development</h1>
    <p>Questo è un paragrafo di esempio.</p>
</body>
</html>
```
* `<!DOCTYPE html>`: Dichiarazione della versione HTML5.
* `<html>`: Elemento radice di tutto il documento.
* `<head>`: Contiene metadati, il titolo della scheda, collegamenti a fogli di stile e script (non visibile direttamente nella pagina).
* `<meta charset="UTF-8">`: Imposta la codifica dei caratteri universale.
* `<meta name="viewport" content="...">`: Essenziale per il Responsive Web Design su dispositivi mobili.
* `<body>`: Contiene tutti gli elementi visibili dall'utente nella pagina web.

#### Elementi di Testo, Liste, Link e Immagini
* **Titoli:** Da `<h1>` (titolo principale) a `<h6>` (sottotitolo di sesto livello). Rispettare sempre la gerarchia progressiva.
* **Paragrafi:** `<p>Testo del paragrafo...</p>`
* **Liste:**
  * Non ordinate (bullet points): `<ul><li>Elemento 1</li><li>Elemento 2</li></ul>`
  * Ordinate (numerate): `<ol><li>Primo passo</li><li>Secondo passo</li></ol>`
* **Link Ipertestuali:** `<a href="URL" target="_blank" rel="noopener noreferrer">Testo del link</a>`
* **Immagini:** `<img src="percorso/immagine.jpg" alt="Descrizione dell'immagine per accessibilità">`

---

### Parte 2: HTML Semantico, Form e Accessibilità

#### HTML Semantico
L'HTML semantico introduce tag dedicati che esprimono chiaramente il significato e il ruolo del contenuto sia per il browser che per i motori di ricerca e gli screen reader:
* `<header>`: Intestazione di un sito o di una sezione (logo, titolo, nav).
* `<nav>`: Sezione riservata ai link di navigazione principali.
* `<main>`: Contenuto principale unico ed esclusivo del documento.
* `<section>`: Raggruppamento tematico di contenuti correlati.
* `<article>`: Blocco autonomo e riutilizzabile (post di blog, notizia, scheda prodotto).
* `<aside>`: Contenuto laterale o secondario correlato (sidebar, link correlati).
* `<footer>`: Pie' di pagina (copyright, contatti, privacy policy).

#### Tabelle Dati
Le tabelle devono essere usate esclusivamente per dati tabellari e mai per la gestione del layout visivo.
```html
<table>
    <caption>Elenco Studenti</caption>
    <thead>
        <tr>
            <th>Nome</th>
            <th>Corso</th>
        </tr>
    </thead>
    <tbody>
        <tr>
            <td>Mario Rossi</td>
            <td>Sviluppo Web</td>
        </tr>
    </tbody>
</table>
```

#### Form ed Elementi di Input
I form consentono l'interazione e la raccolta dati dall'utente.
* `<form action="/submit" method="POST">`
* `<label for="email">Email:</label>`
* `<input type="email" id="email" name="user_email" required placeholder="inserisci la tua email">`
* `<select name="ruolo"><option value="dev">Sviluppatore</option></select>`
* `<textarea name="messaggio" rows="4"></textarea>`
* `<button type="submit">Invia</button>`

**Validazione Nativa:** Attributi come `required`, `type="email"`, `type="number"`, `min`, `max`, `pattern="[0-9]{5}"` attivano il controllo immediato da parte del browser prima dell'invio.

#### Accessibilità (a11y) e Cenni SEO
* **Attributo `alt` obbligatorio** in tutte le immagini informative.
* **Associazione esplicita `<label>` e `<input>`** tramite la coppia di attributi `for` e `id`.
* **Gerarchia H1-H6 coerente:** Un solo `<h1>` per pagina, senza saltare livelli (es. da H1 ad H3).
* **SEO di base:** Uso corretto del tag `<title>`, del meta tag `description` e di marcatori semantici per favorire l'indicizzazione nei motori di ricerca.

---

## Modulo 2: Stile e Design con CSS

### Parte 1: Fondamenti di CSS e Box Model

#### Sintassi e Selettori
CSS (*Cascading Style Sheets*) controlla l'aspetto visivo e il layout del documento HTML.
```css
/* Sintassi: Selettore { proprietà: valore; } */
p {
    color: #333333;
    font-size: 16px;
}
```
* **Selettori di Base:**
  * Elemento/Tag: `h1`, `p`, `a`
  * Classe: `.btn-primary`, `.card`
  * ID (univoco): `#main-header`
  * Discendenza e Combinatori: `article p`, `header > nav`
  * Pseudo-classi: `:hover`, `:focus`, `:active`, `:nth-child(even)`

#### Inserimento del CSS e Specificità
1. **Inline:** `<h1 style="color: red;">` (Sconsigliato per scarsa manutenibilità).
2. **Interno:** Tag `<style>` nella `<head>`.
3. **Esterno (Standard professionale):** `<link rel="stylesheet" href="css/style.css">`

**Cascata e Specificità:**
Quando più regole competono per lo stesso elemento, il browser calcola il punteggio di specificità:
* Inline style: 1000 punti
* ID: 100 punti
* Classi / Pseudo-classi / Attributi: 10 punti
* Tag / Pseudo-elementi: 1 punto

#### Il Box Model
Ogni elemento HTML viene rappresentato come una scatola rettangolare composta da 4 strati concentrici:
1. **Content:** Il contenuto reale (testo, immagine).
2. **Padding:** Lo spazio interno tra contenuto e bordo.
3. **Border:** Il bordo attorno all'elemento.
4. **Margin:** Lo spazio esterno che separa l'elemento dagli altri elementi adiacenti.

```css
* {
    box-sizing: border-box; /* Include padding e border nel calcolo totale di width e height */
}
```

#### Unità di Misura, Colori e Tipografia
* **Unità Assolute:** `px` (pixel).
* **Unità Relative:** `%`, `em` (relativo al font del genitore), `rem` (relativo al font radice `<html>`, standard raccomandato).
* **Colori:** Esadecimale (`#ff0000`), RGB (`rgb(255, 0, 0)`), RGBA (`rgba(255, 0, 0, 0.5)` per trasparenze).
* **Tipografia:** `font-family`, `font-size`, `font-weight`, `line-height`, `text-align`.

---

### Parte 2: Layout Avanzati, Responsive Design e Animazioni

#### Flexbox (Flexible Box Layout)
Strumento monodimensionale (per righe o colonne) ideale per allineare e distribuire lo spazio tra gli elementi.
```css
.container-flex {
    display: flex;
    flex-direction: row; /* row | column */
    justify-content: space-between; /* allineamento asse principale */
    align-items: center; /* allineamento asse trasversale */
    flex-wrap: wrap;
}
```

#### CSS Grid Layout
Strumento bidimensionale (righe e colonne contemporaneamente) ideale per la struttura generale della pagina.
```css
.container-grid {
    display: grid;
    grid-template-columns: repeat(3, 1fr); /* 3 colonne di uguale larghezza */
    gap: 20px; /* Spaziatura tra celle */
}
```

#### Responsive Design e Approccio Mobile-First
Progettare siti web in grado di adattarsi a qualsiasi risoluzione dello schermo (smartphone, tablet, desktop).
* **Approccio Mobile-First:** Scrivere prima lo stile base per schermi piccoli e aggiungere media queries a salire.
```css
/* Stile Base (Mobile) */
.colonna { width: 100%; }

/* Tablet e Desktop */
@media (min-width: 768px) {
    .colonna { width: 50%; }
}
@media (min-width: 1024px) {
    .colonna { width: 33.33%; }
}
```

#### Pseudo-elementi e Transizioni
* **Pseudo-elementi:** `::before` e `::after` per inserire elementi decorativi via CSS.
* **Transizioni CSS:**
```css
.btn {
    background-color: #007bff;
    transition: background-color 0.3s ease, transform 0.2s ease;
}
.btn:hover {
    background-color: #0056b3;
    transform: translateY(-2px);
}
```

---

## Modulo 3: Comportamento Dinamico con JavaScript

### Parte 1: Sintassi, Fondamenti e Strutture Dati

#### Sintassi, Variabili e Tipi di Dato
JavaScript è il linguaggio di programmazione dinamico del Web.
* **Dichiarazione Variabili:**
  * `const`: Dichiarazione di valori costanti (non riassegnabili). Scelta predefinita.
  * `let`: Dichiarazione di variabili con scope di blocco riassegnabili.
  * `var`: Sintassi legacy (da evitare nello sviluppo moderno).
* **Tipi di Dato Primari:** `string`, `number`, `boolean`, `null`, `undefined`, `symbol`, `bigint`.

#### Operatori e Strutture di Controllo
* **Operatori di Confronto:** Usare sempre l'uguaglianza stretta `===` e disuguaglianza stretta `!==` (evita la conversione implicita di tipo di `==`).
* **Condizionali:**
```javascript
if (eta >= 18) {
    console.log("Utente maggiorenne");
} else {
    console.log("Utente minorenne");
}
```
* **Cicli:** Ciclo `for`, `while`, `for...of`.

#### Funzioni
```javascript
// Dichiarazione tradizionale
function somma(a, b) {
    return a + b;
}

// Arrow Function (ES6)
const moltiplica = (a, b) => a * b;
```

#### Array e Oggetti
* **Oggetti:**
```javascript
const utente = {
    nome: "Anna",
    ruolo: "Developer",
    attivo: true
};
```
* **Metodi Principali degli Array:**
  * `forEach`: Esegue una funzione per ogni elemento.
  * `map`: Crea un nuovo array trasformando ogni elemento.
  * `filter`: Ritorna un nuovo array contenente solo gli elementi che soddisfano una condizione.

```javascript
const numeri = [1, 2, 3, 4, 5];
const pari = numeri.filter(n => n % 2 === 0); // [2, 4]
const doppi = numeri.map(n => n * 2); // [2, 4, 6, 8, 10]
```

---

### Parte 2: Manipolazione DOM, Eventi e Validazione Form

#### Selezione e Manipolazione degli Elementi
```javascript
const titolo = document.querySelector("#main-title");
const bottoni = document.querySelectorAll(".btn");

// Modifica contenuto
titolo.textContent = "Nuovo Titolo Dinamico";

// Modifica classi e stili
titolo.classList.add("evidenziato");
titolo.style.color = "blue";
```

#### Event Listener e Gestione Interazioni
```javascript
const form = document.querySelector("#form-contatti");

form.addEventListener("submit", (event) => {
    event.preventDefault(); // Blocca l'invio nativo e il ricaricamento della pagina
    
    const emailInput = document.querySelector("#email");
    if (emailInput.value.trim() === "") {
        alert("Inserisci un'indirizzo email valido!");
    } else {
        console.log("Form inviato con successo:", emailInput.value);
    }
});
```

#### Validazione Dinamica lato Client con Feedback Visivo
Consiste nell'ascoltare l'evento `input` o `blur` sugli elementi del form, verificare la correttezza dei dati (es. tramite Regex) e mostrare messaggi di errore personalizzati manipolando classi CSS di errore/successo.

---

### Parte 3: ES6+ Avanzato, Asincronia (Fetch API) e Backend

#### Feature Moderne ES6+
* **Template Literals:** `${espressione}` per la concatenazione di stringhe pulita.
```javascript
const messaggio = `Benvenuto ${utente.nome}, il tuo ruolo è ${utente.ruolo}.`;
```
* **Destructuring Assignment:**
```javascript
const { nome, ruolo } = utente;
const [primo, secondo] = numeri;
```
* **Operator Spread / Rest (`...`):**
```javascript
const copiaArray = [...numeri, 6, 7];
```

#### Asincronia: Fetch API, JSON e Gestione Errori
La `Fetch API` consente di effettuare richieste di rete asincrone senza ricaricare la pagina (AJAX).
```javascript
async function caricaDatiEsterni() {
    try {
        const response = await fetch("https://jsonplaceholder.typicode.com/users");
        if (!response.ok) {
            throw new Error(`Errore HTTP: ${response.status}`);
        }
        const utenti = await response.json();
        console.log("Utenti ricevuti:", utenti);
    } catch (error) {
        console.error("Si è verificato un errore:", error.message);
    }
}
```

#### Panoramica sull'Integrazione Backend (PHP/Database)
* **Architettura Client-Server:** Il frontend (HTML/CSS/JS) invia dati tramite HTTP (`GET`, `POST`, `PUT`, `DELETE`) e riceve risposte tipicamente in formato `JSON`.
* **Ruolo del Backend:** Linguaggi come PHP elaborano le richieste, eseguono controlli di sicurezza lato server e interagiscono con un Database (es. MySQL/PostgreSQL) per la persistenza dei dati.

---

## Progetto Finale Integrato

### Panoramica del Progetto
Il progetto finale ha l'obiettivo di consolidare tutte le competenze acquisite durante il corso attraverso la creazione di un'applicazione web completa e funzionante.

### Requisiti del Progetto
1. **Struttura HTML5 Semantica:** Uso corretto di header, nav, main, section, article, footer, form e accessibilità base.
2. **Design CSS Responsive:** Layout realizzato con Flexbox/Grid, media queries mobile-first e stile grafico curato.
3. **Interattività JavaScript:**
   * Manipolazione dinamica del DOM.
   * Validazione dinamica avanzata dei form con feedback visivo d'errore/successo.
   * Integrazione asincrona tramite `fetch()` con un'API pubblica per mostrare e filtrare dati dinamici.
4. **Workflow di Consegna:** Codice pulito, commentato, organizzato secondo le convenzioni di naming e testato con i DevTools.
