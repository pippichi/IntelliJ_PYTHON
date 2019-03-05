import os
os.environ['TF_CPP_MIN_LOG_LEVEL'] = '2'

import tensorflow as tf


matrix1 = tf.constant([[3,3]])
matrix2 = tf.constant([[2],
                       [2]])
product = tf.matmul(matrix1,matrix2)


#method1
sess = tf.Session()
result = sess.run(product)
print(result)
sess.close()


#method2 自动关闭tf.Session()
with tf.Session() as sess:
    result = sess.run(product)
    print(result)
state = tf.Variable(0,name='counter')
# print(state.name)
one = tf.constant(1)
new_value = tf.add(state,one)
update = tf.assign(state,new_value)

init = tf.global_variables_initializer()

with tf.Session() as sess:
    sess.run(init)
    for i in range(3):
        sess.run(update)
        print(sess.run(state))

