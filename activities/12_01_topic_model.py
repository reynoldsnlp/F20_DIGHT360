"""Create topic model from texts in gc_texts directory."""

import csv
from glob import glob
from pprint import pprint
import re
import sys

import gensim
# import pyLDAvis.gensim
import spacy


topic_count = 10
word_count = 10

nlp = spacy.load('en')  # your model name may be different


ids = []
doc_complete = []
for filename in glob('gc_texts/*.html'):
    ids.append(filename.split('/')[1][:-5])
    with open(filename) as f:
        doc_complete.append(f.read())


def clean(doc):
    doc = re.sub(r'\s+', ' ', doc)
    return [w.lemma_ for w in nlp(doc)
            if not w.is_stop and not w.is_punct]


print('Cleaning data...', file=sys.stderr)
doc_clean = [clean(doc) for doc in doc_complete]
print('doc_clean', doc_clean)

# Creating the term dictionary of our corpus, where every unique term is
# assigned an index (an int).
print('Creating term dictionary...', file=sys.stderr)
dictionary = gensim.corpora.Dictionary(doc_clean)
dictionary.filter_extremes(no_below=3, no_above=0.5)  # keep_n = 100_000

# Converting list of documents (corpus) into list Document Term Frequency
# Matrix using dictionary prepared above. BOW = Bag Of Words
print('Converting to bag-of-words vectors...', file=sys.stderr)
bow_corpus = [dictionary.doc2bow(doc) for doc in doc_clean]

# Create TF-IDF model from bag-of-words
# see http://www.tfidf.com/
# Example:
# Consider a document containing 100 words wherein the word cat appears 3
# times. The term frequency (i.e., tf) for cat is then (3 / 100) = 0.03. Now,
# assume we have 10 million documents and the word cat appears in one thousand
# of these. Then, the inverse document frequency (i.e., idf) is calculated as
# log(10,000,000 / 1,000) = 4. Thus, the Tf-idf weight is the product of these
# quantities: 0.03 * 4 = 0.12.

print('Making TF-IDF model from bag-of-words vectors...', file=sys.stderr)
tfidf = gensim.models.TfidfModel(bow_corpus)
corpus_tfidf = tfidf[bow_corpus]
print(type(corpus_tfidf), corpus_tfidf[0])

# Running and Training LDA model on the TF-IDF model.
print('Training LDA model...', file=sys.stderr)
ldamodel = gensim.models.ldamodel.LdaModel(corpus_tfidf,
                                           num_topics=topic_count,
                                           id2word=dictionary, passes=50)

topic_keys = ldamodel.print_topics(num_topics=topic_count,
                                   num_words=word_count)
print('topic_keys:')
pprint(topic_keys)
with open('topic_keys.csv', 'w', newline='') as csv_file:
    csv_writer = csv.writer(csv_file)
    for topic, loading in topic_keys:
        y = [x.split('*')[1].replace('"', '').strip()
             for x in loading.split('+')]
        csv_writer.writerow([topic] + y)

# Output document loadings
headers = 'Source Target Type Weight'.split()
with open('doc_topics.csv', 'w', newline='') as csv_file:
    csv_writer = csv.writer(csv_file)
    csv_writer.writerow(headers)
    for doc_name, bow_doc in zip(ids, bow_corpus):
        doc_topics = ldamodel.get_document_topics(bow_doc)
        for topic, loading in doc_topics:
            csv_writer.writerow([doc_name, topic, 'Undirected', loading])

# lda_visualization = pyLDAvis.gensim.prepare(ldamodel, corpus_tfidf, dictionary)
# pyLDAvis.show(lda_visualization)
