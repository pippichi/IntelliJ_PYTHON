import tensorflow as tf

#初始化权值
def weight_variable(shape):
    initial = tf.truncated_normal(shape,stddev=0.1)
    return tf.Variable(initial)

#初始化偏置
def bias_variable(shape):
    initial = tf.constant(0.1,shape=shape)
    return tf.Variable(initial)
#卷积层
def conv2d(x,W):
    return tf.nn.conv2d(x,W,strides=[1,1,1,1],padding='SAME')
#池化层
def max_pool_2x2(x):
    #ksize [1,x,y,1]
    return tf.nn.max_pool(x,ksize=[1,2,2,1],strides=[1,2,2,1],padding="SAME")


def choose_best_model(self,xtrain,xtest,ytrain,ytest):
    sess = tf.Session()
    # 每个批次的大小
    batch_size = 80
    # 计算一共有多少个批次
    n_batch = xtrain.shape[0] // batch_size
    # 定义两个placeholder
    x = tf.placeholder(tf.float32, [None, xtrain.shape[0]*xtrain.shape[1]])
    y = tf.placeholder(tf.float32, [None, xtrain.shape[1]])
    x_matrix = tf.reshape(x,[-1,xtrain.shape[0],xtrain.shape[1],-1])
    #创建一个简单的卷积神经网络
    W_conv1 = weight_variable([5,5,1,32])
    b_conv1 = bias_variable([32])

    # 把x_image和权值向量进行卷积，再加上偏置值，然后应用于relu激活函数
    h_conv_1 = tf.nn.relu(conv2d(x_matrix,W_conv1)+b_conv1)
    h_pool1 = max_pool_2x2(h_conv_1)

    W_conv2 = weight_variable([5,5,32,64])
    b_conv2 = bias_variable([64])

    h_conv2 = tf.nn.relu(conv2d(h_pool1,W_conv2)+b_conv2)
    h_pool2 = max_pool_2x2(h_conv2)

    #初始化第一个全连接层
    W_fc1 = weight_variable([(xtrain.shape[0]/4)*(xtrain.shape[0]/4)*64,1024])
    b_fc1 = bias_variable([1024])

    h_pool2_flat = tf.reshape(h_pool2,[-1,(xtrain.shape[0]/4)*(xtrain.shape[0]/4)*64])
    #第一个全连接层的输出
    h_fc1 = tf.nn.relu(tf.matmul(h_pool2_flat,W_fc1)+b_fc1)

    keep_prob = tf.placeholder(tf.float32)
    h_fc1_drop = tf.nn.dropout(h_fc1,keep_prob)
    #初始化第二个全连接层
    W_fc2 = weight_variable([1024,10])
    b_fc2 = bias_variable([10])
    #计算
    predict = tf.nn.softmax(tf.matmul(h_fc1_drop,W_fc2)+b_fc2)

    #交叉熵代价函数
    cross_entropy = tf.reduce_mean(tf.nn.softmax_cross_entropy_with_logits(labels=y,logits=predict))

    #优化函数

    train_step = tf.train.AdamOptimizer(1e-4).minimize(cross_entropy)

    # 初始化变量
    init = tf.global_variables_initializer()

    # 结果存放在一个布尔型列表中
    correct_predict = tf.equal(tf.argmax(predict, 1), tf.argmax(y, 1))
    # 求准确率
    accuracy = tf.reduce_mean(tf.cast(correct_predict, tf.float32))

    sess.run(tf.global_variables_initializer)
    #产生metadata文件
    if tf.gfile.Exists("corpus\\projector\\projector\\metadata.tsv"):
        tf.gfile.DeleteRecursively("corpus\\projector\\projector\\metadata.tsv")
    with open("corpus\\projector\\projector\\metadata.tsv",'w') as f:
        labels = sess.run(tf.argmax(ytest,1))
        for i in range(xtrain.shape[0]):
            f.write(str(labels[i])+'\n')

    for i in range(n_batch):
        for j in range(batch_size):
            batch_xs,batch_ys = [],[]

            if j%50==0:
                acc = sess.run(accuracy,feed_dict={x:xtest,y:ytest})
                print('Iter '+str(i)+',Testing Accuracy= '+str(acc))
