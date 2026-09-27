# Esercitazioni HTML puro (senza CSS) — con spiegazioni degli attributi

Tag trattati: `body`, `h1`, `p`, `a`, `img`, `ul`, `ol`, `li`

> Nota: `class` non viene usata perché senza CSS non ha alcun effetto. `id` viene usato solo per creare ancore interne (link `#nome`).

---

## body

**Attributi usati e spiegazione**
- `lang="it"` — indica la lingua principale del contenuto della pagina.
- `title="..."` — testo che appare come tooltip al passaggio del mouse.
- `bgcolor="#f0f0f0"` *(obsoleto)* — colore di sfondo della pagina.
- `text="navy"` *(obsoleto)* — colore del testo della pagina.
- `link="green"` *(obsoleto)* — colore dei link non ancora visitati.
- `vlink="purple"` *(obsoleto)* — colore dei link già visitati.
- `background="sfondo.jpg"` *(obsoleto)* — immagine usata come sfondo della pagina.
- `marginwidth` / `marginheight` *(obsoleti)* — margini orizzontali/verticali della pagina.
- `dir="rtl"` — direzione del testo (right-to-left, da destra a sinistra); il valore opposto è `ltr`.

**Esercizi**
1. Aggiungi `lang="it"` e `title="Esercitazione"` al body.
2. Prova `bgcolor="#f0f0f0"` e `text="navy"` e osserva l'effetto.
3. Prova `link="green"` e `vlink="purple"` e osserva i colori dei link.
4. Aggiungi `background="sfondo.jpg"` e osserva l'immagine di sfondo.
5. Prova `marginwidth="50"` e `marginheight="50"`.
6. Aggiungi `dir="rtl"` al body e osserva come cambia l'allineamento generale del testo.

---

## h1

**Attributi usati e spiegazione**
- `id="inizio"` — identificatore univoco dell'elemento; permette di raggiungerlo con un link tipo `href="#inizio"`.
- `title="..."` — tooltip descrittivo al passaggio del mouse.
- `align="center"` *(obsoleto)* — allineamento orizzontale del testo (center, left, right, justify).
- `lang="en"` — lingua specifica di quel singolo elemento, diversa dal resto della pagina.
- `tabindex="0"` — inserisce l'elemento nell'ordine di navigazione tramite tasto Tab (di norma i titoli non sono navigabili con Tab: questo attributo lo rende possibile).
- `accesskey="h"` — assegna una scorciatoia da tastiera per attivare/selezionare l'elemento (es. Alt+H).
- `data-sezione="intro"` — attributo personalizzato per memorizzare informazioni extra, leggibile con gli strumenti di sviluppo o con JavaScript.

**Esercizi**
7. Titolo con `id="inizio"` e `title="Benvenuto"`: osserva il tooltip.
8. Prova `align="center"` e poi `align="right"`.
9. Metti `lang="en"` su un h1 scritto in inglese.
10. Aggiungi `tabindex="0"` e prova a raggiungerlo con il tasto Tab.
11. Aggiungi `accesskey="h"` e prova la scorciatoia da tastiera (es. Alt+H).
12. Aggiungi `data-sezione="intro"` e verificalo con gli strumenti di sviluppo.

---

## p

**Attributi usati e spiegazione**
- `id="par1"` — identificatore univoco, usato per creare un'ancora interna.
- `title="..."` — tooltip descrittivo.
- `hidden` — nasconde completamente l'elemento nella pagina (non produce output visibile).
- `lang="fr"` — lingua specifica di quel paragrafo.
- `align="justify"` *(obsoleto)* — allinea il testo su entrambi i margini (giustificato).
- `contenteditable="true"` — rende il testo dell'elemento modificabile direttamente nel browser (senza salvare le modifiche).
- `spellcheck="true"` — attiva il controllo ortografico del browser sul testo modificabile.
- `translate="no"` — indica ai traduttori automatici del browser di non tradurre quel testo (utile per nomi propri o termini tecnici).
- `dir="rtl"` — direzione del testo, applicata a un singolo paragrafo.
- `draggable="true"` — rende l'elemento trascinabile con il mouse (drag and drop).

**Esercizi**
13. Tre paragrafi con `id="par1"`, `id="par2"`, `id="par3"`, e in cima tre link (`href="#par1"`, ecc.) che portano a ciascuno.
14. Un paragrafo con `title` e uno con `hidden`.
15. `lang="fr"` su un paragrafo in francese.
16. `align="justify"` su un testo lungo.
17. `contenteditable="true"` su un paragrafo: modifica il testo nel browser.
18. `spellcheck="true"` su un paragrafo modificabile e scrivi una parola sbagliata.
19. `translate="no"` su un paragrafo con un nome proprio o un termine tecnico.
20. `dir="rtl"` su un singolo paragrafo (diverso dal resto della pagina).
21. `draggable="true"` su un paragrafo: prova a trascinarlo con il mouse.

