# Il DOM (Document Object Model)

Il **DOM** è una rappresentazione strutturata di un documento HTML (o XML) sotto forma di **albero di oggetti**. È l'interfaccia che permette a linguaggi come JavaScript di leggere e modificare dinamicamente il contenuto, la struttura e lo stile di una pagina web.

## Concetti chiave

**Struttura ad albero**
Ogni elemento HTML diventa un "nodo" (node) nell'albero. Ad esempio:

```html
<html>
  <body>
    <h1>Titolo</h1>
    <p>Paragrafo</p>
  </body>
</html>
```

Diventa una gerarchia: `document` → `html` → `body` → `h1`, `p`.

**Tipi di nodi**
- **Element node**: i tag HTML (`<div>`, `<p>`, ecc.)
- **Text node**: il testo contenuto negli elementi
- **Attribute node**: gli attributi (`class`, `id`, `href`...)
- **Comment node**: i commenti HTML

## A cosa serve

Il DOM non è HTML in sé, ma un **modello vivo in memoria** che il browser costruisce leggendo l'HTML. Grazie a questo modello, JavaScript può:

- **Selezionare elementi**: `document.querySelector('.classe')`, `document.getElementById('id')`
- **Modificare contenuto**: `elemento.textContent = "nuovo testo"`
- **Cambiare stili**: `elemento.style.color = "red"`
- **Aggiungere/rimuovere elementi**: `document.createElement()`, `appendChild()`, `removeChild()`
- **Gestire eventi**: `elemento.addEventListener('click', funzione)`

## Un esempio pratico

```javascript
// Seleziona un elemento
const titolo = document.querySelector('h1');

// Modifica il testo
titolo.textContent = "Nuovo titolo";

// Aggiunge una classe CSS
titolo.classList.add('evidenziato');

// Crea un nuovo elemento e lo inserisce nella pagina
const nuovoParagrafo = document.createElement('p');
nuovoParagrafo.textContent = "Sono stato aggiunto dinamicamente!";
document.body.appendChild(nuovoParagrafo);
```

## Perché è importante

Il DOM è ciò che rende le pagine web **interattive**: senza di esso, JavaScript non avrebbe modo di "vedere" o cambiare cosa c'è sullo schermo dopo che la pagina è stata caricata. È alla base di ogni framework moderno (React, Vue, Angular), anche se questi spesso usano tecniche come il **Virtual DOM** per ottimizzare le performance, evitando di manipolare il DOM reale troppo frequentemente (operazione relativamente costosa).

