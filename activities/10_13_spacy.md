# [spacy](https://spacy.io/)

## Installation: 

```bash
$ python3 -m pip install --user spacy
$ python3 -m spacy download en
```

The second command downloads the "small" English model. Other model names are
listed [here](https://github.com/explosion/spacy-models/tree/master/meta).

## Getting started

```python
import spacy
from spacy import displacy

# Load English tokenizer, tagger, parser, NER and word vectors...
nlp = spacy.load('en')  # this is the all-purpose analyzer
print('nlp:', type(nlp), dir(nlp))
```

## Process a document

```python
pledge = 'I pledge allegiance to the Flag of the United States of America, and to the Republic for which it stands, one Nation under God, indivisible, with liberty and justice for all.'
doc = nlp(pledge)
print('doc:', type(doc), dir(doc))
```

## Do Natural Language Processing things

#### Show lemma, part-of-speech, dependency

```python
print(*'token lemma POS tag dep shape alpha stop'.split(), sep='\t')
for token in doc:
    print(token.text, token.lemma_, token.pos_, token.tag_, token.dep_,
          token.shape_, token.is_alpha, token.is_stop, sep='\t')
print('explain what the JJ tag means:', spacy.explain('JJ'))
```

#### Make dependency visualization of the document on localhost

```python
# on local server that you can view in your browser
displacy.serve(doc, style='dep')

# ...or just save it as a file
svg = displacy.render(doc, style='dep')
with open('dep\_ex.svg', 'w') as f:
    f.write(svg)
```

#### Find named entities, phrases and concepts

```python
doc = nlp('Apple is looking at buying U.K. startup for $1 billion')

print(*'token, start, end, label'.split(), sep='\t')
for ent in doc.ents:
    print(ent.text, ent.start_char, ent.end_char, ent.label_, sep='\t')

# Make named entity visualization on localhost
displacy.serve(doc, style='ent')

# ...or just save it as a file
svg = displacy.render(doc, style='ent')
with open('ent_ex.svg', 'w') as f:
    f.write(svg)
```

#### Determine semantic similarities

```python
doc1 = nlp('the fries were gross')
doc2 = nlp('worst fries ever')
print(f'    similarity between "{doc1}" and "{doc2}":')
print('    ', doc1.similarity(doc2))
```
