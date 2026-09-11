# Class Diagram UML e Classi in C#

Il class diagram UML è stato pensato per modellare classi di linguaggi object-oriented come C#, Java, ecc. La corrispondenza tra i due è quasi 1:1.

## Corrispondenza diretta

| Elemento in C# | Elemento nel Class Diagram UML |
|---|---|
| `public class Cliente` | Rettangolo con nome `Cliente` |
| `public int Id { get; set; }` | Attributo: `+ Id: int` |
| `public string Nome { get; set; }` | Attributo: `+ Nome: string` |
| `public List<Ordine> Ordini` | Associazione 1-a-molti verso `Ordine` |
| `public decimal CalcolaTotaleSpeso()` | Metodo: `+ CalcolaTotaleSpeso(): decimal` |
| Modificatore `public` | Visibilità `+` (public) nel diagramma |
| Modificatore `private` / `protected` | Visibilità `-` / `#` |

Il rettangolo del class diagram è diviso in tre sezioni: **nome della classe**, **attributi**, **metodi** — esattamente le tre parti riconoscibili anche nel codice C# (dichiarazione, proprietà, metodi).

## Esempio di classi in C#

```csharp
public class Cliente
{
    // Attributi
    public int Id { get; set; }
    public string Nome { get; set; }
    public string Email { get; set; }

    // Associazione 1-a-molti: un Cliente ha molti Ordini
    public List<Ordine> Ordini { get; set; } = new List<Ordine>();

    // Metodo (comportamento)
    public decimal CalcolaTotaleSpeso()
    {
        return Ordini.Sum(o => o.Importo);
    }
}

public class Ordine
{
    public int Id { get; set; }
    public DateTime Data { get; set; }
    public decimal Importo { get; set; }

    // Riferimento concettuale al Cliente proprietario dell'ordine
    public int ClienteId { get; set; }
    public Cliente Cliente { get; set; }
}
```

## Il class diagram corrispondente (notazione testuale)

```
┌─────────────────────────────────┐
│           Cliente               │
├─────────────────────────────────┤
│ + Id: int                       │
│ + Nome: string                  │
│ + Email: string                 │
├─────────────────────────────────┤
│ + CalcolaTotaleSpeso(): decimal │
└─────────────────────────────────┘
              │ 1
              │
              │ *
    ┌────────────────────┐
    │        Ordine      │
    ├────────────────────┤
    │ + Id: int          │
    │ + Data: DateTime   │
    │ + Importo: decimal │
    └────────────────────┘
```

L'associazione tra `Cliente` e `Ordine` è disegnata come una linea che collega i due rettangoli, con le molteplicità `1` e `*` agli estremi, corrispondenti al fatto che `Cliente` contiene una `List<Ordine>`.

## Dal class diagram allo schema relazionale (per confronto)

Se le classi persistono su database, la traduzione tipica è:

```sql
CREATE TABLE Cliente (
    Id INT PRIMARY KEY,
    Nome VARCHAR(100),
    Email VARCHAR(100)
);

CREATE TABLE Ordine (
    Id INT PRIMARY KEY,
    Data DATE,
    Importo DECIMAL(10,2),
    ClienteId INT REFERENCES Cliente(Id)
);
```

Da notare: il metodo `CalcolaTotaleSpeso()` esiste solo nella classe C#/nel class diagram — è comportamento, e non ha equivalente diretto in uno schema relazionale, che modella solo dati.

## Strumenti di reverse/forward engineering

La corrispondenza tra codice C# e class diagram è così diretta che esistono strumenti (plugin di Visual Studio, Rider, PlantUML, ecc.) che possono:
- generare **automaticamente** il class diagram a partire dal codice C# (reverse engineering)
- generare lo scheletro di classi C# a partire da un class diagram (forward engineering)
