import numpy as np
from typing import List
from collections import Counter


class countvectorizer:
    def __init__(self):
        self.vocabulary = []

    def fit_transform(self, texts: List[str]) -> np.ndarray:
        """
        Обучение модели и преобразование текстов в матрицу токенов.

        Параметры:
        texts (list of str): Список текстов для обработки.

        Возвращает:
        numpy.ndarray: Матрица подсчета токенов.
        """
        tokenized_text = [text.lower().split() for text in texts]

        for tokens in tokenized_text:
            for token in tokens:
                if token not in self.vocabulary:
                    self.vocabulary.append(token)

        matrix = np.zeros((len(texts), len(self.vocabulary)), dtype="int")

        for id, tokens in enumerate(tokenized_text):
            token_counts = Counter(tokens)
            for j, token in enumerate(self.vocabulary):
                matrix[id, j] = token_counts[token]

        return matrix

    def get_feature_names(self) -> List[str]:
        """
        Получение списка уникальных слов (признаков).

        Возвращает:
        list of str: Список уникальных слов.
        """
        return self.vocabulary


if __name__ == "__main__":
    corpus = [
        "crock pot pasta never boil pasta again",
        "pasta pomodoro fresh ingredients parmesan to taste",
    ]

    vectorizer = countvectorizer()
    matrix = vectorizer.fit_transform(corpus)
    feature_names = vectorizer.get_feature_names()

    print(f"Matrix representation: {matrix}\nFeatures: {feature_names}")
