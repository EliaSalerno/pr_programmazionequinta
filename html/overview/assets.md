# Cosa si trova di solito nella cartella `assets/`

La cartella `assets/` è una convenzione (non uno standard rigido) usata in quasi tutti i progetti web per raccogliere tutte le **risorse statiche** del progetto, separandole dal codice logico (HTML, JS, componenti).

## Contenuto tipico

**Immagini** (`assets/images/` o `assets/img/`)
- Loghi, icone, foto, illustrazioni
- Formati: `.png`, `.jpg`, `.svg`, `.webp`, `.gif`

**Fogli di stile** (`assets/css/` o `assets/styles/`)
- File `.css` o preprocessori (`.scss`, `.sass`, `.less`)

**Script** (`assets/js/`)
- File JavaScript non gestiti da un bundler, librerie esterne locali

**Font** (`assets/fonts/`)
- File `.woff`, `.woff2`, `.ttf`, `.otf` per font personalizzati

**Icone** (`assets/icons/`)
- Spesso SVG separati dalle immagini generiche, usati come icon set

**Media** (`assets/media/` o `assets/videos/`, `assets/audio/`)
- Video, audio, animazioni (es. Lottie `.json`)

**Dati statici** (a volte)
- File `.json`, `.csv` con dati fissi non generati dinamicamente

## Esempio di struttura tipica

```
project/
├── assets/
│   ├── images/
│   │   ├── logo.svg
│   │   └── hero-banner.jpg
│   ├── fonts/
│   │   └── OpenSans-Regular.woff2
│   ├── css/
│   │   └── main.css
│   ├── js/
│   │   └── vendor.js
│   └── icons/
│       └── icon-set.svg
├── index.html
└── src/
```

## Perché si usa questa convenzione

- **Separazione delle responsabilità**: distingue chiaramente "risorse" da "logica applicativa"
- **Build tools**: framework come React, Vue, Angular spesso hanno una cartella `src/assets/` che viene processata dal bundler (Webpack, Vite), mentre una cartella `public/assets/` contiene file serviti "as-is" senza elaborazione
- **Caching**: i file statici vengono spesso cacheati diversamente dal codice applicativo

## Nota importante: `assets/` vs `public/`

In molti framework moderni (Vite, Next.js, Vue CLI) c'è una distinzione:
- **`src/assets/`**: file che vengono **processati** dal bundler (ottimizzati, hashati per il cache-busting, importati nel codice)
- **`public/`**: file serviti **direttamente** senza modifiche, con path fisso (utile per `favicon.ico`, `robots.txt`, manifest)
