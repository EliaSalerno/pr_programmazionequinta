# Composizione nel Class Diagram

La **composizione** è un tipo speciale di associazione (come l'aggregazione) che rappresenta una relazione **"tutto-parte"** (whole-part), ma con un vincolo **forte**: **la parte non può esistere senza il tutto**. Se l'oggetto "tutto" viene distrutto, anche le sue parti vengono distrutte con esso.

È una relazione di **appartenenza esclusiva**: ogni "parte" appartiene a **un solo** "tutto" alla volta, e il suo ciclo di vita è completamente dipendente da esso.

## Notazione grafica

Si rappresenta con una linea che ha, dal lato del "tutto", un **rombo pieno** (◆).

```
┌─────────────────────┐              ┌──────────────────────┐
│         Casa        │◆────────────│        Stanza         │
├─────────────────────┤     1    *   ├──────────────────────┤
│ + Indirizzo: string │              │ + Nome: string       │
└─────────────────────┘              │ + Superficie: double │
                                     └──────────────────────┘
```

Una `Casa` **è composta da** una o più `Stanza`. Le stanze non hanno senso di esistere separatamente dalla casa: se demolisco la casa, le stanze smettono di esistere insieme ad essa.

## Esempio in C#

La caratteristica chiave della composizione, a livello di codice, è che l'oggetto "tutto" **crea e gestisce internamente** il ciclo di vita delle sue "parti" — non le riceve dall'esterno.

```csharp
public class Stanza
{
    public string Nome { get; set; }
    public double Superficie { get; set; }

    // Costruttore accessibile solo internamente al progetto,
    // enfatizza che la Stanza nasce "dentro" la Casa
    public Stanza(string nome, double superficie)
    {
        Nome = nome;
        Superficie = superficie;
    }
}

public class Casa
{
    public string Indirizzo { get; set; }

    // Le Stanze sono create e possedute internamente dalla Casa
    private readonly List<Stanza> stanze = new List<Stanza>();

    public Casa(string indirizzo)
    {
        Indirizzo = indirizzo;

        // Creazione interna: le parti nascono con il tutto
        stanze.Add(new Stanza("Cucina", 15.5));
        stanze.Add(new Stanza("Camera da letto", 20.0));
        stanze.Add(new Stanza("Bagno", 6.0));
    }

    public IReadOnlyList<Stanza> Stanze => stanze.AsReadOnly();

    public void AggiungiStanza(string nome, double superficie)
    {
        // Anche se aggiunta dopo, la Stanza viene comunque creata "dentro" la Casa
        stanze.Add(new Stanza(nome, superficie));
    }
}
```

### Utilizzo

```csharp
Casa casaRossi = new Casa("Via Roma 10");

foreach (var stanza in casaRossi.Stanze)
{
    Console.WriteLine($"{stanza.Nome}: {stanza.Superficie} m²");
}

// Se casaRossi viene eliminata (es. esce dallo scope, garbage collection),
// anche le sue Stanze non sono più referenziabili da nessuna parte:
// non esistono "fuori" dalla Casa che le conteneva.
```

Da notare due dettagli che rinforzano il concetto:
- Il campo `stanze` è **privato** e viene esposto solo in sola lettura (`IReadOnlyList`), impedendo a codice esterno di gestire direttamente le stanze
- Non esiste alcun modo, dall'esterno, di creare una `Stanza` "libera" e poi assegnarla a una casa diversa — nasce già legata alla sua `Casa`

## Differenza con l'aggregazione (confronto rapido)

| | Composizione (◆ pieno) | Aggregazione (◇ vuoto) |
|---|---|---|
| Vincolo di vita | La parte **muore** con il tutto | La parte **sopravvive** al tutto |
| Chi crea la parte | Il "tutto" stesso, internamente | Un soggetto esterno, poi assegnata al tutto |
| Esempio | `Casa` ◆— `Stanza` | `Squadra` ◇— `Giocatore` |
| Analogia | Una stanza non ha senso fuori dalla casa | Un giocatore può cambiare squadra |
| Molteplicità tipica dal lato "parte" | Spesso la parte appartiene a **un solo** tutto | La parte può essere condivisa tra più "tutti" |

## Riepilogo delle relazioni strutturali nel class diagram

| Relazione | Simbolo | Significato |
|---|---|---|
| Associazione | linea semplice | Una classe usa/referenzia un'altra |
| Aggregazione | ◇ rombo vuoto | Tutto-parte, la parte sopravvive |
| **Composizione** | **◆ rombo pieno** | **Tutto-parte, la parte muore con il tutto** |
| Generalizzazione | △ triangolo vuoto, linea continua | Ereditarietà tra classi |
| Realizzazione | △ triangolo vuoto, linea tratteggiata | Implementazione di un'interfaccia |
