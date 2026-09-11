# Dipendenza nel Class Diagram

La **dipendenza** (dependency) è la relazione più "debole" tra classi nel class diagram: indica che una classe **usa** un'altra classe in modo **temporaneo e occasionale**, senza mantenerne un riferimento permanente come attributo. È una relazione del tipo **"usa"** (uses-a), a differenza dell'associazione che rappresenta un legame più stabile e duraturo.

Tipicamente si verifica quando una classe:
- riceve un'altra classe come **parametro di un metodo**
- crea un'istanza **locale** di un'altra classe dentro un metodo (senza salvarla come campo)
- richiama un **metodo statico** di un'altra classe
- usa un'altra classe come **tipo di ritorno** di un metodo

## Notazione grafica

Si rappresenta con una linea **tratteggiata** con una freccia aperta, che punta dalla classe dipendente verso la classe da cui dipende.

```
┌──────────────────────────────┐              ┌───────────────────────────────┐
│   GeneratoreReport           │╌╌╌╌╌╌╌╌╌╌╌╌▷│            Stampante           │
├──────────────────────────────┤              ├───────────────────────────────┤
│                              │              │ + Stampa(testo: string): void │
├──────────────────────────────┤              └───────────────────────────────┘
│ + Genera(s: Stampante): void │
└──────────────────────────────┘
```

`GeneratoreReport` **dipende** da `Stampante`, ma non la possiede come attributo: la riceve solo come parametro nel momento in cui serve.

## Esempio in C#

```csharp
public class Stampante
{
    public void Stampa(string testo)
    {
        Console.WriteLine($"Stampa: {testo}");
    }
}

public class GeneratoreReport
{
    // Nessun campo/attributo di tipo Stampante:
    // la relazione esiste solo "di passaggio", dentro il metodo

    public void Genera(Stampante stampante)  // dipendenza tramite parametro
    {
        string report = "Report mensile - Vendite: 1200€";
        stampante.Stampa(report);
    }
}
```

### Utilizzo

```csharp
GeneratoreReport generatore = new GeneratoreReport();
Stampante stampanteUfficio = new Stampante();

generatore.Genera(stampanteUfficio);
// Stampa: Report mensile - Vendite: 1200€
```

Da notare: `GeneratoreReport` **non conserva** alcun riferimento a `Stampante` dopo l'esecuzione del metodo `Genera()`. La relazione esiste solo per la durata della chiamata — è per questo che si parla di dipendenza e non di associazione.

## Altri casi tipici di dipendenza in C#

```csharp
public class ServizioNotifiche
{
    // Dipendenza: creazione locale di un oggetto, non salvato come campo
    public void InviaNotifica(string messaggio)
    {
        Logger logger = new Logger();       // istanza locale, non un attributo
        logger.Scrivi($"Notifica inviata: {messaggio}");
    }

    // Dipendenza: uso come tipo di ritorno
    public Logger CreaLogger()
    {
        return new Logger();
    }

    // Dipendenza: chiamata a un metodo statico
    public void Valida(string input)
    {
        if (Validatore.EStringaValida(input))  // Validatore è una classe statica
        {
            Console.WriteLine("Input valido");
        }
    }
}

public class Logger
{
    public void Scrivi(string messaggio) => Console.WriteLine(messaggio);
}

public static class Validatore
{
    public static bool EStringaValida(string s) => !string.IsNullOrWhiteSpace(s);
}
```

In tutti e tre i casi (`Logger` creato localmente, `Logger` come tipo di ritorno, `Validatore` richiamato staticamente), `ServizioNotifiche` **dipende** da `Logger` e da `Validatore`, ma nessuna delle due compare come attributo della classe.

## Differenza con l'associazione

Questo è il confronto chiave per non confondere le due relazioni:

| | Dipendenza (linea tratteggiata) | Associazione (linea continua) |
|---|---|---|
| Durata del legame | Temporanea (solo durante l'esecuzione di un metodo) | Duratura (per tutta la vita dell'oggetto) |
| Rappresentazione in codice | Parametro di metodo, variabile locale, tipo di ritorno, chiamata statica | Attributo/campo della classe |
| Esempio | `Genera(Stampante stampante)` | `public List<Ordine> Ordini` |
| Stabilità | Debole: un cambiamento nella classe usata può rompere il metodo che la usa, ma non l'intera classe | Forte: la classe "possiede" concettualmente il riferimento |

## Riepilogo delle relazioni nel class diagram

| Relazione | Simbolo | Significato | Legame |
|---|---|---|---|
| **Dipendenza** | **linea tratteggiata + freccia aperta** | **Uso temporaneo/occasionale** | **Debole** |
| Associazione | linea continua | Riferimento stabile tra classi | Medio |
| Aggregazione | ◇ rombo vuoto | Tutto-parte, la parte sopravvive | Medio-forte |
| Composizione | ◆ rombo pieno | Tutto-parte, la parte muore con il tutto | Forte |
| Generalizzazione | △ triangolo vuoto, linea continua | Ereditarietà tra classi | Strutturale |
| Realizzazione | △ triangolo vuoto, linea tratteggiata | Implementazione di un'interfaccia | Strutturale |
