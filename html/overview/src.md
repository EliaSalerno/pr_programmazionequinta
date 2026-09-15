# Cosa si trova di solito nella cartella `src/`

`src/` (abbreviazione di **"source"**, sorgente) contiene tutto il **codice sorgente** dell'applicazione, cioè la logica vera e propria del progetto — a differenza di `assets/` che contiene solo risorse statiche.

## Contenuto tipico (progetto con framework: React, Vue, Angular...)

```
src/
├── components/       ← componenti riutilizzabili (Button, Navbar, Card...)
├── pages/ (o views/) ← le "pagine" dell'app (Home, About, Contact...)
├── assets/           ← immagini/font/css usati SOLO dal codice, processati dal bundler
├── styles/           ← CSS/SCSS globali
├── hooks/            ← (React) funzioni custom con logica riutilizzabile
├── utils/ (o helpers/) ← funzioni di supporto generiche
├── services/ (o api/) ← chiamate HTTP, logica di comunicazione col backend
├── store/            ← gestione dello stato globale (Redux, Vuex, Pinia...)
├── router/           ← configurazione delle rotte/navigazione
├── types/            ← (TypeScript) definizioni di tipi/interfacce
├── context/           ← (React) Context API
├── App.jsx (o .vue)  ← componente radice dell'applicazione
└── main.jsx (o index.js) ← punto di ingresso, "monta" l'app nel DOM
```

## Esempio concreto — progetto React con Vite

```
project/
├── public/
│   └── index.html
├── src/
│   ├── components/
│   │   ├── Header.jsx
│   │   └── Footer.jsx
│   ├── pages/
│   │   ├── Home.jsx
│   │   └── About.jsx
│   ├── assets/
│   │   └── logo.png
│   ├── styles/
│   │   └── global.css
│   ├── App.jsx
│   └── main.jsx
├── package.json
└── vite.config.js
```

## Il file più importante: `main.jsx` / `index.js`

È il vero "punto di ingresso" del codice JavaScript. Collega l'app React/Vue al DOM dentro `index.html`:

```javascript
// src/main.jsx
import React from 'react';
import ReactDOM from 'react-dom/client';
import App from './App';

ReactDOM.createRoot(document.getElementById('root')).render(<App />);
```

## Differenza chiave: `src/` vs progetto senza build tool

- **Senza bundler** (HTML/CSS/JS puro): di solito non esiste `src/`, tutto sta nella root o in cartelle semplici come `js/`, `css/`
- **Con bundler** (React, Vue, Angular): `src/` contiene il codice "grezzo" che viene **trasformato** (compilato, minificato, ottimizzato) e finisce in una cartella `dist/` o `build/` pronta per la produzione

```
src/     → codice sorgente (quello su cui lavori)
   ↓ (build/compilazione)
dist/    → codice finale ottimizzato (quello che va online)
```

# VANILLA

# `src/` in un progetto Vanilla (senza framework)

In un progetto **vanilla** (HTML/CSS/JS puro, senza React/Vue/Angular), la cartella `src/` è **più semplice** e spesso opzionale — molti piccoli progetti non ce l'hanno nemmeno e mettono tutto in `js/` o nella root.

## Quando ha senso usare `src/`

Se il progetto è abbastanza grande da avere un build tool (Vite, Webpack, Parcel) anche senza framework, `src/` separa il codice sorgente da ciò che verrà generato in `dist/`.

## Struttura tipica

```
project/
├── index.html
├── src/
│   ├── js/
│   │   ├── main.js          ← punto di ingresso
│   │   ├── modules/
│   │   │   ├── navbar.js
│   │   │   ├── slider.js
│   │   │   └── api.js       ← chiamate fetch/AJAX
│   │   └── utils.js         ← funzioni di supporto
│   ├── css/
│   │   ├── main.css
│   │   ├── reset.css
│   │   └── variables.css
│   └── assets/
│       ├── images/
│       └── fonts/
├── dist/                     ← generato dal build (se usi un bundler)
└── package.json              ← se usi npm/bundler
```

## Esempio pratico con moduli ES6

```javascript
// src/js/modules/navbar.js
export function initNavbar() {
  const nav = document.querySelector('.navbar');
  nav.addEventListener('click', () => {
    nav.classList.toggle('open');
  });
}
```

```javascript
// src/js/main.js
import { initNavbar } from './modules/navbar.js';
import { initSlider } from './modules/slider.js';

document.addEventListener('DOMContentLoaded', () => {
  initNavbar();
  initSlider();
});
```

```html
<!-- index.html -->
<script type="module" src="src/js/main.js"></script>
```

## Vanilla semplice (senza bundler, senza `src/`)

Per progetti piccoli, è comune **non avere `src/` affatto** e usare una struttura piatta:

```
project/
├── index.html
├── css/
│   └── style.css
├── js/
│   └── script.js
└── assets/
    └── images/
```

## Quando conviene ciascuna scelta

| Situazione | Struttura consigliata |
|---|---|
| Sito piccolo, 1-2 pagine, no build tool | `css/`, `js/`, `assets/` nella root |
| Sito medio/grande, JS modulare (`import`/`export`) | `src/js/modules/`, `src/css/` |
| Usi Vite/Webpack anche senza framework | `src/` con build verso `dist/` |
