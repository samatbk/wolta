import numpy as np


def get_score(y_test, y_pred, metrics=None, average='weighted', algo_type='clf'):
    if metrics is None:
        if algo_type == 'clf':
            metrics = ['acc']
        elif algo_type == 'reg':
            metrics = ['sq']

    output = ''
    scores = {}

    if algo_type == 'clf':
        for metric in metrics:
            if metric == 'acc':
                from sklearn.metrics import accuracy_score
                score = accuracy_score(y_test, y_pred)
                scores[metric] = score

                if output == '':
                    output = 'Accuracy Score: {}'.format(str(score))
                else:
                    output += '\nAccuracy Score: {}'.format(str(score))

            elif metric == 'f1':
                from sklearn.metrics import f1_score
                score = f1_score(y_test, y_pred, average=average)
                scores[metric] = score

                if output == '':
                    output = 'F1 Score (weighted): {}'.format(str(score))
                else:
                    output += '\nF1 Score (weighted): {}'.format(str(score))

            elif metric == 'hamming':
                from sklearn.metrics import hamming_loss
                score = hamming_loss(y_test, y_pred)
                scores[metric] = score

                if output == '':
                    output = 'Hamming Loss: {}'.format(str(score))
                else:
                    output += '\nHamming Loss: {}'.format(str(score))

            elif metric == 'jaccard':
                from sklearn.metrics import jaccard_score
                score = jaccard_score(y_test, y_pred, average=average)
                scores[metric] = score

                if output == '':
                    output = 'Jaccard: {}'.format(str(score))
                else:
                    output += '\nJaccard: {}'.format(str(score))

            elif metric == 'log':
                from sklearn.metrics import log_loss
                score = log_loss(y_test, y_pred)
                scores[metric] = score

                if output == '':
                    output = 'Log Loss: {}'.format(str(score))
                else:
                    output += '\nLog Loss: {}'.format(str(score))

            elif metric == 'mcc':
                from sklearn.metrics import matthews_corrcoef
                score = matthews_corrcoef(y_test, y_pred)
                scores[metric] = score

                if output == '':
                    output = 'MCC: {}'.format(str(score))
                else:
                    output += '\nMCC: {}'.format(str(score))

            elif metric == 'precision':
                from sklearn.metrics import precision_score
                score = precision_score(y_test, y_pred, average=average)
                scores[metric] = score

                if output == '':
                    output = 'Precision Score: {}'.format(str(score))
                else:
                    output += '\nPrecision Score: {}'.format(str(score))

            elif metric == 'recall':
                from sklearn.metrics import recall_score
                score = recall_score(y_test, y_pred, average=average)
                scores[metric] = score

                if output == '':
                    output = 'Recall Score: {}'.format(str(score))
                else:
                    output += '\nRecall Score: {}'.format(str(score))

            elif metric == 'zol':
                from sklearn.metrics import zero_one_loss
                score = zero_one_loss(y_test, y_pred)
                scores[metric] = score

                if output == '':
                    output = 'Zero One Loss: {}'.format(str(score))
                else:
                    output += '\nZero One Loss: {}'.format(str(score))

    elif algo_type == 'reg':
        for metric in metrics:
            if metric == 'var':
                from sklearn.metrics import explained_variance_score
                score = explained_variance_score(y_test, y_pred)
                scores[metric] = score

                if output == '':
                    output = 'Explained Variance Score: {}'.format(str(score))
                else:
                    output += '\nExplained Variance Score: {}'.format(str(score))

            elif metric == 'max':
                from sklearn.metrics import max_error
                score = max_error(y_test, y_pred)
                scores[metric] = score

                if output == '':
                    output = 'Max Error: {}'.format(str(score))
                else:
                    output += '\nMax Error: {}'.format(str(score))

            elif metric == 'abs':
                from sklearn.metrics import mean_absolute_error
                score = mean_absolute_error(y_test, y_pred)
                scores[metric] = score

                if output == '':
                    output = 'Mean Absolute Error: {}'.format(str(score))
                else:
                    output += '\nMean Absolute Error: {}'.format(str(score))

            elif metric == 'sq':
                from sklearn.metrics import mean_squared_error
                score = mean_squared_error(y_test, y_pred)
                scores[metric] = score

                if output == '':
                    output = 'Mean Squared Error: {}'.format(str(score))
                else:
                    output += '\nMean Squared Error: {}'.format(str(score))

            elif metric == 'rsq':
                from sklearn.metrics import root_mean_squared_error
                score = root_mean_squared_error(y_test, y_pred)
                scores[metric] = score

                if output == '':
                    output = 'Root Mean Squared Error: {}'.format(str(score))
                else:
                    output += '\nRoot Mean Squared Error: {}'.format(str(score))

            elif metric == 'log':
                from sklearn.metrics import mean_squared_log_error
                score = mean_squared_log_error(y_test, y_pred)
                scores[metric] = score

                if output == '':
                    output = 'Mean Squared Log Error: {}'.format(str(score))
                else:
                    output += '\nMean Squared Log Error: {}'.format(str(score))

            elif metric == 'rlog':
                from sklearn.metrics import root_mean_squared_log_error
                score = root_mean_squared_log_error(y_test, y_pred)
                scores[metric] = score

                if output == '':
                    output = 'Root Mean Squared Log Error: {}'.format(str(score))
                else:
                    output += '\nRoot Mean Squared Log Error: {}'.format(str(score))

            elif metric == 'medabs':
                from sklearn.metrics import median_absolute_error
                score = median_absolute_error(y_test, y_pred)
                scores[metric] = score

                if output == '':
                    output = 'Median Absolute Error: {}'.format(str(score))
                else:
                    output += '\nMedian Absolute Error: {}'.format(str(score))

            elif metric == 'poisson':
                from sklearn.metrics import mean_poisson_deviance
                score = mean_poisson_deviance(y_test, y_pred)
                scores[metric] = score

                if output == '':
                    output = 'Mean Poisson Deviance: {}'.format(str(score))
                else:
                    output += '\nMean Poisson Deviance: {}'.format(str(score))

            elif metric == 'gamma':
                from sklearn.metrics import mean_gamma_deviance
                score = mean_gamma_deviance(y_test, y_pred)
                scores[metric] = score

                if output == '':
                    output = 'Mean Gamma Deviance: {}'.format(str(score))
                else:
                    output += '\nMean Gamma Deviance: {}'.format(str(score))

            elif metric == 'per':
                from sklearn.metrics import mean_absolute_percentage_error
                score = mean_absolute_percentage_error(y_test, y_pred)
                scores[metric] = score

                if output == '':
                    output = 'Mean Absolute Percentage Error: {}'.format(str(score))
                else:
                    output += '\nMean Absolute Percentage Error: {}'.format(str(score))

            elif metric == 'd2abs':
                from sklearn.metrics import d2_absolute_error_score
                score = d2_absolute_error_score(y_test, y_pred)
                scores[metric] = score

                if output == '':
                    output = 'D2 Absolute Error Score: {}'.format(str(score))
                else:
                    output += '\nD2 Absolute Error Score: {}'.format(str(score))

            elif metric == 'd2pin':
                from sklearn.metrics import d2_pinball_score
                score = d2_pinball_score(y_test, y_pred)
                scores[metric] = score

                if output == '':
                    output = 'D2 Pinball Score: {}'.format(str(score))
                else:
                    output += '\nD2 Pinball Score: {}'.format(str(score))

            elif metric == 'd2twe':
                from sklearn.metrics import d2_tweedie_score
                score = d2_tweedie_score(y_test, y_pred)
                scores[metric] = score

                if output == '':
                    output = 'D2 Tweedie Score: {}'.format(str(score))
                else:
                    output += '\nD2 Tweedie Score: {}'.format(str(score))

    print(output)
    return scores


