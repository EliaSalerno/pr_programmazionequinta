# Generalizzazione nel Class Diagram

La **generalizzazione** è la relazione che collega una **sottoclasse** (classe specializzata) alla sua **superclasse** (classe generale). È comunemente conosciuta anche come **ereditarietà**, perché la sottoclasse eredita attributi e metodi dalla superclasse, potendoli anche ridefinire o estendere.

Rappresenta una relazione del tipo **"è un"** (is-a): ad esempio, un `Cane` **è un** `Animale`, un `Rettangolo` **è una** `Forma`.

## Notazione grafica

Si rappresenta con una linea **continua** che termina con una **freccia a triangolo vuoto**, puntata dalla sottoclasse verso la superclasse.

```
┌───────────────────────┐
│      Animale          │
├───────────────────────┤
│ + Nome: string        │
│ + Eta: int            │
├───────────────────────┤
│ + EmettiVerso(): void │
└───────────────────────┘
          △
          │
    ┌─────┴───────────────────────────┐
    │                                 │
┌───────────────────────┐ ┌───────────────────────┐
│         Cane          │ │        Gatto          │
├───────────────────────┤ ├───────────────────────┤
│ + Razza: string       │ │ + Colore: string      │
├───────────────────────┤ ├───────────────────────┤
│ + EmettiVerso(): void │ │ + EmettiVerso(): void │
└───────────────────────┘ └───────────────────────┘
```

`Cane` e `Gatto` sono sottoclassi di `Animale`: ereditano gli attributi `Nome` ed `Eta` e il metodo `EmettiVerso()`, che possono anche **ridefinire** (override) con un comportamento specifico (polimorfismo).

## Caratteristiche principali

- La sottoclasse eredita **tutti** gli attributi e metodi pubblici/protetti della superclasse
- Può **aggiungere** nuovi attributi/metodi propri (es. `Razza` in `Cane`, `Colore` in `Gatto`)
- Può **ridefinire** (override) un metodo ereditato per specializzarne il comportamento
- In UML, il diagramma delle classi permette anche l'**ereditarietà multipla** (una sottoclasse con più superclassi), anche se molti linguaggi di programmazione (come C#) non la supportano direttamente per le classi (solo per le interfacce)

## Esempio in C#

```csharp
// Superclasse
public class Animale
{
    public string Nome { get; set; }
    public int Eta { get; set; }

    public Animale(string nome, int eta)
    {
        Nome = nome;
        Eta = eta;
    }

    public virtual void EmettiVerso()
    {
        Console.WriteLine($"{Nome} emette un verso generico.");
    }
}

// Sottoclasse 1
public class Cane : Animale
{
    public string Razza { get; set; }

    public Cane(string nome, int eta, string razza) : base(nome, eta)
    {
        Razza = razza;
    }

    public override void EmettiVerso()
    {
        Console.WriteLine($"{Nome} abbaia: Bau!");
    }
}

// Sottoclasse 2
public class Gatto : Animale
{
    public string Colore { get; set; }

    public Gatto(string nome, int eta, string colore) : base(nome, eta)
    {
        Colore = colore;
    }

    public override void EmettiVerso()
    {
        Console.WriteLine($"{Nome} miagola: Miao!");
    }
}
```

### Utilizzo (polimorfismo)

```csharp
List<Animale> animali = new List<Animale>
{
    new Cane("Rex", 3, "Labrador"),
    new Gatto("Micio", 2, "Nero")
};

foreach (var animale in animali)
{
    animale.EmettiVerso();
    // Rex abbaia: Bau!
    // Micio miagola: Miao!
}
```

Anche se la lista è dichiarata come `List<Animale>`, ogni oggetto esegue la propria versione **specifica** di `EmettiVerso()` — questo è il polimorfismo reso possibile dalla generalizzazione: il codice tratta gli oggetti in modo uniforme (come `Animale`), ma ognuno si comporta secondo la propria sottoclasse concreta.

## Corrispondenza tra class diagram e codice C#

| Class Diagram | C# |
|---|---|
| Freccia △ da `Cane` verso `Animale` | `public class Cane : Animale` |
| Attributi/metodi nella superclasse | Membri di `Animale` ereditati automaticamente |
| Metodo ridefinito nella sottoclasse | `public override void EmettiVerso()` |
| Metodo previsto per essere ridefinito | `public virtual void EmettiVerso()` nella superclasse |
| Costruttore della sottoclasse che richiama quello della superclasse | `: base(nome, eta)` |

## Nota: generalizzazione vs realizzazione

Da non confondere con la relazione di **realizzazione** (implementazione di un'interfaccia), che usa la stessa freccia a triangolo vuoto ma con linea **tratteggiata** invece che continua. La generalizzazione collega classi concrete che ereditano comportamento; la realizzazione collega una classe a un contratto (interfaccia) che non fornisce implementazione.
