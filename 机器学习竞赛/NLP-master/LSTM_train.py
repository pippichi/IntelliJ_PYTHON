import tensorflow as tf
from dataclasses import dataclass,field
import numpy as np

@dataclass
class LSTMtraining:
    xtrain:np.array
    ytrain:np.array
    xtest:np.array
    ytest:np.array
    n_inputs:int=field(default=xtrain.shape[1])
    max_time:int=field(default=xtrain.shape[0])
    lstm_size:int=field(default=100)
    n_classes:int=field(default=22)
    batch_size:int=field(default=50)
    n_batch:int=field(default=(xtrain.shape[0]/batch_size))

    x = tf.placeholder(tf.float32, [None, xtrain.shape[0] * xtrain.shape[1]])
    y = tf.placeholder(tf.float32, [None, xtrain.shape[1]])

    #初始化权值
    weights = tf.Variable(tf.truncated_normal([lstm_size,n_classes],stddev=0.1))
    #初始化偏置值
    biases = tf.Variable(tf.constant(0.1,shape=[n_classes]))

    def RNN(self,X,weights,biases):
        # inputs = [batch_size,max_time,n_inputs]
        inputs = tf.reshape(self.x,[-1,self.max_time,self.n_inputs])
        #定义LSTM基本CELL
        lstm_cell = tf.contrib.rnn.BasicLSTMCell(self.lstm_size)
        outputs,final_state = tf.nn.dynamic_rnn(lstm_cell,inputs,dtype=tf.float32)
        results = tf.nn.softmax(tf.matmul(final_state[1],weights)+biases)
        return results

    def score(self):
        #计算RNN的返回结果
        predict = self.RNN(self.x,self.weights,self.biases)
        cross_entropy = tf.reduce_mean(tf.nn.softmax_cross_entropy_with_logits(labels=self.y,logits=predict))
        train_step = tf.train.AdamOptimizer(1e-4).minimize(cross_entropy)
        correct_predict = tf.equal(tf.argmax(self.y,1),tf.argmax(predict,1))
        accuracy = tf.reduce_mean(tf.cast(correct_predict,tf.float32))

        with tf.Session() as sess:
            sess.run(tf.global_variables_initializer())
            for epoch in range(100):
                for batch in range(self.n_batch):
                    batch_xs, batch_ys = [],[]
                    sess.run(train_step,feed_dict={self.x:self.xtrain,self.y:self.ytrain})
                acc = sess.run(accuracy,feed_dict={self.x:self.xtest,self.y:self.ytest})
                print('Iter ' + str(epoch) + ',Testing Accuracy= ' + str(acc))