---

## a

**Attributi usati e spiegazione**
- `href="https://..."` — indirizzo di destinazione del link (obbligatorio perché il link funzioni).
- `target="_blank"` — apre il link in una nuova scheda/finestra.
- `rel="noopener noreferrer"` — quando usato con `target="_blank"`: `noopener` impedisce alla nuova pagina di accedere via script alla pagina di origine; `noreferrer` fa lo stesso e in più nasconde al sito di destinazione da dove arriva l'utente.
- `href="#sezione2"` — link "ancora": porta a un elemento della stessa pagina che ha `id="sezione2"`.
- `title="..."` — tooltip descrittivo.
- `download` — invita il browser a scaricare il file collegato invece di aprirlo.
- `href="mailto:..."` — apre il programma di posta predefinito per scrivere a quell'indirizzo.
- `href="tel:..."` — su dispositivi con funzione telefono, avvia una chiamata al numero indicato.
- `hreflang="en"` — indica la lingua della risorsa/pagina di destinazione (non della pagina corrente).
- `type="application/pdf"` — indica il tipo MIME del file collegato, così il browser sa cosa aspettarsi.
- `referrerpolicy="no-referrer"` — impedisce l'invio dell'informazione "da dove arriva l'utente" al sito di destinazione.
- `ping="https://..."` — invia automaticamente una richiesta di notifica all'indirizzo indicato quando il link viene cliccato (usato per tracciamento).
- `accesskey="c"` — scorciatoia da tastiera per attivare il link.

**Esercizi**
22. Link esterno: `href="https://..."` con `target="_blank"`.
23. Aggiungi `rel="noopener noreferrer"` e spiega perché serve.
24. Ancora interna: `href="#sezione2"` verso un elemento con `id="sezione2"`.
25. Link con `title` e link con `download`.
26. Link `mailto:` e link `tel:`.
27. Link a un altro file della tua cartella (`href="pagina2.html"`) e ritorno alla prima pagina.
28. Aggiungi `hreflang="en"` su un link che porta a una pagina in inglese.
29. Aggiungi `type="application/pdf"` su un link che scarica un PDF.
30. Prova `referrerpolicy="no-referrer"` su un link esterno.
31. Aggiungi `ping="https://esempio.com/log"` e osserva (con gli strumenti di sviluppo) la richiesta inviata al click.
32. Aggiungi `accesskey="c"` a un link di navigazione.

---

## img

**Attributi usati e spiegazione**
- `src="..."` — percorso o indirizzo dell'immagine da mostrare (obbligatorio).
- `alt="..."` — testo alternativo, mostrato se l'immagine non può essere caricata e letto dai lettori per non vedenti.
- `width` / `height` — larghezza e altezza dell'immagine, in pixel.
- `title="..."` — tooltip descrittivo.
- `loading="lazy"` — ritarda il caricamento dell'immagine finché non sta per entrare nello schermo (migliora le prestazioni su pagine lunghe).
- `border="2"` *(obsoleto)* — spessore del bordo attorno all'immagine.
- `align="left"` *(obsoleto)* — allinea l'immagine a sinistra o a destra, con il testo che le scorre attorno.
- `hspace` / `vspace` *(obsoleti)* — spazio vuoto orizzontale/verticale attorno all'immagine.
- `srcset="..."` — elenco di versioni della stessa immagine a risoluzioni diverse, tra cui il browser sceglie in base allo schermo.
- `sizes="..."` — indica al browser quanto spazio occuperà l'immagine, aiutandolo a scegliere la versione giusta da `srcset`.
- `usemap="#mappa1"` — collega l'immagine a una mappa cliccabile definita con `<map>`.
- `ismap` — indica che l'immagine, se dentro un link, è una mappa server-side (le coordinate del click vengono inviate al server).
- `decoding="async"` — suggerisce al browser di decodificare l'immagine in modo asincrono, senza bloccare il resto della pagina.
- `crossorigin="anonymous"` — gestisce il caricamento di immagini da altri domini rispetto alla pagina.
- `data-autore="..."` — attributo personalizzato per aggiungere informazioni extra (es. l'autore della foto).

**Esercizi**
33. Immagine con `src`, `alt`, `width` e `height`.
34. Sbaglia il `src` e osserva l'`alt`.
35. Aggiungi `title` e `loading="lazy"`.
36. Prova `border="2"` e `align="left"` con un paragrafo accanto.
37. Immagine cliccabile: `<a href="..."><img ...></a>`.
38. Aggiungi `hspace="20"` e `vspace="10"` e osserva la spaziatura.
39. Usa `srcset` con due versioni della stessa immagine (piccola e grande) e `sizes` per scegliere quale caricare.
40. Crea una mappa immagine: `usemap="#mappa1"` sull'img e un tag `<map name="mappa1">` con delle `<area>` cliccabili.
41. Prova `ismap` su un'immagine dentro un link (richiede un server, va solo spiegato/osservato in teoria).
42. Aggiungi `decoding="async"` e `crossorigin="anonymous"`.
43. Aggiungi `data-autore="Mario Rossi"` e verificalo con gli strumenti di sviluppo.

---

## ul / ol / li

**Attributi usati e spiegazione**
- `type="circle"` / `"square"` *(obsoleti su `ul`)* — cambia la forma del pallino della lista puntata.
- `type="A"` / `"a"` / `"I"` / `"i"` (su `ol`) — cambia il tipo di numerazione: lettere maiuscole, minuscole, numeri romani maiuscoli o minuscoli.
- `start="5"` (su `ol`) — indica da quale numero iniziare la numerazione.
- `reversed` (su `ol`) — inverte l'ordine della numerazione (dall'alto verso il basso, decrescente).
- `value="10"` (su `li`) — assegna manualmente un numero a quell'elemento della lista, e i successivi continuano da lì.
- `compact` *(obsoleto)* — riduceva la spaziatura verticale tra gli elementi della lista.
- `data-categoria="frutta"` (su `li`) — attributo personalizzato per etichettare ogni elemento della lista.