def get_supported_metrics():
    return ['acc', 'f1', 'hamming', 'jaccard', 'log', 'mcc', 'precision', 'recall', 'zol']


def get_avg_options():
    return ['micro', 'macro', 'binary', 'weighted', 'samples']


def do_voting(y_pred_list, combinations, strategy='avg'):
    if strategy == 'avg':
        results = []

        for comb in combinations:
            y_sum = None

            for index in comb:
                if y_sum is None:
                    y_sum = y_pred_list[index]
                else:
                    y_sum += y_pred_list[index]

            y_sum = y_sum / len(comb)
            y_sum = y_sum.astype(int)
            results.append(y_sum)

        return results

    elif strategy == 'mode':
        from math import ceil
        import numpy as np

        results = []

        for comb in combinations:
            selected = []
            for index in comb:
                selected.append(y_pred_list[index])

            stack = np.concatenate(selected, axis=1)
            del selected

            req_min = ceil(len(list(stack[0])) / 2)
            length = stack.shape[0]
            modes = []

            for i in range(length):
                result = 0
                max_times = 0
                min_space = max_times + 1
                row = list(stack[i])

                while len(row) > 0:
                    loc = 0
                    obj = row[0]
                    times = 0

                    while loc < len(row):
                        if obj == row[loc]:
                            del row[loc]
                            times += 1
                        else:
                            loc += 1

                    if times > max_times:
                        result = obj
                        max_times = times
                        min_space = max_times + 1

                    if max_times >= req_min or len(row) < min_space:
                        break

                modes.append(result)

            modes = np.array(modes)
            results.append(modes)

        return results


