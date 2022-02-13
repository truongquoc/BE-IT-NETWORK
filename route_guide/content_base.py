import pandas as pd
import numpy as np
# tfidf
from sklearn.feature_extraction.text import TfidfTransformer
from sklearn.linear_model import Ridge
from sklearn import linear_model


class ContentBase:

    @staticmethod
    def getTfidf(x_train):
        transformer = TfidfTransformer(smooth_idf=True, norm='l2')
        tfidf = transformer.fit_transform(x_train.tolist()).toarray()
        return tfidf

    @staticmethod
    def get_items_rated_by_user(rate_matrix, user_id):
        print('user id', user_id);
        print('rate_matrix', rate_matrix);
        print('type', type(rate_matrix))
        if (rate_matrix.size == 0):
            return ([], [])
        y = rate_matrix[:, 0]
        ids = np.where(y == user_id)
        item_ids = rate_matrix[ids, 1];
        scores = rate_matrix[ids, 2]
        return item_ids, scores

    @staticmethod
    def getIndexInArr(index_arr, list_item):
        return list(map((lambda x: np.where(index_arr == x)[0][0]), list_item))

    @staticmethod  # Find the model for each user
    def GetRidgeRegression(self, n_users, rate_train, tfidf, W, b, index_arr):

        for n in n_users:
            i = np.where(n_users == n[0])[0][0]
            ids, scores = self.get_items_rated_by_user(rate_train, n[0])
            clf = Ridge(alpha=0.01, fit_intercept=True)

            if not ids == 0:
                W[:, i] = 0
                b[0, i] = 0
                return W, b

            tests = self.getIndexInArr(index_arr, ids[0])
            Xhat = tfidf[tests, :]
            if Xhat.size != 0:
                clf.fit(Xhat, scores[0])
                W[:, i] = clf.coef_
                b[0, i] = clf.intercept_
            else:
                W[:, i] = 0
                b[0, i] = 0

        return W, b
