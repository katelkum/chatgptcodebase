# Deep Research — modello di esecuzione
## Obiettivo
- Domanda:
- Ambito, periodo e regioni:
- Lingue:
- Numero minimo di query richiesto (se presente):
- Numero minimo di cicli richiesto (se presente):
- Criteri di inclusione/esclusione:

## Registro motori e disponibilità
| Strumento | Nativo/plugin | Disponibile | Funzioni testate | Limiti | Fallback |
|---|---|---|---|---|---|
| Ricerca web nativa | Nativo | da verificare | | | |
| Tavily | Plugin | da verificare | | | |
| Parallel Search | Plugin | da verificare | | | |
| Firecrawl | Plugin | da verificare | | | |
| Altri pertinenti | Plugin | da verificare | | | |

## Cicli
| Ciclo | Query realmente eseguite | Motori (incluso nativo) | Lingue | Nuove fonti | Pagine lette | Contraddizioni | Lacune per ciclo seguente |
|---|---:|---|---|---:|---:|---|---|
| 1 | | | | | | | |

## Registro query (JSONL, una riga per ricerca)
\`{"id":"q001","cycle":1,"engine":"native","language":"it","query":"...","executed":true,"result_count":0,"new_sources":0,"status":"ok","timestamp":"..."}\`

## Registro fonti (JSONL)
\`{"id":"s001","url":"https://...","title":"...","source_type":"primary","found_by":["q001"],"read_with":"native","read_success":true,"published_at":null,"retrieved_at":"..."}\`

## Registro affermazioni (JSONL)
\`{"id":"c001","claim":"...","supports":["s001"],"contradicts":[],"status":"partial","notes":"..."}\`

## Dashboard finale
- Query effettive / soglia:
- Cicli completi / soglia:
- Lingue effettivamente cercate:
- Fonti uniche:
- Fonti lette:
- Risultati nuovi per ciclo:
- Plugin effettivamente usati:
- Strumenti nativi effettivamente usati:
- Errori/blocchi:
- Contraddizioni aperte:
- Crediti/costi verificati:
- Stato: COMPLETA / INCOMPLETA (motivazione)

## Report
1. Risposta sintetica.
2. Evidenze primarie e fonti.
3. Risultati alternativi.
4. Controprove e limitazioni.
5. Lacune residue.
6. Metodologia e copertura verificabile.