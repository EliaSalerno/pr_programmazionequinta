# Guida Completa a HTML5 (da zero)

## Indice
1. [Cos'è HTML](#1-cosè-html)
2. [Come iniziare](#2-come-iniziare)
3. [Struttura base di un documento HTML](#3-struttura-base-di-un-documento-html)
4. [Tag, elementi e attributi](#4-tag-elementi-e-attributi)
5. [Testo e formattazione](#5-testo-e-formattazione)
6. [Liste](#6-liste)
7. [Link (collegamenti ipertestuali)](#7-link-collegamenti-ipertestuali)
8. [Immagini](#8-immagini)
9. [Tabelle](#9-tabelle)
10. [Form (moduli)](#10-form-moduli)
11. [Elementi semantici di HTML5](#11-elementi-semantici-di-html5)
12. [Div e Span](#12-div-e-span)
13. [Commenti](#13-commenti)
14. [Elementi multimediali (audio/video)](#14-elementi-multimediali-audiovideo)
15. [Attributi globali importanti](#15-attributi-globali-importanti)
16. [Collegare CSS e JavaScript](#16-collegare-css-e-javascript)
17. [Novità principali di HTML5](#17-novità-principali-di-html5)
18. [Buone pratiche](#18-buone-pratiche)
19. [Errori comuni da principiante](#19-errori-comuni-da-principiante)
20. [Prossimi passi](#20-prossimi-passi)

---

## 1. Cos'è HTML

**HTML** (HyperText Markup Language) è il linguaggio usato per **strutturare** il contenuto delle pagine web. Non è un linguaggio di programmazione: è un linguaggio di **markup**, cioè serve a "marcare" il testo indicando cosa rappresenta ogni parte (un titolo, un paragrafo, un'immagine, un link...).

Pensa a HTML come allo **scheletro** di una pagina web:
- **HTML** → struttura e contenuto (lo scheletro)
- **CSS** → aspetto e stile (i vestiti)
- **JavaScript** → comportamento e interattività (i muscoli/movimento)

**HTML5** è la quinta e attuale versione dello standard HTML, rilasciata definitivamente nel 2014 e poi evoluta come "living standard". Ha introdotto nuovi elementi semantici, supporto nativo per audio/video, e molte funzionalità che prima richiedevano plugin esterni (come Flash).

---

## 2. Come iniziare

Per scrivere HTML non serve installare nulla di complesso:

1. **Un editor di testo**: consigliato [Visual Studio Code](https://code.visualstudio.com/) (gratuito)
2. **Un browser**: Chrome, Firefox, Edge... per vedere il risultato
3. Crea un file con estensione `.html` (es. `index.html`) e aprilo con il browser

Non serve un server, un compilatore o installazioni particolari: scrivi il file e lo apri direttamente nel browser per vedere il risultato.

---

## 3. Struttura base di un documento HTML

Ogni pagina HTML5 segue questo scheletro minimo:

```html
<!DOCTYPE html>
<html lang="it">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Titolo della pagina</title>
</head>
<body>
    <h1>Ciao mondo!</h1>
    <p>Questo è il mio primo paragrafo.</p>
</body>
</html>
```

### Spiegazione riga per riga

| Riga | Significato |
|---|---|
| `<!DOCTYPE html>` | Dichiara che il documento è HTML5 (deve essere sempre la prima riga) |
| `<html lang="it">` | Elemento radice; `lang` indica la lingua della pagina (utile per accessibilità e SEO) |
| `<head>` | Contiene informazioni "invisibili" alla pagina: metadati, titolo, collegamenti a CSS |
| `<meta charset="UTF-8">` | Imposta la codifica dei caratteri (permette di usare accenti, simboli, emoji correttamente) |
| `<meta name="viewport"...>` | Rende la pagina responsive su dispositivi mobili |
| `<title>` | Il titolo mostrato nella scheda del browser |
| `<body>` | Contiene tutto ciò che è **visibile** all'utente |

---

## 4. Tag, elementi e attributi

### Tag ed elementi

Un **tag** è racchiuso tra parentesi angolari: `<p>`. Un **elemento** è composto da un tag di apertura, un contenuto, e (di solito) un tag di chiusura:

```html
<p>Questo è un paragrafo.</p>
```

- `<p>` → tag di apertura
- `Questo è un paragrafo.` → contenuto
- `</p>` → tag di chiusura (nota lo slash `/`)

### Elementi vuoti (self-closing)

Alcuni elementi non hanno contenuto e non necessitano di chiusura:

```html
<br>       <!-- Interruzione di riga -->
<hr>       <!-- Linea orizzontale -->
<img src="foto.jpg" alt="Descrizione">
<input type="text">
```

### Attributi

Gli **attributi** forniscono informazioni aggiuntive su un elemento e si scrivono sempre nel tag di apertura, nella forma `nome="valore"`:

```html
<a href="https://esempio.com" target="_blank">Vai al sito</a>
```

- `href` → attributo che specifica la destinazione del link
- `target="_blank"` → attributo che apre il link in una nuova scheda

### Nidificazione (annidamento)

Gli elementi possono contenere altri elementi, ma devono essere chiusi **nell'ordine corretto** (come parentesi):

```html
<!-- CORRETTO -->
<p>Testo <strong>importante</strong> nel paragrafo.</p>

<!-- SBAGLIATO: chiusura incrociata -->
<p>Testo <strong>importante</p></strong>
```

---

## 5. Testo e formattazione

### Titoli

HTML offre 6 livelli di titolo, da `<h1>` (più importante) a `<h6>` (meno importante):

```html
<h1>Titolo principale</h1>
<h2>Sottotitolo</h2>
<h3>Sotto-sottotitolo</h3>
```

⚠️ **Regola importante**: usa un solo `<h1>` per pagina (di solito il titolo principale del contenuto) e mantieni una gerarchia logica (non saltare da `<h1>` a `<h4>` senza motivo).

### Paragrafi

```html
<p>Questo è un paragrafo di testo normale.</p>
```

### Formattazione del testo

```html
<strong>Testo importante (grassetto semantico)</strong>
<em>Testo enfatizzato (corsivo semantico)</em>
<b>Grassetto puramente visivo</b>
<i>Corsivo puramente visivo</i>
<mark>Testo evidenziato</mark>
<small>Testo piccolo</small>
<del>Testo cancellato/obsoleto</del>
<ins>Testo inserito/aggiunto</ins>
<sub>pedice</sub>
<sup>apice</sup>
```

💡 **Differenza chiave**: `<strong>` ed `<em>` hanno significato **semantico** (comunicano importanza reale, utile per screen reader e SEO), mentre `<b>` e `<i>` sono puramente visivi.

### Interruzioni

```html
<p>Prima riga<br>Seconda riga (stesso paragrafo)</p>
<hr>
```

---

## 6. Liste

### Lista non ordinata (puntata)

```html
<ul>
    <li>Mela</li>
    <li>Pera</li>
    <li>Banana</li>
</ul>
```

### Lista ordinata (numerata)

```html
<ol>
    <li>Primo passo</li>
    <li>Secondo passo</li>
    <li>Terzo passo</li>
</ol>
```

### Lista di definizioni

```html
<dl>
    <dt>HTML</dt>
    <dd>Linguaggio di markup per la struttura</dd>
    <dt>CSS</dt>
    <dd>Linguaggio per lo stile</dd>
</dl>
```

### Liste annidate

```html
<ul>
    <li>Frutta
        <ul>
            <li>Mela</li>
            <li>Pera</li>
        </ul>
    </li>
    <li>Verdura</li>
</ul>
```

---

## 7. Link (collegamenti ipertestuali)

```html
<!-- Link esterno -->
<a href="https://www.google.com">Vai a Google</a>

<!-- Link che apre in una nuova scheda -->
<a href="https://www.google.com" target="_blank" rel="noopener noreferrer">Google</a>

<!-- Link interno alla stessa pagina (ancora) -->
<a href="#sezione2">Vai alla sezione 2</a>
<h2 id="sezione2">Sezione 2</h2>

<!-- Link a un'altra pagina del sito -->
<a href="chi-siamo.html">Chi siamo</a>

<!-- Link email -->
<a href="mailto:info@esempio.com">Scrivici</a>

<!-- Link telefono -->
<a href="tel:+390212345678">Chiamaci</a>
```

📌 **Nota su `rel="noopener noreferrer"`**: quando apri un link in una nuova scheda con `target="_blank"`, è buona pratica aggiungere questo attributo per motivi di sicurezza (evita che la nuova pagina possa accedere alla finestra di origine).

---

## 8. Immagini

```html
<img src="logo.png" alt="Logo dell'azienda" width="200" height="100">
```

- `src` → percorso dell'immagine (obbligatorio)
- `alt` → testo alternativo, mostrato se l'immagine non carica e letto dagli screen reader (**obbligatorio per accessibilità**)
- `width`/`height` → dimensioni (meglio gestirle via CSS, ma utile specificarle per evitare "salti" di layout)

### Immagine con didascalia

```html
<figure>
    <img src="grafico.png" alt="Grafico vendite 2024">
    <figcaption>Fig. 1 - Andamento vendite nel 2024</figcaption>
</figure>
```

### Percorsi relativi vs assoluti

```html
<img src="assets/images/foto.jpg" alt="Foto">      <!-- relativo -->
<img src="https://esempio.com/foto.jpg" alt="Foto"> <!-- assoluto -->
```

---

## 9. Tabelle

```html
<table>
    <thead>
        <tr>
            <th>Nome</th>
            <th>Età</th>
            <th>Città</th>
        </tr>
    </thead>
    <tbody>
        <tr>
            <td>Marco</td>
            <td>28</td>
            <td>Milano</td>
        </tr>
        <tr>
            <td>Giulia</td>
            <td>34</td>
            <td>Roma</td>
        </tr>
    </tbody>
    <tfoot>
        <tr>
            <td colspan="3">Totale: 2 persone</td>
        </tr>
    </tfoot>
</table>
```

- `<table>` → contenitore della tabella
- `<thead>` → intestazione
- `<tbody>` → corpo dei dati
- `<tfoot>` → piè di tabella
- `<tr>` → riga (table row)
- `<th>` → cella di intestazione (table header)
- `<td>` → cella di dato (table data)
- `colspan`/`rowspan` → uniscono celle orizzontalmente/verticalmente

⚠️ Le tabelle vanno usate **solo per dati tabellari** (come fogli di calcolo), mai per impaginare l'intera pagina — quello è compito del CSS.

---

## 10. Form (moduli)

I form permettono all'utente di inserire dati (login, registrazione, contatti...).

```html
<form action="/invia-dati" method="POST">
    <label for="nome">Nome:</label>
    <input type="text" id="nome" name="nome" placeholder="Il tuo nome" required>

    <label for="email">Email:</label>
    <input type="email" id="email" name="email" required>

    <label for="eta">Età:</label>
    <input type="number" id="eta" name="eta" min="0" max="120">

    <label for="messaggio">Messaggio:</label>
    <textarea id="messaggio" name="messaggio" rows="4"></textarea>

    <label for="paese">Paese:</label>
    <select id="paese" name="paese">
        <option value="it">Italia</option>
        <option value="fr">Francia</option>
        <option value="de">Germania</option>
    </select>

    <input type="checkbox" id="privacy" name="privacy" required>
    <label for="privacy">Accetto la privacy policy</label>

    <input type="radio" id="uomo" name="genere" value="uomo">
    <label for="uomo">Uomo</label>
    <input type="radio" id="donna" name="genere" value="donna">
    <label for="donna">Donna</label>

    <button type="submit">Invia</button>
</form>
```

### Tipi di `input` più comuni (HTML5)

| Tipo | Uso |
|---|---|
| `text` | Testo generico |
| `email` | Valida automaticamente il formato email |
| `password` | Nasconde i caratteri digitati |
| `number` | Solo numeri, con frecce su/giù |
| `date` | Selettore data |
| `checkbox` | Casella di spunta |
| `radio` | Selezione singola tra opzioni |
| `file` | Caricamento file |
| `submit` | Pulsante di invio |
| `tel` | Numero di telefono |
| `url` | Indirizzo web |
| `range` | Slider numerico |
| `color` | Selettore colore |

💡 **`<label for="id">`** è fondamentale per l'accessibilità: collega l'etichetta al campo (cliccando sul testo si attiva l'input) e deve avere lo stesso valore dell'`id` del campo collegato.

---

## 11. Elementi semantici di HTML5

Una delle innovazioni principali di HTML5 sono gli **elementi semantici**: al posto di riempire tutto di `<div>` generici, HTML5 offre tag che descrivono il **significato** del contenuto.

```html
<body>
    <header>
        <h1>Il mio sito</h1>
        <nav>
            <a href="#">Home</a>
            <a href="#">Chi siamo</a>
            <a href="#">Contatti</a>
        </nav>
    </header>

    <main>
        <article>
            <h2>Titolo dell'articolo</h2>
            <p>Contenuto dell'articolo...</p>
            <section>
                <h3>Una sottosezione</h3>
                <p>Altro contenuto...</p>
            </section>
        </article>

        <aside>
            <p>Contenuto correlato o pubblicità</p>
        </aside>
    </main>

    <footer>
        <p>&copy; 2026 - Tutti i diritti riservati</p>
    </footer>
</body>
```

### A cosa servono

| Tag | Significato |
|---|---|
| `<header>` | Intestazione della pagina o di una sezione (logo, titolo, menu) |
| `<nav>` | Blocco di navigazione (menu principale, breadcrumb) |
| `<main>` | Contenuto principale della pagina (uno solo per pagina) |
| `<article>` | Contenuto autonomo e riutilizzabile (un post, una notizia) |
| `<section>` | Raggruppa contenuti tematicamente correlati |
| `<aside>` | Contenuto secondario, correlato ma non essenziale (sidebar) |
| `<footer>` | Piè di pagina (contatti, copyright, link social) |
| `<figure>`/`<figcaption>` | Immagine/grafico con didascalia |
| `<time>` | Data/ora leggibile sia da umani che da macchine |

### Perché usarli invece di `<div>`

1. **Accessibilità**: gli screen reader possono "saltare" direttamente a `<nav>` o `<main>`
2. **SEO**: i motori di ricerca capiscono meglio la struttura della pagina
3. **Leggibilità del codice**: capisci subito cosa fa ogni blocco senza dover leggere classi CSS

---

## 12. Div e Span

Quando nessun elemento semantico è adatto, si usano i contenitori "neutri":

```html
<!-- div: contenitore a blocco (va a capo) -->
<div class="scheda-prodotto">
    <p>Contenuto generico</p>
</div>

<!-- span: contenitore in linea (non va a capo) -->
<p>Questo è un testo con <span class="evidenziato">una parola speciale</span> dentro.</p>
```

- `<div>` → usalo per raggruppare blocchi senza un significato semantico specifico (layout, contenitori per CSS/JS)
- `<span>` → usalo per applicare stili o comportamenti a una porzione di testo **in linea**

---

## 13. Commenti

```html
<!-- Questo è un commento, non viene mostrato nella pagina -->
<p>Testo visibile</p>
<!-- 
    I commenti possono anche
    estendersi su più righe
-->
```

Utili per lasciare note nel codice o disattivare temporaneamente parti di HTML durante lo sviluppo.

---

## 14. Elementi multimediali (audio/video)

Una delle grandi novità di HTML5 è il supporto nativo per audio e video, senza bisogno di plugin come Flash.

```html
<video controls width="640" poster="anteprima.jpg">
    <source src="video.mp4" type="video/mp4">
    <source src="video.webm" type="video/webm">
    Il tuo browser non supporta il tag video.
</video>

<audio controls>
    <source src="musica.mp3" type="audio/mpeg">
    <source src="musica.ogg" type="audio/ogg">
    Il tuo browser non supporta il tag audio.
</audio>
```

- `controls` → mostra i controlli play/pausa/volume
- `<source>` multipli → il browser sceglie il formato che supporta
- Il testo dentro il tag è il messaggio di fallback per browser molto vecchi

### Iframe (contenuti incorporati)

```html
<iframe src="https://www.youtube.com/embed/XXXXX" 
        width="560" height="315" 
        allowfullscreen></iframe>
```

Usato per incorporare video YouTube, mappe Google, o altre pagine web.

---

## 15. Attributi globali importanti

Questi attributi possono essere applicati a **quasi tutti** gli elementi HTML:

```html
<p id="unico">Ha un identificatore univoco nella pagina</p>
<p class="testo-rosso testo-grande">Ha una o più classi (riutilizzabili)</p>
<p style="color: blue;">Stile inline (da evitare, meglio CSS separato)</p>
<p title="Suggerimento al passaggio del mouse">Testo</p>
<p data-utente-id="42">Attributo dati personalizzato</p>
<p contenteditable="true">Testo modificabile direttamente nel browser</p>
<p hidden>Contenuto nascosto</p>
```

| Attributo | A cosa serve |
|---|---|
| `id` | Identificatore **univoco** nella pagina (usato da CSS/JS per riferimenti puntuali) |
| `class` | Etichetta **riutilizzabile** su più elementi (usata da CSS/JS) |
| `style` | CSS applicato direttamente sull'elemento (sconsigliato, meglio file separato) |
| `title` | Tooltip mostrato al passaggio del mouse |
| `data-*` | Attributi personalizzati per memorizzare dati usati da JavaScript |
| `hidden` | Nasconde l'elemento |
| `contenteditable` | Rende il contenuto modificabile dall'utente |

**Differenza chiave `id` vs `class`**: `id` deve essere unico nella pagina (uno per elemento), `class` può essere riutilizzata su tanti elementi diversi.

---

## 16. Collegare CSS e JavaScript

### CSS

```html
<head>
    <!-- CSS esterno (consigliato) -->
    <link rel="stylesheet" href="style.css">

    <!-- CSS interno -->
    <style>
        body { font-family: Arial, sans-serif; }
    </style>
</head>
```

### JavaScript

```html
<body>
    <!-- Contenuto della pagina -->

    <!-- JS esterno, meglio prima della chiusura di </body> -->
    <script src="script.js"></script>
</body>
```

💡 Mettere `<script>` alla fine del `<body>` (o usare l'attributo `defer`) evita che il caricamento del JavaScript blocchi la visualizzazione della pagina.

```html
<script src="script.js" defer></script>
```

---

## 17. Novità principali di HTML5

Rispetto a HTML4/XHTML, HTML5 ha introdotto:

1. **Elementi semantici**: `<header>`, `<nav>`, `<main>`, `<article>`, `<section>`, `<footer>`, `<aside>`
2. **Audio e video nativi**: `<audio>`, `<video>` senza plugin
3. **Canvas**: `<canvas>` per disegnare grafica 2D via JavaScript
4. **SVG integrato**: grafica vettoriale direttamente nell'HTML
5. **Nuovi tipi di input**: `email`, `date`, `number`, `range`, `color`, ecc.
6. **API JavaScript native**: Geolocation, Local Storage, Drag and Drop, Web Workers
7. **DOCTYPE semplificato**: `<!DOCTYPE html>` invece delle lunghe dichiarazioni precedenti
8. **Attributi come `required`, `placeholder`, `autofocus`** nei form, senza bisogno di JavaScript

### Esempio Canvas (cenno)

```html
<canvas id="mioCanvas" width="200" height="100"></canvas>
<script>
    const canvas = document.getElementById('mioCanvas');
    const ctx = canvas.getContext('2d');
    ctx.fillStyle = 'blue';
    ctx.fillRect(10, 10, 150, 80);
</script>
```

---

## 18. Buone pratiche

✅ **Da fare:**
- Usa sempre `<!DOCTYPE html>` e imposta `lang` sull'`<html>`
- Usa un solo `<h1>` per pagina e rispetta la gerarchia dei titoli
- Aggiungi sempre `alt` alle immagini
- Preferisci elementi semantici a `<div>` generici quando ha senso
- Indenta il codice in modo coerente per leggibilità
- Chiudi sempre gli elementi (anche se il browser a volte "perdona" gli errori)
- Usa `id` per elementi unici, `class` per elementi ripetuti
- Separa HTML (struttura), CSS (stile) e JS (comportamento) in file distinti

❌ **Da evitare:**
- Non usare le tabelle per il layout della pagina
- Non usare `<b>`/`<i>` quando il significato è semantico (usa `<strong>`/`<em>`)
- Non abusare di `style="..."` inline
- Non annidare tag in modo scorretto (es. `<p><div>...</div></p>` — `<div>` non può stare dentro `<p>`)
- Non dimenticare il `for` nelle `<label>`

---

## 19. Errori comuni da principiante

```html
<!-- ❌ Attributo alt mancante -->
<img src="foto.jpg">

<!-- ✅ Corretto -->
<img src="foto.jpg" alt="Descrizione della foto">

<!-- ❌ Tag non chiuso -->
<p>Testo senza chiusura

<!-- ✅ Corretto -->
<p>Testo con chiusura</p>

<!-- ❌ id duplicati -->
<div id="box">Uno</div>
<div id="box">Due</div>

<!-- ✅ Corretto: usa class se si ripete -->
<div class="box">Uno</div>
<div class="box">Due</div>

<!-- ❌ Annidamento scorretto -->
<ul>
<p><li>Elemento</li></p>
</ul>

<!-- ✅ Corretto -->
<ul>
<li>Elemento</li>
</ul>
```

---

## 20. Prossimi passi

Una volta consolidate le basi di HTML5, i passaggi naturali sono:

1. **CSS** → per dare stile, colori, layout (Flexbox, Grid) alle tue pagine
2. **JavaScript** → per rendere le pagine interattive e dinamiche
3. **Accessibilità (a11y)** → approfondire attributi ARIA e best practice
4. **Responsive design** → adattare le pagine a schermi diversi (mobile, tablet, desktop)
5. **Strumenti moderni** → editor con estensioni, DevTools del browser (F12) per ispezionare il codice in tempo reale

### Esercizio pratico consigliato

Prova a creare una semplice pagina "Chi sono" con:
- Un `<header>` con il tuo nome
- Una `<nav>` con link finti (Home, Chi sono, Contatti)
- Una sezione `<main>` con una tua foto, una breve biografia e una lista dei tuoi hobby
- Un `<footer>` con i tuoi contatti

Questo esercizio ti farà usare praticamente tutti i concetti visti in questa guida.

---

*Guida creata come riferimento di studio — consultala ogni volta che hai un dubbio su un tag o una struttura HTML5.*
