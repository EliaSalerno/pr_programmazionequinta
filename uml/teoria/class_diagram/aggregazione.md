# Aggregazione nel Class Diagram

L'**aggregazione** è un tipo speciale di associazione che rappresenta una relazione **"tutto-parte"** (whole-part), ma con un vincolo debole: **la parte può esistere indipendentemente dal tutto**. Se il "tutto" viene distrutto, le parti continuano a esistere.

Si rappresenta con una linea che ha, dal lato del "tutto", un **rombo vuoto** (◇).

## Esempio: Squadra e Giocatore

```
┌────────────────┐              ┌────────────────┐
│    Squadra     │◇──────────── │   Giocatore   │
├────────────────┤     1    *   ├────────────────┤
│ + Nome: string │              │ + Nome: string │
└────────────────┘              │ + Ruolo: string│
                                └────────────────┘
```

Una `Squadra` **ha** dei `Giocatore`, ma se la squadra si scioglie, i giocatori **continuano ad esistere** — possono passare ad un'altra squadra, restare svincolati, ecc. Il giocatore non "appartiene" in modo esclusivo e vitale alla squadra.

## In C#

```csharp
public class Giocatore
{
    public string Nome { get; set; }
    public string Ruolo { get; set; }

    public Giocatore(string nome, string ruolo)
    {
        Nome = nome;
        Ruolo = ruolo;
    }
}

public class Squadra
{
    public string Nome { get; set; }
    public List<Giocatore> Giocatori { get; set; } = new List<Giocatore>();

    public Squadra(string nome)
    {
        Nome = nome;
    }

    public void AggiungiGiocatore(Giocatore giocatore)
    {
        Giocatori.Add(giocatore);
    }
}
```

Nota come i `Giocatore` vengono **creati esternamente** (`new Giocatore(...)`) e poi semplicemente "aggiunti" alla squadra. Se elimino l'oggetto `Squadra`, gli oggetti `Giocatore` referenziati altrove nel programma restano perfettamente validi — non vengono distrutti insieme alla squadra.

## Differenza chiave con la Composizione

Questo è il punto che genera più confusione, quindi vale la pena il confronto diretto:

| | Aggregazione (◇ vuoto) | Composizione (◆ pieno) |
|---|---|---|
| Vincolo di vita | La parte **sopravvive** al tutto | La parte **muore** con il tutto |
| Esempio | `Squadra` ◇— `Giocatore` | `Casa` ◆— `Stanza` |
| Analogia | Un giocatore può cambiare squadra | Una stanza non esiste senza la casa che la contiene |
| In codice | L'oggetto "parte" è passato/referenziato dall'esterno | L'oggetto "parte" è creato e distrutto internamente dal "tutto" |

Un esempio di **composizione** per contrasto:

```csharp
public class Casa
{
    private List<Stanza> stanze = new List<Stanza>();

    public Casa()
    {
        // le Stanze vengono create QUI, internamente, non passate da fuori
        stanze.Add(new Stanza("Cucina"));
        stanze.Add(new Stanza("Camera"));
    }
}
```

Se elimino l'oggetto `Casa`, le `Stanza` create al suo interno non hanno più motivo di esistere e vengono eliminate insieme ad essa (garbage collection in C#, ma concettualmente è questo il senso).
