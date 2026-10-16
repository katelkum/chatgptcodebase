# Deep Research Agent — progetto isolato
Questo progetto contiene il protocollo universale di ricerca approfondita multi-motore concordato con l'utente.

## File
- **PROMPT_UNIVERSALE.md** — istruzioni operative complete per l'agente AI, pronte da riutilizzare.
- **RUN_TEMPLATE.md** — modello di esecuzione, registro e report di una ricerca.
- **STATUS.md** — cosa è stato realizzato e cosa resta da implementare.

## Principi
1. Discovery-first, iterazioni, esclusioni, ricerca multilingue, fonti primarie e contraddizioni.
2. Plugin **facoltativi**, strumenti **nativi indipendenti e sempre utilizzati se disponibili**, non soltanto come fallback.
3. Fallback: plugin preferito → plugin alternativo → soli strumenti nativi.
4. Nessuna capacità o connessione presunta; ogni strumento va verificato nel contesto corrente.
5. Tracciabilità dei risultati, conteggio delle query effettive e dichiarazione dei limiti.
6. Ogni altra sezione della repository rimane fuori ambito.

## Uso
All'avvio di un compito Deep Research, leggere questo README e **PROMPT_UNIVERSALE.md**. Per una ricerca concreta, copiare il modello **RUN_TEMPLATE.md** nella cartella dedicata a quella ricerca, quando è richiesto il salvataggio.

## Ambito di questa consegna
Sono state create **istruzioni e modelli**, non un servizio Railway o un agente schedulato. La ricerca avviene tramite strumenti effettivamente accessibili nella conversazione.