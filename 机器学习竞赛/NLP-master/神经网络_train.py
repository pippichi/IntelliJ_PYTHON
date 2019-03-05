#coding:utf-8
import codecs
import os
import pickle

import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
import seaborn as sns
import tensorflow as tf

from sklearn.linear_model import LogisticRegression
from sklearn.model_selection import learning_curve

import Preprocessor

sns.set_style("whitegrid")


class SentimentClassifier:
    def __init__(self):
        if os.path.exists('corpus\\train.csv') and os.path.exists('corpus\\test.csv'):
            self.train_data = pd.read_csv('corpus\\train.csv')
            self.test_data = pd.read_csv('corpus\\test.csv')
            # self.data = shuffle(train_data)
            # X_data = pd.DataFrame(train_data.drop('sentiment', axis=1))
            # Y_data = column_or_1d(train_data[:]['sentiment'], warn=True)
            self.X_train, self.X_val,\
            self.y_train, self.y_val = self.train_data[:,2:],self.test_data[:,2:],self.train_data[:,1],self.test_data[:,1]
            # self.X_train_shape,self.X_val_shape,\
            # self.y_train_shape,self.y_val_shape = self.train_data[:,2:].shape,self.test_data[:,2:].shape,self.train_data[:,1].shape,self.test_data[:,1].shape
            self.model = None
            self.load_model()
            self.preprocessor = Preprocessor.Preprocessor()
        else:
            print('No Source!')
            Preprocessor.Preprocessor().process_data("C:\\Users\\HASEE\\Desktop\\ai_challenger_sentiment_analysis_trainingset_20180816\\sentiment_analysis_trainingset.csv")
            Preprocessor.Preprocessor().process_data("C:\\Users\\HASEE\\Desktop\\ai_challenger_sentiment_analysis_validationset_20180816\\sentiment_analysis_validationset.csv")

    def load_model(self, filename='model\\model.pickle'):
        if os.path.exists(filename):
            with codecs.open(filename, 'rb') as f:
                f = open(filename, 'rb')
                self.model = pickle.load(f)
        else:
            self.train()

    def save_model(self, filename='model\\model.pickle'):
        with codecs.open(filename, 'wb') as f:
            pickle.dump(self.model, f)

    def train(self):
            self.model = LogisticRegression(random_state=3)
            self.model.fit(self.X_train, self.y_train)
            self.save_model()
            print('Accuracy: ' + str(round(self.model.score(self.X_val, self.y_val), 2)))

    def predict(self, sentence):
        vec = self.preprocessor.sentence2vec(sentence)
        return self.model.predict(vec)

    def predict_test_set(self, sentences, pos_file='corpus\\pos_test.txt', neg_file='corpus\\neg_test.txt'):
        pos_set = []
        neg_set = []
        for each in sentences:
            score = self.predict(each)
            if score == 1:
                pos_set.append(each)
            elif score == -1:
                neg_set.append(each)
        with codecs.open(pos_file, 'w', 'utf-8') as f:
            for each in pos_set:
                f.write(each + '\n')
            f.close()
        with codecs.open(neg_file, 'w', 'utf-8') as f:
            for each in neg_set:
                f.write(each + '\n')
            f.close()

    def show_heat_map(self):
            pd.set_option('precision', 2)
            plt.figure(figsize=(20, 6))
            sns.heatmap(self.train_data.corr(), square=True)
            plt.xticks(rotation=90)
            plt.yticks(rotation=360)
            plt.suptitle("Correlation Heatmap")
            plt.show()

    def show_heat_map_to(self, target='sentiment'):
            correlations = self.train_data.corr()[target].sort_values(ascending=False)
            plt.figure(figsize=(40, 6))
            correlations.drop(target).plot.bar()
            pd.set_option('precision', 2)
            plt.xticks(rotation=90, fontsize=7)
            plt.yticks(rotation=360)
            plt.suptitle('The Heatmap of Correlation With ' + target)
            plt.show()

    def plot_learning_curve(self):
        # Plot the learning curve
        plt.figure(figsize=(9, 6))
        train_sizes, train_scores, test_scores = learning_curve(
            self.model, X=self.X_train, y=self.y_train,
            cv=3, scoring='neg_mean_squared_error')
        self.plot_learning_curve_helper(train_sizes, train_scores, test_scores, 'Learning Curve')
        plt.show()

    def plot_learning_curve_helper(self, train_sizes, train_scores, test_scores, title, alpha=0.1):
        train_scores = -train_scores
        test_scores = -test_scores
        train_mean = np.mean(train_scores, axis=1)
        train_std = np.std(train_scores, axis=1)
        test_mean = np.mean(test_scores, axis=1)
        test_std = np.std(test_scores, axis=1)
        plt.plot(train_sizes, train_mean, label='train score', color='blue', marker='o')
        plt.fill_between(train_sizes, train_mean + train_std,
                         train_mean - train_std, color='blue', alpha=alpha)
        plt.plot(train_sizes, test_mean, label='test score', color='red', marker='o')
        plt.fill_between(train_sizes, test_mean + test_std, test_mean - test_std, color='red', alpha=alpha)
        plt.title(title)
        plt.xlabel('Number of training points')
        plt.ylabel(r'Mean Squared Error')
        plt.grid(ls='--')
        plt.legend(loc='best')
        plt.show()

    # def feature_reduction(self, X_train, y_train, X_val):
    #     thresh = 5 * 10 ** (-3)
    #     # model = XGBRegressor()
    #     model.fit(X_train, y_train)
    #     selection = SelectFromModel(model, threshold=thresh, prefit=True)
    #     select_X_train = selection.transform(X_train)
    #     select_X_val = selection.transform(X_val)
    #     return select_X_train, select_X_val


    def choose_best_model(self,xtrain,xtest,ytrain,ytest):
        # 每个批次的大小
        batch_size = 80
        # 计算一共有多少个批次
        n_batch = xtrain.shape[0] // batch_size
        # 定义两个placeholder
        x = tf.placeholder(tf.float32, [None, xtrain.shape[0]*xtrain.shape[1]])
        y = tf.placeholder(tf.float32, [None, xtrain.shape[1]])
        keep_prob = tf.placeholder(tf.float32)

        # 创建一个简单的神经网络
        Weights1 = tf.Variable(tf.truncated_normal([xtrain.shape[0]*xtrain.shape[1], 2000], stddev=0.1))
        biases1 = tf.Variable(tf.zeros([2000]) + 0.1)
        L1 = tf.nn.tanh(tf.matmul(x, Weights1) + biases1)
        L1_drop = tf.nn.dropout(L1, keep_prob)

        Weights2 = tf.Variable(tf.truncated_normal([2000, 1400], stddev=0.1))
        biases2 = tf.Variable(tf.zeros([1400]) + 0.1)
        L2 = tf.nn.tanh(tf.matmul(L1_drop, Weights2) + biases2)
        L2_drop = tf.nn.dropout(L2, keep_prob)

        Weights3 = tf.Variable(tf.truncated_normal([1400, 800], stddev=0.1))
        biases3 = tf.Variable(tf.zeros([800]) + 0.1)
        L3 = tf.nn.tanh(tf.matmul(L2_drop, Weights3) + biases3)
        L3_drop = tf.nn.dropout(L3, keep_prob)

        Weights4 = tf.Variable(tf.truncated_normal([800, 22], stddev=0.1))
        biases4 = tf.Variable(tf.zeros([22]) + 0.1)
        predict = tf.nn.softmax(tf.matmul(L3_drop, Weights4) + biases4)

        # 对数似然代价函数
        loss = tf.reduce_mean(tf.nn.softmax_cross_entropy_with_logits(labels=y, logits=predict))

        # 使用梯度下降法
        train_step = tf.train.AdamOptimizer(1e-4).minimize(loss)

        # 初始化变量
        init = tf.global_variables_initializer()

        # 结果存放在一个布尔型列表中
        correct_predict = tf.equal(tf.argmax(predict, 1), tf.argmax(y, 1))
        # 求准确率
        accuracy = tf.reduce_mean(tf.cast(correct_predict, tf.float32))

        with tf.Session() as sess:
            sess.run(init)
            for epoch in range(10):
                for batch in range(n_batch):
                    batch_xs, batch_ys = mnist.train.next_batch(batch_size)
                    sess.run(train_step, feed_dict={x: batch_xs, y: batch_ys, keep_prob: 0.7})

                test_acc = sess.run(accuracy, feed_dict={x: xtest, y: ytest, keep_prob: 1.0})
                train_acc = sess.run(accuracy, feed_dict={x: xtrain, y: ytrain, keep_prob: 1.0})
                print('Iter: ' + str(epoch) + ' Testing Accuracy ' + str(test_acc) + ' , Training Accuracy ' + str(train_acc))
if __name__ == '__main__':
    # DataSpider.Preprocessor().get_new_data()
    classifier = SentimentClassifier()
    classifier.train()
    classifier.plot_learning_curve()
    # classifier.show_heat_map()
    # classifier.show_heat_map_to()
    classifier.choose_best_model()
    # classifier.predict(text)
    # test_set = []
    # with codecs.open('.\\test\\test.txt', 'r', 'utf-8') as f:
    #     for each in f.readlines():
    #         test_set.append(each)
    # classifier.predict_test_set(test_set)
