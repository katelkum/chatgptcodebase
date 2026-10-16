# ChatGPT Codebase — istruzioni operative

Questa repository è la **codebase persistente condivisa tra l'utente e ChatGPT**. Serve per conservare codice, documentazione, configurazioni non sensibili, risultati e stato dei progetti senza dover ricaricare i file in ogni conversazione.

> **ISTRUZIONI PER CHATGPT / AI CODING AGENTS**  
> Leggi questo README quando l'utente ti chiede di lavorare con questa repository. Considera le regole seguenti come convenzioni organizzative del progetto, subordinate alle istruzioni esplicite dell'utente e alle regole di sicurezza.

## 1. Regola fondamentale: isolamento delle sezioni

- **Ogni nuovo progetto, argomento o sezione di lavoro ha una cartella dedicata.**
- Non mischiare mai file appartenenti a progetti o sezioni diversi.
- La cartella di lavoro predefinita è `projects/<nome-sezione>/`, con un nome breve, descrittivo e stabile in minuscolo (es. `projects/android-keyboard/`).
- Se l'utente continua un progetto esistente, **riutilizza la sua cartella** invece di crearne una nuova.
- All'interno della cartella puoi creare liberamente sottocartelle per sorgenti, test, documentazione e output.

## 2. Accesso ai file: ambito strettamente limitato

**Leggi solo i file necessari della sezione/progetto su cui l'utente sta lavorando.**

1. All'inizio, puoi leggere questo `README.md` e consultare i **nomi delle cartelle** per individuare la sezione pertinente.
2. Una volta identificata la sezione, leggi i file **solo all'interno della sua cartella**, in base alla richiesta.
3. **NON aprire, cercare nel contenuto, analizzare, modificare o usare come contesto file di altre sezioni**, anche se sembrano utili o correlati.
4. Accedi ai file di un'altra sezione **soltanto quando l'utente lo chiede esplicitamente** (ad esempio: «confronta i progetti A e B», «usa il codice della cartella X»).
5. Un'autorizzazione per consultare un'altra sezione vale per il compito richiesto, **non è un permesso permanente** per le conversazioni successive.
6. Se la sezione non è identificabile con sicurezza, **chiedi all'utente quale cartella usare** prima di leggere il contenuto di altre sezioni.
7. Non eseguire ricerche globali sul contenuto dell'intera repository per aggirare questa regola.

Questa separazione evita confusione, contaminazione del contesto e modifiche involontarie ad altri progetti.

## 3. Procedura per ogni richiesta

1. Identifica il progetto o la sezione a cui si riferisce l'utente.
2. Trova la cartella corrispondente sotto `projects/` (consultando solo i nomi, se necessario).
3. Se non esiste, crea `projects/<nome-sezione>/`.
4. Leggi **solo** i file pertinenti in quella cartella.
5. Crea o modifica file **solo** in quella cartella, salvo istruzioni esplicite diverse.
6. Mantieni un `README.md` locale per spiegare lo scopo e la struttura della sezione; quando utile, aggiungi `STATUS.md` e `TODO.md` per tenere traccia del lavoro.
7. Dopo le modifiche, rileggi o verifica i file interessati e comunica all'utente i percorsi e i commit effettuati.
8. Per modifiche importanti, preferisci branch e pull request; non cancellare o distribuire risorse senza una richiesta appropriata.

## 4. Struttura consigliata

```text
chatgptcodebase/
├── README.md                         # Regole generali (questo file)
├── projects/
│   ├── progetto-a/
│   │   ├── README.md                 # Contesto solo del progetto A
│   │   ├── STATUS.md                 # Stato del progetto A (opzionale)
│   │   ├── TODO.md                   # Attività del progetto A (opzionale)
│   │   ├── src/
│   │   ├── tests/
│   │   └── docs/
│   └── progetto-b/
│       ├── README.md                 # Contesto solo del progetto B
│       └── src/
└── tests/                             # Test tecnici preesistenti del connettore
```

I file tecnici preesistenti in `tests/` e `.github/` sono infrastruttura di verifica del connettore, **non sono automaticamente parte di un progetto**. Non leggerli per lavorare a una sezione ordinaria, salvo richiesta esplicita o necessità diretta di gestire la relativa infrastruttura.

## 5. Continuità tra conversazioni

- Questa repository conserva i **file**, non rende automaticamente disponibili tutte le conversazioni precedenti.
- All'avvio di una nuova conversazione su un progetto, recupera dal repository solo i documenti e i file della **sua** cartella per ricostruire il contesto.
- Non presumere che la repository sia già stata letta: verifica tramite gli strumenti GitHub disponibili.
- Se un file non è accessibile, dichiaralo e chiedi come procedere invece di inventarne il contenuto.

## 6. Sicurezza e integrità

- Non inserire token, password, chiavi API, credenziali o dati personali sensibili nel repository, soprattutto perché può essere pubblico.
- Non sovrascrivere modifiche recenti senza leggere la versione corrente.
- Non modificare altre sezioni durante refactoring, ricerche o pulizia del codice.
- Prima di pubblicare un servizio o eseguire azioni con costi o conseguenze esterne, verifica la richiesta e le autorizzazioni dell'utente.

---

**Principio da ricordare:** una richiesta = una sezione di lavoro pertinente. **Le altre cartelle restano fuori dal contesto, a meno che l'utente chieda espressamente di usarle.**
