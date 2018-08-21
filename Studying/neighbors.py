import pandas as pd
import sklearn
from sklearn.cross_validation import KFold, cross_val_score
from sklearn.neighbors import KNeighborsClassifier

df = pd.read_csv('C:\\Coursera\\ML\\wine.data', header=None)
y = df[0]
X = df.loc[:, 1:]

kf = KFold(len(y), n_folds=5, shuffle=True, random_state=42)


def test_accuracy(kf, X, y):
    scores = []
    for k in range(1, 51):
        model = KNeighborsClassifier(n_neighbors=k)
        scores.append(cross_val_score(model, X, y, cv=kf, scoring='accuracy'))

    return pd.DataFrame(scores, range(1, 51)).mean(axis=1).sort_values(ascending=False)


accuracy = test_accuracy(kf, X, y)
top_accuracy = accuracy.head(1)
print(1, top_accuracy.index[0])
print(2, top_accuracy.values[0])

X = sklearn.preprocessing.scale(X)
accuracy = test_accuracy(kf, X, y)

top_accuracy = accuracy.head(1)
print(3, top_accuracy.index[0])
print(4, top_accuracy.values[0])