def do_combinations(indexes, min_item, max_item):
    import itertools
    combinations = []

    for i in range(min_item, max_item + 1):
        combs = list(itertools.combinations(indexes, i))

        for comb in combs:
            combinations.append(list(comb))

    return combinations


def examine_time(model, X_train, y_train):
    import time

    start = time.process_time()
    model.fit(X_train, y_train)
    end = time.process_time()

    consumed = end - start
    return consumed, model


class WelkinClassification:
    def __init__(self, strategy='travel', priority=None, limit=None):
        self.min = {}
        self.max = {}
        self.strategy = strategy
        self.priority = priority
        self.limit = limit

    def fit(self, X_train, y_train):
        import sys

        for i in range(y_train.shape[0]):
            if not y_train[i] in self.min:
                self.min[y_train[i]] = {}
                self.max[y_train[i]] = {}

                for j in range(X_train.shape[1]):
                    self.min[y_train[i]][j] = sys.maxsize
                    self.max[y_train[i]][j] = -sys.maxsize - 1

            row = list(X_train[i])

            for j in range(len(row)):
                if row[j] < self.min[y_train[i]][j]:
                    self.min[y_train[i]][j] = row[j]

                elif row[j] > self.max[y_train[i]][j]:
                    self.max[y_train[i]][j] = row[j]

    def predict(self, X_test):
        if self.strategy == 'travel':
            import numpy as np
            from random import randint

            pred = []

            stage_line = list(self.min.keys())
            if self.priority is not None:
                stage_line = self.priority

            for i in range(X_test.shape[0]):
                max_key = list(self.max.keys())[randint(0, len(list(self.max.keys())) - 1)]
                max_zone = 0

                row = list(X_test[i])

                for output in stage_line:
                    count = 0

                    for j in range(X_test.shape[1]):
                        if row[j] >= self.min[output][j] and row[j] <= self.max[output][j]:
                            count += 1

                    if count > max_zone:
                        max_zone = count
                        max_key = output

                        if count == X_test.shape[0]:
                            break

                pred.append(max_key)

            return np.array(pred)

        elif self.strategy == 'limit' and self.limit is not None:
            import numpy as np
            from random import randint

            pred = []

            stage_line = list(self.min.keys())
            if self.priority is not None:
                stage_line = self.priority

            for i in range(X_test.shape[0]):
                max_key = list(self.max.keys())[randint(0, len(list(self.max.keys())) - 1)]
                max_zone = 0

                row = list(X_test[i])

                for output in stage_line:
                    count = 0

                    for j in range(X_test.shape[1]):
                        if row[j] >= self.min[output][j] and row[j] <= self.max[output][j]:
                            count += 1

                    if count > max_zone:
                        max_zone = count
                        max_key = output

                        if count == X_test.shape[0] or count >= self.limit:
                            break

                pred.append(max_key)

            return np.array(pred)