**Esercizi**
44. Lista puntata di 5 elementi.
45. `ul` con `type="circle"` e poi `type="square"`.
46. `ol` con `type="A"`, `"a"`, `"I"`, `"i"`.
47. `ol` con `start="5"` e un altro con `reversed`.
48. `li` con `value="10"` dentro un `ol`: osserva la numerazione.
49. Liste annidate: un `ul` dentro un `li` di un `ol`.
50. Menu di navigazione: `ul` con `li` che contengono `a`.
51. Prova `compact` su un `ol` (effetto minimo nei browser moderni).
52. Aggiungi `data-categoria="frutta"` su ogni `li` di una lista e verificalo con gli strumenti di sviluppo.

---

## Esercizio finale

Crea una pagina "La mia città" con:

- `body` con `lang="it"` e `dir="ltr"`
- `h1` con `id="inizio"` e `title`
- due `p`, uno dei quali con `contenteditable="true"`
- un'`img` con `alt`, `width`, `height` e `srcset` per due risoluzioni
- un `ul` di luoghi da visitare, con link esterni (`target="_blank"`, `rel="noopener noreferrer"`)
- un `ol` con la classifica dei luoghi preferiti (`start` o `reversed` a scelta)
- un indice in cima con ancore interne verso le sezioni della pagina
- almeno un attributo `data-*` personalizzato, usato su un elemento a scelta
- in fondo un link "Torna su" (`href="#inizio"`)

---

## Riepilogo: attributi globali (validi su qualsiasi tag)

- `id` — identificatore univoco dell'elemento nella pagina.
- `title` — tooltip descrittivo al passaggio del mouse.
- `lang` — lingua del contenuto di quell'elemento.
- `dir` — direzione del testo (`ltr` o `rtl`).
- `hidden` — nasconde completamente l'elemento.
- `tabindex` — inserisce/esclude l'elemento dall'ordine di navigazione con Tab.
- `accesskey` — scorciatoia da tastiera per raggiungere/attivare l'elemento.
- `draggable` — rende l'elemento trascinabile con il mouse.
- `spellcheck` — attiva/disattiva il controllo ortografico del browser.
- `translate` — indica se il contenuto va tradotto automaticamente.
- `contenteditable` — rende il contenuto modificabile direttamente nel browser.
- `data-*` — attributo personalizzato per aggiungere informazioni extra all'elemento.

## Note finali

- **Obsoleti** (funzionano ma sconsigliati in HTML5, da sostituire in futuro con CSS): `bgcolor`, `text`, `link`, `vlink`, `background`, `marginwidth`, `marginheight`, `align`, `border`, `hspace`, `vspace`, `type` su `ul`, `compact`.
- **Richiedono JavaScript per essere davvero osservati a fondo**: `draggable`, `ping` (visibile solo con gli strumenti di sviluppo), `data-*` (leggibile via JS, ma osservabile anche negli strumenti di sviluppo).
- **Utili anche in puro HTML**: `dir`, `lang`, `hidden`, `contenteditable`, `spellcheck`, `translate`, `srcset`, `sizes`, `usemap`, `hreflang`, `download`, `rel`, `title`, `accesskey`.
