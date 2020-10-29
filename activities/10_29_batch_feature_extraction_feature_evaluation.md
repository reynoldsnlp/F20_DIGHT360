# Feature extraction

So far, we have performed feature extraction using one function for each
feature, but sometimes you can use one function to extract a number of
features.

### 1. Parameterization

One way to use one function to extract multiple features is to parameterize one
aspect of the function. For example, assume that we have already applied a
tokenizer and part-of-speech tagger, and now we want to compute the prevalence
of each part of speech. You might begin by writing the following kinds of
functions:

```python
def NN_per_token(doc):
    """Calculate the number of NN tags per token."""
    return len(1 for tok in doc if tok.tag_ == 'NN') / len(doc)


def JJ_per_token(doc):
    """Calculate the number of JJ tags per token."""
    return len(1 for tok in doc if tok.tag_ == 'JJ') / len(doc)

...
```

This begins to feel quite redundant. If your code is repeating itself over and
over, it's usually a good idea to parameterize the piece of code that is
changing in each block. In this case, that is the `NN` and the `JJ`. So we can
write a new function that will do either:

```python
def this_tag_per_token(doc, this_tag):
    """Calcuate the number of `this_tag` tags per token."""
    return (len([1 for tok in doc if tok.tag_ == this_tag])
            / len(doc))
```

Now, you can use a list of the tags to make lists of labels and values that can
be printed in your header and rows, respectively.  This is one way that you
could add the headers (modifying the template you already received):

```python
# TODO add feature names HERE
penn_tags = ['CC', 'CD', 'DT', 'EX', 'FW', 'IN', 'JJ', 'JJR', 'JJS', 'LS',
             'MD', 'NN', 'NNS', 'NNP', 'NNPS', 'PDT', 'POS', 'PRP', 'PRP$',
             'RB', 'RBR', 'RBS', 'RP', 'SYM', 'TO', 'UH', 'VB', 'VBD', 'VBG',
             'VBN', 'VBP', 'VBZ', 'WDT', 'WP', 'WP$', 'WRB']
tag_per_token_labels = [tag + '_per_tok' for tag in penn_tags]
feat_names = ['1st-pro', '2nd-pro', '3rd-pro'] + tag_per_token_labels + ['genre']
```

The values for each document could then be called inside the loop as follows:

```python
print('Extracting features...', file=sys.stderr)
genre_counter = Counter()
with open('mc_features.csv', 'w') as out_file:
    print(*feat_names, sep=',', file=out_file)
    for f in tqdm(glob(MC_DIR + '*.txt')):
        genre = subcorpus(f)
        genre_counter.update([genre])
        if genre_counter[genre] > 10:  # TODO comment out this line
            continue  # move on without finishing the loop  # TODO comment out
        with open(f) as the_file:
            raw_text = clean(the_file)
        # preprocess
        doc = nlp(raw_text)
        tokens = [tok.text for tok in doc]
        tag_per_token_values = [this_tag_per_token(doc, tag)
                                for tag in penn_tags]
        # TODO call functions HERE
        print(pro1_tr(tokens), pro2_tr(tokens), pro3_tr(tokens),
              q_count(raw_text), *tag_per_token_values, genre, sep=',',
              file=out_file)
```

### Functions that return lists

Another alternative is to write functions that return lists of values:

```python
def all_tag_per_token(doc, the_tags):
    """Calcuate the number of `this_tag` tags per token."""
    values = []
    for this_tag in the_tags:
        values.append(len(1 for tok in doc if tok.tag_ == this_tag)
                      / len(doc))
    return values
```

This would be called with `all_tag_per_token(doc, penn_tags)`.

# [Feature evaluation (machine-learning)](https://scikit-learn.org/stable/modules/feature_selection.html)

Not all features are extracted equal, and including only the most useful
features in your model has many benefits:

    * Reduces Overfitting: (overfit = memorizing instead of learning) Less
        redundant data means less opportunity to make decisions based on noise.
    * Improves Accuracy: Less misleading data means modeling accuracy improves.
    * Reduces Training Time: Less data means that algorithms train faster.
    * Reduces Feature Extraction Time: Less work to process data in the wild.

Below are examples of two different ways to evaluate a feature's usefulness.