class DistRegressor:
    import numpy as np

    def __init__(self, verbose=True, clf_model=None, clf_params=None, reg_model=None, reg_params=None,
                 efficiency='time', rus=True):
        self.type_zero_regressor = None
        self.type_one_regressor = None
        self.type_two_regressor = None
        self.rus = rus
        self.verbose = verbose
        self.efficiency = efficiency

        self.clf_model = clf_model
        self.reg_model = reg_model
        self.reg_params = reg_params

        if self.clf_model is not None:
            if clf_params is None:
                self.clf_model = clf_model()
            else:
                self.clf_model = clf_model(**clf_params)

    def fit(self, X_train, y_train):
        std = np.std(y_train)
        mean = np.mean(y_train)
        amin = np.amin(y_train)
        amax = np.amax(y_train)

        border_one = mean - std
        border_two = mean + std

        if amin >= border_one or amax <= border_two:
            raise ValueError('There is no such a normal distribution!')

        if self.verbose:
            print('Basic calculations are completed')

        clf_arr = []
        one_side = 0
        type_zero_X = []
        type_one_X = []
        type_two_X = []
        type_zero_y = []
        type_one_y = []
        type_two_y = []

        if self.efficiency == 'space':
            for i in range(y_train.shape[0]):
                if y_train[i] <= border_one:
                    clf_arr.append(0)
                    one_side += 1
                elif y_train[i] > border_one and y_train[i] < border_two:
                    clf_arr.append(1)
                else:
                    clf_arr.append(2)

            del type_zero_X, type_one_X, type_two_X, type_zero_y, type_one_y, type_two_y

        elif self.efficiency == 'time':
            for i in range(y_train.shape[0]):
                if y_train[i] <= border_one:
                    clf_arr.append(0)
                    type_zero_X.append(list(X_train[i]))
                    type_zero_y.append(y_train[i])
                elif y_train[i] > border_one and y_train[i] < border_two:
                    clf_arr.append(1)
                    type_one_X.append(list(X_train[i]))
                    type_one_y.append(y_train[i])
                else:
                    clf_arr.append(2)
                    type_two_X.append(list(X_train[i]))
                    type_two_y.append(y_train[i])

            type_zero_X = np.array(type_zero_X)
            type_one_X = np.array(type_one_X)
            type_two_X = np.array(type_two_X)
            type_zero_y = np.array(type_zero_y)
            type_one_y = np.array(type_one_y)
            type_two_y = np.array(type_two_y)

        clf_arr = np.array(clf_arr)

        if self.verbose:
            print('Result array is ready for classification')

        small_X = None
        if self.rus:
            from imblearn.under_sampling import RandomUnderSampler

            strategy = {1: one_side}
            rand = RandomUnderSampler(sampling_strategy=strategy)

            small_X, clf_arr = rand.fit_resample(X_train, clf_arr)

        if self.clf_model is None:
            from catboost import CatBoostClassifier

            self.clf_model = CatBoostClassifier(verbose=False, iterations=20)

            if self.rus:
                self.clf_model.fit(small_X, clf_arr)
            else:
                self.clf_model.fit(X_train, clf_arr)
        else:
            if self.rus:
                self.clf_model.fit(small_X, clf_arr)
            else:
                self.clf_model.fit(X_train, clf_arr)

        del small_X, clf_arr

        if self.verbose:
            print('Classification model has been trained')

        if self.efficiency == 'space':
            sub_X = []
            sub_y = []
            for i in range(X_train.shape[0]):
                if y_train[i] <= border_one:
                    sub_X.append(list(X_train[i]))
                    sub_y.append(y_train[i])

            sub_X = np.array(sub_X)
            sub_y = np.array(sub_y)

            if self.reg_model is None:
                from catboost import CatBoostRegressor

                self.type_zero_regressor = CatBoostRegressor(verbose=False, iterations=20)
                self.type_zero_regressor.fit(sub_X, sub_y)
            else:
                if self.reg_params is None:
                    self.type_zero_regressor = self.reg_model()
                else:
                    self.type_zero_regressor = self.reg_model(**self.reg_params)

                self.type_zero_regressor.fit(sub_X, sub_y)

            sub_X = []
            sub_y = []
            for i in range(X_train.shape[0]):
                if y_train[i] > border_one and y_train[i] < border_two:
                    sub_X.append(list(X_train[i]))
                    sub_y.append(y_train[i])

            sub_X = np.array(sub_X)
            sub_y = np.array(sub_y)

            if self.reg_model is None:
                from catboost import CatBoostRegressor

                self.type_one_regressor = CatBoostRegressor(verbose=False, iterations=20)
                self.type_one_regressor.fit(sub_X, sub_y)
            else:
                if self.reg_params is None:
                    self.type_one_regressor = self.reg_model()
                else:
                    self.type_one_regressor = self.reg_model(**self.reg_params)

                self.type_one_regressor.fit(sub_X, sub_y)

            sub_X = []
            sub_y = []
            for i in range(X_train.shape[0]):
                if y_train[i] >= border_two:
                    sub_X.append(list(X_train[i]))
                    sub_y.append(y_train[i])

            sub_X = np.array(sub_X)
            sub_y = np.array(sub_y)

            if self.reg_model is None:
                from catboost import CatBoostRegressor

                self.type_two_regressor = CatBoostRegressor(verbose=False, iterations=20)
                self.type_two_regressor.fit(sub_X, sub_y)
            else:
                if self.reg_params is None:
                    self.type_two_regressor = self.reg_model()
                else:
                    self.type_two_regressor = self.reg_model(**self.reg_params)

                self.type_two_regressor.fit(sub_X, sub_y)

        elif self.efficiency == 'time':
            if self.reg_model is None:
                from catboost import CatBoostRegressor

                self.type_zero_regressor = CatBoostRegressor(verbose=False, iterations=20)
                self.type_one_regressor = CatBoostRegressor(verbose=False, iterations=20)
                self.type_two_regressor = CatBoostRegressor(verbose=False, iterations=20)

                self.type_zero_regressor.fit(type_zero_X, type_zero_y)
                del type_zero_X, type_zero_y

                self.type_one_regressor.fit(type_one_X, type_one_y)
                del type_one_X, type_one_y

                self.type_two_regressor.fit(type_two_X, type_two_y)
                del type_two_X, type_two_y
            else:
                if self.reg_params is None:
                    self.type_zero_regressor = self.reg_model()
                    self.type_one_regressor = self.reg_model()
                    self.type_two_regressor = self.reg_model()
                else:
                    self.type_zero_regressor = self.reg_model(**self.reg_params)
                    self.type_one_regressor = self.reg_model(**self.reg_params)
                    self.type_two_regressor = self.reg_model(**self.reg_params)

                self.type_zero_regressor.fit(type_zero_X, type_zero_y)
                del type_zero_X, type_zero_y

                self.type_one_regressor.fit(type_one_X, type_one_y)
                del type_one_X, type_one_y

                self.type_two_regressor.fit(type_two_X, type_two_y)
                del type_two_X, type_two_y

        if self.verbose:
            print('Regression models have been trained')

    def predict(self, X_test):
        y_pred = []

        for i in range(X_test.shape[0]):
            category = self.clf_model.predict([X_test[i]])

            if category == 0:
                y_pred.append(self.type_zero_regressor.predict([X_test[i]]))
            elif category == 1:
                y_pred.append(self.type_one_regressor.predict([X_test[i]]))
            else:
                y_pred.append(self.type_two_regressor.predict([X_test[i]]))

        y_pred = np.array(y_pred)
        return y_pred

    def is_data_normal(self, y):
        amax = np.amax(y)
        amin = np.amin(y)
        mean = np.mean(y)
        std = np.std(y)

        if amin < mean - std and amax > mean + std:
            return True
        else:
            return False


