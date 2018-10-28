## mushroom_classification

Analyse data from [kaggle](https://www.kaggle.com/uciml/mushroom-classification)
With simple implementation of [hierarchical_clustering](https://en.wikipedia.org/wiki/Hierarchical_clustering)

## How to run

Run train with 3500 items

```bash
make kaggle_1 l=3500
```

Run writing clustering data to file

```bash
make kaggle_2
```

Run check preduction for 1000 items

```bash
make kaggle_3 l=1000 o=35000
```