1. Feature "[importance](https://towardsdatascience.com/explaining-feature-importance-by-example-of-a-random-forest-d9166011959e)"
    * All "tree" models in `sklearn` have a `feature_importances_` attribute.
    * How frequently is this feature used to determine a correct result?
1. Feature correlation coefficients
    * Regression models have a `coef_` attribute with correlation coefficients
      of each feature with each label/class

## "Importance"

```python
from pprint import pprint

from sklearn import datasets
from sklearn.ensemble import ExtraTreesClassifier

# load the iris datasets
dataset = datasets.load_iris()
print('Feature names:')
print(dataset['feature_names'])
print('Class names:')
print(dataset['target_names'])

# fit an Extra Trees model to the data
ETCmodel = ExtraTreesClassifier()
ETCmodel.fit(dataset.data, dataset.target)

# `feature_importances_` is just the values
print(ETCmodel.feature_importances_)

# display the relative importance of each attribute
feat_importances = dict(zip(dataset['feature_names'],
                            ETCmodel.feature_importances_))
print('Importances:')
for f, i in sorted(feat_importances.items(), key=lambda x: x[1], reverse=True):
    print(f, i, sep='\t')
```

## Correlation coefficients

Regression models have a `coef_` attribute with correlation coefficients of
each feature with each label/class

```python
import pandas as pd
from sklearn import datasets
from sklearn.linear_model import LogisticRegression

# load the iris datasets
dataset = datasets.load_iris()

# create a base classifier used to evaluate a subset of features
LRmodel = LogisticRegression()

# train model based on all features
LRmodel_allfeats = LRmodel.fit(dataset.data, dataset.target)

# `coef_` is a list of lists
print(LRmodel_allfeats.coef_)

# print `coef_` in a human-readable format using a pandas.DataFrame
coef_df = pd.DataFrame(LRmodel_allfeats.coef_,
                       index=dataset.target_names,
                       columns=dataset.feature_names)
print(coef_df)
```

## Recursive Feature Elimination (RFE)

Given an external estimator that assigns weights to features (e.g., the
coefficients of a linear model), the goal of recursive feature elimination
(RFE) is to select features by recursively considering smaller and smaller sets
of features. First, the estimator is trained on the initial set of features and
the importance of each feature is obtained either through a coef_ attribute or
through a feature_importances_ attribute. Then, the least important features
are pruned from current set of features. That procedure is recursively repeated
on the pruned set until the desired number of features to select is eventually
reached.

```python
from sklearn import datasets
from sklearn.feature_selection import RFE
from sklearn.linear_model import LogisticRegression

# load the iris datasets
dataset = datasets.load_iris()

# Train models with all features
LRmodel_allfeats = LogisticRegression()
LRmodel_allfeats.fit(dataset.data, dataset.target)
LRmodel = LogisticRegression()

# create the RFE feature selection model and select 3 features
rfe = RFE(LRmodel, 3)
rfe = rfe.fit(dataset.data, dataset.target)

print('summarize the selection of the features')
print(rfe.support_)  # did the feature make the cut?
print(rfe.ranking_)  # the feature's rank (all "passing" features share 1st)

evaluations = zip(dataset['feature_names'], rfe.support_, rfe.ranking_)
print('Recursive feature evaluation:')
print('Name', 'Support', 'Rank', sep='\t')
for name, support, rank in sorted(evaluations, key=lambda x: x[-1],
                                  reverse=True):
    print(name, support, rank, sep='\t')

print('comparing predictions of full model and RFE model...')
toy_data = [(1, 2, 3, 4),
            (1, 1, 1, 1),
            (5, 3, 2, 1),
            (5, 5, 5, 5)]

# Removing one feature does change the predictions
print('Full:', LRmodel_allfeats.predict(toy_data))
print('RFE: ', rfe.predict(toy_data))
```

## RFE with cross-validation

One problem with RFE is that you have to determine a priori how many features
you want back. This seems like a very arbitrary thing to decide without knowing
how informative each feature is!

Scikit learn includes another
[feature selection tool](https://scikit-learn.org/stable/modules/generated/sklearn.feature_selection.RFECV.html)
that automatically determines how many features to keep.  See `RFECV.py` to see
it in use.