def compare_models(algo_type, algorithms, metrics, X_train, y_train, X_test, y_test):
    if algo_type == 'clf':
        from catboost import CatBoostClassifier
        from sklearn.ensemble import AdaBoostClassifier
        from sklearn.tree import DecisionTreeClassifier
        from sklearn.ensemble import RandomForestClassifier
        from lightgbm import LGBMClassifier
        from sklearn.tree import ExtraTreeClassifier
        from sklearn.linear_model import LogisticRegression
        from sklearn.neighbors import KNeighborsClassifier
        from sklearn.naive_bayes import GaussianNB
        from sklearn.linear_model import RidgeClassifier
        from sklearn.naive_bayes import BernoulliNB
        from sklearn.svm import SVC
        from sklearn.linear_model import Perceptron
        from sklearn.naive_bayes import MultinomialNB

        if algorithms[0] == 'all':
            algorithms = ['cat', 'ada', 'dtr', 'raf', 'lbm', 'ext', 'log', 'knn', 'gnb', 'rdg', 'bnb', 'svc', 'per', 'mnb']

        for algo in algorithms:
            if algo == 'cat':
                model = CatBoostClassifier(verbose=False)
                model.fit(X_train, y_train)
                y_pred = model.predict(X_test)

                print('CatBoost')
                get_score(y_test, y_pred, metrics)
                print('***')

            elif algo == 'ada':
                model = AdaBoostClassifier()
                model.fit(X_train, y_train)
                y_pred = model.predict(X_test)

                print('AdaBoost')
                get_score(y_test, y_pred, metrics)
                print('***')

            elif algo == 'dtr':
                model = DecisionTreeClassifier()
                model.fit(X_train, y_train)
                y_pred = model.predict(X_test)

                print('Decision Tree')
                get_score(y_test, y_pred, metrics)
                print('***')

            elif algo == 'raf':
                model = RandomForestClassifier()
                model.fit(X_train, y_train)
                y_pred = model.predict(X_test)

                print('Random Forest')
                get_score(y_test, y_pred, metrics)
                print('***')

            elif algo == 'lbm':
                model = LGBMClassifier()
                model.fit(X_train, y_train)
                y_pred = model.predict(X_test)

                print('LightGBM')
                get_score(y_test, y_pred, metrics)
                print('***')

            elif algo == 'ext':
                model = ExtraTreeClassifier()
                model.fit(X_train, y_train)
                y_pred = model.predict(X_test)

                print('Extra Tree')
                get_score(y_test, y_pred, metrics)
                print('***')

            elif algo == 'log':
                model = LogisticRegression()
                model.fit(X_train, y_train)
                y_pred = model.predict(X_test)

                print('Logistic Regression')
                get_score(y_test, y_pred, metrics)
                print('***')

            elif algo == 'knn':
                model = KNeighborsClassifier()
                model.fit(X_train, y_train)
                y_pred = model.predict(X_test)

                print('KNN')
                get_score(y_test, y_pred, metrics)
                print('***')

            elif algo == 'gnb':
                model = GaussianNB()
                model.fit(X_train, y_train)
                y_pred = model.predict(X_test)

                print('GaussianNB')
                get_score(y_test, y_pred, metrics)
                print('***')

            elif algo == 'rdg':
                model = RidgeClassifier()
                model.fit(X_train, y_train)
                y_pred = model.predict(X_test)

                print('Ridge')
                get_score(y_test, y_pred, metrics)
                print('***')

            elif algo == 'bnb':
                model = BernoulliNB()
                model.fit(X_train, y_train)
                y_pred = model.predict(X_test)

                print('BernoulliNB')
                get_score(y_test, y_pred, metrics)
                print('***')

            elif algo == 'svc':
                model = SVC()
                model.fit(X_train, y_train)
                y_pred = model.predict(X_test)

                print('SVC')
                get_score(y_test, y_pred, metrics)
                print('***')

            elif algo == 'per':
                model = Perceptron()
                model.fit(X_train, y_train)
                y_pred = model.predict(X_test)

                print('Perceptron')
                get_score(y_test, y_pred, metrics)
                print('***')

            elif algo == 'mnb':
                model = MultinomialNB()
                model.fit(X_train, y_train)
                y_pred = model.predict(X_test)

                print('MultinomialNB')
                get_score(y_test, y_pred, metrics)
                print('***')

    elif algo_type == 'reg':
        from catboost import CatBoostRegressor
        from sklearn.ensemble import AdaBoostRegressor
        from sklearn.tree import DecisionTreeRegressor
        from sklearn.ensemble import RandomForestRegressor
        from lightgbm import LGBMRegressor
        from sklearn.tree import ExtraTreeRegressor
        from sklearn.linear_model import LinearRegression
        from sklearn.neighbors import KNeighborsRegressor
        from sklearn.svm import SVR

        if algorithms[0] == 'all':
            algorithms = ['cat', 'ada', 'dtr', 'raf', 'lbm', 'ext', 'lin', 'knn', 'svr']

        for algo in algorithms:
            if algo == 'cat':
                model = CatBoostRegressor(verbose=False)
                model.fit(X_train, y_train)
                y_pred = model.predict(X_test)

                print('CatBoost')
                get_score(y_test, y_pred, metrics, algo_type='reg')
                print('***')

            elif algo == 'ada':
                model = AdaBoostRegressor()
                model.fit(X_train, y_train)
                y_pred = model.predict(X_test)

                print('AdaBoost')
                get_score(y_test, y_pred, metrics, algo_type='reg')
                print('***')

            elif algo == 'dtr':
                model = DecisionTreeRegressor()
                model.fit(X_train, y_train)
                y_pred = model.predict(X_test)

                print('Decision Tree')
                get_score(y_test, y_pred, metrics, algo_type='reg')
                print('***')

            elif algo == 'raf':
                model = RandomForestRegressor()
                model.fit(X_train, y_train)
                y_pred = model.predict(X_test)

                print('Random Forest')
                get_score(y_test, y_pred, metrics, algo_type='reg')
                print('***')

            elif algo == 'lbm':
                model = LGBMRegressor()
                model.fit(X_train, y_train)
                y_pred = model.predict(X_test)

                print('LightGBM')
                get_score(y_test, y_pred, metrics, algo_type='reg')
                print('***')

            elif algo == 'ext':
                model = ExtraTreeRegressor()
                model.fit(X_train, y_train)
                y_pred = model.predict(X_test)

                print('Extra Tree')
                get_score(y_test, y_pred, metrics, algo_type='reg')
                print('***')

            elif algo == 'lin':
                model = LinearRegression()
                model.fit(X_train, y_train)
                y_pred = model.predict(X_test)

                print('Linear Regression')
                get_score(y_test, y_pred, metrics, algo_type='reg')
                print('***')

            elif algo == 'knn':
                model = KNeighborsRegressor()
                model.fit(X_train, y_train)
                y_pred = model.predict(X_test)

                print('KNN')
                get_score(y_test, y_pred, metrics, algo_type='reg')
                print('***')

            elif algo == 'svr':
                model = SVR()
                model.fit(X_train, y_train)
                y_pred = model.predict(X_test)

                print('SVR')
                get_score(y_test, y_pred, metrics, algo_type='reg')
                print('***')